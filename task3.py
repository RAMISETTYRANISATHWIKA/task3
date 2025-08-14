import nltk
from nltk.chat.util import Chat, reflections
nltk.download('punkt', quiet=True)
nltk.download('wordnet', quiet=True)
nltk.download('omw-1.4', quiet=True)
pairs = [
    [
        r"hi|hello|hey",
        ["Hello there!", "Hi, how can I help you?", "Hey!"]
    ],
    [
        r"what is your name ?",
        ["I'm an AI chatbot!"]
    ],
    [
        r"how are you ?",
        ["I'm just a program, but I'm functioning perfectly!"]
    ],
    [
        r"what can you do ?",
        ["I can answer simple questions. Try asking about your name, greetings, or how I am."]
    ],
    [
        r"(.*) your name ?",
        ["My name is AI Chatbot. What's yours?"]
    ],
    [
        r"quit|exit",
        ["Goodbye!", "See you next time!", "Bye!"]
    ],
    [
        r"(.*)",
        ["I'm not sure I understand. Can you rephrase?"]
    ]
]
chatbot = Chat(pairs, reflections)

def run_chatbot():
    print("🤖 Welcome! Type 'quit' or 'exit' to end the chat.")
    chatbot.converse()
if __name__ == "__main__":
    run_chatbot()
