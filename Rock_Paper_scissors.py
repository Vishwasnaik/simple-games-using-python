import random

options = ("Rock" , "Paper" , "Scissors")
running = True

while running:
    
    player = None
    computer = random.choice(options)


    while player not in options:
        player = input("enter a choice (Rock,Paper,Scissors): ")


    print(f"player :{player}")
    print(f"computer:{computer}")


    if player == computer:
        print("It's a tie!")
    elif player == "Rock" and computer == "Scissors":
        print("You win!")
    elif player == "Paper" and computer == "Rock":
        print("You win!")
    elif player == "Scissors" and computer == "Paper":
        print("You win!")

    else:
        print("You lose!")

    if not input("play again? (y/n): ").lower() == "y":
        running = False


print("thanks for playing ")