# 🔒 Security Guide for FISH 510 Chatbot

## API Key Security

### ✅ DO:
- **Keep API keys in `.env` file** (automatically ignored by git)
- **Add API keys to deployment platform** (Railway, Vercel, etc.)
- **Use environment variables** for all sensitive data
- **Rotate API keys** periodically for security

### ❌ DON'T:
- **Never commit `.env` files** to git
- **Never put API keys** in code files
- **Never share API keys** in chat or email
- **Never hardcode secrets** in your repository

## Safe Deployment Process

### 1. Local Development
```bash
# Create .env file (this is safe - it's in .gitignore)
cd chatbot
cp env_template.txt .env
# Edit .env and add your API key
```

### 2. Git Push (Safe)
```bash
git add .
git commit -m "Add chatbot"
git push origin main
# .env file is automatically ignored and won't be pushed
```

### 3. Deployment Platform Setup
- **Railway**: Add environment variables in dashboard
- **Vercel**: Add environment variables in project settings
- **Docker**: Use environment files or docker secrets

## Environment Variables

### Required Variables
```bash
# OpenAI API Key (get from https://platform.openai.com/api-keys)
OPENAI_API_KEY=sk-your-api-key-here

# Environment
FLASK_ENV=production
```

### Optional Variables
```bash
# Debug mode (disable in production)
FLASK_DEBUG=False

# Custom API URL for frontend
REACT_APP_API_URL=https://your-backend-url.up.railway.app
```

## Platform-Specific Security

### Railway
1. Go to your project dashboard
2. Click "Variables" tab
3. Add environment variables:
   - `OPENAI_API_KEY`: Your OpenAI API key
   - `FLASK_ENV`: production

### Vercel
1. Go to your project dashboard
2. Click "Settings" → "Environment Variables"
3. Add variables for each environment (production, preview, development)

### Docker
```bash
# Option 1: Environment file
docker run --env-file .env your-app

# Option 2: Environment variables
docker run -e OPENAI_API_KEY=sk-your-key your-app
```

## Checking Security

### Verify .env is Ignored
```bash
# Check if .env is in .gitignore
cat .gitignore | grep .env

# Check git status (should not show .env)
git status
```

### Verify No Secrets in Code
```bash
# Search for potential API keys in code
grep -r "sk-" . --exclude-dir=.git
grep -r "OPENAI_API_KEY" . --exclude-dir=.git
```

## API Key Management

### Creating OpenAI API Key
1. Go to https://platform.openai.com/api-keys
2. Click "Create new secret key"
3. Copy the key immediately (you can't see it again)
4. Set usage limits and monitoring

### Best Practices
- **Use separate API keys** for development and production
- **Set usage limits** to prevent unexpected charges
- **Monitor usage** regularly
- **Rotate keys** every 90 days
- **Revoke unused keys**

## Troubleshooting Security Issues

### If API Key is Accidentally Committed
1. **Immediately revoke** the exposed API key
2. **Create a new API key**
3. **Remove from git history**:
   ```bash
   git filter-branch --force --index-filter \
   'git rm --cached --ignore-unmatch chatbot/.env' \
   --prune-empty --tag-name-filter cat -- --all
   ```
4. **Force push** (be careful with shared repositories)

### If Environment Variables Not Working
1. **Check spelling** of variable names
2. **Verify deployment platform** has the variables
3. **Restart the application** after adding variables
4. **Check logs** for error messages

## Cost Management

### OpenAI API Usage
- **Monitor usage** in OpenAI dashboard
- **Set usage limits** to prevent overage
- **Use appropriate models** (GPT-4 is more expensive than GPT-3.5)
- **Implement rate limiting** if needed

### Deployment Platform Costs
- **Railway**: $5/month base + usage
- **Vercel**: Free tier available
- **Monitor usage** in platform dashboards

## Emergency Procedures

### If API Key is Compromised
1. **Revoke immediately** in OpenAI dashboard
2. **Create new API key**
3. **Update all deployment platforms**
4. **Monitor for unauthorized usage**

### If Deployment is Compromised
1. **Take down the deployment**
2. **Review access logs**
3. **Update all credentials**
4. **Redeploy with new keys**

---

**Remember**: Security is everyone's responsibility. When in doubt, err on the side of caution and rotate your credentials.
