# FISH 510 Chatbot Deployment Guide

This guide covers multiple options for deploying the chatbot so students can access it online.

## 🚀 Recommended: Railway (Easiest)

Railway is the simplest option for full-stack deployment.

### Step 1: Prepare Repository

1. **Create .env file locally** (DO NOT commit this):
   ```bash
   cd chatbot
   cp env_template.txt .env
   # Edit .env and add your OpenAI API key
   ```

2. **Push to GitHub** (if not already done):
   ```bash
   git add .
   git commit -m "Add FISH 510 course chatbot"
   git push origin main
   ```
   **Note**: The `.env` file is automatically ignored by git and won't be pushed.

### Step 2: Create Railway Account
- Go to https://railway.app
- Sign up with GitHub

### Step 3: Deploy Backend

1. **Create New Project**:
   - Click "New Project" → "Deploy from GitHub repo"
   - Select your `course-FISH510-2025` repository

2. **Configure Backend**:
   - Railway will auto-detect the Flask app in `/chatbot`
   - Set root directory to `chatbot`
   - Add environment variables:
     ```
     OPENAI_API_KEY=your_openai_api_key_here
     FLASK_ENV=production
     ```

3. **Deploy**:
   - Railway will automatically build and deploy
   - Note the generated URL (e.g., `https://fish510-chatbot-production.up.railway.app`)

### Step 3: Deploy Frontend

1. **Create Second Service**:
   - In same Railway project, click "New Service"
   - Choose "GitHub Repo" again
   - Set root directory to `chatbot/frontend`

2. **Configure Frontend**:
   - Add environment variable:
     ```
     REACT_APP_API_URL=https://your-backend-url.up.railway.app
     ```

3. **Deploy**:
   - Railway will build and deploy the React app
   - Students can access via the frontend URL

## 🌐 Alternative: Vercel + Railway

### Frontend on Vercel (Free)

1. **Create Vercel Account**:
   - Go to https://vercel.com
   - Sign up with GitHub

2. **Deploy Frontend**:
   - Import your GitHub repository
   - Set root directory to `chatbot/frontend`
   - Add environment variable:
     ```
     REACT_APP_API_URL=https://your-railway-backend-url.up.railway.app
     ```
   - Deploy

### Backend on Railway
Follow the Railway backend steps above.

## 🐳 Alternative: Docker Deployment

### Option 1: Railway with Docker

1. **Create `railway.json`** in chatbot directory:
   ```json
   {
     "$schema": "https://railway.app/railway.schema.json",
     "build": {
       "builder": "DOCKERFILE"
     },
     "deploy": {
       "startCommand": "python app.py",
       "healthcheckPath": "/api/health",
       "healthcheckTimeout": 100,
       "restartPolicyType": "ON_FAILURE"
     }
   }
   ```

2. **Deploy**:
   - Push to GitHub
   - Railway will use the Dockerfile automatically

### Option 2: Self-hosted Server

1. **Server Requirements**:
   - Ubuntu/CentOS server
   - Docker and Docker Compose
   - Domain name (optional)

2. **Deploy**:
   ```bash
   # On your server
   git clone https://github.com/your-username/course-FISH510-2025.git
   cd course-FISH510-2025/chatbot
   
   # Set environment variables
   cp env_template.txt .env
   # Edit .env with your OpenAI API key
   
   # Deploy with Docker Compose
   docker-compose up -d
   ```

3. **Configure Nginx** (optional):
   ```nginx
   server {
       listen 80;
       server_name your-domain.com;
       
       location / {
           proxy_pass http://localhost:3000;
       }
       
       location /api/ {
           proxy_pass http://localhost:5000;
       }
   }
   ```

## 🔧 Environment Variables

### Backend Variables
```bash
OPENAI_API_KEY=sk-your-api-key-here
FLASK_ENV=production
FLASK_DEBUG=False
```

### Frontend Variables
```bash
REACT_APP_API_URL=https://your-backend-url.up.railway.app
```

## 📋 Pre-Deployment Checklist

- [ ] OpenAI API key obtained
- [ ] Repository pushed to GitHub
- [ ] Environment variables configured
- [ ] Domain name ready (if using custom domain)
- [ ] SSL certificate configured (Railway/Vercel handle this automatically)

## 🎯 Student Access

Once deployed, students can access the chatbot at:
- **Railway**: `https://your-project-name.up.railway.app`
- **Vercel**: `https://your-project-name.vercel.app`
- **Custom Domain**: `https://your-domain.com`

## 💰 Cost Estimates

### Railway
- **Free Tier**: $5/month credit
- **Pro Plan**: $5/month + usage
- **Estimated Cost**: $5-10/month for moderate usage

### Vercel
- **Frontend**: Free for personal projects
- **Backend**: Use Railway (see above)

### Self-hosted
- **VPS**: $5-20/month (DigitalOcean, Linode, etc.)
- **Domain**: $10-15/year (optional)

## 🔍 Monitoring & Maintenance

### Health Checks
- Backend: `https://your-backend-url/api/health`
- Frontend: Check if React app loads

### Logs
- Railway: Built-in log viewer
- Vercel: Function logs in dashboard
- Self-hosted: `docker-compose logs -f`

### Updates
1. Push changes to GitHub
2. Platform will auto-deploy (Railway/Vercel)
3. Or manually redeploy (self-hosted)

## 🚨 Troubleshooting

### Common Issues

1. **CORS Errors**:
   - Ensure `REACT_APP_API_URL` matches backend URL exactly
   - Check Flask-CORS configuration in `app.py`

2. **Build Failures**:
   - Check environment variables are set
   - Verify OpenAI API key is valid

3. **Slow Responses**:
   - First query may be slow (document indexing)
   - Consider upgrading Railway plan for better performance

4. **Memory Issues**:
   - ChromaDB may use significant memory
   - Monitor usage in Railway dashboard

## 📞 Support

- **Railway**: https://railway.app/help
- **Vercel**: https://vercel.com/help
- **Docker**: https://docs.docker.com/

---

**Recommended Path**: Railway for both frontend and backend (simplest setup)
**Budget Option**: Railway backend + Vercel frontend (free frontend)
**Full Control**: Self-hosted with Docker
