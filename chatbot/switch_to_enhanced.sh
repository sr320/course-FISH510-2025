#!/bin/bash

# Switch to enhanced version files
echo "🔄 Switching to enhanced chatbot version..."

# Backup current files
cp app.py app_simple_backup.py
cp requirements.txt requirements_simple_backup.txt

# Switch to enhanced versions
cp app_enhanced.py app.py
cp requirements_enhanced.txt requirements.txt

echo "✅ Switched to enhanced version!"
echo "📁 Files updated:"
echo "   - app.py (now enhanced version)"
echo "   - requirements.txt (now enhanced version)"
echo ""
echo "🚀 Ready to deploy to Railway!"
echo "💡 Don't forget to add your OPENAI_API_KEY environment variable"
