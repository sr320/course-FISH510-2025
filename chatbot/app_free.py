"""
FISH 510 Course Chatbot - Free Version
Uses local embeddings and simple retrieval without OpenAI API
"""

import os
import logging
from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import SentenceTransformerEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import DirectoryLoader, TextLoader
import chromadb
from chromadb.config import Settings

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)
CORS(app)

# Initialize local embeddings (free)
embeddings = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")

# Initialize ChromaDB
client = chromadb.PersistentClient(path="./chroma_db")
collection_name = "fish510_course_content"

class CourseChatbot:
    def __init__(self):
        self.vectorstore = None
        self.setup_knowledge_base()
        
    def setup_knowledge_base(self):
        """Initialize the vector store"""
        try:
            # Load course documents
            loader = DirectoryLoader(
                "../", 
                glob="**/*.md",
                loader_cls=TextLoader,
                show_progress=True
            )
            documents = loader.load()
            
            # Split documents into chunks
            text_splitter = RecursiveCharacterTextSplitter(
                chunk_size=1000,
                chunk_overlap=200,
                length_function=len,
            )
            texts = text_splitter.split_documents(documents)
            
            # Create vector store
            self.vectorstore = Chroma.from_documents(
                documents=texts,
                embedding=embeddings,
                collection_name=collection_name,
                client=client
            )
            
            logger.info(f"Knowledge base initialized with {len(texts)} document chunks")
            
        except Exception as e:
            logger.error(f"Error setting up knowledge base: {e}")
            raise
    
    def query(self, question):
        """Query the chatbot with a question using simple retrieval"""
        try:
            # Find relevant documents
            docs = self.vectorstore.similarity_search(question, k=5)
            
            # Create response from retrieved documents
            context = "\n\n".join([doc.page_content for doc in docs])
            sources = [doc.metadata.get("source", "Unknown") for doc in docs]
            
            # Simple response based on context
            if context:
                response = f"""Based on the course materials, here's what I found:

{context[:2000]}...

This information comes from the FISH 510 course materials. For more detailed answers, please refer to the specific documents or contact your instructor.

Note: This is a simplified version without AI-generated responses. For full AI capabilities, please ensure your OpenAI API key has sufficient quota."""
            else:
                response = "I couldn't find relevant information in the course materials for that question. Please try rephrasing your question or check the course materials directly."
            
            return {
                "answer": response,
                "sources": sources
            }
        except Exception as e:
            logger.error(f"Error querying chatbot: {e}")
            return {
                "answer": "I'm sorry, I encountered an error processing your question. Please try again.",
                "sources": []
            }

# Initialize chatbot
chatbot = CourseChatbot()

@app.route('/api/chat', methods=['POST'])
def chat():
    """Handle chat messages"""
    try:
        data = request.get_json()
        question = data.get('message', '')
        
        if not question:
            return jsonify({"error": "No message provided"}), 400
        
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
    return jsonify({"status": "healthy", "service": "FISH 510 Course Chatbot (Free Version)"})

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
        "version": "Free Version (No OpenAI API required)",
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
    app.run(debug=True, host='0.0.0.0', port=5000)
