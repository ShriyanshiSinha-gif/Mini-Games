import random 



def rock_paper_scissors():
    preferences = ["rock", "paper", "scissors"]
    print("\n--- Rock, Paper, Scissors ---")
    user = input("Pick Rock , Paper, or Scissors: ").lower()
    
    if user not in preferences:
        print("Invalid preference!")
        return

    comp = random.choice(preferences)
    print(f"Computer: {comp}")

    if user == comp:
        print("Result: No Winner This Time-It's a Draw!")
    elif (user == "rock" and comp == "scissors") or \
         (user == "paper" and comp == "rock") or \
         (user == "scissors" and comp == "paper"):
        print("Result: Awesome! You Won the Game!")
    else:
        print("Result:Computer Wins This Round!")