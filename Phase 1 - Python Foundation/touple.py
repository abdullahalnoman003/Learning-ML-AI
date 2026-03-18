# ============================================================
# FILE: touple.py
# TOPIC: Tuples and Sets in Python
# ============================================================
# This file covers TWO types of collections:
#
#   TUPLE: Like a list, but CANNOT be changed after creation.
#          Use it when data should stay fixed (e.g., coordinates,
#          days of the week, RGB colors).
#
#   SET:   A collection of UNIQUE, UNORDERED values.
#          Great for removing duplicates and doing math-like
#          operations (union, intersection, difference).
# ============================================================


# ============================================================
# PART 1: TUPLES
# ============================================================

# ---------------------------------------------------------
# SECTION 1: CREATING A TUPLE
# ---------------------------------------------------------
# A tuple is written with ROUND parentheses ().
# Items inside are separated by commas.

print("=" * 40)
print("PART 1: TUPLES")
print("=" * 40)

print("\n--- Creating Tuples ---")
colors      = ("red", "green", "blue")
coordinates = (23.8, 90.4)                  # Latitude, Longitude (never changes)
months      = ("Jan", "Feb", "Mar", "Apr")
mixed       = (1, "hello", True, 3.14)      # Can hold mixed types

print("Colors:",      colors)
print("Coordinates:", coordinates)
print("Months:",      months)
print("Type:",        type(colors))          # <class 'tuple'>


# ---------------------------------------------------------
# SECTION 2: ACCESSING TUPLE ITEMS
# ---------------------------------------------------------
# Access items using index (same as lists). Starts from 0.

print("\n--- Accessing Tuple Items ---")
print(colors[0])    # red   <- index 0
print(colors[2])    # blue  <- index 2
print(colors[-1])   # blue  <- last item (negative index)


# ---------------------------------------------------------
# SECTION 3: TUPLES CANNOT BE MODIFIED
# ---------------------------------------------------------
# Once a tuple is created, you CANNOT change, add, or remove items.
# This is called being "immutable".
#
# Trying to change a tuple will cause a TypeError:
#   colors[0] = "yellow"   -> ERROR!

print("\n--- Tuples are Immutable ---")
print("Trying to change colors[0] will cause an ERROR.")
print("This protects data that should never be changed.")
# Uncomment the line below to see the error:
# colors[0] = "yellow"   # TypeError: 'tuple' object does not support item assignment


# ---------------------------------------------------------
# SECTION 4: LOOPING THROUGH A TUPLE
# ---------------------------------------------------------

print("\n--- Looping Through a Tuple ---")
for color in colors:
    print(" -", color)

# With index using enumerate:
for index, color in enumerate(colors):
    print(f"  {index}: {color}")


# ---------------------------------------------------------
# SECTION 5: TUPLE WITH ONE ITEM (Important!)
# ---------------------------------------------------------
# If a tuple has ONLY ONE item, you MUST add a trailing comma.
# Without the comma, Python thinks it's just a regular value
# in parentheses (not a tuple).

print("\n--- Single Item Tuple ---")
single_good = (10,)     # This IS a tuple  <- note the trailing comma
single_bad  = (10)      # This is NOT a tuple, it's just the integer 10

print("Single with comma:",    single_good, "|", type(single_good))  # tuple
print("Single without comma:", single_bad,  "|", type(single_bad))   # int


# ---------------------------------------------------------
# SECTION 6: TUPLE METHODS AND OPERATIONS
# ---------------------------------------------------------

print("\n--- Tuple Methods ---")
nums = (5, 10, 15, 10, 20, 10)

print("Tuple:",         nums)
print("Length:",        len(nums))        # 6
print("Count of 10:",   nums.count(10))   # 3  (10 appears 3 times)
print("Index of 15:",   nums.index(15))   # 2  (first position of 15)
print("Max:",           max(nums))
print("Min:",           min(nums))
print("Is 5 in tuple:", 5 in nums)        # True


# ---------------------------------------------------------
# SECTION 7: TUPLE UNPACKING
# ---------------------------------------------------------
# You can assign multiple variables from a tuple in one line!
# This is called "unpacking". Very useful in real projects.

print("\n--- Tuple Unpacking ---")
point = (10, 20, 30)
x, y, z = point     # Unpack all 3 values into 3 variables
print(f"x = {x}, y = {y}, z = {z}")

person = ("Noman", 22, "Dhaka")
name, age, city = person
print(f"Name: {name}, Age: {age}, City: {city}")


# ============================================================
# PART 2: SETS
# ============================================================
print("\n" + "=" * 40)
print("PART 2: SETS")
print("=" * 40)

# ---------------------------------------------------------
# SECTION 8: CREATING A SET
# ---------------------------------------------------------
# A set is written with CURLY BRACES {}, just like a dictionary,
# but WITHOUT key-value pairs - just values.
#
# KEY PROPERTIES OF A SET:
#   1. No duplicates allowed - each value appears ONLY ONCE
#   2. Unordered - items have no guaranteed position/index
#   3. Fast for checking membership (if item in set)

print("\n--- Creating Sets ---")
my_set = {1, 2, 3, 4, 5}
print("Set:", my_set)           # Values, but order may vary!
print("Type:", type(my_set))    # <class 'set'>

# Duplicates are automatically removed:
nums_with_duplicates = {1, 2, 2, 3, 3, 3, 4}
print("With duplicates removed:", nums_with_duplicates)  # {1, 2, 3, 4}


# ---------------------------------------------------------
# SECTION 9: ADDING AND REMOVING FROM A SET
# ---------------------------------------------------------

print("\n--- Adding and Removing ---")
animals = {"cat", "dog", "rabbit"}
print("Original:", animals)

# .add(item) -> adds ONE item
animals.add("fish")
print("After add('fish'):", animals)

# Adding a duplicate is simply ignored (no error)
animals.add("cat")              # "cat" already exists, nothing changes
print("After add('cat') again:", animals)

# .remove(item) -> removes the item (causes ERROR if not found)
animals.remove("rabbit")
print("After remove('rabbit'):", animals)

# .discard(item) -> SAFER remove (no error if item not found)
animals.discard("lion")         # "lion" doesn't exist, but no error
print("After discard('lion') [no error]:", animals)


# ---------------------------------------------------------
# SECTION 10: LOOPING THROUGH A SET
# ---------------------------------------------------------

print("\n--- Looping Through a Set ---")
fruits = {"apple", "banana", "cherry"}

for fruit in fruits:
    print(" -", fruit)  # Note: order is NOT guaranteed!


# ---------------------------------------------------------
# SECTION 11: SET OPERATIONS (Like Math)
# ---------------------------------------------------------
# Sets support powerful mathematical operations.
# Think of it like Venn diagrams from school!

print("\n--- Set Operations ---")
a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}

print("Set A:", a)
print("Set B:", b)

# UNION (|) -> all items from BOTH sets (no duplicates)
print("A | B (Union):",        a | b)   # {1,2,3,4,5,6,7,8}

# INTERSECTION (&) -> only items that exist in BOTH
print("A & B (Intersection):", a & b)   # {4, 5}

# DIFFERENCE (-) -> items in A but NOT in B
print("A - B (Difference):",   a - b)   # {1, 2, 3}
print("B - A (Difference):",   b - a)   # {6, 7, 8}

# SYMMETRIC DIFFERENCE (^) -> items in either A or B but NOT BOTH
print("A ^ B (Sym. Diff):",    a ^ b)   # {1, 2, 3, 6, 7, 8}


# ---------------------------------------------------------
# SECTION 12: CHECKING MEMBERSHIP (Very Fast!)
# ---------------------------------------------------------

print("\n--- Checking Membership ---")
prime_numbers = {2, 3, 5, 7, 11, 13, 17, 19}

print("Is 7 prime?",  7 in prime_numbers)   # True
print("Is 9 prime?",  9 in prime_numbers)   # False (9 = 3*3)
print("Is 13 prime?", 13 in prime_numbers)  # True


# ---------------------------------------------------------
# REAL LIFE EXAMPLE: Remove Duplicate Students
# ---------------------------------------------------------
print("\n--- Real Life Example: Remove Duplicates ---")
attendance = ["Noman", "Ali", "Noman", "Rahim", "Ali", "Sara", "Noman"]
print("Raw attendance list:", attendance)
print("Total entries:",       len(attendance))

unique_students = set(attendance)       # Automatically removes duplicates!
print("Unique students:",     unique_students)
print("Unique count:",        len(unique_students))

# ============================================================
# SUMMARY:
# TUPLES:
#   - tuple = (item1, item2, ...) -> IMMUTABLE (cannot change)
#   - Access by index: tuple[0], tuple[-1]
#   - Use when data should NOT change
#   - Unpack: a, b, c = my_tuple
#
# SETS:
#   - set = {item1, item2, ...} -> UNIQUE, UNORDERED values
#   - .add(), .remove(), .discard()
#   - Set math: | (union), & (intersection), - (difference)
#   - Great for removing duplicates from lists
# ============================================================

## Access Tuple Items

print(colors[0])
print(colors[-1])

## Tuple Cannot Be Modified ❌

#colors[0] = "yellow"   # ERROR

# This is the main difference from lists.

## Loop Through Tuple

for color in colors:
    print(color)


## Tuple with One Item (Important!)

single = (10,)

#Without comma → it’s not a tuple.

# PART 2: SETS

## What is a Set?
### A **set** is a collection of: Unique values ,Unordered, No duplicates

### Example

numbers = {1, 2, 3, 4}


##  8. Duplicate Values Removed Automatically

nums = {1, 2, 2, 3, 3, 4}
print(nums)


## Add & Remove Items in Set

numbers.add(10)
numbers.remove(10)


## Loop Through Set

for n in numbers:
    print(n)


## Set Operations (VERY IMPORTANT)

## Union

a = {1, 2, 3}
b = {3, 4, 5}

print(a | b)


### Intersection

print(a & b)


### Difference

print(a - b)


##  12. Real-Life Example (Unique Students)

students = ["Noman", "Ali", "Noman", "Rahim"]
unique_students = set(students)

print(unique_students)


