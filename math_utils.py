# math.py

def add_numbers(a, b):
    return a + b

def calculate_factorial(number):
    if not isinstance(number, int) or number < 0:
        raise ValueError("Input must be a non-negative integer")
    if number > 1:
        return number * calculate_factorial(number-1)
    return 1

def calculate_fibonacci(number):
    if not isinstance(number, int) or number < 0:
        raise ValueError("Input must be a non-negative integer")

    if number == 0:
        return [0]
    elif number == 1:
        return [0, 1]

    sequence = [0, 1]
    a, b = 0, 1

    for _ in range(2, number+1):
        a, b = b, a + b
        sequence.append(b)
    return sequence

a = 3
b = 4
factorial_number = 5
fibonacci_number = 6
if __name__ == "__main__":
    print(f"add_numbers({a}, {b}) => {add_numbers(a,b)}")
    print(f"calculate_factorial({factorial_number}) => {calculate_factorial(factorial_number)}")
    print(f"calculate_fibonacci({fibonacci_number}) => {calculate_fibonacci(fibonacci_number)}")
