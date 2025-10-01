import React, { useState, useEffect, useRef } from 'react';
import { Send, Bot, User, BookOpen, Clock, Users, FileText } from 'lucide-react';
import axios from 'axios';

const API_BASE_URL = process.env.REACT_APP_API_URL || 'http://localhost:5000';

function App() {
  const [messages, setMessages] = useState([]);
  const [inputMessage, setInputMessage] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const [courseInfo, setCourseInfo] = useState(null);
  const messagesEndRef = useRef(null);

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: "smooth" });
  };

  useEffect(() => {
    scrollToBottom();
  }, [messages]);

  useEffect(() => {
    // Load course information
    const fetchCourseInfo = async () => {
      try {
        const response = await axios.get(`${API_BASE_URL}/api/course-info`);
        setCourseInfo(response.data);
      } catch (error) {
        console.error('Error fetching course info:', error);
      }
    };

    fetchCourseInfo();

    // Add welcome message
    setMessages([
      {
        id: 1,
        text: "Welcome to FISH 510! I'm your course assistant for Marine Organism Resilience and Epigenetics. I can help you with course content, assignments, readings, and any questions about the seminar. What would you like to know?",
        sender: 'bot',
        timestamp: new Date().toLocaleTimeString()
      }
    ]);
  }, []);

  const sendMessage = async (e) => {
    e.preventDefault();
    if (!inputMessage.trim() || isLoading) return;

    const userMessage = {
      id: Date.now(),
      text: inputMessage,
      sender: 'user',
      timestamp: new Date().toLocaleTimeString()
    };

    setMessages(prev => [...prev, userMessage]);
    setInputMessage('');
    setIsLoading(true);

    try {
      const response = await axios.post(`${API_BASE_URL}/api/chat`, {
        message: inputMessage
      });

      const botMessage = {
        id: Date.now() + 1,
        text: response.data.response,
        sender: 'bot',
        timestamp: new Date().toLocaleTimeString(),
        sources: response.data.sources
      };

      setMessages(prev => [...prev, botMessage]);
    } catch (error) {
      console.error('Error sending message:', error);
      const errorMessage = {
        id: Date.now() + 1,
        text: "I'm sorry, I encountered an error. Please try again or check if the server is running.",
        sender: 'bot',
        timestamp: new Date().toLocaleTimeString()
      };
      setMessages(prev => [...prev, errorMessage]);
    } finally {
      setIsLoading(false);
    }
  };

  const suggestedQuestions = [
    "What are the course requirements?",
    "Tell me about Week 1 readings",
    "What is DNA methylation?",
    "How does climate change affect marine organisms?",
    "What are the assignment deadlines?",
    "Explain transgenerational inheritance"
  ];

  return (
    <div className="min-h-screen bg-gradient-to-br from-ocean-50 to-marine-50">
      {/* Header */}
      <div className="bg-white shadow-sm border-b border-ocean-200">
        <div className="max-w-4xl mx-auto px-4 py-4">
          <div className="flex items-center space-x-3">
            <div className="p-2 bg-ocean-500 rounded-lg">
              <BookOpen className="h-6 w-6 text-white" />
            </div>
            <div>
              <h1 className="text-xl font-semibold text-gray-900">
                FISH 510 Course Assistant
              </h1>
              <p className="text-sm text-gray-600">
                Marine Organism Resilience and Epigenetics
              </p>
            </div>
          </div>
          {courseInfo && (
            <div className="mt-3 flex flex-wrap gap-4 text-sm text-gray-600">
              <div className="flex items-center space-x-1">
                <Users className="h-4 w-4" />
                <span>Graduate Seminar</span>
              </div>
              <div className="flex items-center space-x-1">
                <Clock className="h-4 w-4" />
                <span>Fall 2025</span>
              </div>
              <div className="flex items-center space-x-1">
                <FileText className="h-4 w-4" />
                <span>{courseInfo.credits} Credits</span>
              </div>
            </div>
          )}
        </div>
      </div>

      {/* Main Chat Interface */}
      <div className="max-w-4xl mx-auto px-4 py-6">
        <div className="bg-white rounded-xl shadow-lg border border-gray-200 h-[600px] flex flex-col">
          {/* Messages */}
          <div className="flex-1 overflow-y-auto p-6 space-y-4">
            {messages.map((message) => (
              <div
                key={message.id}
                className={`flex ${message.sender === 'user' ? 'justify-end' : 'justify-start'} message-enter`}
              >
                <div
                  className={`max-w-[80%] rounded-lg px-4 py-2 ${
                    message.sender === 'user'
                      ? 'bg-ocean-500 text-white'
                      : 'bg-gray-100 text-gray-900'
                  }`}
                >
                  <div className="flex items-start space-x-2">
                    {message.sender === 'bot' && (
                      <Bot className="h-5 w-5 text-ocean-500 mt-0.5 flex-shrink-0" />
                    )}
                    {message.sender === 'user' && (
                      <User className="h-5 w-5 text-white mt-0.5 flex-shrink-0" />
                    )}
                    <div className="flex-1">
                      <p className="whitespace-pre-wrap">{message.text}</p>
                      {message.sources && message.sources.length > 0 && (
                        <div className="mt-2 text-xs opacity-75">
                          <p className="font-medium">Sources:</p>
                          <ul className="list-disc list-inside">
                            {message.sources.slice(0, 3).map((source, index) => (
                              <li key={index}>
                                {source.split('/').pop()}
                              </li>
                            ))}
                          </ul>
                        </div>
                      )}
                    </div>
                  </div>
                  <div className={`text-xs mt-1 ${
                    message.sender === 'user' ? 'text-ocean-100' : 'text-gray-500'
                  }`}>
                    {message.timestamp}
                  </div>
                </div>
              </div>
            ))}
            
            {isLoading && (
              <div className="flex justify-start">
                <div className="bg-gray-100 rounded-lg px-4 py-2">
                  <div className="flex items-center space-x-2">
                    <Bot className="h-5 w-5 text-ocean-500" />
                    <div className="flex space-x-1">
                      <div className="w-2 h-2 bg-ocean-500 rounded-full typing-indicator"></div>
                      <div className="w-2 h-2 bg-ocean-500 rounded-full typing-indicator" style={{animationDelay: '0.2s'}}></div>
                      <div className="w-2 h-2 bg-ocean-500 rounded-full typing-indicator" style={{animationDelay: '0.4s'}}></div>
                    </div>
                  </div>
                </div>
              </div>
            )}
            <div ref={messagesEndRef} />
          </div>

          {/* Suggested Questions */}
          {messages.length === 1 && (
            <div className="px-6 pb-4">
              <p className="text-sm text-gray-600 mb-3">Try asking:</p>
              <div className="flex flex-wrap gap-2">
                {suggestedQuestions.map((question, index) => (
                  <button
                    key={index}
                    onClick={() => setInputMessage(question)}
                    className="px-3 py-1 bg-ocean-100 text-ocean-700 rounded-full text-sm hover:bg-ocean-200 transition-colors"
                  >
                    {question}
                  </button>
                ))}
              </div>
            </div>
          )}

          {/* Input */}
          <div className="border-t border-gray-200 p-4">
            <form onSubmit={sendMessage} className="flex space-x-3">
              <input
                type="text"
                value={inputMessage}
                onChange={(e) => setInputMessage(e.target.value)}
                placeholder="Ask about course content, assignments, or readings..."
                className="flex-1 px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-ocean-500 focus:border-transparent"
                disabled={isLoading}
              />
              <button
                type="submit"
                disabled={!inputMessage.trim() || isLoading}
                className="px-4 py-2 bg-ocean-500 text-white rounded-lg hover:bg-ocean-600 disabled:opacity-50 disabled:cursor-not-allowed transition-colors flex items-center space-x-2"
              >
                <Send className="h-4 w-4" />
                <span>Send</span>
              </button>
            </form>
          </div>
        </div>

        {/* Footer */}
        <div className="mt-6 text-center text-sm text-gray-600">
          <p>FISH 510: Marine Organism Resilience and Epigenetics | University of Washington</p>
          <p className="mt-1">Powered by AI • Course materials and discussions</p>
        </div>
      </div>
    </div>
  );
}

export default App;
