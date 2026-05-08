#!/usr/bin/env python3
"""
Speech Recognition Module
Converts speech to text
"""

import speech_recognition as sr
from utils.logger import setup_logger

logger = setup_logger(__name__)

class SpeechRecognizer:
    """Handle speech-to-text conversion"""
    
    def __init__(self, language="en-US"):
        """
        Initialize Speech Recognizer
        
        Args:
            language (str): Language code for recognition
        """
        self.recognizer = sr.Recognizer()
        self.language = language
        self.microphone = sr.Microphone()
        
        logger.info(f"Speech Recognizer initialized with language: {language}")
    
    def listen(self, timeout=5, phrase_time_limit=15):
        """
        Listen to microphone and convert speech to text
        
        Args:
            timeout (int): Timeout in seconds
            phrase_time_limit (int): Maximum phrase duration
            
        Returns:
            str: Recognized text or None if failed
        """
        try:
            with self.microphone as source:
                # Adjust for ambient noise
                self.recognizer.adjust_for_ambient_noise(source, duration=0.5)
                
                logger.info("Listening...")
                audio = self.recognizer.listen(
                    source,
                    timeout=timeout,
                    phrase_time_limit=phrase_time_limit
                )
            
            # Use Google Speech Recognition (free)
            text = self.recognizer.recognize_google(audio, language=self.language)
            logger.info(f"Recognized: {text}")
            return text
            
        except sr.UnknownValueError:
            logger.warning("Could not understand audio")
            return None
        except sr.RequestError as e:
            logger.error(f"Speech recognition error: {e}")
            return None
        except Exception as e:
            logger.error(f"Error during speech recognition: {e}")
            return None
    
    def set_language(self, language):
        """
        Change recognition language
        
        Args:
            language (str): Language code
        """
        self.language = language
        logger.info(f"Language changed to: {language}")
