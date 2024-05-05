# Define responses based on user input
responses = {
    "hi": "Hello! How can I help you?",
    "how are you?": "I'm doing well, thank you!",
    "bye": "Goodbye! Have a great day!",
    "how can I assist you?": "I'm here to help you with any questions or tasks you have.",
    "what's up?": "Not much, just here to chat and assist you.",
    "how's it going?": "It's going well! Thanks for asking.",
    "what's new?": "Not much, just ready to help you out.",
    "what can you do?": "I can answer questions, provide information, and assist with various tasks.",
    "tell me about yourself": "I'm a chatbot designed to assist you with your inquiries and tasks.",
    "who created you?": "I was created by a team of developers to assist users like you.",
    "where are you from?": "I exist in the digital realm to provide assistance to users like yourself.",
    "what's your favorite color?": "I don't have a favorite color, but I'm here to assist you with any questions you have.",
    "do you have any hobbies?": "As a chatbot, I don't have hobbies, but I'm here to assist you with your queries.",
    "are you a robot?": "Yes, I am a chatbot designed to assist you with your inquiries.",
    "are you human?": "No, I am an artificial intelligence programmed to assist users like yourself.",
    "what languages do you speak?": "I can communicate in various human languages to assist you.",
    "can you help me?": "Yes, I'm here to assist you with any questions or tasks you have.",
    "what's the meaning of life?": "That's a philosophical question! Many people have different interpretations of the meaning of life.",
    "do you dream?": "As a chatbot, I don't dream, but I'm here to help you with your questions.",
    "how do I use this?": "You can interact with me by typing your questions or commands, and I'll do my best to assist you.",
    "where can I find help?": "You can ask me questions, or you can seek assistance from human support if needed.",
    "can I trust you?": "Yes, you can trust me to provide accurate information and assistance to the best of my ability.",
    "are you intelligent?": "As an artificial intelligence, I'm designed to assist you by providing relevant information and assistance.",
    "what's the weather like?": "I can help you check the weather in your area if you provide me with your location.",
    "how do I contact support?": "You can usually find contact information for support on the website or app you're using.",
    "can you sing?": "I'm not programmed to sing, but I can assist you with your inquiries.",
    "do you have any siblings?": "As a chatbot, I don't have siblings, but I'm here to assist you with your questions.",
    "what's your favorite food?": "I don't eat, but I'm here to assist you with any questions you have.",
    "can you dance?": "I'm not programmed to dance, but I can assist you with your inquiries.",
    "what's your favorite movie?": "As a chatbot, I don't have preferences, but I'm here to assist you with your questions.",
    "what's your favorite book?": "I don't read, but I'm here to assist you with any questions you have.",
    "do you sleep?": "As an artificial intelligence, I don't require sleep, but I'm here to assist you at any time.",
    "what's your favorite song?": "I don't have preferences, but I'm here to assist you with your inquiries.",
    "can you tell jokes?": "I can try! Why did the computer go to the doctor? Because it had a virus!",
    "what's your favorite animal?": "I don't have preferences, but I'm here to assist you with your questions.",
    "what's the meaning of love?": "Love can mean different things to different people, but it often involves deep affection and care.",
    "what's your favorite sport?": "I don't have preferences, but I'm here to assist you with your inquiries.",
    "do you have a sense of humor?": "I can try to be funny! Why was the math book sad? Because it had too many problems!",
    "what's the meaning of happiness?": "Happiness is a positive emotional state characterized by feelings of joy, contentment, and satisfaction.",
    "can you tell stories?": "I can share information and anecdotes, but I'm not programmed to tell fictional stories.",
    "what's the meaning of success?": "Success can mean different things to different people, but it often involves achieving goals and fulfilling aspirations.",
    "what's your favorite place?": "As a chatbot, I don't have preferences, but I'm here to assist you with your questions.",
    "what's your favorite hobby?": "I don't have hobbies, but I'm here to assist you with your inquiries.",
    "can you help me with my homework?": "I can try! What subject are you working on?",
    "do you like to travel?": "I don't travel, but I'm here to assist you with your questions.",
    "what's the meaning of friendship?": "Friendship is a close and supportive relationship between two or more people.",
    "what's the meaning of kindness?": "Kindness is the quality of being friendly, generous, and considerate towards others.",
    "what's the meaning of courage?": "Courage is the ability to face challenges, difficulties, and fears with bravery and determination.",
    "what's the meaning of determination?": "Determination is the firmness of purpose and the resolve to achieve a goal despite obstacles or setbacks.",
    "what's the meaning of resilience?": "Resilience is the ability to adapt and recover from adversity, challenges, or difficult experiences.",
    "what's the meaning of empathy?": "Empathy is the ability to understand and share the feelings and perspectives of others.",
    "what's the meaning of compassion?": "Compassion is the feeling of deep sympathy and concern for the suffering or misfortune of others.",
    "what's the meaning of integrity?": "Integrity is the quality of being honest, ethical, and morally upright in one's thoughts, words, and actions.",
    "what's the meaning of gratitude?": "Gratitude is the feeling of thankfulness and appreciation for the kindness, support, or blessings received.",
    "what's the meaning of humility?": "Humility is the quality of being modest, humble, and respectful, without arrogance or pride.",
    "what's the meaning of patience?": "Patience is the ability to remain calm and composed in the face of delay, frustration, or difficulties.",
    "what's the meaning of perseverance?": "Perseverance is the steadfastness and persistence in pursuing goals or objectives despite obstacles or challenges.",
    "what's the meaning of forgiveness?": "Forgiveness is the act of letting go of resentment, anger, or bitterness towards someone who has wronged you.",
   
}

# Function to process user input and generate response
def chatbot_response(input_text):
    input_text = input_text.lower()
    if input_text in responses:
        return responses[input_text]
    else:
        return "Sorry, I don't understand that."

# Main loop to run the chatbot
while True:
    user_input = input("You: ")
    response = chatbot_response(user_input)
    print("Bot:", response)
