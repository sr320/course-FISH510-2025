# Quick Setup Guide

## Prerequisites
- Python 3.8+
- Node.js 16+
- OpenAI API key

## Quick Start

1. **Get OpenAI API Key**
   - Go to https://platform.openai.com/api-keys
   - Create a new API key
   - Copy the key (starts with `sk-`)

2. **Set Environment Variables**
   ```bash
   cd chatbot
   cp env_template.txt .env
   # Edit .env and paste your OpenAI API key
   ```

3. **Run the Application**
   ```bash
   # Option 1: Use the automated script
   ./run.sh
   
   # Option 2: Manual setup
   python -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   python app.py &
   cd frontend
   npm install
   npm start
   ```

4. **Access the Chatbot**
   - Open http://localhost:3000 in your browser
   - Start asking questions about the course!

## Example Questions to Try

- "What is this course about?"
- "Tell me about Week 1 readings"
- "What are the assignment deadlines?"
- "Explain DNA methylation in marine organisms"
- "What papers should I read for Week 2?"

## Troubleshooting

- **API Key Error**: Make sure your OpenAI API key is correctly set in `.env`
- **Port Already in Use**: Change ports in `app.py` (line 158) and `package.json`
- **Module Not Found**: Run `pip install -r requirements.txt` again

## Need Help?

Check the full README.md for detailed instructions and troubleshooting.
