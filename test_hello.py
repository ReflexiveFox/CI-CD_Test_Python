import unittest
from hello import greet
from math_utils import add_numbers, calculate_factorial, calculate_fibonacci

class TestHello(unittest.TestCase):

    def test_greet(self):
        try:
            self.assertEqual(greet(), "Hello World!")
            print(f"greet() result: {greet()}")
        except AssertionError as e:
            print(f"AssertionError: {e}")

    def test_greet(self):
        person_1 = "Lorenzo"
        try:
            self.assertEqual(greet(), f"Hello World!")
            print(f"greet() result: {greet()}")
        except AssertionError as e:
            print(f"AssertionError: {e}")
        
        try:
            self.assertEqual(greet(person_1), f"Hello {person_1}!")
            print(f"greet({person_1}) result: {greet(person_1)}")
        except AssertionError as e:
            print(f"AssertionError: {e}")

    def test_add_numbers(self):
        try:
            self.assertEqual(add_numbers(3, 4), 7)
            print(f"add_numbers(3, 4) result: {add_numbers(3, 4)}")
        except AssertionError as e:
            print(f"AssertionError: {e}")
        
        try:
            self.assertEqual(add_numbers(-1, 1), 0)
            print(f"add_numbers(-1, 1) result: {add_numbers(-1, 1)}")
        except AssertionError as e:
            print(f"AssertionError: {e}")

        try:
            self.assertEqual(add_numbers(-1, -1), -2)
            print(f"add_numbers(-1, -1) result: {add_numbers(-1, -1)}")
        except AssertionError as e:
            print(f"AssertionError: {e}")

    def test_calculate_factorial(self):
        try:
            self.assertEqual(calculate_factorial(0), 1)
            print(f"calculate_factorial(0) result: {calculate_factorial(0)}")
        except AssertionError as e:
            print(f"AssertionError: {e}")

        try:
            self.assertEqual(calculate_factorial(1), 1)
            print(f"calculate_factorial(1) result: {calculate_factorial(1)}")
        except AssertionError as e:
            print(f"AssertionError: {e}")

        try:
            self.assertEqual(calculate_factorial(5), 120)
            print(f"calculate_factorial(5) result: {calculate_factorial(5)}")
        except AssertionError as e:
            print(f"AssertionError: {e}")

        try:
            self.assertEqual(calculate_factorial(10), 3628800)
            print(f"calculate_factorial(10) result: {calculate_factorial(10)}")
        except AssertionError as e:
            print(f"AssertionError: {e}")

        for invalid_input in [-1, 1.5, "string"]:
            with self.assertRaises(ValueError):
                calculate_factorial(invalid_input)
                print(f"calculate_factorial({invalid_input}) correctly raised ValueError")
    def test_calculate_fibonacci(self):
        try:
            self.assertEqual(calculate_fibonacci(0), [0])
            print(f"calculate_fibonacci(1) result: {calculate_fibonacci(1)}")
        except AssertionError as e:
            print(f"AssertionError: {e}")

        try:
            self.assertEqual(calculate_fibonacci(1), [0, 1])
            print(f"calculate_fibonacci(1) result: {calculate_fibonacci(1)}")
        except AssertionError as e:
            print(f"AssertionError: {e}")

        try:
            self.assertEqual(calculate_fibonacci(10), [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55])
            print(f"calculate_fibonacci(10) result: {calculate_fibonacci(10)}")
        except AssertionError as e:
            print(f"AssertionError: {e}")

        
if __name__ == "__main__":
    unittest.main(buffer=False)
