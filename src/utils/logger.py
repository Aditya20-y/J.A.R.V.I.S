#!/usr/bin/env python3
"""
Logging Configuration
"""

import logging
import sys
from pathlib import Path

# Create logs directory
logsdir = Path("logs")
logsdir.mkdir(exist_ok=True)

def setup_logger(name, level=logging.INFO):
    """
    Setup logger
    
    Args:
        name (str): Logger name
        level: Logging level
        
    Returns:
        logger: Configured logger
    """
    logger = logging.getLogger(name)
    logger.setLevel(level)
    
    # Avoid adding handlers multiple times
    if logger.hasHandlers():
        return logger
    
    # Console handler
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(level)
    console_formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    console_handler.setFormatter(console_formatter)
    logger.addHandler(console_handler)
    
    # File handler
    file_handler = logging.FileHandler(f"logs/{name.replace('.', '_')}.log")
    file_handler.setLevel(level)
    file_formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    file_handler.setFormatter(file_formatter)
    logger.addHandler(file_handler)
    
    return logger
