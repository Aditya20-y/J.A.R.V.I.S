#!/usr/bin/env python3
"""
Unit tests for J.A.R.V.I.S Assistant
"""

import pytest
import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent / 'src'))

from core.assistant import JarvisAssistant
from core.memory import Memory
from core.brain import Brain
from utils.config import Config

class TestJarvisAssistant:
    """Test Jarvis Assistant"""
    
    @pytest.fixture
    def jarvis(self):
        """Create Jarvis instance for testing"""
        return JarvisAssistant(debug=True, voice_enabled=False)
    
    def test_initialization(self, jarvis):
        """Test Jarvis initialization"""
        assert jarvis is not None
        assert jarvis.debug is True
        assert jarvis.voice_enabled is False
    
    def test_get_response(self, jarvis):
        """Test getting response"""
        response = jarvis.get_response("Hello")
        assert response is not None
        assert isinstance(response, str)
        assert len(response) > 0
    
    def test_get_status(self, jarvis):
        """Test getting status"""
        status = jarvis.get_status()
        assert "name" in status
        assert status["name"] == "J.A.R.V.I.S"
        assert status["status"] == "active"
    
    def test_get_personality(self, jarvis):
        """Test getting personality"""
        personality = jarvis.get_personality()
        assert "name" in personality
        assert personality["name"] == "J.A.R.V.I.S"
        assert "catchphrases" in personality
    
    def test_clear_memory(self, jarvis):
        """Test memory clearing"""
        jarvis.get_response("Test message")
        assert len(jarvis.memory.interactions) > 0
        
        result = jarvis.clear_memory()
        assert "cleared" in result.lower()
        assert len(jarvis.memory.interactions) == 0

class TestMemory:
    """Test Memory system"""
    
    @pytest.fixture
    def memory(self):
        """Create Memory instance for testing"""
        return Memory(max_size=100)
    
    def test_add_interaction(self, memory):
        """Test adding interaction"""
        memory.add_interaction("Test message")
        assert len(memory.interactions) == 1
    
    def test_add_response(self, memory):
        """Test adding response"""
        memory.add_interaction("Test message")
        memory.add_response("Test response")
        assert memory.interactions[-1]["response"] == "Test response"
    
    def test_preferences(self, memory):
        """Test preferences"""
        memory.add_preference("name", "John")
        assert memory.get_preference("name") == "John"
    
    def test_clear(self, memory):
        """Test clearing memory"""
        memory.add_interaction("Test")
        memory.add_preference("key", "value")
        
        memory.clear()
        assert len(memory.interactions) == 0
        assert len(memory.preferences) == 0

class TestBrain:
    """Test Brain (AI processing)"""
    
    @pytest.fixture
    def brain(self):
        """Create Brain instance for testing"""
        config = Config()
        return Brain(config)
    
    def test_initialization(self, brain):
        """Test Brain initialization"""
        assert brain is not None
        assert brain.config is not None
    
    def test_time_command(self, brain):
        """Test time command"""
        response = brain.process("What time is it?")
        assert response is not None
        assert any(word in response.lower() for word in ["time", ":"])
    
    def test_greeting_command(self, brain):
        """Test greeting command"""
        response = brain.process("Hello")
        assert response is not None
        assert len(response) > 0
    
    def test_who_are_you_command(self, brain):
        """Test who are you command"""
        response = brain.process("Who are you?")
        assert "J.A.R.V.I.S" in response

if __name__ == "__main__":
    pytest.main([__file__, "-v"])
