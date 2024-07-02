import unittest
from hello import main

class TestHello(unittest.TestCase):
    def test_main(self):
        self.assertEqual(main(), "Hello, World!")

if __name__ == "__main__":
    unittest.main()
