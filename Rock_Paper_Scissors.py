import random

user_wins = 0
Computer_wins = 0

options = ["rock", "paper", "scissors"]

while True:
    user_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower
    if user_input == "q":
        quit
    if user_input not in ["rock", "paper", "scissors"]:
        print("Invalid Input")
        continue

    random_number = random.randint(0,2)
    computer_pick = options[random_number]
    print("Computer picked", computer_pick+".")
    
    if user_inputs == "rock" and computer_pick == "scissors":
        print("You won!")
        user_wins +=1
    elif user_inputs == "paper" and computer_pick == "rock":
        print("You won!")
        user_wins +=1
    elif user_inputs == "scissors" and computer_pick == "paper":
        print("You won!")
        user_wins +=1
    else:
        print("You lost!")
        Computer_wins+=1
    
print("You won", )
print("Goodbye!")