#!/usr/bin/env python3
"""
GitHub Discussions Statistics Script

This script fetches discussion data from the GitHub repository and counts
the number of posts (discussions + comments) by each user.

Usage:
    python discussion_stats.py

Requirements:
    - PyGithub library (install with: pip install PyGithub)
    - GitHub Personal Access Token (set as GITHUB_TOKEN environment variable)
      or pass as --token argument
"""

import os
import sys
import argparse
from collections import defaultdict
from typing import Dict

try:
    import requests
except ImportError:
    print("Error: requests library not found. Install it with: pip install requests")
    sys.exit(1)


def fetch_discussions_graphql(owner: str, repo: str, token: str) -> Dict[str, int]:
    """
    Fetch discussions and comments using GitHub GraphQL API.
    
    Args:
        owner: Repository owner
        repo: Repository name
        token: GitHub personal access token
        
    Returns:
        Dictionary mapping usernames to post counts
    """
    url = "https://api.github.com/graphql"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
    }
    
    user_posts = defaultdict(int)
    has_next_page = True
    end_cursor = None
    
    while has_next_page:
        # GraphQL query to fetch discussions and comments
        query = """
        query($owner: String!, $repo: String!, $cursor: String) {
          repository(owner: $owner, name: $repo) {
            discussions(first: 100, after: $cursor) {
              pageInfo {
                hasNextPage
                endCursor
              }
              nodes {
                author {
                  login
                }
                comments(first: 100) {
                  nodes {
                    author {
                      login
                    }
                  }
                }
              }
            }
          }
        }
        """
        
        variables = {
            "owner": owner,
            "repo": repo,
            "cursor": end_cursor
        }
        
        try:
            response = requests.post(
                url,
                json={"query": query, "variables": variables},
                headers=headers
            )
            response.raise_for_status()
            data = response.json()
            
            if "errors" in data:
                print(f"GraphQL errors: {data['errors']}")
                return user_posts
            
            discussions = data["data"]["repository"]["discussions"]
            
            # Count discussion posts (original posts)
            for discussion in discussions["nodes"]:
                if discussion["author"] and discussion["author"]["login"]:
                    user_posts[discussion["author"]["login"]] += 1
                
                # Count comments
                for comment in discussion["comments"]["nodes"]:
                    if comment["author"] and comment["author"]["login"]:
                        user_posts[comment["author"]["login"]] += 1
            
            # Check pagination
            page_info = discussions["pageInfo"]
            has_next_page = page_info["hasNextPage"]
            end_cursor = page_info["endCursor"]
            
        except requests.exceptions.RequestException as e:
            print(f"Error fetching data from GitHub API: {e}")
            return user_posts
        except (KeyError, TypeError) as e:
            print(f"Error parsing response: {e}")
            return user_posts
    
    return user_posts


def display_stats(user_posts: Dict[str, int], sort_by: str = "posts"):
    """
    Display user post statistics.
    
    Args:
        user_posts: Dictionary mapping usernames to post counts
        sort_by: Sort by 'posts' (count) or 'username'
    """
    if not user_posts:
        print("No discussion posts found.")
        return
    
    # Sort users
    if sort_by == "posts":
        sorted_users = sorted(user_posts.items(), key=lambda x: x[1], reverse=True)
    else:
        sorted_users = sorted(user_posts.items(), key=lambda x: x[0].lower())
    
    # Display results
    print("\n" + "="*60)
    print("GitHub Discussions - Posts by User")
    print("="*60)
    print(f"{'Username':<30} {'Posts':>10}")
    print("-"*60)
    
    total_posts = 0
    for username, count in sorted_users:
        print(f"{username:<30} {count:>10}")
        total_posts += count
    
    print("-"*60)
    print(f"{'TOTAL':<30} {total_posts:>10}")
    print(f"{'Unique Users':<30} {len(user_posts):>10}")
    print("="*60 + "\n")


def main():
    """Main function to run the script."""
    parser = argparse.ArgumentParser(
        description="Count posts by user in GitHub Discussions"
    )
    parser.add_argument(
        "--owner",
        default="sr320",
        help="Repository owner (default: sr320)"
    )
    parser.add_argument(
        "--repo",
        default="course-FISH510-2025",
        help="Repository name (default: course-FISH510-2025)"
    )
    parser.add_argument(
        "--token",
        help="GitHub personal access token (or set GITHUB_TOKEN env var)"
    )
    parser.add_argument(
        "--sort",
        choices=["posts", "username"],
        default="posts",
        help="Sort by posts count or username (default: posts)"
    )
    
    args = parser.parse_args()
    
    # Get GitHub token
    token = args.token or os.environ.get("GITHUB_TOKEN")
    if not token:
        print("Error: GitHub token is required.")
        print("Either set GITHUB_TOKEN environment variable or pass --token argument")
        print("\nTo create a token:")
        print("1. Go to https://github.com/settings/tokens")
        print("2. Generate a new token with 'read:discussion' scope")
        sys.exit(1)
    
    print(f"Fetching discussions from {args.owner}/{args.repo}...")
    user_posts = fetch_discussions_graphql(args.owner, args.repo, token)
    
    if user_posts:
        display_stats(user_posts, args.sort)
    else:
        print("No posts found or error occurred.")


if __name__ == "__main__":
    main()
