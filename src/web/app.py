#!/usr/bin/env python3
"""
J.A.R.V.I.S Web Application
Flask-based web interface
"""

from flask import Flask, jsonify, request, render_template
from flask_cors import CORS

from utils.logger import setup_logger

logger = setup_logger(__name__)

def create_app(jarvis_assistant):
    """
    Create Flask application
    
    Args:
        jarvis_assistant: JarvisAssistant instance
        
    Returns:
        Flask app instance
    """
    app = Flask(__name__, template_folder='templates', static_folder='static')
    CORS(app)
    
    # Store Jarvis instance
    app.jarvis = jarvis_assistant
    
    # ==================== Routes ====================
    
    @app.route('/')
    def home():
        """Home page"""
        return render_template('index.html')
    
    @app.route('/api/chat', methods=['POST'])
    def chat():
        """
        Chat endpoint
        
        Expected JSON:
        {
            "message": "User message here"
        }
        """
        try:
            data = request.get_json()
            user_message = data.get('message', '').strip()
            
            if not user_message:
                return jsonify({"error": "Empty message"}), 400
            
            # Get response from Jarvis
            response = app.jarvis.get_response(user_message)
            
            return jsonify({
                "success": True,
                "user_message": user_message,
                "jarvis_response": response,
            })
            
        except Exception as e:
            logger.error(f"Chat error: {e}", exc_info=True)
            return jsonify({"error": str(e)}), 500
    
    @app.route('/api/status', methods=['GET'])
    def status():
        """Get Jarvis status"""
        try:
            return jsonify(app.jarvis.get_status())
        except Exception as e:
            logger.error(f"Status error: {e}")
            return jsonify({"error": str(e)}), 500
    
    @app.route('/api/personality', methods=['GET'])
    def personality():
        """Get Jarvis personality"""
        try:
            return jsonify(app.jarvis.get_personality())
        except Exception as e:
            logger.error(f"Personality error: {e}")
            return jsonify({"error": str(e)}), 500
    
    @app.route('/api/clear-memory', methods=['POST'])
    def clear_memory():
        """Clear conversation memory"""
        try:
            result = app.jarvis.clear_memory()
            return jsonify({"success": True, "message": result})
        except Exception as e:
            logger.error(f"Clear memory error: {e}")
            return jsonify({"error": str(e)}), 500
    
    # ==================== Error Handlers ====================
    
    @app.errorhandler(404)
    def not_found(error):
        return jsonify({"error": "Endpoint not found"}), 404
    
    @app.errorhandler(500)
    def server_error(error):
        return jsonify({"error": "Internal server error"}), 500
    
    logger.info("Flask app created successfully")
    return app
