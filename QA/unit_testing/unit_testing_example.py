"""
Unit Testing Concept:
Unit testing is a software testing technique where individual units or components of a program are tested in isolation to ensure they work as expected. In Python, the built-in `unittest` module provides a framework for writing and running unit tests. Unit tests help catch bugs early, improve code quality, and make refactoring safer.

A unit test typically checks the output of a function or method for given inputs, and can also verify that exceptions are raised when expected. Tests are organized into test cases (classes) and test methods (functions).

"""

import unittest

# Example function to test
def add(a, b):
    return a + b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

class TestMathFunctions(unittest.TestCase):
    """Test cases for math functions"""

    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(0, 0), 0)

    def test_divide(self):
        self.assertEqual(divide(10, 2), 5)
        self.assertAlmostEqual(divide(5, 2), 2.5)

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            divide(1, 0)

if __name__ == "__main__":
    unittest.main()

"""
USEFUL UNITTEST FUNCTIONS AND EXAMPLES:

Core Functions:
- unittest.TestCase: Base class for creating test cases
- self.assertEqual(a, b): Check if a == b
- self.assertNotEqual(a, b): Check if a != b
- self.assertTrue(x): Check if x is True
- self.assertFalse(x): Check if x is False
- self.assertRaises(Exception): Check if exception is raised

Running Tests:
- python -m unittest test_file.py: Run all tests in a file
- unittest.main(): Run tests when script is executed directly

Real-World Examples:
1. Testing a function that processes strings:
   def reverse_string(s):
       return s[::-1]

   class TestStringFunctions(unittest.TestCase):
       def test_reverse(self):
           self.assertEqual(reverse_string('abc'), 'cba')

2. Testing a class:
   class Counter:
       def __init__(self):
           self.value = 0
       def increment(self):
           self.value += 1

   class TestCounter(unittest.TestCase):
       def test_increment(self):
           c = Counter()
           c.increment()
           self.assertEqual(c.value, 1)

Common Patterns:
- Use setUp() and tearDown() methods for test setup/cleanup
- Group related tests in the same class
- Use descriptive test method names
- Test both normal and edge cases
- Run tests automatically in CI/CD pipelines
"""
