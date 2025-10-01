#!/bin/bash

# FISH 510 Course Chatbot - Free Version Deployment

echo "🐠 FISH 510 Chatbot - Free Version Deployment"
echo "=============================================="

# Check if we're in the right directory
if [ ! -f "app_free.py" ]; then
    echo "❌ Error: Please run this script from the chatbot directory"
    echo "   cd chatbot && ./deploy_free.sh"
    exit 1
fi

echo "✅ Free version detected!"
echo ""
echo "🚀 This version uses local embeddings and doesn't require OpenAI API"
echo "   - No API key needed"
echo "   - No billing/quota issues"
echo "   - Uses sentence-transformers for embeddings"
echo "   - Provides document retrieval without AI generation"
echo ""

echo "📋 Deployment Options:"
echo "1. Railway (Recommended)"
echo "2. Vercel + Railway"
echo "3. Docker"
echo "4. Manual instructions"
echo ""

read -p "Choose deployment option (1-4): " choice

case $choice in
    1)
        echo ""
        echo "🚂 Railway Deployment (Free Version):"
        echo "1. Go to https://railway.app"
        echo "2. Sign up with GitHub"
        echo "3. Click 'New Project' → 'Deploy from GitHub repo'"
        echo "4. Select your course-FISH510-2025 repository"
        echo "5. Set root directory to 'chatbot'"
        echo "6. Rename app_free.py to app.py: mv app_free.py app.py"
        echo "7. Rename requirements_free.txt to requirements.txt: mv requirements_free.txt requirements.txt"
        echo "8. Add environment variable: FLASK_ENV=production"
        echo "9. Deploy!"
        echo ""
        echo "💡 Note: No OpenAI API key needed for this version"
        ;;
    2)
        echo ""
        echo "🌐 Vercel + Railway Deployment:"
        echo ""
        echo "Backend (Railway):"
        echo "1. Follow Railway steps above"
        echo "2. Note your Railway backend URL"
        echo ""
        echo "Frontend (Vercel):"
        echo "1. Go to https://vercel.com"
        echo "2. Import your GitHub repository"
        echo "3. Set root directory to 'chatbot/frontend'"
        echo "4. Add environment variable:"
        echo "   REACT_APP_API_URL=https://your-railway-url.up.railway.app"
        echo "5. Deploy"
        ;;
    3)
        echo ""
        echo "🐳 Docker Deployment:"
        echo "1. Rename files: mv app_free.py app.py && mv requirements_free.txt requirements.txt"
        echo "2. Run: docker-compose up -d"
        echo "3. Access at http://localhost:3000"
        ;;
    4)
        echo ""
        echo "📖 Manual Setup:"
        echo "1. Rename app_free.py to app.py"
        echo "2. Rename requirements_free.txt to requirements.txt"
        echo "3. Follow regular deployment instructions"
        echo "4. No OpenAI API key needed!"
        ;;
    *)
        echo "❌ Invalid option. Please run the script again."
        ;;
esac

echo ""
echo "🎓 Free Version Features:"
echo "   ✅ Document retrieval and search"
echo "   ✅ Course content access"
echo "   ✅ Source attribution"
echo "   ❌ AI-generated responses (uses document excerpts)"
echo "   ❌ No OpenAI API costs"
echo ""
echo "💡 To upgrade to full AI version:"
echo "   1. Fix OpenAI billing/quota"
echo "   2. Use the original app.py"
echo "   3. Redeploy"
