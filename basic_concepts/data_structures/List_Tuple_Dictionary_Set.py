"""
=== LIST, TUPLE, DICTIONARY, SET - KEY DIFFERENCES ===

How to create each data structure in Python:

- List: Use square brackets [] or the list() constructor.
    fruits = ["apple", "banana", "cherry"]
    numbers = list((1, 2, 3))

- Tuple: Use parentheses () or the tuple() constructor.
    point = (1, 2)
    colors = tuple(["red", "green", "blue"])

- Dictionary: Use curly braces {} with key-value pairs, or the dict() constructor.
    person = {"name": "Alice", "age": 30}
    empty_dict = dict()

- Set: Use curly braces {} with values, or the set() constructor.
    unique_numbers = {1, 2, 3}
    empty_set = set()

These are Python's four fundamental built-in data structures, each optimized for different use cases:

LIST: Mutable, ordered collection that allows duplicates. Think of it as a dynamic array
      where you can modify, add, or remove elements. Best for when you need to maintain
      order and frequently modify the collection.

TUPLE: Immutable, ordered collection that allows duplicates. Once created, it cannot be
       changed. More memory efficient than lists and can be used as dictionary keys.
       Best for fixed data that won't change, like coordinates or database records.

DICTIONARY: Mutable collection of key-value pairs with fast O(1) lookups. Keys must be
            unique and immutable. Best for when you need fast access to data based on
            a unique identifier.

SET: Mutable collection of unique elements with no particular order. Automatically
     removes duplicates and provides fast membership testing. Best for mathematical
     set operations and when you need to ensure uniqueness.

Key Trade-offs:
- Mutability: List/Dict/Set are mutable, Tuple is immutable
- Ordering: List/Tuple maintain order, Set doesn't guarantee order, Dict maintains insertion order (Python 3.7+)
- Duplicates: List/Tuple allow duplicates, Dict/Set don't
- Performance: Dict/Set have O(1) lookups, List/Tuple have O(n) searches
"""

# ===== LIST EXAMPLES =====
print("=== LIST EXAMPLES ===")

# Basic list operations
fruits = ["apple", "banana", "cherry"]
print(f"Original list: {fruits}")

# Adding elements
fruits.append("orange")
fruits.insert(1, "grape")
print(f"After adding: {fruits}")

# Removing elements
fruits.remove("banana")
last_fruit = fruits.pop()
print(f"After removing: {fruits}, removed: {last_fruit}")

# List slicing syntax
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(f"Original: {numbers}")
print(f"First 5: {numbers[:5]}")          # [0, 1, 2, 3, 4]
print(f"Last 3: {numbers[-3:]}")          # [7, 8, 9]
print(f"Every 2nd: {numbers[::2]}")       # [0, 2, 4, 6, 8]
print(f"Reversed: {numbers[::-1]}")       # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
print(f"Middle section: {numbers[2:8]}")  # [2, 3, 4, 5, 6, 7]
print(f"Skip first and last: {numbers[1:-1]}")  # [1, 2, 3, 4, 5, 6, 7, 8]

# List comprehension
squares = [x**2 for x in range(5)]
evens = [x for x in range(10) if x % 2 == 0]
print(f"Squares: {squares}")
print(f"Even numbers: {evens}")

print()

# ===== TUPLE EXAMPLES =====
print("=== TUPLE EXAMPLES ===")

# Creating and using tuples
point = (10, 20)
person = ("Alice", 30, "Engineer")
empty_tuple = ()
single_item = (42,)  # Comma needed for single item

print(f"Point: {point}")
print(f"Person: {person}")

# Tuple unpacking
x, y = point
name, age, job = person
print(f"Unpacked: x={x}, y={y}")
print(f"Person: {name}, {age}, {job}")

# Tuple slicing (same syntax as lists)
letters = ('a', 'b', 'c', 'd', 'e', 'f')
print(f"Letters: {letters}")
print(f"First 3: {letters[:3]}")          # ('a', 'b', 'c')
print(f"Last 2: {letters[-2:]}")          # ('e', 'f')
print(f"Reversed: {letters[::-1]}")       # ('f', 'e', 'd', 'c', 'b', 'a')
print(f"Every other: {letters[::2]}")     # ('a', 'c', 'e')

# Using tuples as dictionary keys
locations = {
    (0, 0): "Origin",
    (1, 2): "Point A",
    (3, 4): "Point B"
}
print(f"Location at (1,2): {locations[(1, 2)]}")

print()

# ===== DICTIONARY EXAMPLES =====
print("=== DICTIONARY EXAMPLES ===")

# Basic dictionary operations
student = {"name": "John", "age": 20, "grade": "A"}
print(f"Student: {student}")

# Adding and updating
student["email"] = "john@email.com"
student["age"] = 21
print(f"Updated: {student}")

# Dictionary methods
print(f"Keys: {list(student.keys())}")
print(f"Values: {list(student.values())}")
print(f"Get with default: {student.get('phone', 'Not provided')}")

# Dictionary comprehension
word_lengths = {word: len(word) for word in ["apple", "banana", "cherry"]}
squares_dict = {x: x**2 for x in range(5)}
print(f"Word lengths: {word_lengths}")
print(f"Squares: {squares_dict}")

# Dictionary slicing with items()
items_list = list(student.items())
print(f"All items: {items_list}")
print(f"First 2 items: {items_list[:2]}")
print(f"Last item: {items_list[-1:]}")

print()

# ===== SET EXAMPLES =====
print("=== SET EXAMPLES ===")

# Basic set operations
colors = {"red", "green", "blue"}
print(f"Colors: {colors}")

# Adding and removing
colors.add("yellow")
colors.discard("green")
print(f"Modified colors: {colors}")

# Set operations
set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}

print(f"Set A: {set_a}")
print(f"Set B: {set_b}")
print(f"Union (A | B): {set_a | set_b}")
print(f"Intersection (A & B): {set_a & set_b}")
print(f"Difference (A - B): {set_a - set_b}")

# Removing duplicates
duplicate_list = [1, 2, 2, 3, 3, 3, 4, 5, 5]
unique_list = list(set(duplicate_list))
print(f"Original: {duplicate_list}")
print(f"Unique: {unique_list}")

# Set comprehension
even_squares = {x**2 for x in range(10) if x % 2 == 0}
print(f"Even squares: {even_squares}")

# Converting set to sorted list for slicing
sorted_set = sorted(set_a)
print(f"Sorted set as list: {sorted_set}")
print(f"First 3 elements: {sorted_set[:3]}")
print(f"Last 2 elements: {sorted_set[-2:]}")

print()

# ===== PRACTICAL EXAMPLES =====
print("=== PRACTICAL EXAMPLES ===")

# Shopping cart with slicing
cart = ["apple", "bread", "milk", "eggs", "butter", "cheese"]
print(f"Full cart: {cart}")
print(f"First 3 items: {cart[:3]}")
print(f"Last 2 items: {cart[-2:]}")
print(f"Every other item: {cart[::2]}")

# Processing data with different structures
data = "python programming tutorial"
words = data.split()
print(f"Words list: {words}")
print(f"Reversed words: {words[::-1]}")

# Word frequency
word_count = {}
for word in words:
    word_count[word] = word_count.get(word, 0) + 1
print(f"Word frequency: {word_count}")

# Unique characters
unique_chars = set(data.replace(" ", ""))
print(f"Unique characters: {unique_chars}")

print()

# ===== SLICING SYNTAX SUMMARY =====
print("=== SLICING SYNTAX REFERENCE ===")

sample = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
slicing_examples = {
    "sample[:]": sample[:],           # Copy entire list
    "sample[2:5]": sample[2:5],       # Elements from index 2 to 4
    "sample[:5]": sample[:5],         # First 5 elements
    "sample[5:]": sample[5:],         # From index 5 to end
    "sample[-3:]": sample[-3:],       # Last 3 elements
    "sample[:-2]": sample[:-2],       # All except last 2
    "sample[::2]": sample[::2],       # Every 2nd element
    "sample[::3]": sample[::3],       # Every 3rd element
    "sample[::-1]": sample[::-1],     # Reverse the list
    "sample[1::2]": sample[1::2],     # Every 2nd starting from index 1
    "sample[2:8:2]": sample[2:8:2]    # From 2 to 7, every 2nd
}

for syntax, result in slicing_examples.items():
    print(f"{syntax:15} = {result}")