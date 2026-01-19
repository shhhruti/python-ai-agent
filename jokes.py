import random

jokes = [
    "Why don’t programmers like nature? Too many bugs.",
    "Why did the Python developer go broke? Because he used up all his cache.",
    "Why was the computer cold? It forgot to close its Windows."
]

def tell_joke():
    return random.choice(jokes)
