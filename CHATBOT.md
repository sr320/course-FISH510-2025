# FISH 510 Course Chatbot

This repository includes a web-based chatbot designed to help students with the FISH 510: Marine Organism Resilience and Epigenetics graduate seminar course.

## 🤖 What is the Chatbot?

The chatbot is a web-based AI assistant that can answer questions about:
- **Course Content**: Weekly topics, learning objectives, and key concepts
- **Assignments**: Deadlines, requirements, and expectations
- **Readings**: Research papers, summaries, and discussion points
- **Course Logistics**: Schedule, policies, and participation guidelines

## 🚀 Quick Start

### **For Students (Use the Live Version)**
The chatbot is already deployed and ready to use at:
**https://course-fish510-2025-production.up.railway.app**

Simply visit the URL and start asking questions!

### **For Development/Instructors**
1. **Navigate to the chatbot directory**:
   ```bash
   cd chatbot
   ```

2. **Run the chatbot locally**:
   ```bash
   python app.py
   ```

3. **Open your browser** to http://localhost:5000

## 💡 How It Works

The chatbot uses **keyword-based intelligent responses**:

1. **Smart Recognition**: Recognizes keywords in student questions
2. **Pre-built Responses**: Provides detailed, course-specific answers
3. **Comprehensive Coverage**: Covers all major course topics and concepts
4. **Reliable Operation**: No external API dependencies, always available

## 🎯 Example Questions

Try asking the chatbot:

- "What are the learning objectives for Week 3?"
- "Tell me about DNA methylation in marine organisms"
- "What papers do I need to read this week?"
- "How does climate change affect epigenetic processes?"
- "What are the assignment deadlines?"
- "Explain transgenerational inheritance"

## 🏗️ Technical Architecture

- **Backend**: Python Flask API with keyword-based responses
- **Frontend**: Built-in HTML interface (marine-themed design)
- **Deployment**: Railway cloud platform
- **Response System**: Intelligent keyword matching and pre-built responses
- **Reliability**: No external dependencies, always available

## 📁 Project Structure

```
chatbot/
├── app.py                 # Flask backend with built-in HTML frontend
├── requirements.txt       # Python dependencies (minimal)
├── app_simple.py         # Simple version (currently deployed)
├── app_free.py           # Free version with local embeddings
├── frontend/             # React frontend (optional)
├── README.md             # Detailed documentation
├── DEPLOYMENT.md         # Deployment guide
├── SECURITY.md           # Security best practices
└── railway.json          # Railway deployment config
```

## 🔧 For Instructors

The chatbot can help with:
- **Student Support**: Answering common questions about course content
- **Course Logistics**: Providing quick access to schedules and requirements
- **Content Delivery**: Helping students navigate complex topics
- **24/7 Availability**: Students can get help outside of office hours

## 🎓 For Students

The chatbot provides:
- **Instant Help**: Get answers to course questions anytime
- **Study Support**: Understand readings and concepts better
- **Assignment Guidance**: Clarify requirements and expectations
- **Course Navigation**: Find relevant materials quickly

## 🌊 Course Integration

The chatbot is designed specifically for FISH 510 and includes:
- **Marine Biology Focus**: Specialized knowledge about marine epigenetics
- **Graduate Level**: Appropriate depth for seminar-level discussions
- **Research Integration**: Access to all assigned papers and readings
- **UW Context**: University-specific policies and resources

## 📚 Content Coverage

The chatbot provides comprehensive information about:
- Course structure and learning objectives
- Assignment deadlines and requirements
- Key concepts in marine epigenetics
- Research papers and reading materials
- Climate change and organism responses
- DNA methylation and epigenetic mechanisms
- Course policies and participation guidelines

## 🔒 Privacy & Security

- **No External APIs**: No data sent to external services
- **Local Responses**: All responses generated locally
- **No Storage**: Conversations are not stored or logged
- **Academic Use**: Designed specifically for educational purposes
- **Open Source**: All code is transparent and auditable

## 🛠️ Customization

The chatbot can be customized by:
- **Adding Responses**: Modify the keyword responses in `app.py`
- **UI Changes**: Update the HTML interface and styling
- **New Features**: Add new question categories and responses
- **Deployment**: Easy deployment to Railway or other platforms

## 📖 Full Documentation

For detailed setup instructions, troubleshooting, and technical documentation, see:
- `chatbot/README.md` - Complete technical documentation
- `chatbot/SETUP.md` - Quick setup guide

---

**Ready to try it?** Navigate to the `chatbot/` directory and follow the setup instructions!

*This chatbot is part of the FISH 510 course materials and is designed to enhance student learning and course engagement.*
