
"""
OOP Principles Concept:
Object-Oriented Programming (OOP) is a paradigm based on the concept of objects, 
which bundle data (attributes) and behavior (methods). 
Python supports OOP and its four main principles: 
Encapsulation, Inheritance, Polymorphism, and Abstraction.

OOP helps organize code, promote reuse, and model real-world systems. 
This file demonstrates each principle with practical, runnable examples.
"""

# === ENCAPSULATION ===
class Person:
	def __init__(self, name):
		self.name = name  # encapsulated attribute
	def greet(self):
		print(f"Hello, my name is {self.name}")

# === INHERITANCE ===
class Animal:
	def speak(self):
		print("Animal speaks")

class Dog(Animal):
	def speak(self):
		print("Woof!")

# === POLYMORPHISM ===
def animal_sound(animal):
	animal.speak()

# === ABSTRACTION ===
from abc import ABC, abstractmethod

class Shape(ABC):
	@abstractmethod
	def area(self):
		pass

class Square(Shape):
	def __init__(self, side):
		self.side = side
	def area(self):
		return self.side * self.side

# Run the OOP examples
if __name__ == "__main__":
	print("--- Encapsulation Example ---")
	p = Person("Alice")
	p.greet()  # Output: Hello, my name is Alice

	print("\n--- Inheritance Example ---")
	d = Dog()
	d.speak()  # Output: Woof!

	print("\n--- Polymorphism Example ---")
	animal_sound(Animal())  # Output: Animal speaks
	animal_sound(Dog())     # Output: Woof!

	print("\n--- Abstraction Example ---")
	s = Square(4)
	print(f"Area of square: {s.area()}")  # Output: 16

"""
USEFUL OOP CONCEPTS AND EXAMPLES:

Core Principles:
- Encapsulation: Hide internal state, expose behavior via methods.
- Inheritance: Reuse code by creating subclasses.
- Polymorphism: Use a common interface for different types.
- Abstraction: Define abstract base classes and interfaces.

Common Patterns:
- Composition: Build complex objects by combining simpler ones.
- Method Overriding: Subclasses provide specific implementations.
- Duck Typing: "If it walks like a duck and quacks like a duck..."

Best Practices:
- Use classes to model real-world entities.
- Keep attributes private (prefix with _ or __) when needed.
- Favor composition over inheritance for flexibility.
- Use abstract base classes for shared interfaces.
"""
