# ============================================================
# FILE: functions_advanced.py
# TOPIC: Advanced Functions in Python
# ============================================================
# You already know how to create basic functions (functions.py).
# Now let's learn the ADVANCED features that make functions
# even more powerful and flexible!
#
# In this file you will learn:
#   1. return values (functions that give back results)
#   2. Default parameters (optional arguments)
#   3. *args (accept unlimited positional arguments)
#   4. **kwargs (accept unlimited keyword arguments)
#   5. Lambda functions (short one-line functions)
#   6. Functions calling other functions
# ============================================================


# ---------------------------------------------------------
# SECTION 1: RETURN VALUES
# ---------------------------------------------------------
# A function can COMPUTE something and give the result back
# using the 'return' keyword.
# The calling code can then use that result.

print("--- Return Values ---")

def square(number):
    """Returns the square (number * itself) of the given number."""
    return number * number    # Compute and send the value back

# We can STORE the returned value in a variable:
result = square(5)
print("Square of 5:", result)          # 25

# Or use it directly in an expression:
print("Square of 7:", square(7))       # 49
print("Double of square of 3:", square(3) * 2)  # 18

# A function can return MULTIPLE values at once (as a tuple!)
def min_max(numbers):
    """Returns BOTH the minimum and maximum of a list."""
    return min(numbers), max(numbers)  # Two values returned!

scores = [85, 42, 93, 67, 71]
lowest, highest = min_max(scores)      # Receive both values (tuple unpacking)
print(f"Lowest: {lowest}, Highest: {highest}")


# ---------------------------------------------------------
# SECTION 2: DEFAULT PARAMETERS
# ---------------------------------------------------------
# A default parameter has a PRESET value.
# If the caller doesn't provide that argument, the default is used.
# It makes arguments OPTIONAL.

print("\n--- Default Parameters ---")

def greet(name, greeting="Hello"):  # 'greeting' has a default value
    print(f"{greeting}, {name}!")

greet("Noman")                   # Uses default: "Hello, Noman!"
greet("Ali", "Good morning")    # Override default: "Good morning, Ali!"
greet("Sara", "Hi")             # Override: "Hi, Sara!"

def create_profile(name, age, role="Student", city="Unknown"):
    print(f"Name: {name} | Age: {age} | Role: {role} | City: {city}")

create_profile("Noman", 22)                         # Uses both defaults
create_profile("Ali", 30, "Developer")             # Overrides role only
create_profile("Sara", 25, "Designer", "Dhaka")   # Overrides both


# ---------------------------------------------------------
# SECTION 3: *args (Unlimited Positional Arguments)
# ---------------------------------------------------------
# Sometimes you don't know in advance how many arguments
# someone will pass to your function. Use *args to accept
# ANY NUMBER of positional arguments.
#
# *args collects all extra positional arguments into a TUPLE.
# (The name 'args' is a convention; you could use *values etc.)

print("\n--- *args (Unlimited Arguments) ---")

def total(*args):
    """Adds together any number of values."""
    print("Received:", args)         # args is a tuple
    return sum(args)                  # sum() works on any tuple/list

print("Total of 1,2,3:",      total(1, 2, 3))           # 6
print("Total of 10,20:",      total(10, 20))             # 30
print("Total of 1,2,3,4,5:", total(1, 2, 3, 4, 5))     # 15

# Another example: print() itself uses *args!
def my_print(*args):
    for item in args:
        print(item, end=" ")
    print()  # new line at the end

my_print("Hello", "World", "from", "Python")


# ---------------------------------------------------------
# SECTION 4: **kwargs (Unlimited Keyword Arguments)
# ---------------------------------------------------------
# **kwargs lets you accept ANY NUMBER of keyword arguments
# (arguments passed as name=value).
#
# **kwargs collects them into a DICTIONARY where:
#   key   = the argument name
#   value = the argument value
#
# (The name 'kwargs' is a convention for 'keyword arguments'.)

print("\n--- **kwargs (Unlimited Keyword Arguments) ---")

def show_info(**kwargs):
    """Displays any number of keyword arguments."""
    print("Information received:")
    for key, value in kwargs.items():
        print(f"  {key}: {value}")

show_info(name="Noman", age=22, city="Dhaka")
print()
show_info(subject="Python", level="Beginner", year=2025)

# You can also combine *args and **kwargs in one function!
def everything(*args, **kwargs):
    print("Positional args:", args)
    print("Keyword args:",    kwargs)

everything(1, 2, 3, name="Noman", language="Python")


# ---------------------------------------------------------
# SECTION 5: LAMBDA FUNCTIONS (One-Line Anonymous Functions)
# ---------------------------------------------------------
# A lambda function is a small, one-line function WITHOUT a name.
# Use it for simple operations that don't need a full def block.
#
# Syntax:  lambda parameters : expression
# It automatically returns the result of the expression.

print("\n--- Lambda Functions ---")

# Regular function:
def add_regular(a, b):
    return a + b

# Same thing as a lambda:
add_lambda = lambda a, b: a + b

print("Regular function: 3 + 4 =", add_regular(3, 4))  # 7
print("Lambda function:  3 + 4 =", add_lambda(3, 4))   # 7

# More lambda examples:
square    = lambda x: x ** 2
is_even   = lambda n: n % 2 == 0
greeting  = lambda name: f"Hello, {name}!"

print("Square of 9:", square(9))           # 81
print("Is 4 even?",   is_even(4))          # True
print("Is 7 even?",   is_even(7))          # False
print(greeting("Noman"))                    # Hello, Noman!

# Lambda is MOST USEFUL when passing a function as an argument.
# For example, sorting a list of dictionaries by a specific key:
students = [
    {"name": "Rahim", "gpa": 3.2},
    {"name": "Noman", "gpa": 3.8},
    {"name": "Ali",   "gpa": 2.9},
]

# Sort students by their 'gpa' value using a lambda:
students.sort(key=lambda s: s["gpa"])
print("\nStudents sorted by GPA:")
for s in students:
    print(f"  {s['name']}: {s['gpa']}")


# ---------------------------------------------------------
# SECTION 6: FUNCTIONS CALLING OTHER FUNCTIONS
# ---------------------------------------------------------
# Functions can call other functions.
# This is a good practice to keep code organized (each function
# does one job, and a "main" function puts it all together).

print("\n--- Functions Calling Other Functions ---")

def get_grade(score):
    """Returns a letter grade based on a numeric score."""
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

def print_report(name, score):
    """Calls get_grade() to create and print a student report."""
    grade = get_grade(score)    # Calling another function!
    print(f"Student: {name:<10} Score: {score}   Grade: {grade}")

# Now use print_report which internally calls get_grade:
print_report("Noman", 92)
print_report("Ali",   75)
print_report("Sara",  58)
print_report("Rahim", 83)

# ============================================================
# SUMMARY:
# - return  → sends a value back from the function
# - Return multiple values: return a, b  (received as a, b = func())
# - Default params: def func(x, y="default") → y is optional
# - *args   → accepts unlimited POSITIONAL args (stored as tuple)
# - **kwargs → accepts unlimited KEYWORD args (stored as dict)
# - lambda x: expression → short one-line function, no name needed
# - Functions can call other functions to stay organized
# ============================================================
