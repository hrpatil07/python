# Variable Declaration:
# Variables are created by assigning a value to a name.

x = 10
name = "John"

# Variable Naming Rules:
# Variables must start with a letter or underscore, can contain letters, numbers, and underscores. Case-sensitive.

_my_variable = 42
age = 25

# Dynamic Typing:
# Python is dynamically typed, allowing variable reassignment to different data types.

x = 10
x = "hello"

# Data Types:
# Common data types include int, float, str, bool.

age = 25          # int
height = 5.9      # float
name = "Alice"    # str
is_student = True  # bool

# Multiple Assignment:
# You can assign multiple variables in a single line.

a, b, c = 1, 2, 3

# Type Conversion:
# Convert between data types using type casting.

x = 10
y = str(x)    # Converts x to a string

# Global vs. Local Variables:
# Variables declared outside a function have a global scope. Variables inside a function have a local scope.

global_var = 50

def my_function():
    local_var = 20

# Constants:
# Although Python doesn't have true constants, it's a convention to use uppercase names for constant-like variables.

PI = 3.14

# None Type:
# Represents the absence of a value or a null value.

empty_variable = None

# Deleting Variables:
# You can delete a variable using the del keyword.

x = 5
del x
