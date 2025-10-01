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
    app.run(debug=True, host='0.0.0.0', port=5000)
