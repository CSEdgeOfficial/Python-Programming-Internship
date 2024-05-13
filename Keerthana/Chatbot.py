import tkinter as tk
from tkinter import scrolledtext
from tkinter import messagebox
from nltk.chat.util import Chat, reflections

# Define patterns and responses for the chatbot
patterns = [
    (r'hi|hello|hey', ['Hello!', 'Hey there!', 'Hi!']),
    (r'how are you?', ['I am doing well, thank you.', 'I am fine, thanks for asking.']),
    (r'what is your name?', ['I am a chatbot.', 'You can call me Chatbot.']),
    (r'my name is (.*)', ['Hello %1!', 'Nice to meet you, %1.']),
    (r'(.*) (location|city|country)', ['I am not sure about %2.']),
    (r'quit', ['Bye, take care!', 'Goodbye!', 'See you later.']),
]

# Create the chatbot
chatbot = Chat(patterns, reflections)

# Function to handle sending user messages and receiving responses
def send_message():
    user_input = user_entry.get()
    user_entry.delete(0, tk.END)
    if user_input.lower() == 'quit':
        root.quit()
    response = chatbot.respond(user_input)
    chat_display.config(state=tk.NORMAL)
    chat_display.insert(tk.END, "You: " + user_input + "\n")
    chat_display.insert(tk.END, "Chatbot: " + response + "\n\n")
    chat_display.config(state=tk.DISABLED)
    chat_display.yview(tk.END)

# Create the GUI window
root = tk.Tk()
root.title("Chatbot")

# Create a scrolled text widget for displaying chat messages
chat_display = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=50, height=20)
chat_display.grid(row=0, column=0, padx=10, pady=10, columnspan=2)
chat_display.config(state=tk.DISABLED)

# Create an entry widget for user input
user_entry = tk.Entry(root, width=40)
user_entry.grid(row=1, column=0, padx=10, pady=10)

# Create a button to send user input
send_button = tk.Button(root, text="Send", command=send_message)
send_button.grid(row=1, column=1, padx=10, pady=10)

# Run the GUI application
root.mainloop()
