import unittest
from hello import greet

class TestGreetFunction(unittest.TestCase):
    def test_greet(self):
        self.assertEqual(greet("Anshu"), "Hello, Anshu!")
        self.assertEqual(greet("World"), "Hello, World!")

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
