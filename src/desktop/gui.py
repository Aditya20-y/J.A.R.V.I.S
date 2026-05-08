#!/usr/bin/env python3
"""
J.A.R.V.I.S Desktop GUI
Tkinter-based desktop application
"""

import tkinter as tk
from tkinter import scrolledtext, messagebox
import threading

from utils.logger import setup_logger

logger = setup_logger(__name__)

class JarvisGUI:
    """Desktop GUI for Jarvis"""
    
    def __init__(self, jarvis_assistant):
        """
        Initialize GUI
        
        Args:
            jarvis_assistant: JarvisAssistant instance
        """
        self.jarvis = jarvis_assistant
        self.root = tk.Tk()
        self.root.title("J.A.R.V.I.S - Personal AI Assistant")
        self.root.geometry("900x700")
        self.root.configure(bg="#1a1a2e")
        
        self._create_widgets()
        logger.info("GUI initialized")
    
    def _create_widgets(self):
        """Create GUI widgets"""
        # Header
        header = tk.Frame(self.root, bg="#0f3460", height=50)
        header.pack(fill=tk.X)
        
        title = tk.Label(
            header,
            text="J.A.R.V.I.S",
            font=("Arial", 24, "bold"),
            fg="#e94560",
            bg="#0f3460"
        )
        title.pack(pady=10)
        
        # Chat display
        chat_frame = tk.Frame(self.root, bg="#1a1a2e")
        chat_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        self.chat_display = scrolledtext.ScrolledText(
            chat_frame,
            height=20,
            width=100,
            bg="#0f3460",
            fg="#4ecca3",
            font=("Arial", 10),
            wrap=tk.WORD,
            state=tk.DISABLED,
            relief=tk.FLAT,
            border=2
        )
        self.chat_display.pack(fill=tk.BOTH, expand=True)
        
        # Initial message
        self._append_message("J.A.R.V.I.S", "Good morning, Sir. I am J.A.R.V.I.S. How may I assist you?")
        
        # Input frame
        input_frame = tk.Frame(self.root, bg="#1a1a2e")
        input_frame.pack(fill=tk.X, padx=10, pady=10)
        
        self.input_field = tk.Entry(
            input_frame,
            font=("Arial", 12),
            bg="#0f3460",
            fg="#fff",
            insertbackground="#e94560",
            relief=tk.FLAT,
            border=1
        )
        self.input_field.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 10))
        self.input_field.bind("<Return>", lambda e: self._send_message())
        
        send_btn = tk.Button(
            input_frame,
            text="Send",
            command=self._send_message,
            bg="#e94560",
            fg="#fff",
            font=("Arial", 10, "bold"),
            relief=tk.FLAT,
            padx=20
        )
        send_btn.pack(side=tk.LEFT, padx=5)
        
        clear_btn = tk.Button(
            input_frame,
            text="Clear",
            command=self._clear_chat,
            bg="#e94560",
            fg="#fff",
            font=("Arial", 10, "bold"),
            relief=tk.FLAT,
            padx=20
        )
        clear_btn.pack(side=tk.LEFT)
        
        # Status bar
        self.status = tk.Label(
            self.root,
            text="Status: Ready",
            bg="#0f3460",
            fg="#4ecca3",
            font=("Arial", 9),
            anchor=tk.W,
            padx=10
        )
        self.status.pack(fill=tk.X)
    
    def _send_message(self):
        """Send message and get response"""
        message = self.input_field.get().strip()
        
        if not message:
            return
        
        # Display user message
        self._append_message("You", message)
        self.input_field.delete(0, tk.END)
        
        # Update status
        self._update_status("Processing...")
        
        # Get response in separate thread
        thread = threading.Thread(target=self._get_response, args=(message,))
        thread.daemon = True
        thread.start()
    
    def _get_response(self, message):
        """Get response from Jarvis"""
        try:
            response = self.jarvis.get_response(message)
            self.root.after(0, lambda: self._append_message("J.A.R.V.I.S", response))
            self.root.after(0, lambda: self._update_status("Status: Ready"))
        except Exception as e:
            logger.error(f"GUI error: {e}")
            self.root.after(0, lambda: self._append_message("J.A.R.V.I.S", "Error processing request."))
            self.root.after(0, lambda: self._update_status("Status: Error"))
    
    def _append_message(self, sender, message):
        """Append message to chat display"""
        self.chat_display.config(state=tk.NORMAL)
        self.chat_display.insert(tk.END, f"{sender}: {message}\n\n")
        self.chat_display.see(tk.END)
        self.chat_display.config(state=tk.DISABLED)
    
    def _clear_chat(self):
        """Clear chat history"""
        if messagebox.askyesno("Clear", "Clear all messages?"):
            self.chat_display.config(state=tk.NORMAL)
            self.chat_display.delete(1.0, tk.END)
            self.chat_display.config(state=tk.DISABLED)
            self.jarvis.clear_memory()
    
    def _update_status(self, text):
        """Update status bar"""
        self.status.config(text=text)
    
    def run(self):
        """Run the GUI"""
        self.root.mainloop()
