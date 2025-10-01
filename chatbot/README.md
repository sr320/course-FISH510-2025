# FISH 510 Course Chatbot

A web-based AI assistant for the FISH 510: Marine Organism Resilience and Epigenetics graduate seminar course. The chatbot uses Retrieval-Augmented Generation (RAG) to answer questions about course content, assignments, readings, and materials.

## Features

- 🤖 **AI-Powered Responses**: Uses OpenAI GPT-4 with course-specific context
- 📚 **Course Knowledge Base**: Indexes all course materials, readings, and discussions
- 💬 **Real-time Chat Interface**: Modern, responsive web interface
- 🔍 **Semantic Search**: Finds relevant information from course documents
- 📖 **Source Attribution**: Shows which course materials informed each response
- 🎨 **Marine Theme**: Beautiful ocean-inspired design

## Architecture

- **Backend**: Python Flask API with LangChain RAG system
- **Frontend**: React with Tailwind CSS
- **Vector Database**: ChromaDB for semantic search
- **LLM**: OpenAI GPT-4 for response generation
- **Document Processing**: Automatic indexing of markdown files

## Setup Instructions

### Prerequisites

- Python 3.8+
- Node.js 16+
- OpenAI API key

### 1. Backend Setup

```bash
# Navigate to chatbot directory
cd chatbot

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Set up environment variables
cp env_template.txt .env
# Edit .env and add your OpenAI API key
```

### 2. Frontend Setup

```bash
# Navigate to frontend directory
cd frontend

# Install dependencies
npm install

# Start development server
npm start
```

### 3. Running the Application

```bash
# Terminal 1: Start backend
cd chatbot
python app.py

# Terminal 2: Start frontend
cd frontend
npm start
```

The application will be available at:
- Frontend: http://localhost:3000
- Backend API: http://localhost:5000

## Usage

### For Students

1. **Course Questions**: Ask about weekly topics, learning objectives, or course structure
2. **Assignment Help**: Get information about deadlines, requirements, and expectations
3. **Reading Support**: Ask questions about assigned papers and supplementary materials
4. **Discussion Topics**: Explore key concepts and research questions

### Example Questions

- "What are the learning objectives for Week 3?"
- "Tell me about DNA methylation in marine organisms"
- "What papers do I need to read for Week 2?"
- "How does climate change affect epigenetic processes?"
- "What are the assignment deadlines?"

### For Instructors

The chatbot can help answer common student questions and provide quick access to course information. It's particularly useful for:

- Course logistics and deadlines
- Assignment requirements and grading
- Discussion topics and expectations
- Research paper summaries and key points

## API Endpoints

- `POST /api/chat` - Send a message to the chatbot
- `GET /api/course-info` - Get basic course information
- `GET /api/health` - Health check endpoint

## Course Content Coverage

The chatbot has access to:

- **Course Structure**: Syllabus, schedule, and requirements
- **Weekly Content**: Learning objectives, topics, and activities
- **Readings**: Research papers and supplementary materials
- **Assignments**: Details, deadlines, and expectations
- **Discussions**: Guidelines and participation requirements
- **Resources**: Additional materials and tools

## Technical Details

### Document Processing

The system automatically processes all markdown files in the course repository:
- Splits documents into semantic chunks
- Creates vector embeddings using OpenAI
- Stores in ChromaDB for efficient retrieval

### Response Generation

1. User asks a question
2. System searches course documents for relevant content
3. Retrieves top 5 most relevant chunks
4. Passes context to GPT-4 with course-specific prompt
5. Returns response with source attribution

### Customization

To add new content to the knowledge base:
1. Add markdown files to the course repository
2. Restart the backend server
3. The system will automatically reindex all documents

## Deployment

### Local Development

Follow the setup instructions above for local development.

### Production Deployment

For production deployment, consider:

1. **Environment Variables**:
   - Set `FLASK_ENV=production`
   - Use production OpenAI API key
   - Configure proper CORS settings

2. **Server Setup**:
   - Use a production WSGI server (e.g., Gunicorn)
   - Set up reverse proxy (e.g., Nginx)
   - Configure SSL certificates

3. **Frontend Build**:
   ```bash
   cd frontend
   npm run build
   ```

4. **Database Persistence**:
   - ChromaDB data is stored in `./chroma_db`
   - Ensure proper backup and persistence

## Troubleshooting

### Common Issues

1. **OpenAI API Key**: Ensure your API key is correctly set in `.env`
2. **Port Conflicts**: Change ports in `app.py` and `package.json` if needed
3. **CORS Issues**: Check that frontend URL is allowed in backend CORS settings
4. **Document Loading**: Ensure course files are accessible from the chatbot directory

### Performance

- First startup may take time to index all course documents
- Subsequent queries are fast due to vector database caching
- Consider document chunking strategy for very large files

## Contributing

To improve the chatbot:

1. **Content Updates**: Add new course materials to the repository
2. **Prompt Engineering**: Modify the system prompt in `app.py`
3. **UI Improvements**: Update React components in `frontend/src/`
4. **New Features**: Add new API endpoints and frontend functionality

## License

This project is part of the FISH 510 course materials at the University of Washington.

---

**Course**: FISH 510: Marine Organism Resilience and Epigenetics  
**Instructor**: Steven Roberts  
**University**: University of Washington  
**Semester**: Fall 2025
