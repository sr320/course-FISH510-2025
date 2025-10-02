"""
FISH 510 Course Chatbot - Enhanced Version
Uses OpenAI API with RAG system for intelligent responses
"""

import os
import logging
from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings
from langchain.chains import RetrievalQA
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import DirectoryLoader, TextLoader, PyPDFLoader
from langchain.prompts import PromptTemplate
import chromadb
from chromadb.config import Settings

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)
CORS(app)

# Configurable documents directory (set via DOCS_DIR; defaults to repo root)
# On Railway, working dir is /app (the chatbot folder), so ".." gets the repo root
DOCS_DIR = os.getenv("DOCS_DIR", "..")

# Initialize OpenAI components
llm = ChatOpenAI(
    model="gpt-4",
    temperature=0.1,
    openai_api_key=os.getenv("OPENAI_API_KEY")
)

embeddings = OpenAIEmbeddings(openai_api_key=os.getenv("OPENAI_API_KEY"))

# Initialize ChromaDB (disable anonymized telemetry to avoid PostHog errors)
client = chromadb.PersistentClient(
    path="./chroma_db",
    settings=Settings(anonymized_telemetry=False)
)
collection_name = "fish510_course_content"

class CourseChatbot:
    def __init__(self):
        self.vectorstore = None
        self.qa_chain = None
        self.setup_knowledge_base()
        
    def setup_knowledge_base(self):
        """Initialize the vector store and QA chain"""
        try:
            # Load course documents (Markdown + PDFs) from the configured directory
            logger.info(f"Loading documents from DOCS_DIR={DOCS_DIR}")
            logger.info(f"Absolute path: {os.path.abspath(DOCS_DIR)}")
            
            # Check if directory exists
            if not os.path.exists(DOCS_DIR):
                logger.error(f"DOCS_DIR does not exist: {DOCS_DIR}")
                raise FileNotFoundError(f"Directory not found: {DOCS_DIR}")
            
            loader_md = DirectoryLoader(
                DOCS_DIR,
                glob="**/*.md",
                loader_cls=TextLoader,
                show_progress=True
            )
            loader_pdf = DirectoryLoader(
                DOCS_DIR,
                glob="**/*.pdf",
                loader_cls=PyPDFLoader,
                show_progress=True
            )
            logger.info("Loading Markdown files...")
            md_docs = loader_md.load()
            logger.info("Loading PDF files...")
            pdf_docs = loader_pdf.load()
            documents = md_docs + pdf_docs
            logger.info(f"Loaded {len(md_docs)} markdown and {len(pdf_docs)} PDFs from {DOCS_DIR}")
            
            # Safety cap to avoid excessive indexing in constrained environments
            if len(documents) > 2000:
                documents = documents[:2000]
                logger.info("Capped documents to 2000 for performance")
            
            # Split documents into chunks
            logger.info(f"Splitting {len(documents)} documents into chunks...")
            text_splitter = RecursiveCharacterTextSplitter(
                chunk_size=800,
                chunk_overlap=160,
                length_function=len,
            )
            texts = text_splitter.split_documents(documents)
            logger.info(f"Created {len(texts)} text chunks")
            
            # Create vector store
            logger.info(f"Creating vector store with {len(texts)} chunks...")
            self.vectorstore = Chroma.from_documents(
                documents=texts,
                embedding=embeddings,
                collection_name=collection_name,
                client=client
            )
            logger.info("Vector store created successfully")
            
            # Create QA chain with custom prompt
            prompt_template = """You are a helpful assistant for FISH 510: Marine Organism Resilience and Epigenetics, a graduate seminar course at the University of Washington. 

Use the following pieces of context to answer the student's question about the course. If you don't know the answer based on the context, politely say that you don't have that information and suggest they check the course materials or contact the instructor.

Context: {context}

Question: {question}

Answer: Provide a helpful, accurate response based on the course content. Include relevant details about:
- Course structure and requirements
- Weekly topics and learning objectives  
- Assignment details and deadlines
- Discussion guidelines
- Research papers and readings
- Assessment methods

If the question is about a specific week or topic, reference the relevant materials and provide context about what students should focus on."""

            PROMPT = PromptTemplate(
                template=prompt_template,
                input_variables=["context", "question"]
            )
            
            logger.info("Creating QA chain...")
            self.qa_chain = RetrievalQA.from_chain_type(
                llm=llm,
                chain_type="stuff",
                retriever=self.vectorstore.as_retriever(search_kwargs={"k": 4}),
                chain_type_kwargs={"prompt": PROMPT},
                return_source_documents=True
            )
            
            logger.info(f"✅ Knowledge base initialized successfully with {len(texts)} document chunks")
            
        except Exception as e:
            logger.error(f"Error setting up knowledge base: {e}")
            # Do not raise; allow app to start and report not-ready
            self.vectorstore = None
            self.qa_chain = None
    
    def query(self, question):
        """Query the chatbot with a question"""
        try:
            logger.info(f"Querying chatbot with question: {question}")
            result = self.qa_chain({"query": question})
            logger.info(f"Got result from LLM: {result['result'][:200]}...")
            return {
                "answer": result["result"],
                "sources": [doc.metadata.get("source", "Unknown") for doc in result["source_documents"]]
            }
        except Exception as e:
            logger.error(f"Error querying chatbot: {e}")
            return {
                "answer": f"I'm sorry, I encountered an error processing your question: {str(e)}. Please try again.",
                "sources": []
            }

# Initialize chatbot (non-blocking)
chatbot = None

def initialize_chatbot():
    """Initialize chatbot in background"""
    global chatbot
    try:
        logger.info("=== Starting chatbot initialization ===")
        logger.info(f"DOCS_DIR: {DOCS_DIR}")
        logger.info(f"OpenAI API key present: {bool(os.getenv('OPENAI_API_KEY'))}")
        logger.info(f"Current working directory: {os.getcwd()}")
        chatbot = CourseChatbot()
        logger.info("=== Chatbot initialized successfully ===")
    except Exception as e:
        logger.error(f"=== FAILED to initialize chatbot ===")
        logger.error(f"Error: {e}", exc_info=True)
        chatbot = None

# Start initialization in background
import threading
init_thread = threading.Thread(target=initialize_chatbot)
init_thread.daemon = True
init_thread.start()

@app.route('/')
def home():
    """Home page with course information"""
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>FISH 510 Course Chatbot - Enhanced</title>
        <style>
            body { font-family: Arial, sans-serif; margin: 40px; background: #f0f9ff; }
            .container { max-width: 800px; margin: 0 auto; background: white; padding: 30px; border-radius: 10px; box-shadow: 0 2px 10px rgba(0,0,0,0.1); }
            h1 { color: #0369a1; }
            .chat-box { background: #f8fafc; padding: 20px; border-radius: 8px; margin: 20px 0; }
            .api-info { background: #e0f2fe; padding: 15px; border-radius: 5px; margin: 20px 0; }
            .enhanced { background: #dcfce7; border-left: 4px solid #16a34a; }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>🐠 FISH 510 Course Chatbot - Enhanced</h1>
            <h2>Marine Organism Resilience and Epigenetics</h2>
            
            <div class="enhanced">
                <h3>🚀 Enhanced Features:</h3>
                <ul>
                    <li><strong>AI-Powered Responses:</strong> GPT-4 powered intelligent responses</li>
                    <li><strong>Document Search:</strong> Searches through all course materials</li>
                    <li><strong>Context-Aware:</strong> Understands relationships between concepts</li>
                    <li><strong>Source Attribution:</strong> Shows which documents informed each response</li>
                </ul>
            </div>
            
            <div class="api-info">
                <h3>📚 Course Information:</h3>
                <p><strong>Instructor:</strong> Steven Roberts</p>
                <p><strong>University:</strong> University of Washington</p>
                <p><strong>Semester:</strong> Fall 2025</p>
                <p><strong>Credits:</strong> 2</p>
            </div>
            
            <div class="chat-box">
                <h3>🤖 Chat with the Enhanced Course Assistant</h3>
                <div id="chat-container">
                    <div id="messages" style="height: 300px; overflow-y: auto; border: 1px solid #ccc; padding: 10px; margin: 10px 0; background: white;"></div>
                    <div style="display: flex; gap: 10px;">
                        <input type="text" id="messageInput" placeholder="Ask any question about the course..." style="flex: 1; padding: 10px; border: 1px solid #ccc; border-radius: 5px;">
                        <button onclick="sendMessage()" style="padding: 10px 20px; background: #0369a1; color: white; border: none; border-radius: 5px; cursor: pointer;">Send</button>
                    </div>
                </div>
                
                <div style="margin-top: 20px;">
                    <p><strong>Quick Questions:</strong></p>
                    <div style="display: flex; flex-wrap: wrap; gap: 10px;">
                        <button onclick="askQuestion('What is this course about?')" style="padding: 5px 10px; background: #e0f2fe; border: 1px solid #0369a1; border-radius: 15px; cursor: pointer; font-size: 12px;">What is this course about?</button>
                        <button onclick="askQuestion('Tell me about assignments')" style="padding: 5px 10px; background: #e0f2fe; border: 1px solid #0369a1; border-radius: 15px; cursor: pointer; font-size: 12px;">Tell me about assignments</button>
                        <button onclick="askQuestion('Explain DNA methylation in marine organisms')" style="padding: 5px 10px; background: #e0f2fe; border: 1px solid #0369a1; border-radius: 15px; cursor: pointer; font-size: 12px;">Explain DNA methylation</button>
                        <button onclick="askQuestion('What papers should I read for Week 2?')" style="padding: 5px 10px; background: #e0f2fe; border: 1px solid #0369a1; border-radius: 15px; cursor: pointer; font-size: 12px;">Week 2 readings</button>
                    </div>
                </div>
            </div>
            
            <script>
                function addMessage(message, isUser = false, sources = []) {
                    const messagesDiv = document.getElementById('messages');
                    const messageDiv = document.createElement('div');
                    messageDiv.style.margin = '10px 0';
                    messageDiv.style.padding = '10px';
                    messageDiv.style.borderRadius = '5px';
                    messageDiv.style.backgroundColor = isUser ? '#e0f2fe' : '#f8fafc';
                    messageDiv.style.borderLeft = isUser ? '4px solid #0369a1' : '4px solid #14b8a6';
                    
                    if (isUser) {
                        messageDiv.innerHTML = '<strong>You:</strong> ' + message;
                    } else {
                        let sourcesHtml = '';
                        if (sources && sources.length > 0) {
                            sourcesHtml = '<div style="margin-top: 10px; padding: 8px; background: #f1f5f9; border-radius: 3px; font-size: 12px;"><strong>Sources:</strong> ' + sources.slice(0, 3).join(', ') + '</div>';
                        }
                        messageDiv.innerHTML = '<strong>Assistant:</strong> ' + message.replace(/\\n/g, '<br>') + sourcesHtml;
                    }
                    
                    messagesDiv.appendChild(messageDiv);
                    messagesDiv.scrollTop = messagesDiv.scrollHeight;
                }
                
                async function sendMessage() {
                    const input = document.getElementById('messageInput');
                    const message = input.value.trim();
                    
                    if (!message) return;
                    
                    addMessage(message, true);
                    input.value = '';
                    
                    // Show typing indicator
                    const typingDiv = document.createElement('div');
                    typingDiv.id = 'typing';
                    typingDiv.innerHTML = '<em>Assistant is thinking...</em>';
                    document.getElementById('messages').appendChild(typingDiv);
                    
                    try {
                        const response = await fetch('/api/chat', {
                            method: 'POST',
                            headers: {
                                'Content-Type': 'application/json',
                            },
                            body: JSON.stringify({ message: message })
                        });
                        
                        const data = await response.json();
                        document.getElementById('typing').remove();
                        addMessage(data.response, false, data.sources);
                    } catch (error) {
                        document.getElementById('typing').remove();
                        addMessage('Sorry, I encountered an error. Please try again.');
                    }
                }
                
                function askQuestion(question) {
                    document.getElementById('messageInput').value = question;
                    sendMessage();
                }
                
                // Allow Enter key to send message
                document.getElementById('messageInput').addEventListener('keypress', function(e) {
                    if (e.key === 'Enter') {
                        sendMessage();
                    }
                });
                
                // Add welcome message
                addMessage('Welcome to the Enhanced FISH 510 Course Assistant! I can search through all course materials and provide intelligent responses. What would you like to know?');
            </script>
            
            <div class="api-info">
                <h3>💡 Enhanced Capabilities:</h3>
                <ul>
                    <li>Search through all course documents and readings</li>
                    <li>Understand complex questions and concepts</li>
                    <li>Provide detailed explanations with sources</li>
                    <li>Connect different course topics and materials</li>
                    <li>Answer nuanced questions about marine epigenetics</li>
                </ul>
            </div>
        </div>
    </body>
    </html>
    """

@app.route('/api/chat', methods=['POST'])
def chat():
    """Handle chat messages"""
    try:
        data = request.get_json()
        question = data.get('message', '')
        
        if not question:
            return jsonify({"error": "No message provided"}), 400
        
        # Check if chatbot is ready
        if chatbot is None or chatbot.qa_chain is None:
            return jsonify({
                "response": "The enhanced chatbot is still initializing. Please wait a moment and try again, or use the free version at: https://course-fish510-2025-production.up.railway.app",
                "sources": []
            })
        
        # Get response from chatbot
        response = chatbot.query(question)
        
        return jsonify({
            "response": response["answer"],
            "sources": response["sources"]
        })
        
    except Exception as e:
        logger.error(f"Error in chat endpoint: {e}")
        return jsonify({"error": "Internal server error"}), 500

@app.route('/api/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    try:
        ready = bool(chatbot and getattr(chatbot, "vectorstore", None))
        return jsonify({
            "status": "ok", 
            "service": "FISH 510 Course Chatbot - Enhanced Version",
            "knowledge_base_ready": ready
        })
    except Exception as e:
        logger.error(f"Health check error: {e}")
        return jsonify({
            "status": "ok", 
            "service": "FISH 510 Course Chatbot - Enhanced Version",
            "knowledge_base_ready": False
        })

@app.route('/api/startup', methods=['GET'])
def startup_check():
    """Startup check endpoint - responds immediately"""
    return jsonify({
        "status": "starting", 
        "service": "FISH 510 Course Chatbot - Enhanced Version",
        "message": "Initializing knowledge base, please wait...",
        "knowledge_base_ready": bool(chatbot and getattr(chatbot, "vectorstore", None))
    })

@app.route('/api/debug', methods=['GET'])
def debug_info():
    """Debug endpoint to check chatbot status"""
    return jsonify({
        "chatbot_exists": chatbot is not None,
        "chatbot_type": str(type(chatbot)),
        "has_vectorstore": bool(chatbot and hasattr(chatbot, 'vectorstore') and chatbot.vectorstore),
        "has_qa_chain": bool(chatbot and hasattr(chatbot, 'qa_chain') and chatbot.qa_chain),
        "docs_dir": DOCS_DIR,
        "docs_dir_exists": os.path.exists(DOCS_DIR),
        "docs_dir_absolute": os.path.abspath(DOCS_DIR),
        "current_working_dir": os.getcwd(),
        "openai_key_present": bool(os.getenv('OPENAI_API_KEY')),
    })

@app.route('/api/test-llm', methods=['GET'])
def test_llm():
    """Test endpoint to verify LLM is working"""
    try:
        if chatbot and chatbot.qa_chain:
            # Simple test query
            result = chatbot.query("What is DNA methylation?")
            return jsonify({
                "status": "success",
                "llm_working": True,
                "test_response": result["answer"][:200] + "...",
                "sources": result["sources"]
            })
        else:
            return jsonify({
                "status": "error",
                "llm_working": False,
                "message": "Chatbot not initialized yet",
                "debug_info": {
                    "chatbot_exists": chatbot is not None,
                    "has_qa_chain": bool(chatbot and hasattr(chatbot, 'qa_chain') and chatbot.qa_chain)
                }
            })
    except Exception as e:
        return jsonify({
            "status": "error",
            "llm_working": False,
            "error": str(e)
        })

@app.route('/api/course-info', methods=['GET'])
def course_info():
    """Get basic course information"""
    return jsonify({
        "course": "FISH 510: Marine Organism Resilience and Epigenetics",
        "instructor": "Steven Roberts",
        "university": "University of Washington",
        "school": "School of Aquatic and Fishery Sciences",
        "semester": "Fall 2025",
        "credits": 2,
        "format": "Graduate Seminar",
        "version": "Enhanced Version (OpenAI GPT-4 + RAG)",
        "features": [
            "AI-powered intelligent responses",
            "Document search and retrieval",
            "Source attribution",
            "Context-aware conversations",
            "Comprehensive course knowledge"
        ],
        "topics": [
            "DNA methylation in marine species",
            "Environmental stressors and gene expression",
            "Histone modifications and chromatin structure",
            "Non-coding RNAs and regulation",
            "Transgenerational epigenetic inheritance",
            "Climate change and epigenetic responses",
            "Population-level epigenetic variation",
            "Methodology and techniques",
            "Current frontiers and future directions"
        ]
    })

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=False, host='0.0.0.0', port=port)