import math_challenges
import logical_challenges
import chance_challenges
import pere_fouras_challenge
import final_challenge
import utility_functions


def game():
    utility_functions.introduction()
    print()
    team = utility_functions.compose_equipe()
    print()
    total_keys = 0
    for i in range(len(team)):
        total_keys+=team[0]["keys_won"]
    while total_keys<3:
        print("Keys won by the team :", total_keys)
        challenge_number = utility_functions.challenges_menu()
        print()
        player = utility_functions.choose_player(team)
        print()
        if challenge_number==1:
            won=math_challenges.math_challenge()
            if won:
                player["keys_won"] +=1
            utility_functions.record_history("math_challenge", player, won)
        elif challenge_number==2:
            won = logical_challenges.battleship_game()
            if won:
                player["keys_won"] += 1
            utility_functions.record_history("logical_challenge", player, won)
        elif challenge_number==3:
            won = chance_challenges.chance_challenge()
            if won:
                player["keys_won"] += 1
            utility_functions.record_history("chance_challenge", player, won)
        elif challenge_number==4:
            won = pere_fouras_challenge.pere_fouras_riddles()
            if won:
                player["keys_won"] += 1
            utility_functions.record_history("pere_fouras_riddles", player, won)
        total_keys = 0
        for i in range(len(team)):
            total_keys += team[0]["keys_won"]
        print()
    final_challenge.treasure_room()


game()





