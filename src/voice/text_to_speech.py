#!/usr/bin/env python3
"""
Text-to-Speech Module
Converts text to speech
"""

import pyttsx3
from utils.logger import setup_logger

logger = setup_logger(__name__)

class TextToSpeech:
    """Handle text-to-speech conversion"""
    
    def __init__(self, engine="pyttsx3", voice="default", speed=1.0):
        """
        Initialize Text-to-Speech
        
        Args:
            engine (str): TTS engine to use
            voice (str): Voice preference
            speed (float): Speech speed multiplier
        """
        self.engine = pyttsx3.init(engine)
        self.voice = voice
        self.speed = speed
        
        # Configure voice
        self.set_voice(voice)
        self.set_speed(speed)
        
        logger.info(f"TTS initialized with engine: {engine}")
    
    def speak(self, text, wait=True):
        """
        Convert text to speech and speak
        
        Args:
            text (str): Text to speak
            wait (bool): Wait for speech to finish
        """
        try:
            logger.info(f"Speaking: {text[:50]}...")
            self.engine.say(text)
            
            if wait:
                self.engine.runAndWait()
            else:
                self.engine.startLoop(False)
                
        except Exception as e:
            logger.error(f"TTS error: {e}")
    
    def set_voice(self, voice_id):
        """
        Set voice
        
        Args:
            voice_id (str): Voice identifier
        """
        try:
            voices = self.engine.getProperty('voices')
            if voice_id == "male":
                self.engine.setProperty('voice', voices[0].id)
            elif voice_id == "female":
                self.engine.setProperty('voice', voices[1].id if len(voices) > 1 else voices[0].id)
            else:
                self.engine.setProperty('voice', voices[0].id)
            
            self.voice = voice_id
            logger.info(f"Voice set to: {voice_id}")
        except Exception as e:
            logger.error(f"Error setting voice: {e}")
    
    def set_speed(self, speed):
        """
        Set speech speed
        
        Args:
            speed (float): Speed multiplier (0.5 - 2.0)
        """
        try:
            rate = int(150 * speed)  # Base rate is 150
            self.engine.setProperty('rate', rate)
            self.speed = speed
            logger.info(f"Speech speed set to: {speed}")
        except Exception as e:
            logger.error(f"Error setting speed: {e}")
