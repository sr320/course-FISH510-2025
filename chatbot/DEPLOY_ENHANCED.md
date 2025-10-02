# 🚀 Deploy Enhanced FISH 510 Chatbot

## Overview

This guide helps you deploy the enhanced version of the FISH 510 chatbot that uses OpenAI API and RAG (Retrieval-Augmented Generation) for intelligent responses.

## 🆚 Version Comparison

### Free Version (Current)
- ✅ Always available, no costs
- ✅ Basic keyword-based responses
- ✅ Good for common questions
- 🌐 URL: https://course-fish510-2025-production.up.railway.app

### Enhanced Version (New)
- 🚀 AI-powered intelligent responses
- 🧠 Searches through all course documents
- 🔍 Context-aware conversations
- 📚 Source attribution
- 💰 Requires OpenAI API key (minimal cost)

## 🚀 Deployment Steps

### Step 1: Create New Railway Project

1. **Go to Railway**: https://railway.app/dashboard
2. **Click "New Project"** → **"Deploy from GitHub repo"**
3. **Select your repository**: `course-FISH510-2025`
4. **Name it**: `fish510-enhanced` or similar

### Step 2: Configure Enhanced Version

1. **Set Root Directory**: `chatbot`
2. **Rename Files**:
   ```bash
   # In Railway, you'll need to update the files:
   mv app_enhanced.py app.py
   mv requirements_enhanced.txt requirements.txt
   ```

### Step 3: Set Environment Variables

In Railway dashboard, add:
```
OPENAI_API_KEY=sk-your-api-key-here
FLASK_ENV=production
```

### Step 4: Deploy

Railway will automatically deploy the enhanced version!

## 🔧 Alternative: Local Setup

### Quick Test Locally

1. **Copy enhanced files**:
   ```bash
   cd chatbot
   cp app_enhanced.py app.py
   cp requirements_enhanced.txt requirements.txt
   ```

2. **Set up environment**:
   ```bash
   # Create .env file with your OpenAI API key
   echo "OPENAI_API_KEY=sk-your-api-key-here" > .env
   ```

3. **Run locally**:
   ```bash
   python app.py
   ```

4. **Test**: http://localhost:5000

## 🎯 Benefits of Enhanced Version

### For Students
- **Smarter Responses**: AI understands context and nuance
- **Document Search**: Can find specific information in course materials
- **Better Explanations**: More detailed and accurate answers
- **Source Attribution**: Shows which documents informed responses

### For Instructors
- **Reduced Support Load**: Handles complex questions automatically
- **Better Student Experience**: More helpful and accurate responses
- **Comprehensive Coverage**: Access to all course materials
- **Professional Quality**: AI-powered assistance

## 💰 Cost Considerations

### OpenAI API Costs
- **Minimal Usage**: Most questions cost < $0.01
- **Monthly Estimate**: $5-20 for typical course usage
- **Usage Monitoring**: Track costs in OpenAI dashboard
- **Rate Limits**: Set usage limits to control costs

### Cost Management
1. **Set Usage Alerts**: Monitor spending in OpenAI dashboard
2. **Rate Limiting**: Implement daily/monthly limits
3. **Fallback System**: Use free version if API limits reached

## 🔄 Dual Deployment Strategy

### Recommended Setup
1. **Free Version**: https://course-fish510-2025-production.up.railway.app
   - Always available backup
   - Basic questions and reliability

2. **Enhanced Version**: New Railway URL
   - Advanced AI capabilities
   - Document search and analysis

### Student Instructions
```
For basic questions: Use the free version
For detailed help: Use the enhanced version
If enhanced is down: Free version always works
```

## 🛠️ Customization

### Adding Course Content
1. **Add new markdown files** to the course repository
2. **Redeploy** - The system automatically indexes new content
3. **Test** - Ask questions about new materials

### Modifying Responses
1. **Edit prompts** in `app_enhanced.py`
2. **Adjust temperature** for response creativity
3. **Change search parameters** for document retrieval

## 📊 Monitoring

### Railway Dashboard
- **Deployment Status**: Monitor health and uptime
- **Logs**: Check for errors or issues
- **Performance**: Track response times

### OpenAI Dashboard
- **Usage**: Monitor API calls and costs
- **Errors**: Check for API issues
- **Rate Limits**: Ensure within limits

## 🚨 Troubleshooting

### Common Issues
1. **API Key Errors**: Verify key is correct and has credits
2. **Document Loading**: Check file paths and permissions
3. **Memory Issues**: ChromaDB may use significant memory
4. **Slow Responses**: First query may be slow (document indexing)

### Fallback Strategy
- **Free Version**: Always available as backup
- **Error Handling**: Graceful degradation to simple responses
- **Monitoring**: Alert if enhanced version goes down

---

## 🎓 Ready to Deploy?

The enhanced version provides significantly better student experience while maintaining reliability through the free version backup.

**Next Steps:**
1. Create new Railway project
2. Deploy enhanced version
3. Test with students
4. Monitor usage and costs

Your students will love the intelligent, document-aware responses! 🐠📚
