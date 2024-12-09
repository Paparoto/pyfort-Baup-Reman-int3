import time


def introduction():
    print("Hey !")
    time.sleep(0.5)
    print("Welcome to the Fort Boyard game !!!")
    time.sleep(0.25)
    print("Here are the rules :")
    time.sleep(0.5)
    print("You have to complete challenges to earn keys and unlock the treasure room")
    time.sleep(1.5)
    print("The aim is to collect tree keys to access it.")

def compose_equipe():
    team_size = 0
    while not 1>=team_size>=3:
        try :
            team_size = int(input("Please enter the size of your team (1 to 3 players) : "))
            if not 1>=team_size>=3:
                print("That's not a correct number of teammates !")
        except:
            print("That's not a correct number of teammates !")
    
