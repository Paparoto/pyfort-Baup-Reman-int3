def next_player(player):
    if player == 1:
        return 0
    else:
        return 1
def empty_grid():
    return [[""]*3]*3

def display_grid(grid, message):
    print(message)
    for i in range(3):
        print("| ", end="")
        for j in range(3):
            print(grid[i][j], end=" | ")
        print()

def ask_position():
    while True:
        x = int(input("Enter the row position :"))
        y = int(input("Enter the collumn position :"))
        if 0<=x<=3 and 0<=y<=3:
            return (x, y)
        else:
            print("Wrong coordonates ! Enter them again.")



def initialize():
    grid = empty_grid()
    print("Place your first Boat : ")
    position = ask_position()
    grid[position[0]][[position[1]]] = "B"
    print("Place your second Boat : ")
    position = ask_position()
    grid[position[0]][[position[1]]] = "B"
    return grid

def turn(player, player_shots_grid, opponent_grid):
    if player==0:
        print(player_shots_grid)
    