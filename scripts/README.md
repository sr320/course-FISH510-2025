# Scripts Directory

This directory contains utility scripts for managing and analyzing course data.

## Available Scripts

### discussion_stats.py

A Python script that fetches and displays statistics about GitHub Discussions in this repository, including the number of posts (discussions + comments) by each user.

#### Requirements

- Python 3.6 or higher
- `requests` library: `pip install requests`
- GitHub Personal Access Token with `read:discussion` scope

#### Usage

Basic usage (uses environment variable for token):
```bash
export GITHUB_TOKEN="your_github_token_here"
python scripts/discussion_stats.py
```

With command-line arguments:
```bash
python scripts/discussion_stats.py --token YOUR_TOKEN --owner sr320 --repo course-FISH510-2025
```

Sort by username instead of post count:
```bash
python scripts/discussion_stats.py --sort username
```

#### Creating a GitHub Token

1. Go to https://github.com/settings/tokens
2. Click "Generate new token" (classic)
3. Give it a descriptive name (e.g., "Discussion Stats Script")
4. Select the `read:discussion` scope
5. Click "Generate token"
6. Copy the token and use it with the script

#### Output Example

```
Fetching discussions from sr320/course-FISH510-2025...

============================================================
GitHub Discussions - Posts by User
============================================================
Username                              Posts
------------------------------------------------------------
student1                                 45
instructor                               38
student2                                 32
student3                                 28
------------------------------------------------------------
TOTAL                                   143
Unique Users                              4
============================================================
```

## Future Scripts

Additional scripts for course management and analysis can be added to this directory.
