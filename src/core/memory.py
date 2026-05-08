#!/usr/bin/env python3
"""
J.A.R.V.I.S Memory System
Stores and manages conversation history and user preferences
"""

from datetime import datetime
from collections import deque

from utils.logger import setup_logger

logger = setup_logger(__name__)

class Memory:
    """Memory system for Jarvis"""
    
    def __init__(self, max_size=10000):
        """
        Initialize Memory
        
        Args:
            max_size (int): Maximum number of interactions to store
        """
        self.max_size = max_size
        self.interactions = deque(maxlen=max_size)
        self.preferences = {}
        self.learned_patterns = {}
        
        logger.info(f"Memory initialized with max size: {max_size}")
    
    def add_interaction(self, user_input):
        """
        Add user interaction to memory
        
        Args:
            user_input (str): User's message
        """
        interaction = {
            "timestamp": datetime.now().isoformat(),
            "input": user_input,
            "response": None,
        }
        self.interactions.append(interaction)
        logger.debug(f"Interaction stored: {user_input[:50]}...")
    
    def add_response(self, response):
        """
        Add Jarvis response to last interaction
        
        Args:
            response (str): Jarvis response
        """
        if self.interactions:
            self.interactions[-1]["response"] = response
            logger.debug(f"Response stored: {response[:50]}...")
    
    def get_context(self, depth=5):
        """
        Get recent conversation context
        
        Args:
            depth (int): Number of recent interactions to retrieve
            
        Returns:
            dict: Context information
        """
        recent = list(self.interactions)[-depth:]
        return {
            "interactions": recent,
            "total_interactions": len(self.interactions),
            "preferences": self.preferences,
        }
    
    def add_preference(self, key, value):
        """
        Store user preference
        
        Args:
            key (str): Preference key
            value: Preference value
        """
        self.preferences[key] = value
        logger.debug(f"Preference stored: {key} = {value}")
    
    def get_preference(self, key, default=None):
        """
        Retrieve user preference
        
        Args:
            key (str): Preference key
            default: Default value if not found
            
        Returns:
            Preference value or default
        """
        return self.preferences.get(key, default)
    
    def clear(self):
        """Clear all memory"""
        self.interactions.clear()
        self.preferences.clear()
        self.learned_patterns.clear()
        logger.info("Memory cleared")
    
    def get_statistics(self):
        """
        Get memory statistics
        
        Returns:
            dict: Memory statistics
        """
        return {
            "total_interactions": len(self.interactions),
            "max_size": self.max_size,
            "preferences_count": len(self.preferences),
            "learned_patterns_count": len(self.learned_patterns),
        }
