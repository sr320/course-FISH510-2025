# FISH 510 Course Chatbot

This repository includes an AI-powered chatbot designed to help students with the FISH 510: Marine Organism Resilience and Epigenetics graduate seminar course.

## 🤖 What is the Chatbot?

The chatbot is a web-based AI assistant that can answer questions about:
- **Course Content**: Weekly topics, learning objectives, and key concepts
- **Assignments**: Deadlines, requirements, and expectations
- **Readings**: Research papers, summaries, and discussion points
- **Course Logistics**: Schedule, policies, and participation guidelines

## 🚀 Quick Start

1. **Navigate to the chatbot directory**:
   ```bash
   cd chatbot
   ```

2. **Set up your OpenAI API key**:
   ```bash
   cp env_template.txt .env
   # Edit .env and add your OpenAI API key
   ```

3. **Run the chatbot**:
   ```bash
   ./run.sh
   ```

4. **Open your browser** to http://localhost:3000

## 💡 How It Works

The chatbot uses **Retrieval-Augmented Generation (RAG)** technology:

1. **Document Indexing**: All course materials (syllabus, weekly content, papers) are automatically processed and indexed
2. **Semantic Search**: When you ask a question, it finds the most relevant course materials
3. **AI Response**: It uses GPT-4 to generate accurate, course-specific answers
4. **Source Attribution**: Shows which course documents informed each response

## 🎯 Example Questions

Try asking the chatbot:

- "What are the learning objectives for Week 3?"
- "Tell me about DNA methylation in marine organisms"
- "What papers do I need to read this week?"
- "How does climate change affect epigenetic processes?"
- "What are the assignment deadlines?"
- "Explain transgenerational inheritance"

## 🏗️ Technical Architecture

- **Backend**: Python Flask API with LangChain RAG system
- **Frontend**: React with Tailwind CSS (marine-themed design)
- **Vector Database**: ChromaDB for semantic search
- **AI Model**: OpenAI GPT-4 for response generation
- **Document Processing**: Automatic indexing of all markdown files

## 📁 Project Structure

```
chatbot/
├── app.py                 # Flask backend API
├── requirements.txt       # Python dependencies
├── frontend/             # React web interface
│   ├── src/
│   │   ├── App.js        # Main React component
│   │   └── index.css     # Styling
│   └── package.json      # Node.js dependencies
├── README.md             # Detailed documentation
├── SETUP.md              # Quick setup guide
├── run.sh                # Automated startup script
└── docker-compose.yml    # Docker deployment
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

The chatbot has access to all course materials:
- Syllabus and course policies
- Weekly learning objectives and topics
- Research papers and supplementary readings
- Assignment descriptions and deadlines
- Discussion guidelines and participation requirements
- GitHub Discussions structure and expectations

## 🔒 Privacy & Security

- **Local Processing**: Course documents are processed locally
- **API Usage**: Only question content is sent to OpenAI (no course materials)
- **No Storage**: Conversations are not stored or logged
- **Academic Use**: Designed specifically for educational purposes

## 🛠️ Customization

The chatbot can be customized by:
- **Adding Content**: New course materials are automatically indexed
- **Modifying Prompts**: Adjust the AI's response style and focus
- **UI Changes**: Update the interface design and features
- **New Features**: Add functionality like assignment tracking or study guides

## 📖 Full Documentation

For detailed setup instructions, troubleshooting, and technical documentation, see:
- `chatbot/README.md` - Complete technical documentation
- `chatbot/SETUP.md` - Quick setup guide

---

**Ready to try it?** Navigate to the `chatbot/` directory and follow the setup instructions!

*This chatbot is part of the FISH 510 course materials and is designed to enhance student learning and course engagement.*
