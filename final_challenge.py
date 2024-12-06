import json, random, time
def treasure_room():
    tv_game = json.load(open("data/TRClues.json", "r"))
    year = random.choice(list(tv_game["Fort Boyard"].keys()))
    show = random.choice(list(tv_game["Fort Boyard"][year].keys()))
    clues = tv_game["Fort Boyard"][year][show]["Clues"]
    code_word = tv_game["Fort Boyard"][year][show]["CODE-WORD"]
    print("Here are the first 3 clues :")
    for i in range(3):
        time.sleep(1)
        print(clues[i])
    attempts=3
    answer_correct = False
    while attempts > 0:
        answ
