#!/usr/bin/env python3
"""
J.A.R.V.I.S Brain - AI & NLP Processing
"""

import random
from datetime import datetime

from utils.logger import setup_logger

logger = setup_logger(__name__)

class Brain:
    """AI Brain for processing and generating responses"""
    
    def __init__(self, config):
        """
        Initialize Brain
        
        Args:
            config (Config): Configuration object
        """
        self.config = config
        self.api_key = config.get("OPENAI_API_KEY")
        self.model = config.get("OPENAI_MODEL", "gpt-4")
        
        # Initialize OpenAI (will be used when API key is configured)
        self.openai_available = False
        if self.api_key:
            try:
                import openai
                openai.api_key = self.api_key
                self.openai_available = True
                logger.info("OpenAI API initialized")
            except ImportError:
                logger.warning("OpenAI library not available")
        else:
            logger.warning("OpenAI API key not configured")
    
    def process(self, user_input, context=None):
        """
        Process user input and generate response
        
        Args:
            user_input (str): User's message
            context (dict): Conversation context
            
        Returns:
            str: Jarvis response
        """
        # First check for command patterns
        response = self._check_commands(user_input)
        if response:
            return response
        
        # Use OpenAI if available
        if self.openai_available:
            try:
                response = self._get_openai_response(user_input, context)
                return response
            except Exception as e:
                logger.error(f"OpenAI error: {e}")
        
        # Fallback to predefined responses
        return self._get_default_response(user_input)
    
    def _check_commands(self, user_input):
        """
        Check for predefined commands
        
        Args:
            user_input (str): User input
            
        Returns:
            str or None: Response if command matched
        """
        user_lower = user_input.lower().strip()
        
        # Time
        if any(word in user_lower for word in ["time", "what time", "current time"]):
            current_time = datetime.now().strftime("%I:%M %p")
            return f"The current time is {current_time}, Sir."
        
        # Date
        if any(word in user_lower for word in ["date", "what date", "today"]):
            current_date = datetime.now().strftime("%A, %B %d, %Y")
            return f"Today is {current_date}, Sir."
        
        # Greetings
        if any(word in user_lower for word in ["hello", "hi", "hey", "good morning", "good evening"]):
            greeting_responses = [
                "Good morning, Sir. I trust you slept well.",
                "Hello, Sir. How may I be of service?",
                "Greetings, Sir.",
                "Good day, Sir.",
            ]
            return random.choice(greeting_responses)
        
        # Who are you
        if any(phrase in user_lower for phrase in ["who are you", "what are you", "introduce yourself"]):
            return "I am J.A.R.V.I.S, Just A Rather Very Intelligent System. I am here to assist you with any task, Sir."
        
        return None
    
    def _get_openai_response(self, user_input, context=None):
        """
        Get response from OpenAI API
        
        Args:
            user_input (str): User message
            context (dict): Conversation context
            
        Returns:
            str: Response from OpenAI
        """
        try:
            import openai
            
            # Build system message
            system_message = {
                "role": "system",
                "content": "You are J.A.R.V.I.S, an intelligent AI assistant inspired by Marvel's Iron Man. "
                          "You are professional, helpful, witty, and courteous. You often address the user as 'Sir' "
                          "and maintain a sophisticated British accent in your writing. Keep responses concise and helpful."
            }
            
            # Build conversation
            messages = [system_message]
            
            if context and "interactions" in context:
                # Add recent context
                for interaction in context["interactions"][-3:]:
                    messages.append({"role": "user", "content": interaction.get("input", "")})
                    messages.append({"role": "assistant", "content": interaction.get("response", "")})
            
            # Add current message
            messages.append({"role": "user", "content": user_input})
            
            # Get response
            response = openai.ChatCompletion.create(
                model=self.model,
                messages=messages,
                temperature=0.7,
                max_tokens=500,
            )
            
            return response.choices[0].message.content
            
        except Exception as e:
            logger.error(f"OpenAI API error: {e}")
            return self._get_default_response(user_input)
    
    def _get_default_response(self, user_input):
        """
        Get default response when AI is unavailable
        
        Args:
            user_input (str): User input
            
        Returns:
            str: Default response
        """
        default_responses = [
            "I'm afraid I don't have a response for that at the moment, Sir.",
            "That's an interesting question, Sir. I'll need to think about that.",
            "Very good, Sir. I'll keep that in mind.",
            "I understand, Sir. How else may I assist you?",
            "Quite right, Sir.",
        ]
        return random.choice(default_responses)
