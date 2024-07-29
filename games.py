# games.py
# This file contains small games

import random

def guessing_game():
    min_number, max_number = 1 , 100
    number_to_guess = random.randint(min_number, max_number)
    attempts = 0
    print(f"I'm thinking a number (integer) between {min_number} and {max_number}, which one is it?")
    while True:
        guessed_number = int(input(f"\nEnter your guess number between {min_number} and {max_number}\nAny number outside range will quit the game: "))
    
        attempts += 1
        
        if guessed_number < min_number or guessed_number > max_number:
                print(f"This number ({guessed_number}) is out of range!\nQuitting game...")
            break
        
        elif guessed_number < number_to_guess:
            print("Too low!")

        elif guessed_number > number_to_guess:
            print("Too high!")

        else:
            print(f"Correct! You guessed it in {attempts} attempts.")
            break
