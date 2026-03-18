# ============================================================
# FILE: modules.py
# TOPIC: Modules and Imports in Python
# ============================================================
# A module is simply a FILE containing Python code (functions,
# variables, classes) that you can REUSE in other files.
# Python comes with hundreds of built-in modules.
# You can also install extra ones or create your own!
#
# Think of a module like a toolbox:
#   - You don't carry every tool everywhere.
#   - You import only the tools you need.
#
# In this file you will learn:
#   1. import statement (importing a whole module)
#   2. from module import name (importing specific items)
#   3. Built-in modules: math, random, os, datetime, json
#   4. Creating your own module (conceptually)
#   5. Installing external packages with pip
# ============================================================


# ---------------------------------------------------------
# SECTION 1: THE import STATEMENT
# ---------------------------------------------------------
# 'import module_name' loads an entire module.
# To use something from it: module_name.function_or_variable

print("=" * 50)
print("SECTION 1: import statement")
print("=" * 50)

import math    # Load the 'math' module

# Now we use math. before each function/constant:
print("PI:",              math.pi)               # 3.14159...
print("Square root of 16:",math.sqrt(16))        # 4.0
print("Ceiling of 4.3:", math.ceil(4.3))         # 5  (round UP)
print("Floor of 4.7:",   math.floor(4.7))        # 4  (round DOWN)
print("2 to the power 10:", math.pow(2, 10))     # 1024.0
print("log base 10 of 1000:", math.log10(1000))  # 3.0
print("Absolute value of -7:", math.fabs(-7))    # 7.0


# ---------------------------------------------------------
# SECTION 2: from module import name
# ---------------------------------------------------------
# Instead of importing the whole module, import ONLY what you need.
# This lets you use the name WITHOUT the module prefix.

print("\n" + "=" * 50)
print("SECTION 2: from ... import ...")
print("=" * 50)

from math import pi, sqrt, factorial

# Now we can use them directly (no 'math.' prefix needed):
print("PI:",                 pi)              # 3.14159...
print("Square root of 25:", sqrt(25))        # 5.0
print("5! (factorial):",    factorial(5))    # 120  (5*4*3*2*1)

# Import with an ALIAS (rename for convenience):
import math as m    # Now 'math' is referred to as 'm'
print("Cosine of 0:", m.cos(0))   # 1.0
print("Sine of pi/2:", m.sin(pi / 2))  # 1.0 (approximately)


# ---------------------------------------------------------
# SECTION 3: THE random MODULE
# ---------------------------------------------------------
# 'random' lets you generate random numbers, pick random items,
# shuffle lists, and more. Very useful for games and simulations!

print("\n" + "=" * 50)
print("SECTION 3: random module")
print("=" * 50)

import random

# random.randint(a, b) -> random integer between a and b (inclusive)
print("Random integer (1-10):",    random.randint(1, 10))
print("Random integer (1-100):",   random.randint(1, 100))

# random.random() -> random float between 0.0 and 1.0
print("Random float (0-1):",       random.random())

# random.uniform(a, b) -> random float between a and b
print("Random float (1.0-5.0):",   random.uniform(1.0, 5.0))

# random.choice(list) -> picks ONE random item from a list
fruits = ["apple", "banana", "cherry", "date"]
print("Random fruit:",             random.choice(fruits))

# random.shuffle(list) -> randomly shuffles the list IN PLACE
numbers = [1, 2, 3, 4, 5]
random.shuffle(numbers)
print("Shuffled list:",            numbers)

# random.sample(list, k) -> picks k unique items randomly
sample = random.sample(range(1, 50), 6)   # Pick 6 lottery numbers
print("Lottery numbers:",          sorted(sample))


# ---------------------------------------------------------
# SECTION 4: THE os MODULE
# ---------------------------------------------------------
# 'os' lets you interact with the operating system:
# files, directories, environment variables, paths.

print("\n" + "=" * 50)
print("SECTION 4: os module")
print("=" * 50)

import os

# Current working directory (where your script is running):
print("Current directory:", os.getcwd())

# List files and folders in the current directory:
print("Files in current dir:", os.listdir("."))

# Check if a path (file/folder) exists:
print("Does 'basics.py' exist?", os.path.exists("basics.py"))
print("Does 'fake.txt' exist?",  os.path.exists("fake.txt"))

# Join paths (OS-safe, works on Windows AND Linux/Mac):
full_path = os.path.join("Python Foundation", "basics.py")
print("Joined path:", full_path)

# Get file size (in bytes):
if os.path.exists("basics.py"):
    size = os.path.getsize("basics.py")
    print(f"Size of basics.py: {size} bytes")

# Get just the filename from a full path:
print("Basename:", os.path.basename("/home/user/Python/basics.py"))

# Get just the directory part of a path:
print("Dirname:",  os.path.dirname("/home/user/Python/basics.py"))


# ---------------------------------------------------------
# SECTION 5: THE datetime MODULE
# ---------------------------------------------------------
# 'datetime' gives you tools to work with dates and times.

print("\n" + "=" * 50)
print("SECTION 5: datetime module")
print("=" * 50)

from datetime import datetime, date, timedelta

# Current date and time:
now = datetime.now()
print("Right now:",       now)
print("Year:",            now.year)
print("Month:",           now.month)
print("Day:",             now.day)
print("Hour:",            now.hour)
print("Minute:",          now.minute)

# Format dates into strings:
formatted = now.strftime("%d %B %Y, %H:%M")   # e.g., 28 February 2026, 14:30
print("Formatted date:",  formatted)

# Today's date only (no time):
today = date.today()
print("Today's date:",    today)

# Calculate a future/past date:
one_week_later = today + timedelta(days=7)
birthday       = date(2025, 12, 25)     # Create a specific date

print("One week from today:", one_week_later)
print("Days until Christmas:", (birthday - today).days)

# Measure how long code takes to run:
start_time = datetime.now()

total = 0
for i in range(1_000_000):   # Count to 1 million
    total += i

end_time = datetime.now()
elapsed  = (end_time - start_time).total_seconds()
print(f"\nCounted to 1,000,000. Time taken: {elapsed:.3f} seconds")


# ---------------------------------------------------------
# SECTION 6: THE json MODULE
# ---------------------------------------------------------
# JSON (JavaScript Object Notation) is the most common format
# for sharing data between programs and web services.
# It looks almost identical to Python dictionaries.
#
# json.dumps() -> Convert Python dict to JSON STRING
# json.loads() -> Convert JSON STRING back to Python dict
# json.dump()  -> Write JSON to a FILE
# json.load()  -> Read JSON from a FILE

print("\n" + "=" * 50)
print("SECTION 6: json module")
print("=" * 50)

import json

# Python dictionary:
student = {
    "name": "Noman",
    "age": 22,
    "courses": ["Python", "Math", "Physics"],
    "active": True
}

# Convert Python dict to JSON string:
json_string = json.dumps(student, indent=4)   # indent=4 makes it pretty
print("Python dict as JSON string:")
print(json_string)

# Convert JSON string back to Python dict:
parsed_back = json.loads(json_string)
print("\nParsed back to Python dict:")
print("Name:",    parsed_back["name"])
print("Courses:", parsed_back["courses"])

# Save JSON to a file:
with open("student_data.json", "w") as f:
    json.dump(student, f, indent=4)
print("\nSaved student data to 'student_data.json'")

# Read JSON from a file:
with open("student_data.json", "r") as f:
    loaded = json.load(f)
print("Loaded from file:", loaded["name"], "|", loaded["courses"])

# Cleanup:
os.remove("student_data.json")


# ---------------------------------------------------------
# SECTION 7: CREATING YOUR OWN MODULE
# ---------------------------------------------------------
# Any Python file (.py) is a module!
# If you create a file called 'my_tools.py' with functions,
# you can import it in another file like this:
#
#   import my_tools
#   my_tools.greet("Noman")
#
# Or:
#   from my_tools import greet
#   greet("Noman")
#
# This is how large Python projects are organized.

print("\n" + "=" * 50)
print("SECTION 7: Creating Your Own Module")
print("=" * 50)

# Let's simulate creating a module by writing a file:
module_code = '''# This file is my_math_tools.py
# It's a custom module with helper functions.

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def average(numbers):
    return sum(numbers) / len(numbers)

PI = 3.14159
'''

with open("my_math_tools.py", "w") as f:
    f.write(module_code)
print("Created 'my_math_tools.py'")

# Now import and use it:
import my_math_tools

print("add(3, 7):",         my_math_tools.add(3, 7))            # 10
print("subtract(10, 4):",   my_math_tools.subtract(10, 4))     # 6
print("average([5,10,15]):",my_math_tools.average([5, 10, 15])) # 10.0
print("PI:",                my_math_tools.PI)                   # 3.14159

os.remove("my_math_tools.py")   # Cleanup


# ---------------------------------------------------------
# SECTION 8: EXTERNAL PACKAGES (pip)
# ---------------------------------------------------------
# Python has thousands of extra packages on PyPI (Python Package Index).
# Install them using pip in the terminal:
#
#   pip install requests        <- HTTP requests (fetch web pages)
#   pip install numpy           <- Numerical computing
#   pip install pandas          <- Data analysis
#   pip install matplotlib      <- Data visualization
#   pip install scikit-learn    <- Machine learning
#
# After installing, import as usual:
#   import requests
#   import numpy as np
#   import pandas as pd
#
# You will use ALL of these in later phases of this course!

print("\n" + "=" * 50)
print("SECTION 8: External Packages (pip)")
print("=" * 50)
print("Install packages with: pip install package_name")
print()
print("Essential packages for AI/ML learning:")
packages = [
    ("requests",     "Fetch data from websites/APIs"),
    ("numpy",        "Fast numerical computing with arrays"),
    ("pandas",       "Data analysis with DataFrames"),
    ("matplotlib",   "Create charts and graphs"),
    ("scikit-learn", "Machine learning algorithms"),
    ("tensorflow",   "Deep learning (neural networks)"),
]
for pkg, desc in packages:
    print(f"  pip install {pkg:<15} -> {desc}")

# ============================================================
# SUMMARY:
# - import module              -> load the whole module
# - from module import name    -> load only specific items
# - import module as alias     -> give the module a shorter name
# - math   -> pi, sqrt, ceil, floor, factorial, sin, cos
# - random -> randint, random, choice, shuffle, sample
# - os     -> getcwd, listdir, path.exists, path.join, remove
# - datetime -> now(), date.today(), timedelta, strftime()
# - json   -> dumps(), loads(), dump(), load()
# - Any .py file can be your own custom module
# - Use pip install to get external packages from PyPI
# ============================================================
