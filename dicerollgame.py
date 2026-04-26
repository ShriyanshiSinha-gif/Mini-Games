import random

def dice_roll_game():
    print("\n--- Dice Roll Game ---")
    user = random.randint(1, 6)
    comp = random.randint(1, 6)
    
    print(f"You: {user} | Computer: {comp}")
    
    if user > comp:
        print("Result: Awesome! You Won the Game!")
    elif comp > user:
        print("Result: Computer Wins This Round!")
    else:
        print("Result: No Winner This Time-It's a Draw!")