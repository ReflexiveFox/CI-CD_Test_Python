def main():
    return "Hello, World!"

def greet(name):
    return f"Hello {name}!"

def add_numbers(a, b):
    return a + b

def calculate_factorial(number):
    if(number > 1):
        return number * calculate_factorial(number-1)
    return 1

a = 3
b = 4
factorial_number = 0
if __name__ == "__main__":
    print(main())
    print(greet("Lorenzo"))
    print(f"add_numbers({a}, {b}) => {add_numbers(a,b)}")
    print(f"calculate_factorial({factorial_number}) => {calculate_factorial(factorial_number)}")
