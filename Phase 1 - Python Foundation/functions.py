# ============================================================
# FILE: functions.py
# TOPIC: Functions in Python (Basics)
# ============================================================
# A function is a REUSABLE block of code that does a specific job.
# Instead of writing the same code again and again, you write it
# ONCE as a function, then CALL it whenever you need it.
#
# Real-life analogy:
# A microwave oven is like a function. You press the button (call it),
# it does the job (heats food), and you get the result. You don't
# need to know HOW it works inside every time.
#
# In this file you will learn:
#   1. Defining a function with def
#   2. Calling a function
#   3. Functions with parameters
#   4. Functions with return values
#   5. Real-life examples
# ============================================================


# ---------------------------------------------------------
# SECTION 1: DEFINING AND CALLING A FUNCTION
# ---------------------------------------------------------
# To CREATE a function: use the 'def' keyword, then the name,
# then parentheses (), then a colon :.
# The code inside must be indented.
#
# To USE (call) the function: write its name followed by ().

print("--- Basic Function ---")

def say_hello():
    # This function prints a greeting every time it is called.
    print("Hello! Welcome to Python Functions!")

# Calling/using the function:
say_hello()   # First call
say_hello()   # Second call → same code runs again automatically!
say_hello()   # Third call  → no need to repeat the print line!


# ---------------------------------------------------------
# SECTION 2: FUNCTIONS WITH PARAMETERS
# ---------------------------------------------------------
# A parameter is a variable that you PASS INTO the function.
# It lets the function work with different values each time.
# The value you pass when calling is called an "argument".

print("\n--- Function With Parameters ---")

def greet(name):           # 'name' is the parameter
    print(f"Hello, {name}! How are you today?")

# 'Noman', 'Abdullah', 'Ali' are arguments passed to the function:
greet("Noman")
greet("Abdullah")
greet("Ali")


# ---------------------------------------------------------
# SECTION 3: FUNCTIONS WITH MULTIPLE PARAMETERS
# ---------------------------------------------------------
# You can have more than one parameter, separated by commas.

print("\n--- Function With Multiple Parameters ---")

def add(a, b):             # Two parameters: a and b
    result = a + b
    print(f"{a} + {b} = {result}")

add(10, 20)   # a=10, b=20
add(5, 7)     # a=5,  b=7
add(100, 250) # a=100, b=250

def introduce(name, age, city):
    print(f"My name is {name}, I am {age} years old, from {city}.")

introduce("Noman", 22, "Dhaka")
introduce("Ali", 19, "Chittagong")


# ---------------------------------------------------------
# SECTION 4: FUNCTIONS WITH RETURN VALUES
# ---------------------------------------------------------
# Sometimes a function CALCULATES something and you want to
# USE that result elsewhere. Use 'return' to send a value back.
#
# Think of it like asking a friend to do a calculation:
# you give them numbers, they give you the ANSWER back.

print("\n--- Function With Return ---")

def multiply(a, b):
    return a * b      # Calculate and SEND the result back

# The function returns a value, so we can STORE it in a variable:
result1 = multiply(4, 5)
result2 = multiply(3, 7)

print("4 x 5 =", result1)   # 20
print("3 x 7 =", result2)   # 21

# Or use the result directly inside print():
print("6 x 8 =", multiply(6, 8))


# ---------------------------------------------------------
# SECTION 5: FUNCTION THAT RETURNS A DECISION
# ---------------------------------------------------------
# Functions can also return True/False (boolean).

print("\n--- Function That Returns True/False ---")

def is_even(number):
    # Returns True if the number is even, False if odd
    if number % 2 == 0:
        return True
    else:
        return False

print(is_even(4))    # True
print(is_even(7))    # False
print(is_even(100))  # True


# ---------------------------------------------------------
# REAL LIFE EXAMPLE: Simple Calculator Function
# ---------------------------------------------------------
print("\n--- Real Life Example: Calculator ---")

def calculate(num1, num2, operation):
    """This function performs basic math operations.
    Parameters:
        num1, num2 → the two numbers
        operation  → '+', '-', '*', or '/'
    Returns:
        The result of the calculation
    """
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    elif operation == "/":
        if num2 == 0:
            return "Error: Cannot divide by zero!"
        return num1 / num2
    else:
        return "Error: Unknown operation!"

print(calculate(10, 5, "+"))  # 15
print(calculate(10, 5, "-"))  # 5
print(calculate(10, 5, "*"))  # 50
print(calculate(10, 5, "/"))  # 2.0
print(calculate(10, 0, "/"))  # Error message

# ============================================================
# SUMMARY:
# - def function_name():  → defines a function
# - function_name()       → calls (runs) a function
# - Parameters are variables the function accepts as input
# - Arguments are the actual values you pass when calling
# - return sends a value back from the function
# - Functions help us AVOID repeating code (DRY principle)
#   DRY = Don't Repeat Yourself
# ============================================================
