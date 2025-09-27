import os
import tkinter as tk
from tkinter import scrolledtext   
import mysql.connector
import ollama
from vosk import Model, KaldiRecognizer
import pyaudio
import json

# ========== CONFIG ==========
DB_NAME = "project_db"
MODEL_PATH = r"C:\Users\bappi\OneDrive\Desktop\Emergency\New folder\PYTHON\vosk-model-small-en-us-0.15"

# ========== DATABASE SETUP ==========
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password=""
)
cursor = db.cursor()

cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DB_NAME}")
db.database = DB_NAME

cursor.execute("""
    CREATE TABLE IF NOT EXISTS history (
        id INT AUTO_INCREMENT PRIMARY KEY,
        user_input TEXT,
        bot_response TEXT
    )
""")
db.commit()

# ========== VOSK MODEL ==========
if not os.path.exists(MODEL_PATH):
    raise Exception(f"Vosk model not found at {MODEL_PATH}. Please download and extract it correctly.")
vosk_model = Model(MODEL_PATH)

is_listening = False

# ========== FUNCTIONS ==========
def save_to_db(user_text, bot_text):
    sql = "INSERT INTO history (user_input, bot_response) VALUES (%s, %s)"
    cursor.execute(sql, (user_text, bot_text))
    db.commit()

def get_response(user_text):
    try:
        response = ollama.chat(model="mistral:latest", messages=[
            {"role": "user", "content": user_text}
        ])
        return response["message"]["content"]
    except Exception as e:
        return "Error: " + str(e)

def add_to_chat(text, tag=None):
    chat_window.config(state=tk.NORMAL)
    chat_window.insert(tk.END, text, tag)
    chat_window.config(state=tk.DISABLED)
    chat_window.see(tk.END)

def send_message():
    user_text = entry.get("1.0", tk.END).strip()
    if user_text == "":
        return

    add_to_chat("You: " + user_text + "\n", "user")
    entry.delete("1.0", tk.END)

    bot_text = get_response(user_text)
    add_to_chat("Bot: " + bot_text + "\n\n", "bot")

    save_to_db(user_text, bot_text)

def start_listening():
    global is_listening
    is_listening = True
    add_to_chat("🎤 Listening... Speak now!\n", "system")

    rec = KaldiRecognizer(vosk_model, 16000)
    mic = pyaudio.PyAudio().open(format=pyaudio.paInt16, channels=1, rate=16000,
                                 input=True, frames_per_buffer=8192)
    mic.start_stream()

    while is_listening:
        data = mic.read(4096, exception_on_overflow=False)
        if rec.AcceptWaveform(data):
            result = json.loads(rec.Result())
            user_text = result.get("text", "")
            if user_text.strip():
                entry.delete("1.0", tk.END)
                entry.insert(tk.END, user_text)
                add_to_chat(f"You said: {user_text}\n", "user")
                break

def stop_listening():
    global is_listening
    is_listening = False
    add_to_chat("⏹ Listening stopped.\n", "system")

def load_history():
    cursor.execute("SELECT user_input, bot_response FROM history ORDER BY id DESC LIMIT 10")
    rows = cursor.fetchall()
    add_to_chat("----- Chat History -----\n", "system")
    for row in rows[::-1]:
        add_to_chat("You: " + row[0] + "\n", "user")
        add_to_chat("Bot: " + row[1] + "\n\n", "bot")
    add_to_chat("-------------------------\n", "system")

# ========== GUI ==========
root = tk.Tk()
root.title("AI Chatbot (Offline AI Chitthi)")
root.geometry("700x550")
root.configure(bg="#1e1e2f")  # dark background

# Chat Window
chat_window = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=70, height=20,
                                        state=tk.DISABLED, bg="#2b2b3d", fg="white",
                                        font=("Arial", 11))
chat_window.pack(padx=10, pady=10)

# Text tag colors
chat_window.tag_config("user", foreground="#4FC3F7")     # light blue for user
chat_window.tag_config("bot", foreground="#A5D6A7")      # light green for bot
chat_window.tag_config("system", foreground="#FFD54F")   # yellow for system messages

# Entry + Send button
frame = tk.Frame(root, bg="#1e1e2f")
frame.pack(padx=10, pady=5, fill="x")

entry = tk.Text(frame, height=3, width=50, bg="#2b2b3d", fg="white",
                insertbackground="white", font=("Arial", 11))
entry.pack(side="left", padx=5)

send_button = tk.Button(frame, text="Send", command=send_message, bg="#4CAF50", fg="white",
                        font=("Arial", 11, "bold"))
send_button.pack(side="right", padx=5)

# Voice controls
voice_frame = tk.Frame(root, bg="#1e1e2f")
voice_frame.pack(pady=5)

start_button = tk.Button(voice_frame, text="🎤 Start Listening", command=start_listening,
                         bg="#2196F3", fg="white", font=("Arial", 10, "bold"))
start_button.pack(side="left", padx=5)

stop_button = tk.Button(voice_frame, text="⏹ Stop Listening", command=stop_listening,
                        bg="#f44336", fg="white", font=("Arial", 10, "bold"))
stop_button.pack(side="left", padx=5)

# History button
bottom_frame = tk.Frame(root, bg="#1e1e2f")
bottom_frame.pack(pady=5, fill="x")

history_button = tk.Button(bottom_frame, text="📜 Load History", command=load_history,
                           bg="#9C27B0", fg="white", font=("Arial", 10, "bold"))
history_button.pack(side="left", padx=5)

root.mainloop()
