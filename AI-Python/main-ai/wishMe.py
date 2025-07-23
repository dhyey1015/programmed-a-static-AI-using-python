import random

wish = [
    "How may I assist you?",
    "What can I do for you today?",
    "How can I help you?",
    "Is there anything I can help you with?",
    "Can I help you with something?",
    "How can I be of service?",
    "Want me to do something for you?",
]

def wishMe(wish):
    num = random.randint(0, len(wish) - 1)
    return wish[num]

