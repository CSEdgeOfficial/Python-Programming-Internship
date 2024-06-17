import nltk
from nltk.chat.util import Chat, reflections

# Define pairs of patterns and responses
pairs = [
    (r'hi|hello|hey', ['Hello!', 'Hey there!', 'Hi! How can I help you?']),
    (r'how are you?', ['I\'m doing well, thank you!', 'I\'m good, thanks for asking!']),
    (r'what\'s your name\??', ['I\'m a chatbot!', 'You can call me ChatBot.']),
    (r'(.*) your name\??', ['I\'m a chatbot!', 'You can call me ChatBot.']),
    # Add more patterns and responses as needed
]

# Create a Chatbot instance
chatbot = Chat(pairs, reflections)

print("Welcome! Type 'quit' to end the conversation.")

# Start the conversation loop
while True:
    user_input = input("You: ")
    if user_input.lower() == 'quit':
        print("ChatBot: Bye! Have a great day!")
        break
    else:
        response = chatbot.respond(user_input)
        print("ChatBot:", response)
