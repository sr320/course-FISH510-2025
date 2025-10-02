"""
FISH 510 Course Chatbot - Simple Version
Basic Flask app that works without document loading
"""

import os
import logging
from flask import Flask, request, jsonify
from flask_cors import CORS

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    """Home page with course information"""
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>FISH 510 Course Chatbot</title>
        <style>
            body { font-family: Arial, sans-serif; margin: 40px; background: #f0f9ff; }
            .container { max-width: 800px; margin: 0 auto; background: white; padding: 30px; border-radius: 10px; box-shadow: 0 2px 10px rgba(0,0,0,0.1); }
            h1 { color: #0369a1; }
            .chat-box { background: #f8fafc; padding: 20px; border-radius: 8px; margin: 20px 0; }
            .api-info { background: #e0f2fe; padding: 15px; border-radius: 5px; margin: 20px 0; }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>🐠 FISH 510 Course Chatbot</h1>
            <h2>Marine Organism Resilience and Epigenetics</h2>
            
            <div class="api-info">
                <h3>📚 Course Information:</h3>
                <p><strong>Instructor:</strong> Steven Roberts</p>
                <p><strong>University:</strong> University of Washington</p>
                <p><strong>Semester:</strong> Fall 2025</p>
                <p><strong>Credits:</strong> 2</p>
            </div>
            
            <div class="chat-box">
                <h3>🤖 Chat with the Course Assistant</h3>
                <div id="chat-container">
                    <div id="messages" style="height: 300px; overflow-y: auto; border: 1px solid #ccc; padding: 10px; margin: 10px 0; background: white;"></div>
                    <div style="display: flex; gap: 10px;">
                        <input type="text" id="messageInput" placeholder="Ask a question about the course..." style="flex: 1; padding: 10px; border: 1px solid #ccc; border-radius: 5px;">
                        <button onclick="sendMessage()" style="padding: 10px 20px; background: #0369a1; color: white; border: none; border-radius: 5px; cursor: pointer;">Send</button>
                    </div>
                </div>
                
                <div style="margin-top: 20px;">
                    <p><strong>Quick Questions:</strong></p>
                    <div style="display: flex; flex-wrap: wrap; gap: 10px;">
                        <button onclick="askQuestion('What is this course about?')" style="padding: 5px 10px; background: #e0f2fe; border: 1px solid #0369a1; border-radius: 15px; cursor: pointer; font-size: 12px;">What is this course about?</button>
                        <button onclick="askQuestion('Tell me about assignments')" style="padding: 5px 10px; background: #e0f2fe; border: 1px solid #0369a1; border-radius: 15px; cursor: pointer; font-size: 12px;">Tell me about assignments</button>
                        <button onclick="askQuestion('Explain DNA methylation')" style="padding: 5px 10px; background: #e0f2fe; border: 1px solid #0369a1; border-radius: 15px; cursor: pointer; font-size: 12px;">Explain DNA methylation</button>
                        <button onclick="askQuestion('What papers should I read?')" style="padding: 5px 10px; background: #e0f2fe; border: 1px solid #0369a1; border-radius: 15px; cursor: pointer; font-size: 12px;">What papers should I read?</button>
                    </div>
                </div>
            </div>
            
            <script>
                function addMessage(message, isUser = false) {
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
                        messageDiv.innerHTML = '<strong>Assistant:</strong> ' + message.replace(/\\n/g, '<br>');
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
                    
                    try {
                        const response = await fetch('/api/chat', {
                            method: 'POST',
                            headers: {
                                'Content-Type': 'application/json',
                            },
                            body: JSON.stringify({ message: message })
                        });
                        
                        const data = await response.json();
                        addMessage(data.response);
                    } catch (error) {
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
                addMessage('Welcome to FISH 510! I can help you with course content, assignments, readings, and concepts in marine epigenetics. What would you like to know?');
            </script>
            
            <div class="api-info">
                <h3>💡 Example Questions:</h3>
                <p>Try asking:</p>
                <ul>
                    <li>"What is this course about?"</li>
                    <li>"Tell me about assignments"</li>
                    <li>"What papers should I read?"</li>
                    <li>"Explain DNA methylation"</li>
                    <li>"How does climate change affect marine organisms?"</li>
                </ul>
            </div>
        </div>
    </body>
    </html>
    """

@app.route('/api/chat', methods=['POST'])
def chat():
    """Handle chat messages with simple responses"""
    try:
        data = request.get_json()
        question = data.get('message', '')
        
        if not question:
            return jsonify({"error": "No message provided"}), 400
        
        # Simple responses based on keywords
        question_lower = question.lower()
        
        if 'course' in question_lower or 'fish 510' in question_lower:
            response = """FISH 510: Marine Organism Resilience and Epigenetics

📚 **Course Information:**
• Graduate Seminar (2 credits)
• Instructor: Steven Roberts
• University: Washington
• Semester: Fall 2025

🎯 **Key Topics:**
• DNA methylation in marine species
• Environmental stressors and gene expression
• Histone modifications and chromatin structure
• Non-coding RNAs and regulation
• Transgenerational epigenetic inheritance
• Climate change and epigenetic responses
• Population-level epigenetic variation
• Methodology and techniques

📖 **Course Structure:**
10 weekly modules covering different aspects of marine epigenetics and organism resilience."""
            
        elif 'assignment' in question_lower or 'deadline' in question_lower:
            response = """**Assignment Information:**

📝 **Assessment Methods:**
• Participation and Discussion (40%)
• Literature Presentations (30%)
• Research Synthesis Paper (30%)

📅 **Important Dates:**
• Weekly discussion posts: Due by Thursday of each week
• Peer responses: Due by Monday of each week
• Presentation assignments: Individual scheduling during Weeks 3-10
• Final research synthesis paper: Due Week 10

📋 **Assignment Types:**
• Course introduction post (Week 1)
• Environmental stressor literature review (Week 2)
• Student-led paper presentations (Weeks 3-10)
• Final research synthesis paper (Week 10)"""
            
        elif 'reading' in question_lower or 'paper' in question_lower:
            response = """**Reading Materials:**

📚 **Key Papers by Week:**
• Week 1: Eirin-Lopez & Putnam (2019) - Marine environmental epigenetics
• Week 2: Hofmann (2017), Kenkel & Matz (2016) - Environmental stressors
• Week 3-4: DNA methylation and chromatin studies
• Week 5-6: Non-coding RNAs and transgenerational inheritance
• Week 7-8: Climate change and population variation
• Week 9-10: Methodology and future directions

📖 **Access:**
• All papers available through course repository
• UW Libraries electronic resources
• Open access publications included

💡 **Reading Tips:**
• Focus on methodology and key findings
• Note experimental approaches and limitations
• Connect to broader marine science themes"""
            
        elif 'dna methylation' in question_lower or 'methylation' in question_lower:
            response = """**DNA Methylation in Marine Species:**

🧬 **Key Concepts:**
• DNA methylation is a key epigenetic mechanism
• Involves addition of methyl groups to cytosine bases
• Regulates gene expression without changing DNA sequence
• Important for environmental adaptation in marine organisms

🐠 **Marine Context:**
• Unique patterns in marine species (e.g., intragenic methylation in oysters)
• Environmental stressors can alter methylation patterns
• Transgenerational inheritance of methylation changes
• Role in thermal tolerance and stress responses

📊 **Research Methods:**
• Bisulfite sequencing for methylation detection
• Whole-genome methylation profiling
• Correlation with gene expression patterns
• Population-level methylation variation studies"""
            
        elif 'climate' in question_lower or 'warming' in question_lower:
            response = """**Climate Change and Epigenetic Responses:**

🌊 **Environmental Stressors:**
• Ocean warming and thermal stress
• Ocean acidification (pH changes)
• Hypoxia and oxygen stress
• Salinity fluctuations

🧬 **Epigenetic Responses:**
• DNA methylation changes under stress
• Histone modifications and chromatin remodeling
• Non-coding RNA regulation
• Transgenerational acclimation

🔬 **Research Examples:**
• Coral bleaching and methylation patterns
• Fish thermal tolerance inheritance
• Population-level adaptation mechanisms
• Long-term climate adaptation strategies

📈 **Implications:**
• Rapid adaptation potential
• Conservation and management applications
• Restoration strategies
• Future research directions"""
            
        else:
            response = """Welcome to the FISH 510 Course Assistant! 

I can help you with information about:
• Course structure and requirements
• Assignment deadlines and expectations
• Reading materials and papers
• Key concepts in marine epigenetics
• Climate change and organism responses

Try asking about:
- "What is this course about?"
- "Tell me about assignments"
- "What papers should I read?"
- "Explain DNA methylation"
- "How does climate change affect marine organisms?"

For detailed questions about specific topics, please refer to the course materials or contact your instructor."""
        
        return jsonify({
            "response": response,
            "sources": ["Course syllabus and materials"]
        })
        
    except Exception as e:
        logger.error(f"Error in chat endpoint: {e}")
        return jsonify({"error": "Internal server error"}), 500

@app.route('/api/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({"status": "healthy", "service": "FISH 510 Course Chatbot (Simple Version)"})

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
        "version": "Simple Version (No external dependencies)",
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
