import json
import random

def load_riddles(file):
    with open(file, 'r') as f:
        riddles = json.load(f)
    return riddles


def pere_fouras_riddles():
    riddles = load_riddles("PFRiddles.json")
    riddle = random.choice(riddles)
    question = riddle['question']
    correct_answer = riddle['answer'].lower()
    print("Welcome to the Father Fouras puzzle challenge!")
    print("You have 3 attempts to solve this puzzle:")
    print(f"Enigma : {question}")

