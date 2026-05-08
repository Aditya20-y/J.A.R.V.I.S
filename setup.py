from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="jarvis-assistant",
    version="1.0.0",
    author="Aditya Yadav",
    author_email="your.email@example.com",
    description="A personal AI assistant inspired by Iron Man's Jarvis",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Aditya20-y/J.A.R.V.I.S",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 3 - Alpha",
        "Intended Audience :: End Users/Desktop",
    ],
    python_requires=">=3.8,<3.12",
    install_requires=[
        "openai>=1.3.0",
        "SpeechRecognition>=3.10.0",
        "pyttsx3>=2.90",
        "Flask>=3.0.0",
        "python-dotenv>=1.0.0",
        "requests>=2.31.0",
        "SQLAlchemy>=2.0.21",
    ],
)
