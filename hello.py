# hello.py 
import  math_utils
def greet(name="World"):
    return f"Hello {name}!"

if __name__ == "__main__":
    while True:
        print("+-----------------------+")
        print("| Choose an option:")
        print("\n| 1. Greet")
        print("\n| 2. Add Numbers")
        print("\n| 3. Calculate factorial")
        print("\n| 4. Calculate Fibonacci")
        print("\n| 5. Exit")
        print("+-----------------------+")
        choice = input("\nEnter your choice: ")
        if choice == '1':
            name = input("Enter your name: ")
            print(f"\n{greet(name)}")
        elif choice == '2':
            a = float(input("\nEnter first number: "))
            b = float(input("Enter second number: "))
            print(f"\nThe sum is {math_utils.add_numbers(a,b)}")
        elif choice == '3':
            a = int(input("Enter non negative integer: "))
            try:
                print(f"\nFactorial of {a}: {math_utils.calculate_factorial(a)}")
            except ValueError as e:
                print(e)
        elif choice == '4':
            n = int(input("\nEnter a non-negative integer: "))
            try:
                fibonacci_sequence = math_utils.calculate_fibonacci(n)
                print(f"The Fibonacci sequence up to {n} is: {fibonacci_sequence}")
            except ValueError as e:
                print(e)
        elif choice == '5':
            print("\nLeaving application...")
            break
        else:
            print("\nInput not recognized, try again")
            continue

