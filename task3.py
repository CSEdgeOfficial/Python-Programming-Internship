import nltk
from nltk.tokenize import word_tokenize

# Download NLTK data
nltk.download('punkt')

# Define chatbot responses
responses = {
    "hi": "Hello! How can I assist you?",
    "how are you": "I'm just a program, so I don't have feelings, but I'm here to help!",
    # Add more predefined responses here
}

def preprocess_input(user_input):
    tokens = word_tokenize(user_input.lower())
    # Additional preprocessing steps if needed
    return tokens

def chatbot_response(user_input):
    tokens = preprocess_input(user_input)
    for query, response in responses.items():
        if any(token in query for token in tokens):
            return response
    return "I didn't understand. Can you please rephrase?"

if __name__ == "__main__":
    while True:
        user_query = input("You: ")
        if user_query.lower() == "exit":
            print("Chatbot: Goodbye!")
            break
        print("Chatbot:", chatbot_response(user_query))
