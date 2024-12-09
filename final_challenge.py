import json, random, time
def treasure_room():
    tv_game = json.load(open("data/TRClues.json", "r"))
    year = random.choice(list(tv_game["Fort Boyard"].keys()))
    show = random.choice(list(tv_game["Fort Boyard"][year].keys()))
    clues = tv_game["Fort Boyard"][year][show]["Clues"]
    code_word = tv_game["Fort Boyard"][year][show]["CODE-WORD"]
    print("Here are the first 3 clues :")
    i=0
    while i<3:
        time.sleep(1)
        print(clues[i])
        i+=1
    attempts=3
    answer_correct = False
    while attempts > 0 and not answer_correct:
        answer = input("Please write down your answer below :\n")
        if answer == code_word:
            answer_correct = True
        else:
            print("Wrong !")
            attempts-=1
            if attempts>0:
                time.sleep(0.5)
                print(attempts, "attemps remaining")
                time.sleep(0.5)
                i+=1
                print(f"Here is another clue : \"{clues[i]}\"")
            else:
                print(f"The correct word was \"{code_word}\"")
    time.sleep(1)
    if answer_correct:
        print("Victory !")
    else:
        print("Fail :(")

