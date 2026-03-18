# ============================================================
# FILE: list_comprehension.py
# TOPIC: List Comprehension, Dict Comprehension, map(), filter()
# ============================================================
# List comprehension is a shorter, cleaner way to CREATE a list.
# Instead of writing a for loop and .append(), you do it all
# in ONE line inside square brackets [].
#
# Regular way (the long way):
#   result = []
#   for item in old_list:
#       result.append(item * 2)
#
# Comprehension way (the short way):
#   result = [item * 2 for item in old_list]
#
# In this file you will learn:
#   1. Basic list comprehension
#   2. Comprehension with conditions (filtering)
#   3. Comprehension with transformations
#   4. Nested list comprehension
#   5. Dictionary comprehension
#   6. Set comprehension
#   7. map() function
#   8. filter() function
# ============================================================


# ---------------------------------------------------------
# SECTION 1: BASIC LIST COMPREHENSION
# ---------------------------------------------------------
# Syntax: [expression  for  item  in  iterable]
# Read it as: "Give me (expression) for each (item) in (iterable)"

print("--- Section 1: Basic List Comprehension ---")

# ---- Long way (for loop + append) ----
squares_long = []
for x in range(1, 6):
    squares_long.append(x ** 2)
print("Long way:  ", squares_long)   # [1, 4, 9, 16, 25]

# ---- Short way (list comprehension) ----
squares_short = [x ** 2 for x in range(1, 6)]
print("Short way: ", squares_short)  # [1, 4, 9, 16, 25]

# More examples:
doubles   = [x * 2      for x in range(1, 8)]   # Multiply each by 2
cubes     = [x ** 3     for x in range(1, 6)]   # Cube each number
uppercase = [s.upper()  for s in ["hello", "world", "python"]]  # Uppercase each

print("Doubles:  ", doubles)
print("Cubes:    ", cubes)
print("Uppercase:", uppercase)


# ---------------------------------------------------------
# SECTION 2: COMPREHENSION WITH CONDITIONS (Filtering)
# ---------------------------------------------------------
# Syntax: [expression  for  item  in  iterable  if  condition]
# Only items where the condition is True are included.

print("\n--- Section 2: Comprehension with Condition ---")

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Get only EVEN numbers:
evens = [x for x in numbers if x % 2 == 0]
print("Even numbers:", evens)           # [2, 4, 6, 8, 10]

# Get only ODD numbers:
odds = [x for x in numbers if x % 2 != 0]
print("Odd numbers:", odds)             # [1, 3, 5, 7, 9]

# Get numbers greater than 5:
greater = [x for x in numbers if x > 5]
print("Greater than 5:", greater)       # [6, 7, 8, 9, 10]

# Filter words longer than 4 characters:
words = ["cat", "elephant", "dog", "butterfly", "bee", "python"]
long_words = [w for w in words if len(w) > 4]
print("Words longer than 4 chars:", long_words)


# ---------------------------------------------------------
# SECTION 3: TRANSFORMATION + CONDITION TOGETHER
# ---------------------------------------------------------
# You can BOTH transform AND filter in the same comprehension!

print("\n--- Section 3: Transform + Filter Together ---")

# Get the SQUARES of only the even numbers:
even_squares = [x ** 2 for x in range(1, 11) if x % 2 == 0]
print("Squares of evens:    ", even_squares)   # [4, 16, 36, 64, 100]

# Uppercase only words that start with 'p':
words = ["python", "java", "php", "javascript", "perl"]
p_words = [w.upper() for w in words if w.startswith("p")]
print("Words starting with p:", p_words)       # ['PYTHON', 'PHP', 'PERL']

# Get student names who passed (marks >= 50):
students = [("Noman", 85), ("Ali", 42), ("Sara", 91), ("Rahim", 38)]
passed = [name for name, mark in students if mark >= 50]
print("Students who passed:", passed)


# ---------------------------------------------------------
# SECTION 4: if-else INSIDE COMPREHENSION
# ---------------------------------------------------------
# You can put if-else INSIDE the expression part (before 'for').
# This transforms EVERY item (not just filters).
# Syntax: [value_if_true if condition else value_if_false  for item in list]

print("\n--- Section 4: if-else Inside Comprehension ---")

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Label each number as "even" or "odd":
labeled = ["even" if x % 2 == 0 else "odd" for x in numbers]
print("Even/Odd labels:", labeled)

# Mark each mark as "Pass" or "Fail":
marks   = [85, 42, 90, 33, 67, 55]
results = ["Pass" if m >= 50 else "Fail" for m in marks]
print("Results:", results)


# ---------------------------------------------------------
# SECTION 5: NESTED LIST COMPREHENSION
# ---------------------------------------------------------
# A comprehension can loop over multiple things.
# This is like a nested for loop, but in one line.

print("\n--- Section 5: Nested Comprehension ---")

# Create a multiplication table as a 2D list:
table = [[row * col for col in range(1, 4)] for row in range(1, 4)]
print("3x3 Multiplication table:")
for row in table:
    print(" ", row)

# Flatten a 2D list (list of lists) into a 1D list:
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat   = [item for row in matrix for item in row]
print("Flattened matrix:", flat)   # [1,2,3,4,5,6,7,8,9]


# ---------------------------------------------------------
# SECTION 6: DICTIONARY COMPREHENSION
# ---------------------------------------------------------
# Same idea as list comprehension, but creates a DICTIONARY.
# Syntax: {key_expr: value_expr  for  item  in  iterable}

print("\n--- Section 6: Dictionary Comprehension ---")

# Create a dict mapping number to its square:
squares_dict = {x: x ** 2 for x in range(1, 6)}
print("Squares dict:", squares_dict)   # {1:1, 2:4, 3:9, 4:16, 5:25}

# Create a dict of word lengths:
fruits = ["apple", "banana", "cherry"]
lengths = {f: len(f) for f in fruits}
print("Fruit lengths:", lengths)

# Filter: only include fruits with more than 5 letters:
long_fruits = {f: len(f) for f in fruits if len(f) > 5}
print("Long fruits:", long_fruits)

# Swap keys and values in a dictionary:
original = {"a": 1, "b": 2, "c": 3}
swapped  = {v: k for k, v in original.items()}
print("Swapped dict:", swapped)   # {1:'a', 2:'b', 3:'c'}


# ---------------------------------------------------------
# SECTION 7: SET COMPREHENSION
# ---------------------------------------------------------
# Same idea, but creates a SET (removes duplicates).
# Syntax: {expression  for  item  in  iterable}

print("\n--- Section 7: Set Comprehension ---")

numbers = [1, 2, 2, 3, 3, 3, 4, 5, 5]
unique_squares = {x ** 2 for x in numbers}   # Automatically removes duplicates!
print("Unique squares:", unique_squares)


# ---------------------------------------------------------
# SECTION 8: map() FUNCTION
# ---------------------------------------------------------
# map(function, iterable) applies a function to EVERY item
# in the iterable and returns a map object.
# It's similar to list comprehension but uses a function reference.

print("\n--- Section 8: map() Function ---")

numbers = [1, 2, 3, 4, 5]

# Using map with a defined function:
def triple(x):
    return x * 3

result = list(map(triple, numbers))   # Apply triple() to every number
print("Tripled with map:", result)     # [3, 6, 9, 12, 15]

# Using map with a lambda (shorter, for simple operations):
squared = list(map(lambda x: x ** 2, numbers))
print("Squared with map:", squared)   # [1, 4, 9, 16, 25]

# map() with strings:
names = ["  noman  ", "  ali  ", "  sara  "]
cleaned = list(map(str.strip, names))   # .strip() removes spaces
print("Cleaned names:", cleaned)


# ---------------------------------------------------------
# SECTION 9: filter() FUNCTION
# ---------------------------------------------------------
# filter(function, iterable) returns only the items for which
# the function returns True. It FILTERS the iterable.

print("\n--- Section 9: filter() Function ---")

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Filter only even numbers:
def is_even(n):
    return n % 2 == 0

evens = list(filter(is_even, numbers))
print("Even numbers (filter):", evens)   # [2, 4, 6, 8, 10]

# Filter with lambda:
odds = list(filter(lambda n: n % 2 != 0, numbers))
print("Odd numbers (filter):", odds)     # [1, 3, 5, 7, 9]

# Filter students who passed:
marks_list = [45, 78, 90, 33, 67, 55]
passed_marks = list(filter(lambda m: m >= 50, marks_list))
print("Passing marks:", passed_marks)


# ---- Comparison: map & filter vs comprehension ----
print("\n--- Comparison: All Three Ways ---")
data = range(1, 11)

# Get squares of even numbers only:
way1_map_filter = list(map(lambda x: x**2, filter(lambda x: x%2==0, data)))
way2_comprehension = [x**2 for x in range(1, 11) if x % 2 == 0]

print("map+filter:",    way1_map_filter)
print("comprehension:", way2_comprehension)
print("Both give the same result!")

# ============================================================
# SUMMARY:
# - List comprehension:  [expr for item in iterable if cond]
# - If-else in comp.:    [a if cond else b for item in iterable]
# - Dict comprehension:  {key: val for item in iterable}
# - Set comprehension:   {expr for item in iterable}
# - map(func, list):     apply func to every item
# - filter(func, list):  keep items where func returns True
# - Comprehensions are usually shorter and more readable than
#   writing explicit for loops + append.
# ============================================================
