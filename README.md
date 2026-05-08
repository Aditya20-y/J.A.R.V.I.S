# J.A.R.V.I.S - Personal AI Assistant

> "Sir, I've taken the liberty of preparing breakfast." - J.A.R.V.I.S

## Overview

**J.A.R.V.I.S** is a sophisticated personal AI assistant inspired by Tony Stark's AI system from the Iron Man movies. Built with Python, it provides voice recognition, natural language processing, and intelligent responses through multiple interfaces (desktop, web, and CLI).

### Key Features

✨ **Multi-Interface Support**
- 🎙️ Voice Control (Speech-to-Text & Text-to-Speech)
- 💻 Desktop GUI Application (Tkinter)
- 🌐 Web Interface (Flask REST API)
- 📝 Command-Line Interface (CLI)

🧠 **AI & Learning**
- GPT-4 Integration via OpenAI API
- User Preference Learning
- Conversation Memory & History
- Context-Aware Responses

🔧 **Smart Capabilities**
- Task Automation
- Weather Information
- Calendar Integration (planned)
- Smart Home Control (planned)
- Natural Conversation

⚙️ **Developer Friendly**
- Modular Architecture
- Easy Configuration
- Comprehensive Logging
- Unit Tests Included
- Docker Support (coming soon)

---

## Tech Stack

| Component | Technology |
|-----------|------------|
| **Language** | Python 3.8+ |
| **AI/NLP** | OpenAI GPT-4, NLTK |
| **Voice** | SpeechRecognition, pyttsx3, Google TTS |
| **Web Framework** | Flask, Flask-CORS |
| **Desktop GUI** | Tkinter, Pillow |
| **Database** | SQLAlchemy, SQLite |
| **Testing** | pytest |

---

## Project Structure

```
J.A.R.V.I.S/
├── src/
│   ├── core/
│   │   ├── __init__.py
│   │   ├── assistant.py          # Main Jarvis class
│   │   ├── brain.py              # AI & NLP processing
│   │   └── memory.py             # User memory & learning
│   ├── voice/
│   │   ├── __init__.py
│   │   ├── speech_recognition.py # Speech-to-Text
│   │   └── text_to_speech.py     # Text-to-Speech
│   ├── web/
│   │   ├── __init__.py
│   │   ├── app.py                # Flask application
│   │   ├── routes.py             # API endpoints
│   │   └── templates/            # HTML templates
│   ├── desktop/
│   │   ├── __init__.py
│   │   └── gui.py                # Tkinter GUI
│   ├── utils/
│   │   ├── __init__.py
│   │   ├── config.py             # Configuration management
│   │   └── logger.py             # Logging setup
│   └── main.py                   # Entry point
├── tests/
│   ├── __init__.py
│   └── test_assistant.py         # Unit tests
├── docs/
│   ├── SETUP.md                  # Installation guide
│   ├── API.md                    # API documentation
│   └── USAGE.md                  # Usage guide
├── .env.example                  # Environment variables template
├── .gitignore                    # Git ignore rules
├── requirements.txt              # Python dependencies
├── setup.py                      # Package setup
├── LICENSE                       # MIT License
└── README.md                     # This file
```

---

## Installation & Setup

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- OpenAI API key (free tier available)
- Microphone for voice input
- Speakers for audio output

### Quick Start

**1. Clone the Repository**
```bash
git clone https://github.com/Aditya20-y/J.A.R.V.I.S.git
cd J.A.R.V.I.S
```

**2. Create Virtual Environment**
```bash
python -m venv venv

# On Windows
venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate
```

**3. Install Dependencies**
```bash
pip install -r requirements.txt
```

**4. Configure Environment**
```bash
cp .env.example .env
# Edit .env with your OpenAI API key and preferences
```

**5. Run J.A.R.V.I.S**

```bash
# Desktop GUI Mode (Recommended)
python src/main.py --mode desktop

# Web Interface Mode
python src/main.py --mode web
# Access at http://localhost:5000

# CLI Mode
python src/main.py --mode cli
```

---

## Usage Examples

### Voice Commands
```
User: "Jarvis, what's the weather?"
J.A.R.V.I.S: "The weather today is sunny, 75 degrees Fahrenheit."

User: "Set a reminder for tomorrow at 9 AM"
J.A.R.V.I.S: "Reminder set for tomorrow at 9:00 AM."

User: "Tell me a joke"
J.A.R.V.I.S: "Why do programmers prefer dark mode? Because light attracts bugs!"
```

### Web Interface
Visit `http://localhost:5000` to:
- Chat with J.A.R.V.I.S via text
- Use voice input/output
- View conversation history
- Manage preferences

### Desktop Application
- GUI with real-time chat
- Voice button for quick commands
- Settings panel
- Conversation history

---

## Configuration

Edit `.env` file to customize:

```env
# API Keys
OPENAI_API_KEY=sk-...

# Voice Settings
SPEECH_RECOGNITION_LANGUAGE=en-US
TTS_ENGINE=google
TTS_VOICE=default

# Application
DEBUG=False
LOG_LEVEL=INFO
```

See [SETUP.md](docs/SETUP.md) for detailed configuration.

---

## Roadmap

### Phase 1 (Current)
- ✅ Basic conversational AI
- ✅ Voice input/output
- ✅ Desktop & Web interfaces
- ✅ Memory system

### Phase 2
- 🔄 Calendar integration
- 🔄 Weather API integration
- 🔄 Email handling
- 🔄 Advanced NLP

### Phase 3
- 📋 Smart home automation
- 📋 Mobile app support
- 📋 Custom skill plugins
- 📋 Multi-user support

### Phase 4
- 🚀 Machine learning improvements
- 🚀 Cloud synchronization
- 🚀 Advanced personalization
- 🚀 Multi-language support

---

## Development

### Running Tests
```bash
pytest tests/ -v --cov=src
```

### Code Quality
```bash
# Format code
black src/ tests/

# Lint
flake8 src/ tests/

# Sort imports
isort src/ tests/
```

### Contributing
1. Create a feature branch: `git checkout -b feature/amazing-feature`
2. Commit changes: `git commit -m 'Add amazing feature'`
3. Push to branch: `git push origin feature/amazing-feature`
4. Open a Pull Request

---

## Troubleshooting

### Microphone Not Detected
- Check system audio settings
- Ensure microphone permissions are granted
- Test with `python -m speech_recognition`

### OpenAI API Errors
- Verify API key in `.env`
- Check API key permissions
- Ensure sufficient API credits

### GUI Not Rendering
- Ensure tkinter is installed: `python -m tkinter`
- On Linux: `sudo apt-get install python3-tk`
- On macOS: included with Python

For more help, see [SETUP.md](docs/SETUP.md)

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## Acknowledgments

- Inspired by J.A.R.V.I.S from Marvel's Iron Man
- Built with ❤️ using Python
- OpenAI GPT-4 for intelligent responses
- Community contributions welcome!

---

## Contact & Support

- **Author:** Aditya Yadav
- **GitHub:** [@Aditya20-y](https://github.com/Aditya20-y)
- **Issues:** [Report a bug](https://github.com/Aditya20-y/J.A.R.V.I.S/issues)

---

**J.A.R.V.I.S** - *"I am always here to help, Sir."* 🤖
