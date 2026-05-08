# J.A.R.V.I.S Setup Guide

## Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Microphone and speakers
- OpenAI API key (optional for advanced features)

## Installation Steps

### 1. Clone Repository

```bash
git clone https://github.com/Aditya20-y/J.A.R.V.I.S.git
cd J.A.R.V.I.S
```

### 2. Create Virtual Environment

```bash
# Create venv
python -m venv venv

# Activate on Windows
venv\Scripts\activate

# Activate on macOS/Linux
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment

```bash
# Copy example configuration
cp .env.example .env

# Edit .env with your settings
# Add your OpenAI API key if you have one
```

## Configuration

Edit `.env` file:

```env
# OpenAI API (required for advanced AI)
OPENAI_API_KEY=sk-...
OPENAI_MODEL=gpt-4

# Voice Settings
SPEECH_RECOGNITION_LANGUAGE=en-US
TTS_ENGINE=pyttsx3
TTS_VOICE=default
TTS_SPEED=1.0

# Application
DEBUG=False
LOG_LEVEL=INFO

# Web Server
FLASK_HOST=0.0.0.0
FLASK_PORT=5000
```

## Running J.A.R.V.I.S

### Desktop GUI Mode (Recommended)

```bash
python src/main.py --mode desktop
```

### Web Interface Mode

```bash
python src/main.py --mode web
```

Then open browser: http://localhost:5000

### Command-Line Mode

```bash
python src/main.py --mode cli
```

## Troubleshooting

### Microphone Issues

```bash
# Test microphone
python -m speech_recognition
```

### OpenAI API Errors

- Verify API key in `.env`
- Check API key has correct permissions
- Ensure sufficient API credits

### Module Not Found

```bash
# Reinstall dependencies
pip install -r requirements.txt --force-reinstall
```

### Audio Output Issues

Linux users may need:

```bash
sudo apt-get install espeak
```

## Development

### Running Tests

```bash
pytest tests/ -v
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

## Getting Help

- Check logs in `logs/` directory
- Open an issue on GitHub
- Review documentation in `docs/`
