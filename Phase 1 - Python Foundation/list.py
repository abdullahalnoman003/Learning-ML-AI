# ============================================================
# FILE: list.py
# TOPIC: Lists in Python
# ============================================================
# A list is a collection of multiple items stored in one variable.
# Think of it like a shopping list or a to-do list — multiple
# items, all in one place, in order.
#
# In this file you will learn:
#   1. Creating a list
#   2. Accessing items (indexing)
#   3. Negative indexing
#   4. Slicing a list
#   5. Looping through a list
#   6. Modifying list items
#   7. Adding and removing items
#   8. Useful list methods
#   9. Checking if an item exists
#  10. Real-life example
# ============================================================


# ---------------------------------------------------------
# SECTION 1: CREATING A LIST
# ---------------------------------------------------------
# A list is written with square brackets []
# Items are separated by commas.
# A list can hold ANY type of data: numbers, text, mixed.

print("--- Creating Lists ---")
numbers = [1, 2, 3, 4, 5]           # A list of integers
names   = ["Noman", "Ali", "Rahim"] # A list of strings
mixed   = [1, "Python", True, 3.5]  # A mixed list (all types allowed)
empty   = []                         # An empty list

print("Numbers:", numbers)
print("Names:",   names)
print("Mixed:",   mixed)
print("Empty:",   empty)


# ---------------------------------------------------------
# SECTION 2: ACCESSING ITEMS (INDEXING)
# ---------------------------------------------------------
# Each item in a list has a position called an "index".
# Indexing starts from 0 (not 1!).
#
#  "Noman"   "Ali"   "Rahim"
#     0         1       2      ← Positive index
#    -3        -2      -1      ← Negative index

print("\n--- Accessing Items by Index ---")
names = ["Noman", "Ali", "Rahim"]

print(names[0])    # Noman  ← first item
print(names[1])    # Ali
print(names[2])    # Rahim  ← last item
# print(names[3])  # This would cause an ERROR! Index out of range.


# ---------------------------------------------------------
# SECTION 3: NEGATIVE INDEXING
# ---------------------------------------------------------
# Negative indexes count from the END of the list.
# -1 is always the last item, -2 is second to last, etc.

print("\n--- Negative Indexing ---")
print(names[-1])   # Rahim  ← last item
print(names[-2])   # Ali    ← second from end
print(names[-3])   # Noman  ← first item (from the end)


# ---------------------------------------------------------
# SECTION 4: SLICING A LIST
# ---------------------------------------------------------
# Get a PORTION of a list.
# Syntax: list[start : stop]  ← gives items from start up to (not including) stop

print("\n--- Slicing a List ---")
five_nums = [10, 20, 30, 40, 50]

print(five_nums[1:4])   # [20, 30, 40]  ← index 1, 2, 3
print(five_nums[:3])    # [10, 20, 30]  ← from start to index 2
print(five_nums[2:])    # [30, 40, 50]  ← from index 2 to end
print(five_nums[-2:])   # [40, 50]      ← last 2 items
print(five_nums[::-1])  # [50, 40, 30, 20, 10]  ← reversed list


# ---------------------------------------------------------
# SECTION 5: LOOPING THROUGH A LIST
# ---------------------------------------------------------
# Use a for loop to go through every item in a list.

print("\n--- Looping Through a List ---")
fruits = ["apple", "banana", "cherry"]

# Method 1: Direct (simple and clean)
print("Method 1: Direct loop")
for fruit in fruits:
    print(" -", fruit)

# Method 2: Using index with range(len())
print("Method 2: With index")
for i in range(len(fruits)):   # range(3) → 0, 1, 2
    print(f"  Index {i}: {fruits[i]}")

# Method 3: enumerate() – gives both index AND value (recommended!)
print("Method 3: enumerate (best way)")
for index, fruit in enumerate(fruits):
    print(f"  {index}: {fruit}")


# ---------------------------------------------------------
# SECTION 6: MODIFYING LIST ITEMS
# ---------------------------------------------------------
# Lists are MUTABLE — you CAN change their contents after creation.
# (Unlike tuples, which you'll see in touple.py)

print("\n--- Modifying Items ---")
numbers = [10, 20, 30]
print("Before:", numbers)

numbers[1] = 99    # Change the item at index 1 from 20 to 99
print("After changing index 1:", numbers)


# ---------------------------------------------------------
# SECTION 7: ADDING ITEMS
# ---------------------------------------------------------

print("\n--- Adding Items ---")
my_list = [1, 2, 3]

# .append(item) → adds ONE item to the END of the list
my_list.append(4)
print("After append(4):", my_list)     # [1, 2, 3, 4]

# .insert(index, item) → adds an item at a SPECIFIC position
my_list.insert(1, 99)                  # Insert 99 at index 1
print("After insert(1, 99):", my_list) # [1, 99, 2, 3, 4]

# .extend([items]) → adds MULTIPLE items from another list
my_list.extend([10, 11, 12])
print("After extend:", my_list)        # [1, 99, 2, 3, 4, 10, 11, 12]


# ---------------------------------------------------------
# SECTION 8: REMOVING ITEMS
# ---------------------------------------------------------

print("\n--- Removing Items ---")
colors = ["red", "green", "blue", "green", "yellow"]
print("Original:", colors)

# .remove(value) → removes the FIRST occurrence of that value
colors.remove("green")          # Removes only the first "green"
print("After remove('green'):", colors)

# .pop() → removes and RETURNS the LAST item
last = colors.pop()
print("Popped item:", last)     # yellow
print("After pop():", colors)

# .pop(index) → removes and returns item at a specific index
item = colors.pop(0)            # Remove item at index 0
print("Popped at index 0:", item)
print("After pop(0):", colors)

# del keyword → deletes by index
nums = [5, 10, 15, 20]
del nums[2]                     # Delete item at index 2 (value 15)
print("After del nums[2]:", nums)


# ---------------------------------------------------------
# SECTION 9: USEFUL LIST METHODS
# ---------------------------------------------------------

print("\n--- Useful List Methods ---")
scores = [90, 55, 78, 90, 33, 67, 90]

print("List:", scores)
print("Length (len):",     len(scores))         # Number of items: 7
print("Largest (max):",    max(scores))         # 90
print("Smallest (min):",   min(scores))         # 33
print("Total (sum):",      sum(scores))         # Sum of all
print("Count of 90:",      scores.count(90))   # How many times 90 appears: 3
print("Index of 78:",      scores.index(78))   # Position of 78: 2

# Sort the list (ascending order)
scores.sort()
print("Sorted ascending:", scores)

# Sort in descending order
scores.sort(reverse=True)
print("Sorted descending:", scores)

# Reverse the list (not the same as sort)
scores.reverse()
print("Reversed:", scores)

# Copy a list (creates an independent copy)
copy_of_scores = scores.copy()
print("Copy:", copy_of_scores)


# ---------------------------------------------------------
# SECTION 10: CHECK IF ITEM EXISTS
# ---------------------------------------------------------

print("\n--- Check if Item Exists ---")
animals = ["cat", "dog", "rabbit", "fish"]

if "dog" in animals:
    print("Yes, dog is in the list!")

if "lion" not in animals:
    print("Lion is NOT in the list.")


# ---------------------------------------------------------
# REAL LIFE EXAMPLE: Student Marks System
# ---------------------------------------------------------
print("\n--- Real Life Example: Marks System ---")
marks = [45, 78, 90, 33, 67, 55, 82]

total   = sum(marks)
average = total / len(marks)
highest = max(marks)
lowest  = min(marks)

print(f"Marks:   {marks}")
print(f"Total:   {total}")
print(f"Average: {average:.1f}")
print(f"Highest: {highest}")
print(f"Lowest:  {lowest}")

# Count how many students passed (marks >= 50)
passed = 0
for mark in marks:
    if mark >= 50:
        passed += 1   # Same as: passed = passed + 1

print(f"Passed:  {passed} out of {len(marks)} students")
print(f"Failed:  {len(marks) - passed} students")

# ============================================================
# SUMMARY:
# - List: [item1, item2, ...] → ordered, changeable collection
# - Index starts at 0. Negative index counts from the end.
# - Slicing: list[start:stop] → extract a portion
# - Loop: for item in my_list: → goes through each item
# - Add: .append(), .insert(), .extend()
# - Remove: .remove(), .pop(), del
# - Check: item in list
# - Useful: len(), sum(), max(), min(), .sort(), .count()
# ============================================================
