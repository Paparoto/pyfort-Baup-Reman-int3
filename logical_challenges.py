import random, time
def next_player(player):
    if player == 1:
        return 0
    else:
        return 1
def empty_grid():
    return [[" " for _ in range(3)] for _ in range(3)]

def display_grid(grid, message):
    print(message)
    for i in range(3):
        print("| ", end="")
        for j in range(3):
            print(grid[i][j], end=" | ")
        print()

def ask_position():
    while True:
        x = int(input("Enter the row position : "))
        y = int(input("Enter the collumn position : "))
        if 1<=x<=3 and 1<=y<=3:
            return (x-1, y-1)
        else:
            print("Wrong coordonates ! Enter them again.")



def initialize():
    print("Place your boats:")
    grid = empty_grid()
    for i in range(1,3):
        print(f"Boat {i}")
        position = ask_position()
        grid[position[0]][position[1]] = "B"
    return grid

def turn(player, player_shots_grid, opponent_grid):
    if player==0:
        print("It's your turn to shoot!")
        display_grid(player_shots_grid, "History of your previous shots:")
        time.sleep(0.5)
        print("Choose a new position for a new shot :")
        shot = ask_position()
        if opponent_grid[shot[0]][shot[1]] == "B":
            print("Hit, sunk!")
            player_shots_grid[shot[0]][shot[1]] = "x"
        else:
            print("Splash...")
            player_shots_grid[shot[0]][shot[1]] = "."
    else:
        time.sleep(2)

        print("It's the game master's turn:")
        shot = (random.randint(0,2),random.randint(0,2))
        while player_shots_grid[shot[0]][shot[1]] != " ":
            shot = (random.randint(0,2), random.randint(0,2))
        time.sleep(1)
        print(f"The game master shoots at position {shot[0]+1}, {shot[1]+1}")
        if opponent_grid[shot[0]][shot[1]] == "B":
            time.sleep(1)
            print("Hit, sunk!")
            player_shots_grid[shot[0]][shot[1]] = "x"
            time.sleep(2)
        else:
            time.sleep(1)
            print("Splash...")
            player_shots_grid[shot[0]][shot[1]] = "."
            time.sleep(2)

def has_won(player_shots_grid):
    hits=0
    for i in range(3):
        for j in range(3):
            if player_shots_grid[i][j] == "x":
                hits+=1
    if hits==2:
        return True
    else:
        return False

def battleship_game():
    print("Each player must place 2 boats on a 3x3 grid.\nBoats are represented by 'B' and missed shots by '.'. Sunk boats are marked by 'x'.")
    player_grid = initialize()
    game_master_grid = empty_grid()
    game_master_grid[random.randint(0,2)][random.randint(0,2)]="B"
    boat2=(random.randint(0,2),random.randint(0,2))
    while game_master_grid[boat2[0]][boat2[1]] == "B":
        boat2 = (random.randint(0,2), random.randint(0,2))
    game_master_grid[boat2[0]][boat2[1]] = "B"
    player_shooting_grid = empty_grid()
    game_master_shooting_grid = empty_grid()
    player=0
    while True:
        if player==0:
            turn(player,player_shooting_grid,game_master_grid)
        else:
            turn(player, game_master_shooting_grid, player_grid)
        if has_won(player_shooting_grid):
            print("The player won!")
            time.sleep(1)
            return True
        elif has_won(game_master_shooting_grid):
            print("The player loose!")
            time.sleep(1)
            return False
        else:
            player = next_player(player)