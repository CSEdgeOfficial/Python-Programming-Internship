import nltk
from nltk.chat.util import Chat, reflections

pairs = [
    ['hi|hello|hey', ['Hello!', 'Hi there!', 'Hey!']],
    ['how are you?', ['I am doing well, thank you!', 'I am good, thanks for asking!']],
    ['what is your name?', ['I am just a chatbot.', 'I am a chatbot designed to assist you.']],
    ['what can you do?', ['I can provide information on various topics. Feel free to ask me anything!']],
    ['bye|goodbye', ['Goodbye!', 'Bye! Have a great day!']],
    ['(.*) weather (.*)', ['Sorry, I cannot provide weather information at the moment.']],
    ['(.*) news (.*)', ['I am not able to provide news updates right now.']],
    ['(.*) time (.*)', ['Sorry, I cannot provide time information currently.']]
]

chat = Chat(pairs, reflections)

def chat_respond(user_input):
    return chat.respond(user_input)

def main():
    print("Hello! I'm a simple chatbot.")
    
    while True:
        user_input = input("You : ")
        response = chat_respond(user_input)
        print("Bot:",response)
        if user_input.lower() == 'bye':
            break
        
if __name__ == "__main__":
    main()