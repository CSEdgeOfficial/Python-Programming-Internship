import nltk
from nltk.chat.util import Chat, reflections

# Define patterns and responses
patterns = [
    (r'hi|hello|hey', ['Hello!', 'Hi there!', 'Hey!']),
    (r'how are you?', ["I'm doing well, thank you!", "I'm great, thanks for asking!"]),
    (r'what is your name?', ["I'm just a simple chatbot.", "I'm a chatbot designed to assist you."]),
    (r'bye|goodbye', ["Goodbye!", "See you later!", "Bye!"]),
    # Add more patterns and responses as needed
]

# Create a chatbot
chatbot = Chat(patterns, reflections)

# Define a function to chat with the user
def chat():
    print("Hello! How can I assist you today?")
    while True:
        user_input = input("> ")
        response = chatbot.respond(user_input)
        print(response)
        if user_input.lower() == 'bye':
            break

# Start the chat
if __name__ == "__main__":
    chat()
