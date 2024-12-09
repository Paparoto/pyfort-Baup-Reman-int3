import json
import random

def load_riddles(file):
    with open(file, 'r') as f:
        riddles = json.load(f)
    return riddles


def pere_fouras_riddles():
    riddles = load_riddles("data/PFRiddles.json")
    riddle = random.choice(riddles)
    question = riddle['question']
    correct_answer = riddle['answer'].lower()
    print("Welcome to the Père Fouras puzzle challenge!")
    print("You have 3 attempts to solve this puzzle:")
    print(f"Enigma : {question}")
    attempts = 3
    while attempts > 0:
        answer = input("Your answer : ").strip().lower()
        if answer == correct_answer:
            print("Great job ! You find the right answer. You win a key !")
            return True
        else:
            attempts -= 1
            if attempts > 0:
                print(f"Wrong answer. you have {attempts} attempt(s) remaining.")
            else:
                print(f"Shame ! You have no more attempts. The correct answer was : '{correct_answer}'.")
                return False

