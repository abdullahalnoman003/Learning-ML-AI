# ============================================================
# FILE: loop.py
# TOPIC: Loops in Python (for / while)
# ============================================================
# A "loop" makes Python repeat a block of code automatically.
# Instead of writing the same line 100 times, write it once
# and tell Python: "Repeat this 100 times!"
#
# In this file you will learn:
#   1. for loop with range()
#   2. for loop over a list
#   3. while loop
#   4. break (exit the loop early)
#   5. continue (skip the current step)
#   6. else with loops
#   7. Nested loops (loop inside a loop)
# ============================================================


# ---------------------------------------------------------
# SECTION 1: FOR LOOP WITH range()
# ---------------------------------------------------------
# A for loop repeats code a specific number of times.
# range() generates a sequence of numbers.
#
#   range(stop)         → 0, 1, 2, ..., stop-1
#   range(start, stop)  → start, ..., stop-1
#   range(start, stop, step) → start, start+step, ... (until stop)

print("--- For Loop: Basic (0 to 4) ---")
for i in range(5):        # i goes: 0, 1, 2, 3, 4
    print("Count:", i)

print("\n--- For Loop: With Start and Stop ---")
for i in range(1, 6):     # i goes: 1, 2, 3, 4, 5
    print("Number:", i)

print("\n--- For Loop: With Step (count by 2) ---")
for i in range(0, 11, 2): # i goes: 0, 2, 4, 6, 8, 10
    print("Even number:", i)

print("\n--- For Loop: Counting Backwards ---")
for i in range(5, 0, -1): # i goes: 5, 4, 3, 2, 1
    print("Countdown:", i)
print("Blast off!")


# ---------------------------------------------------------
# SECTION 2: FOR LOOP OVER A LIST
# ---------------------------------------------------------
# You can loop directly over items in a list.
# Python picks each item one by one automatically.

print("\n--- For Loop: Over a List ---")
fruits = ["apple", "banana", "cherry", "date"]

for fruit in fruits:       # 'fruit' holds one item each time
    print("Fruit:", fruit)

# Using index with enumerate()
# enumerate() gives you BOTH the index and the value
print("\n--- For Loop: With Index (enumerate) ---")
for index, fruit in enumerate(fruits):
    print(f"  {index}: {fruit}")


# ---------------------------------------------------------
# SECTION 3: WHILE LOOP
# ---------------------------------------------------------
# A while loop keeps running AS LONG AS a condition is True.
# It is useful when you don't know in advance how many times
# the loop should run.
#
# WARNING: If the condition NEVER becomes False, the loop
# runs forever (infinite loop). Always make sure the
# condition will eventually become False!

print("\n--- While Loop: Basic ---")
counter = 1
while counter <= 5:        # Keep running while counter is <= 5
    print("Counter:", counter)
    counter = counter + 1  # Increase counter each time (very important!)
print("Loop finished!")


# ---------------------------------------------------------
# SECTION 4: break (Exit the Loop Early)
# ---------------------------------------------------------
# 'break' immediately STOPS the loop and jumps out of it.
# Useful when you find what you are looking for and don't
# need to continue.

print("\n--- break: Stop Loop Early ---")
password = "1234"

for attempt in range(3):   # Allow maximum 3 attempts
    user_input = input(f"Attempt {attempt + 1}: Enter password: ")

    if user_input == password:
        print("Login successful! Access granted.")
        break              # Stop the loop immediately
    else:
        print("Wrong password. Try again.")
else:
    # This 'else' belongs to the 'for' loop.
    # It runs ONLY if the loop finished WITHOUT a break.
    print("3 failed attempts. Account locked!")


# ---------------------------------------------------------
# SECTION 5: continue (Skip to Next Iteration)
# ---------------------------------------------------------
# 'continue' SKIPS the rest of the current loop step
# and jumps straight to the NEXT iteration.

print("\n--- continue: Skip Certain Items ---")
print("Printing only odd numbers from 1 to 10:")
for i in range(1, 11):
    if i % 2 == 0:     # If i is even (remainder when divided by 2 is 0)
        continue       # Skip even numbers, go to next i
    print(i)           # Only odd numbers reach this line


# ---------------------------------------------------------
# SECTION 6: WHILE LOOP WITH break (Infinite Until Condition)
# ---------------------------------------------------------
# A common pattern: start an infinite loop (while True)
# and use 'break' to exit when a condition is met.

print("\n--- While True with break ---")
print("Type 'quit' to exit the loop.")
while True:
    user_text = input("Enter something (or 'quit' to stop): ")
    if user_text.lower() == "quit":
        print("Goodbye!")
        break           # Exit the loop
    print(f"You entered: {user_text}")


# ---------------------------------------------------------
# SECTION 7: NESTED LOOPS (Loop Inside a Loop)
# ---------------------------------------------------------
# A nested loop is a loop inside another loop.
# The INNER loop runs completely for EACH step of the outer loop.

print("\n--- Nested Loops: Multiplication Table ---")
for row in range(1, 4):        # Outer loop: rows 1, 2, 3
    for col in range(1, 4):    # Inner loop: columns 1, 2, 3
        result = row * col
        print(f"{row} x {col} = {result}", end="   ")  # end=" " keeps on same line
    print()  # Print a new line after each row


# ---------------------------------------------------------
# REAL LIFE EXAMPLE: Find the First Even Number in a List
# ---------------------------------------------------------
print("\n--- Real Life Example: Find First Even Number ---")
numbers = [7, 13, 9, 24, 5, 10]

for num in numbers:
    if num % 2 == 0:    # If number has no remainder when divided by 2, it's even
        print(f"First even number found: {num}")
        break           # Stop as soon as we find the first one

# ============================================================
# SUMMARY:
# - for loop: repeats a fixed number of times (use with range or list)
# - while loop: repeats as long as a condition is True
# - break: exits the loop immediately
# - continue: skips the current step, moves to next
# - Nested loops: a loop inside another loop
# - Always make sure while loops have a way to end!
# ============================================================
