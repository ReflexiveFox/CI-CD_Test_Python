import unittest
from hello import main, greet, add_numbers

class TestHello(unittest.TestCase):
    def test_main(self):
        self.assertEqual(main(), "Hello, World!")

    def test_greet(self):
        self.assertEqual(greet("Lorenzo"), "Hello Lorenzo!")
        self.assertEqual(greet("Giorgia"), "Hello Giorgia!")

    def test_add_numbers(self):
        self.assertEqual(add_numbers(3,4), 7)
        self.assertEqual(add_numbers(-1,1), 0)
        self.assertEqual(add_numbers(-1,-10) , -11)

if __name__ == "__main__":
    unittest.main()
