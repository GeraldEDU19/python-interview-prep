

"""
*args and **kwargs in Python

In Python, *args and **kwargs are used to pass a variable number of arguments to a function.
*args collects extra positional arguments as a tuple.
**kwargs collects extra keyword arguments as a dictionary.
"""

def print_args(*args):
	print("Arguments received (as tuple):", args)
	for arg in args:
		print(arg)

def print_kwargs(**kwargs):
	print("Keyword arguments received (as dict):", kwargs)
	for key, value in kwargs.items():
		print(f"{key}: {value}")

def print_all(*args, **kwargs):
	print("Positional arguments:", args)
	print("Keyword arguments:", kwargs)

if __name__ == "__main__":
	print("--- Example: *args ---")
	print_args(1, 2, 3)
	# Output:
	# Arguments received (as tuple): (1, 2, 3)
	# 1
	# 2
	# 3

	print("\n--- Example: **kwargs ---")
	print_kwargs(name="Alice", age=30)
	# Output:
	# Keyword arguments received (as dict): {'name': 'Alice', 'age': 30}
	# name: Alice
	# age: 30

	print("\n--- Example: *args and **kwargs together ---")
	print_all(1, 2, name="Bob", job="Engineer")
	# Output:
	# Positional arguments: (1, 2)
	# Keyword arguments: {'name': 'Bob', 'job': 'Engineer'}


# === Summary ===
#
# *args is used when you want to accept a variable number of positional arguments.
#   - Useful when you don't know in advance how many arguments will be passed.
#   - The arguments are accessible as a tuple.
#
# **kwargs is used when you want to accept a variable number of keyword arguments.
#   - Useful for functions that accept optional or named parameters.
#   - The arguments are accessible as a dictionary.
#
# You can use both together, but *args must come before **kwargs in the function definition.
#
# === Scenarios ===
#
# 1. *args: When you want to sum any number of numbers
def sum_all(*args):
	return sum(args)

print("\n--- Scenario: *args for summing numbers ---")
print(sum_all(1, 2, 3))      # 6
print(sum_all(5, 10, 15, 20)) # 50

# 2. **kwargs: When you want to build a dictionary from named arguments
def build_profile(**kwargs):
	return kwargs

print("\n--- Scenario: **kwargs for building a profile ---")
print(build_profile(name="Alice", age=30, job="Engineer"))
# {'name': 'Alice', 'age': 30, 'job': 'Engineer'}

# 3. *args and **kwargs: When you want to accept both types of arguments
def flexible_function(*args, **kwargs):
	print("Positional:", args)
	print("Keyword:", kwargs)

print("\n--- Scenario: *args and **kwargs together ---")
flexible_function(1, 2, 3, a=10, b=20)
# Positional: (1, 2, 3)
# Keyword: {'a': 10, 'b': 20}
