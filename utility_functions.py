import time



def introduction():
    print("Hey !")
    time.sleep(0.5)
    print("Welcome to the Fort Boyard game !!!")
    time.sleep(1)
    print("Here are the rules :")
    time.sleep(1)
    print("You have to complete challenges to earn keys and unlock the treasure room")
    time.sleep(1.5)
    print("The aim is to collect tree keys to access it.")
    time.sleep(1.5)

def compose_equipe():
    team_size = 0
    while not 1<=team_size<=3:
        try :
            team_size = int(input("Please enter the size of your team (1 to 3 players) : "))
            if not 1<=team_size<=3:
                time.sleep(0.5)
                print("That's not a correct number of teammates !")
        except:
            time.sleep(0.5)
            print("That's not a correct number of teammates !")
        time.sleep(1)
    time.sleep(1)
    team = []
    for i in range(team_size):
        player = {}
        print(f"Who is player {i+1} ?")
        time.sleep(0.5)
        player["name"] = input("What's his name ?\nHis name is ")
        player["profession"] = input("And his profession ?\n")
        player["leader"]= input("Is he the team leader ? (write yes if so, just press enter if not) : ").upper() == "YES"
        player["keys_won"] = 0
        team.append(player)
    leader_found = True
    for player in team:
        leader_found = player["leader"]
        if leader_found:
            break
    if not leader_found:
        new_lead = team[0]
        new_lead["leader"] = True
        time.sleep(0.5)
        print(f"No player were assignated as the team leader at initialisation so {new_lead['name']} has been automatically given this role.")
        time.sleep(2.5)
    return team

def challenges_menu():
    print("1. Mathematics challenge\n2. Logic challenge\n3. Chance challenge\n4. Père Fouras' riddle")
    time.sleep(2)
    challenge_selected = 0
    while not 1<=challenge_selected<=4:
        try :
            challenge_selected = int(input("What challenge do you wish to do ? (1, 2, 3 or 4) : "))
            if challenge_selected>4 or challenge_selected<1:
                time.sleep(0.5)
                print("You're not very good at this are you ? :(")
        except:
            time.sleep(0.5)
            print("This is not even a number ! You have to enter a number")
    return challenge_selected

def choose_player(team):
    bool_to_lead = {True : "Leader", False:"Member"}
    for i in range(len(team)):
        print(f"{i+1}. {team[i]['name']} ({team[i]['profession']}) - {bool_to_lead[team[i]['leader']]}")
    player_number=0
    while not 1<=player_number<=len(team):
        try :
            player_number = int(input("Enter the player's number: "))
            if not 1<=player_number<=len(team):
                time.sleep(0.5)
                print("Do you see this number as an option displayed ?")
                time.sleep(0.5)
                print("No ?")
                time.sleep(0.5)
                print("Then don't make me loose my time")
                time.sleep(1.5)
        except:
            print("I said player's NUMBER. Are you serious ? Try again...")
    return team[player_number-1]

def record_history(challenge_name, player, result):
    with open("output/history.txt", "a") as f:
        f.write(f"Player : {player['name']} ; Challenge : {challenge_name} ; Won : {result}\n")



