#!/usr/bin/env python3
"""
J.A.R.V.I.S Main Entry Point
Run the assistant in different modes: desktop, web, or CLI
"""

import argparse
import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent))

from utils.logger import setup_logger
from core.assistant import JarvisAssistant

logger = setup_logger(__name__)

def main():
    parser = argparse.ArgumentParser(
        description="J.A.R.V.I.S - Personal AI Assistant",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python main.py --mode desktop    # Run desktop GUI
  python main.py --mode web        # Run web server
  python main.py --mode cli        # Run CLI mode
        """
    )
    
    parser.add_argument(
        "--mode",
        choices=["desktop", "web", "cli"],
        default="cli",
        help="Mode to run J.A.R.V.I.S in (default: cli)"
    )
    
    parser.add_argument(
        "--voice",
        action="store_true",
        help="Enable voice input/output"
    )
    
    parser.add_argument(
        "--debug",
        action="store_true",
        help="Enable debug mode"
    )
    
    args = parser.parse_args()
    
    # Initialize Jarvis
    logger.info(f"Initializing J.A.R.V.I.S in {args.mode} mode...")
    jarvis = JarvisAssistant(debug=args.debug, voice_enabled=args.voice)
    
    try:
        if args.mode == "desktop":
            logger.info("Starting Desktop GUI...")
            from desktop.gui import JarvisGUI
            gui = JarvisGUI(jarvis)
            gui.run()
            
        elif args.mode == "web":
            logger.info("Starting Web Server...")
            from web.app import create_app
            app = create_app(jarvis)
            app.run(debug=args.debug, host="0.0.0.0", port=5000)
            
        else:  # CLI mode
            logger.info("Starting CLI Mode...")
            run_cli(jarvis)
            
    except KeyboardInterrupt:
        logger.info("\nShutting down J.A.R.V.I.S...")
        print("\nGoodbye, Sir. Until next time.")
        sys.exit(0)
    except Exception as e:
        logger.error(f"Error: {e}", exc_info=True)
        sys.exit(1)

def run_cli(jarvis):
    """
    Run J.A.R.V.I.S in CLI mode
    """
    print("\n" + "="*50)
    print("  J.A.R.V.I.S - Personal AI Assistant")
    print("  Version: 1.0.0")
    print("="*50)
    print("\nType 'exit' or 'quit' to exit")
    print("Type 'help' for available commands\n")
    
    while True:
        try:
            user_input = input("You: ").strip()
            
            if not user_input:
                continue
                
            if user_input.lower() in ["exit", "quit"]:
                print("\nJ.A.R.V.I.S: Goodbye, Sir. Until next time.")
                break
                
            if user_input.lower() == "help":
                print("\nAvailable commands:")
                print("  exit/quit - Exit the application")
                print("  clear     - Clear conversation history")
                print("  help      - Show this help message\n")
                continue
                
            # Get response from Jarvis
            response = jarvis.get_response(user_input)
            print(f"\nJ.A.R.V.I.S: {response}\n")
            
        except EOFError:
            print("\nJ.A.R.V.I.S: Goodbye, Sir.")
            break
        except Exception as e:
            logger.error(f"Error processing input: {e}")
            print(f"Error: {e}\n")

if __name__ == "__main__":
    main()
