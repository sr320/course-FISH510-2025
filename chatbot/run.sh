#!/bin/bash

# FISH 510 Course Chatbot Startup Script

echo "🐠 Starting FISH 510 Course Chatbot..."

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python -m venv venv
fi

# Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate

# Install Python dependencies
echo "Installing Python dependencies..."
pip install -r requirements.txt

# Check if .env file exists
if [ ! -f ".env" ]; then
    echo "⚠️  No .env file found!"
    echo "Please copy env_template.txt to .env and add your OpenAI API key:"
    echo "cp env_template.txt .env"
    echo "Then edit .env and add your OPENAI_API_KEY"
    exit 1
fi

# Check if OpenAI API key is set
if ! grep -q "OPENAI_API_KEY=sk-" .env; then
    echo "⚠️  OpenAI API key not found in .env file!"
    echo "Please add your OpenAI API key to the .env file"
    exit 1
fi

# Start the backend
echo "🚀 Starting Flask backend..."
python app.py &

# Wait a moment for the backend to start
sleep 3

# Navigate to frontend directory
cd frontend

# Check if node_modules exists
if [ ! -d "node_modules" ]; then
    echo "Installing Node.js dependencies..."
    npm install
fi

# Start the frontend
echo "🎨 Starting React frontend..."
npm start

echo "✅ FISH 510 Chatbot is running!"
echo "Frontend: http://localhost:3000"
echo "Backend API: http://localhost:5000"
