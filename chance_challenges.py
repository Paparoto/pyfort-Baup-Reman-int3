import random, time


def shell_game():
    shells = ['A','B','C']
    attempt = 0
    sentences = "Welcome to the shell game!\nYou have to guess under which shell (A, B or C) the key is hidden.\nYou have two attempts to find the key."
    for char in sentences:
        print(char, end='', flush=True)
        time.sleep(0.05)
    while attempt < 2:
        attempt += 1
        key_shell = random.choice(shells)
        print(f"\nTentative {attempt}/2")
        player_choice = input("Choose a shell (A, B or C):").upper()
        if player_choice in shells:
            if player_choice == key_shell:
                print("Well done ! You found the key under the shell", player_choice)
                return True
            else:
                print("Too bad ! The key is not under the shell", player_choice)
        else:
            print("Invalid choice. Please choose from A, B or C.")
        time.sleep(1)
        print(f"The key was under the shell {key_shell}.")
        time.sleep(1)
        print("Remixing the shells...")
        time.sleep(1)
    time.sleep(1)
    print("You have used both of your attempts. You lost!")
    time.sleep(1)
    return False




def rolling_dice_game():
    attempts = 0
    while attempts <3:
        print(3-attempts, "attempts remaining")
        input("Roll the dice (press ENTER ) : ")
        time.sleep(1)
        rolls = (random.randint(1,6), random.randint(1,6))
        print(f"Here are the rolls results : {rolls[0]} and {rolls[1]}")
        if 6 in rolls:
            print("Congratulations ! You've won a key.")
            return True
        time.sleep(2)
        print("The game master is rolling the dice")
        time.sleep(1)
        rolls = (random.randint(1,6), random.randint(1,6))
        print(f"Here are the rolls results : {rolls[0]} and {rolls[1]}")
        if 6 in rolls:
            time.sleep(1)
            print("Oh No ! The game master won the game, you loose.")
            time.sleep(1)
            return False
        time.sleep(2)
        attempts+=1
        if attempts<3:
            print("No 6 were rolled, moving on to the next attempt...\n\n")
            time.sleep(2)
            print("...\n\n")
            time.sleep(2)
        else:
            print("No 6 were rolled for the third time now, no one won the game, it's a draw.")
            time.sleep(1)
            return False


def chance_challenge():
    challenge = random.randint(1, 2)
    if challenge == 1:
        if shell_game():
            return True
    elif challenge == 2:
        if rolling_dice_game():
            return True
    return False



