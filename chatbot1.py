import tkinter as tk
from tkinter import scrolledtext
import datetime
import random

# Chatbot logic
def get_bot_response(user_input):
    user_input = user_input.lower()
    jokes = [
        "Why don’t programmers like nature? It has too many bugs.",
        "Why did the computer go to the doctor? It caught a virus!",
        "Why do Python programmers wear glasses? Because they can't C."
    ]
    
    if any(word in user_input for word in ["hi", "hello", "hey", "good morning", "good evening"]):
        return "Hello! I'm Nova, Varsha's AI chatbot. How can I help you?"

    elif "name" in user_input or "who are you" in user_input:
        return "My name is Nova. Varsha created me!"

    elif "how are you" in user_input or "how do you do" in user_input:
        return "I'm just a program, but I'm doing great! How about you?"

    elif "who made you" in user_input or "creator" in user_input:
        return "I was built by Varsha, my awesome creator!"

    elif "anime" in user_input or "favourite anime" in user_input or "which anime" in user_input:
        return "Varsha loves 'Yona of the Dawn' — I’ve heard it’s amazing!"

    elif "game" in user_input or "favourite game" in user_input or "which game" in user_input:
        return "Varsha is working on cool games like a Pixel Game and AI Chatbot!"

    elif "time" in user_input:
        return f"The current time is {datetime.datetime.now().strftime('%H:%M:%S')}."

    elif "date" in user_input or "today" in user_input:
        return f"Today's date is {datetime.datetime.now().strftime('%d %B %Y')}."

    elif "joke" in user_input or "funny" in user_input:
        return random.choice(jokes)

    elif "bye" in user_input or "exit" in user_input:
        return "Goodbye! Have a great day!"

    else:
        return "Hmm, I don't understand that. Try asking something else!"

# Send message function
def send_message():
    user_input = entry.get()
    if user_input.strip() != "":
        chat_window.config(state=tk.NORMAL)
        chat_window.insert(tk.END, f"You: {user_input}\n")
        entry.delete(0, tk.END)

        bot_response = get_bot_response(user_input)
        chat_window.insert(tk.END, f"Bot: {bot_response}\n\n")
        chat_window.config(state=tk.DISABLED)
        chat_window.yview(tk.END)

# GUI setup
root = tk.Tk()
root.title("Varsha's AI Chatbot")
root.geometry("400x500")

chat_window = scrolledtext.ScrolledText(root, wrap=tk.WORD, state=tk.DISABLED)
chat_window.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

entry = tk.Entry(root, font=("Arial", 14))
entry.pack(padx=10, pady=5, fill=tk.X)

send_button = tk.Button(root, text="Send", command=send_message, bg="#6a5acd", fg="white")
send_button.pack(pady=5)

root.mainloop()
