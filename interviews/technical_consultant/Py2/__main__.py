#1.
#How can we get the last element from a list in different ways. Let´s say we don´t know the number of elements in the list.

my_list = [10, 20, 30, 40, 50]

#Response

# Method 1: Using negative indexing
last_element = my_list[-1]
print(f"Last element using negative indexing: {last_element}")

# Method 2: Using the pop() method
last_element = my_list.pop()
print(f"Last element using pop(): {last_element}")

# Method 3: Using the slice notation
last_element = my_list[len(my_list)-1]
print(f"Last element using slice notation: {last_element}")

# Method 4: Using a loop
for i, element in enumerate(my_list):
    if i == len(my_list) - 1:
        last_element = element
print(f"Last element using loop: {last_element}")


#2.

def examplePyFunction(name, msg):
    print("Hello " + name + ", " + msg)
    
#What will be the output for the following function calls?

##examplePyFunction("Alice", "Good Morning")
    #Response: Hello Alice, Good Morning
##examplePyFunction("Juan")
    ##Response: TypeError Exception



