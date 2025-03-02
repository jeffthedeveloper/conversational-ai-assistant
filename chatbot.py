import nltk
from nltk.chat.util import Chat, reflections

pairs = [
    (r'hi|hello|hey', ['Hello!', 'Hi there!', 'Hey!']),
    (r'bye|goodbye', ['Goodbye!', 'See you later!', 'Bye!']),
    (r'how are you|how\'s it going', ['I am doing well, thank you!', 'I\'m good, how about you?']),
    (r'what is your name|who are you', ['I am a chatbot.', 'You can call me AI Assistant.']),
    (r'tell me a joke', ['Why don\'t scientists trust atoms? Because they make up everything!']),
    (r'what is the weather today', ['I\'m sorry, I cannot provide real-time information.']),
    (r'default', ['I\'m not sure I understand.']), # Resposta padrão
]

chatbot = Chat(pairs, reflections)

def respond_to_user(message):
    return chatbot.respond(message)