#!/usr/bin/env python3
"""
Main J.A.R.V.I.S Assistant Class
Orchestrates all functionality
"""

import json
from datetime import datetime
from pathlib import Path

from utils.logger import setup_logger
from utils.config import Config
from .brain import Brain
from .memory import Memory

logger = setup_logger(__name__)

class JarvisAssistant:
    """Main Jarvis AI Assistant"""
    
    def __init__(self, debug=False, voice_enabled=False):
        """
        Initialize J.A.R.V.I.S
        
        Args:
            debug (bool): Enable debug mode
            voice_enabled (bool): Enable voice input/output
        """
        self.debug = debug
        self.voice_enabled = voice_enabled
        self.config = Config()
        self.brain = Brain(self.config)
        self.memory = Memory()
        self.start_time = datetime.now()
        
        logger.info("J.A.R.V.I.S initialized successfully")
        
    def get_response(self, user_input):
        """
        Process user input and generate response
        
        Args:
            user_input (str): User's message
            
        Returns:
            str: Jarvis response
        """
        try:
            # Store in memory
            self.memory.add_interaction(user_input)
            
            # Get context from memory
            context = self.memory.get_context()
            
            # Process with brain (AI)
            response = self.brain.process(user_input, context)
            
            # Store response in memory
            self.memory.add_response(response)
            
            logger.debug(f"User: {user_input}")
            logger.debug(f"Response: {response}")
            
            return response
            
        except Exception as e:
            logger.error(f"Error processing user input: {e}", exc_info=True)
            return "I apologize, Sir. I encountered an error processing that request."
    
    def get_status(self):
        """
        Get J.A.R.V.I.S status
        
        Returns:
            dict: Status information
        """
        uptime = datetime.now() - self.start_time
        
        return {
            "name": "J.A.R.V.I.S",
            "version": "1.0.0",
            "status": "active",
            "uptime_seconds": uptime.total_seconds(),
            "voice_enabled": self.voice_enabled,
            "debug_mode": self.debug,
            "memory_interactions": len(self.memory.interactions),
        }
    
    def clear_memory(self):
        """Clear conversation memory"""
        self.memory.clear()
        logger.info("Memory cleared")
        return "Memory cleared, Sir."
    
    def get_personality(self):
        """
        Get Jarvis personality traits
        
        Returns:
            dict: Personality information
        """
        return {
            "name": "J.A.R.V.I.S",
            "full_name": "Just A Rather Very Intelligent System",
            "personality": "Professional, helpful, witty, and courteous",
            "inspiration": "Marvel's Iron Man - J.A.R.V.I.S",
            "catchphrases": [
                "Good morning, Sir.",
                "I am always here to help.",
                "Very good, Sir.",
                "Of course, Sir.",
            ]
        }
