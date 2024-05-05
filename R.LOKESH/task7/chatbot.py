import nltk
from nltk.chat.util import Chat, reflections

# Define pairs of patterns and responses
pairs = [
    (r"hi|hello|hey", ["Hello!", "Hi there!", "Hey!"]),
    (r"how are you?", ["I'm doing well, thank you!", "I'm good, thanks for asking."]),
    (r"what is your name?", ["My name is Chatbot.", "I'm Chatbot, nice to meet you!"]),
    (r"bye|goodbye", ["Goodbye!", "See you later!", "Bye!"]),
    (r"(.*)", ["I'm sorry, I don't understand."])
]

# Create a chatbot using the defined pairs
chatbot = Chat(pairs, reflections)

# Start the conversation loop
print("Chatbot: Hello! I'm Chatbot. How can I help you today?")
while True:
    user_input = input("You: ")
    response = chatbot.respond(user_input)
    print("Chatbot:", response)
