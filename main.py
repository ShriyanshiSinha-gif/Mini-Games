import random
from rockpaperscissor import rock_paper_scissors
from dicerollgame import dice_roll_game
def game():
    while True:
        print("\n1. Rock-Paper-Scissors\n2. Dice Roll\n3. Exit")
        preference = input("Please Select Your Preference: ")
        
        if preference == "1":
            rock_paper_scissors()
        elif preference == "2":
            dice_roll_game()
        elif preference == "3":
            break
        else:
            print("Try again.")
game()