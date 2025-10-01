"""
FISH 510 Course Chatbot
A RAG-based chatbot for Marine Organism Resilience and Epigenetics course
"""

import os
import logging
from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import OpenAIEmbeddings
from langchain.chains import RetrievalQA
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import DirectoryLoader, TextLoader
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

# Initialize OpenAI components
llm = ChatOpenAI(
    model="gpt-4",
    temperature=0.1,
    openai_api_key=os.getenv("OPENAI_API_KEY")
)

embeddings = OpenAIEmbeddings(openai_api_key=os.getenv("OPENAI_API_KEY"))

# Initialize ChromaDB
client = chromadb.PersistentClient(path="./chroma_db")
collection_name = "fish510_course_content"

class CourseChatbot:
    def __init__(self):
        self.vectorstore = None
        self.qa_chain = None
        self.setup_knowledge_base()
        
    def setup_knowledge_base(self):
        """Initialize the vector store and QA chain"""
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
            
            self.qa_chain = RetrievalQA.from_chain_type(
                llm=llm,
                chain_type="stuff",
                retriever=self.vectorstore.as_retriever(search_kwargs={"k": 5}),
                chain_type_kwargs={"prompt": PROMPT},
                return_source_documents=True
            )
            
            logger.info(f"Knowledge base initialized with {len(texts)} document chunks")
            
        except Exception as e:
            logger.error(f"Error setting up knowledge base: {e}")
            raise
    
    def query(self, question):
        """Query the chatbot with a question"""
        try:
            result = self.qa_chain({"query": question})
            return {
                "answer": result["result"],
                "sources": [doc.metadata.get("source", "Unknown") for doc in result["source_documents"]]
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
    return jsonify({"status": "healthy", "service": "FISH 510 Course Chatbot"})

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
