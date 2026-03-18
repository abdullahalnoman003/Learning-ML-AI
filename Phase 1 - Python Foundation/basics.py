# ============================================================
# FILE: basics.py
# TOPIC: Python Basics - Variables, Data Types & Input
# ============================================================
# In this file you will learn:
#   1. What are variables and how to create them
#   2. The 4 main data types in Python
#   3. How to check what type a variable is
#   4. How to do basic math (arithmetic)
#   5. How to take input from the user
#   6. Type casting (converting one type to another)
# ============================================================


# ---------------------------------------------------------
# SECTION 1: WHAT IS A VARIABLE?
# ---------------------------------------------------------
# A variable is like a labeled box where you store information.
# You give the box a name, and put a value inside it.
# In Python, you just write:  variable_name = value
# No need to declare the type — Python figures it out for you!

name   = "Abdullah Al Noman"   # Storing text (called a String)
age    = 22                     # Storing a whole number (called an Integer)
dept   = "Software Engineering" # Another String
cgpa   = 3.92                   # Storing a decimal number (called a Float)
active = True                   # Storing True/False (called a Boolean)

print("--- Our Variables ---")
print("Name:",   name)
print("Age:",    age)
print("Dept:",   dept)
print("CGPA:",   cgpa)
print("Active:", active)


# ---------------------------------------------------------
# SECTION 2: THE 4 MAIN DATA TYPES
# ---------------------------------------------------------
# Python has 4 basic (primitive) data types:
#
#   str   (String)  → text, written inside quotes    → "Hello"
#   int   (Integer) → whole numbers, no decimal      → 22, -5, 0
#   float (Float)   → decimal/fractional numbers     → 3.14, -0.5
#   bool  (Boolean) → only two values: True or False → True, False

my_string  = "Hello, Python!"    # str
my_int     = 100                  # int
my_float   = 9.81                 # float
my_bool    = False                # bool

print("\n--- Data Type Examples ---")
print(my_string)
print(my_int)
print(my_float)
print(my_bool)


# ---------------------------------------------------------
# SECTION 3: CHECKING THE TYPE OF A VARIABLE
# ---------------------------------------------------------
# Use the built-in type() function to see what type a variable is.
# This is very useful when you are debugging or learning.

print("\n--- Checking Types with type() ---")
print(type(name))    # <class 'str'>   → it's a String
print(type(age))     # <class 'int'>   → it's an Integer
print(type(cgpa))    # <class 'float'> → it's a Float
print(type(active))  # <class 'bool'>  → it's a Boolean


# ---------------------------------------------------------
# SECTION 4: BASIC ARITHMETIC (MATH OPERATIONS)
# ---------------------------------------------------------
# Python can work like a calculator.
# Here are the math operators:
#
#   +   Addition
#   -   Subtraction
#   *   Multiplication
#   /   Division (always gives a float result)
#   //  Floor Division (divides and drops the decimal part)
#   %   Modulus (gives the REMAINDER after division)
#   **  Exponent (power: 2 ** 3 means 2 to the power of 3)

a = 10
b = 3

print("\n--- Arithmetic Operations ---")
print("a + b  =", a + b)    # 13  → Addition
print("a - b  =", a - b)    # 7   → Subtraction
print("a * b  =", a * b)    # 30  → Multiplication
print("a / b  =", a / b)    # 3.333... → Division
print("a // b =", a // b)   # 3   → Floor Division (ignores remainder)
print("a % b  =", a % b)    # 1   → Remainder (10 = 3*3 + 1)
print("a ** b =", a ** b)   # 1000 → 10 to the power of 3


# ---------------------------------------------------------
# SECTION 5: TAKING INPUT FROM THE USER
# ---------------------------------------------------------
# input() pauses the program and waits for the user to type something.
# Whatever they type is returned as a STRING (text).

print("\n--- User Input ---")
user_name = input("What is your name? ")
print("Hello,", user_name, "! Welcome to Python learning.")


# ---------------------------------------------------------
# SECTION 6: TYPE CASTING (CONVERTING TYPES)
# ---------------------------------------------------------
# Because input() ALWAYS returns a string, if you need a NUMBER
# from the user, you must CONVERT it.
#
# This conversion is called "Type Casting".
#
#   int("22")    → 22   (string to integer)
#   float("3.5") → 3.5  (string to float)
#   str(22)      → "22" (integer to string)

user_age = int(input("How old are you? "))           # Convert to integer
user_gpa = float(input("What is your GPA (e.g. 3.5)? "))  # Convert to float

print("\n--- Your Profile ---")
print("Name:", user_name)
print("Age:",  user_age,  "| Type:", type(user_age))
print("GPA:",  user_gpa,  "| Type:", type(user_gpa))

# Notice: after casting, type() shows int and float, not str!

# ---------------------------------------------------------
# BONUS: STRING CONCATENATION vs f-strings
# ---------------------------------------------------------
# You can combine (join) strings using + or using f-strings.
# f-strings are the modern, cleaner way.

greeting_old = "Hello, " + user_name + "! You are " + str(user_age) + " years old."
greeting_new = f"Hello, {user_name}! You are {user_age} years old."  # f-string

print("\n--- String Joining ---")
print(greeting_old)  # Old way
print(greeting_new)  # Better way (f-string)

# ============================================================
# SUMMARY:
# - Variables store data. Python auto-detects the type.
# - 4 main types: str, int, float, bool
# - type() tells you the type of any variable
# - Python does math with: + - * / // % **
# - input() always returns a STRING
# - Use int() or float() to convert user input to numbers
# - f-strings (f"...") are the cleanest way to format output
# ============================================================
