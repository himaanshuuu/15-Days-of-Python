#game 

# Game: Random Number Guessing

import random

number = random.randint(1, 100)
tries = 0

while True:
    guess = int(input("Please guess a number between 1 to 100: "))
    tries += 1

    if number == guess:
        print(f"You are right! You guessed the number in {tries} tries.")
        break

    elif number > guess:
        print("Go a little higher.")

    elif number < guess:
        print("Go a little lower.")
     