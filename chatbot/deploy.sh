#!/bin/bash

# FISH 510 Chatbot Deployment Helper Script

echo "🐠 FISH 510 Chatbot Deployment Helper"
echo "====================================="

# Check if we're in the right directory
if [ ! -f "app.py" ]; then
    echo "❌ Error: Please run this script from the chatbot directory"
    echo "   cd chatbot && ./deploy.sh"
    exit 1
fi

# Check if .env file exists
if [ ! -f ".env" ]; then
    echo "⚠️  No .env file found!"
    echo "Please create .env file with your OpenAI API key:"
    echo "   cp env_template.txt .env"
    echo "   # Then edit .env and add your API key"
    echo ""
    echo "🔒 SECURITY NOTE: .env files are automatically ignored by git"
    echo "   Your API key will NOT be pushed to GitHub"
    exit 1
fi

# Check if OpenAI API key is set
if ! grep -q "OPENAI_API_KEY=sk-" .env; then
    echo "⚠️  OpenAI API key not found in .env file!"
    echo "Please add your OpenAI API key to the .env file"
    echo ""
    echo "🔒 Remember: The .env file is in .gitignore and won't be committed"
    exit 1
fi

echo "✅ Environment configuration looks good!"
echo ""
echo "🚀 Deployment Options:"
echo "1. Railway (Recommended - Easiest)"
echo "2. Vercel + Railway (Free frontend)"
echo "3. Docker (Self-hosted)"
echo "4. Manual setup instructions"
echo ""

read -p "Choose deployment option (1-4): " choice

case $choice in
    1)
        echo ""
        echo "🚂 Railway Deployment:"
        echo "1. Go to https://railway.app"
        echo "2. Sign up with GitHub"
        echo "3. Click 'New Project' → 'Deploy from GitHub repo'"
        echo "4. Select your course-FISH510-2025 repository"
        echo "5. Railway will auto-detect the chatbot"
        echo "6. Add environment variables in Railway dashboard:"
        echo "   - OPENAI_API_KEY=your-key-here"
        echo "   - FLASK_ENV=production"
        echo "7. Railway will provide a URL for your students!"
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
        echo "1. Ensure Docker is installed on your server"
        echo "2. Run: docker-compose up -d"
        echo "3. Access at http://localhost:3000"
        echo ""
        echo "For production server:"
        echo "1. Set up domain name and SSL"
        echo "2. Configure reverse proxy (nginx)"
        echo "3. Set up monitoring and backups"
        ;;
    4)
        echo ""
        echo "📖 Manual Setup:"
        echo "See DEPLOYMENT.md for detailed instructions"
        echo ""
        echo "Quick steps:"
        echo "1. Push repository to GitHub"
        echo "2. Choose hosting platform (Railway recommended)"
        echo "3. Configure environment variables"
        echo "4. Deploy and share URL with students"
        ;;
    *)
        echo "❌ Invalid option. Please run the script again."
        ;;
esac

echo ""
echo "📚 For detailed instructions, see:"
echo "   - DEPLOYMENT.md (complete guide)"
echo "   - QUICK_DEPLOY.md (quick start)"
echo "   - README.md (full documentation)"
echo ""
echo "🎓 Once deployed, students can access the chatbot and ask questions about:"
echo "   - Course content and readings"
echo "   - Assignment deadlines and requirements"
echo "   - Marine epigenetics concepts"
echo "   - Discussion topics and expectations"
