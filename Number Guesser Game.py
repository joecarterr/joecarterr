import random

#Name
print("Hello there and welcome to the number guesser game!\n")

#Person Selects Number Range
top_of_range = input('Type your desired number here:\n ')

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print('Only numbers larger than 0')
        quit()
else:
    print('Type in only numbers')
    quit()

#Giving The Numbers Between
r = random.randint(0, top_of_range)
player_guess = 0

while True:
    player_guess += 1
    users_guess = input("\nFeel free to make your guess here: ")
    if users_guess.isdigit():
        users_guess = int(users_guess)
    else:
        print('Type in only numbers')
        continue

    if users_guess == r:
        print('You got it right!')
        break
    else:
        if users_guess > r:
            print('\nYou were above the desired number')
        else:
            print('\nYou were below your desired number')

print('You were able to find the number in', player_guess, 'amount of attempts')