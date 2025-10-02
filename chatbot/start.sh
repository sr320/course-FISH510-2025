#!/bin/bash

# Enhanced FISH 510 Chatbot Startup Script

echo "🐠 Starting Enhanced FISH 510 Course Chatbot..."

# Install dependencies
echo "📦 Installing Python dependencies..."
pip install --upgrade pip
pip install -r requirements.txt

# Start the application
echo "🚀 Starting Flask application..."
python app.py
