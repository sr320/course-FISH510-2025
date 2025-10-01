# 🚀 Quick Deployment Guide

## Option 1: Railway (Recommended - Easiest)

### Step 1: Get OpenAI API Key
1. Go to https://platform.openai.com/api-keys
2. Create new API key
3. Copy the key (starts with `sk-`)

### Step 2: Set Up Environment Variables Locally
```bash
cd chatbot
cp env_template.txt .env
# Edit .env and add your API key
```
**Important**: The `.env` file is in `.gitignore` and will NOT be pushed to GitHub.

### Step 3: Deploy to Railway
1. Go to https://railway.app
2. Sign up with GitHub
3. Click "New Project" → "Deploy from GitHub repo"
4. Select your `course-FISH510-2025` repository
5. Railway will auto-detect the chatbot

### Step 4: Configure Environment Variables in Railway
1. In Railway dashboard, go to "Variables" tab
2. Add these environment variables:
   ```
   OPENAI_API_KEY=sk-your-api-key-here
   FLASK_ENV=production
   ```
3. Railway will automatically redeploy

### Step 5: Access Your Chatbot
- Railway will provide a URL like: `https://fish510-chatbot-production.up.railway.app`
- Share this URL with your students!

## Option 2: Vercel + Railway (Free Frontend)

### Deploy Backend (Railway)
Follow steps 1-3 above for Railway backend.

### Deploy Frontend (Vercel)
1. Go to https://vercel.com
2. Sign up with GitHub
3. Import your repository
4. Set root directory to `chatbot/frontend`
5. Add environment variable:
   ```
   REACT_APP_API_URL=https://your-railway-backend-url.up.railway.app
   ```
6. Deploy

## Option 3: Docker (Self-hosted)

### On Your Server
```bash
# Clone repository
git clone https://github.com/your-username/course-FISH510-2025.git
cd course-FISH510-2025/chatbot

# Set environment variables
echo "OPENAI_API_KEY=sk-your-api-key-here" > .env
echo "FLASK_ENV=production" >> .env

# Deploy with Docker
docker-compose up -d
```

## 🎯 Share with Students

Once deployed, students can access the chatbot at your deployment URL and ask questions like:
- "What is this course about?"
- "Tell me about Week 1 readings"
- "What are the assignment deadlines?"
- "Explain DNA methylation in marine organisms"

## 💰 Cost
- **Railway**: ~$5-10/month
- **Vercel Frontend**: Free
- **Total**: ~$5-10/month for full deployment

## 🔧 Troubleshooting
- **CORS errors**: Make sure `REACT_APP_API_URL` matches your backend URL exactly
- **API errors**: Verify your OpenAI API key is correct
- **Build failures**: Check that all environment variables are set

---

**Need help?** Check the full `DEPLOYMENT.md` for detailed instructions!
