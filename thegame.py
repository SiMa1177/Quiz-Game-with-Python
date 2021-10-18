Solar System Game 2020
This script runs my Solar System Quiz (planetquiz.py) file
and displays the top scorers up to ten.
By Roch Derilo
"""

# Import Planet Quiz file
import planetquiz as pq

#Set dictionary as players
players = {}
play_again = "YES"

# Loop the quiz
while play_again == "YES" :
    # Call the game
    pq.play_game()
    
    # Adding names to the list
    players[pq.name] = pq.score
    sorted_values = sorted(players.values(), reverse=True)
    sorted_players = {}

    i = 0
    for v in sorted_values :
        i = i + 1
        if i == 10 :
            break
        for key, value in players.items() :
            if value == v :
                sorted_players[key] = value

    if len(players) == 1 :
        print("\n\nHere is the top scorer:\n")
    elif len(players) <= 10 :
        print("\n\nHere are the top scorers:\n")
    else :
        print("\n\nHere are the top ten scorers:\n")

    for key, value in sorted_players.items():
        print (key + " with score " + str(value))

    # Play again prompt
    play_again = input("Would you like to play again? Type YES.")
