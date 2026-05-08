#!/usr/bin/env python3
"""
Configuration Management
"""

import os
from dotenv import load_dotenv

from utils.logger import setup_logger

logger = setup_logger(__name__)

class Config:
    """Configuration manager"""
    
    def __init__(self, env_file=".env"):
        """
        Initialize configuration
        
        Args:
            env_file (str): Path to .env file
        """
        # Load environment variables
        load_dotenv(env_file)
        
        # Default configuration
        self.defaults = {
            "APP_NAME": "J.A.R.V.I.S",
            "APP_VERSION": "1.0.0",
            "DEBUG": False,
            "LOG_LEVEL": "INFO",
            "OPENAI_MODEL": "gpt-4",
            "SPEECH_RECOGNITION_LANGUAGE": "en-US",
            "TTS_ENGINE": "pyttsx3",
            "TTS_VOICE": "default",
            "TTS_SPEED": 1.0,
            "FLASK_HOST": "0.0.0.0",
            "FLASK_PORT": 5000,
            "DATABASE_URL": "sqlite:///jarvis_memory.db",
            "ENABLE_MEMORY": True,
            "MAX_MEMORY_SIZE": 10000,
        }
        
        logger.info("Configuration loaded")
    
    def get(self, key, default=None):
        """
        Get configuration value
        
        Args:
            key (str): Configuration key
            default: Default value if not found
            
        Returns:
            Configuration value
        """
        value = os.getenv(key, default or self.defaults.get(key))
        
        # Type conversion
        if isinstance(self.defaults.get(key), bool):
            return value.lower() in ['true', 'yes', '1'] if isinstance(value, str) else bool(value)
        elif isinstance(self.defaults.get(key), int):
            return int(value) if value else 0
        elif isinstance(self.defaults.get(key), float):
            return float(value) if value else 0.0
        
        return value
    
    def get_all(self):
        """
        Get all configuration
        
        Returns:
            dict: All configuration
        """
        return {key: self.get(key) for key in self.defaults}
    
    def set(self, key, value):
        """
        Set configuration value
        
        Args:
            key (str): Configuration key
            value: Configuration value
        """
        os.environ[key] = str(value)
        logger.debug(f"Config set: {key}")
