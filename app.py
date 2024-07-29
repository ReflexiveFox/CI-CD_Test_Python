# app.py
# This file is handles the user interaction

import hello
import math_utils
import games

def interactive(inputs=None):
    input_func = inputs.pop if inputs else input

    while True:
        print("+-----------------------------+")
        print("| Choose an option:")
        print("\n| 1. Greet")
        print("\n| 2. Sum 2 numbers")
        print("\n| 3. Calculate factorial")
        print("\n| 4. Calculate Fibonacci")
        print("\n| 5. Play Guessing Game")
        print("\n| 6. Exit")
        print("+-----------------------------+")

        choice = input_func("\nEnter your choice: ")
        
        if choice == '1':
            print("\n~~~~~~ Greeting time ~~~~~~")
            name = str(input_func("Enter a name: "))
            print(f"\n{hello.greet(name)}")
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")

        elif choice == '2':
            print("\n~~~~~~ Sum 2 numbers ~~~~~~")
            num_A = float(input_func("Enter first number: "))
            num_B = float(input_func("Enter second number: "))

            print(f"\nThe sum of {num_A} and {num_B} is {math_utils.add_numbers(num_A, num_B)}")
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
        
        elif choice == '3':
            print("\n~~~~~~ Factorial calculation ~~~~~~")
            factorial_num = int(input_func("Enter a non-negative integer number: "))
            if factorial_num > 0:
                print(f"The factorial of {factorial_num}: {math_utils.calculate_factorial(factorial_num)}")
            else:
                print("Input not valid, back to main menu.")

            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
        
        elif choice == '4':
            print("\n~~~~~~ Fibonacci serie ~~~~~~")
            fibo_num = int(input_func("Enter a non-negative integer number: "))
            if fibo_num > 0:
                print(f"Fibonacci numbers for {fibo_num}: {math_utils.calculate_fibonacci(fibo_num)}")
            else:
                print("Input not valid, back to main menu.")

            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")

        elif choice == '5':
            print("\n~~~~~~~~~~~~~~~~~~~~~~~ IT'S GUESSING TIME!!! ~~~~~~~~~~~~~~~~~~~~~~~")
            games.guessing_game()
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
        
        elif choice == '6':
            print("\n! ! ! ! ! ! ! ! ! ! ! ! ! ! ! !")
            print("Leaving application...")
            print("! ! ! ! ! ! ! ! ! ! ! ! ! ! ! !")
            break

        else:
            print("\n################################")
            print("## Input not valid! Try again ##")
            print("################################\n")

if __name__ == "__main__":
    interactive()
