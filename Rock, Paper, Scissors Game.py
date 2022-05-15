import random

#Wins
user_wins = 0
computer_wins = 0

options = ["Rock", "Paper", "Scissors"]

while True:
    user_input = input("Type Rock/Paper/Scissors or press Q to quit ")
    if user_input == "q":
        break

    if user_input not in options:
        continue

    random_number = random.randint(0, 2)
    #rock: 0, paper: 1, scissors: 2
    computer_guess = options[random_number]
    print("Computer picked", computer_guess + ".")

    if user_input == "rock" and computer_guess == "scissors":
        print("You win!")
        user_wins += 1
        continue
    if user_input == "scissors" and computer_guess == "paper":
        print("You win!")
        user_wins += 1
        continue
    if user_input == "paper" and computer_guess == "rock":
        print("You win!")
        user_wins += 1
        continue

    else:
        print("You lost!")
        computer_wins += 1

print("You won this many times:", user_wins)
print("The computer won this many times:", computer_wins)
print("Goodbye!")
