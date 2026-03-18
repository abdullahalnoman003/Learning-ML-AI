# ============================================================
# FILE: IfElse.py
# TOPIC: Conditions and Decision Making (if / elif / else)
# ============================================================
# In real life, we make decisions all the time:
#   "IF it is raining, THEN take an umbrella, ELSE go without."
# Python uses if / elif / else to make decisions in code!
#
# In this file you will learn:
#   1. Basic if / else
#   2. if / elif / else (multiple conditions)
#   3. Comparison operators
#   4. Logical operators (and, or, not)
#   5. Nested if statements
#   6. Short one-line if (ternary)
# ============================================================


# ---------------------------------------------------------
# SECTION 1: COMPARISON OPERATORS
# ---------------------------------------------------------
# These operators COMPARE two values and return True or False.
#
#   ==   Equal to                (5 == 5 → True)
#   !=   Not equal to            (5 != 3 → True)
#   >    Greater than            (7 > 3  → True)
#   <    Less than               (2 < 9  → True)
#   >=   Greater than or equal   (5 >= 5 → True)
#   <=   Less than or equal      (3 <= 7 → True)

print("--- Comparison Operators ---")
print(5 == 5)   # True
print(5 == 3)   # False
print(10 > 7)   # True
print(4 != 4)   # False  (4 IS equal to 4, so NOT-equal is False)


# ---------------------------------------------------------
# SECTION 2: BASIC IF / ELSE
# ---------------------------------------------------------
# Syntax:
#   if condition:
#       code runs if condition is True
#   else:
#       code runs if condition is False
#
# IMPORTANT: Python uses INDENTATION (spaces) to know what
# belongs inside the if block. Always indent by 4 spaces.

print("\n--- Basic If / Else ---")
temperature = 35  # degrees Celsius

if temperature > 30:
    print("It's HOT outside! Drink water.")
else:
    print("The weather is nice. Enjoy!")


# ---------------------------------------------------------
# SECTION 3: IF / ELIF / ELSE (Multiple Conditions)
# ---------------------------------------------------------
# When you have MORE than 2 possibilities, use elif ("else if").
# Python checks each condition ONE BY ONE from the top.
# Once it finds a True condition, it runs that block and STOPS.

print("\n--- If / Elif / Else ---")
age = 22

if age < 0:
    # This handles an impossible/invalid age
    print("This age is invalid! Age cannot be negative.")
elif age == 0:
    # Exactly zero
    print("Just born!")
elif age > 0 and age <= 12:
    # Between 1 and 12
    print("You are a child.")
elif age >= 13 and age <= 17:
    # Between 13 and 17
    print("You are a teenager. You will soon be an adult!")
elif age >= 18 and age <= 60:
    # Between 18 and 60
    print("You are an adult. You are eligible to vote!")
else:
    # 61 and above
    print("You are a senior citizen. Respect!")


# ---------------------------------------------------------
# SECTION 4: LOGICAL OPERATORS (and, or, not)
# ---------------------------------------------------------
# Sometimes you need to check MULTIPLE conditions at the same time.
#
#   and  → BOTH conditions must be True
#   or   → AT LEAST ONE condition must be True
#   not  → REVERSES the condition (True becomes False)

print("\n--- Logical Operators ---")
score = 75
attendance = 85

# 'and': student passes only if BOTH score >= 60 AND attendance >= 75
if score >= 60 and attendance >= 75:
    print("Student PASSED the course.")
else:
    print("Student FAILED the course.")

# 'or': get a discount if you are a student OR a senior citizen
is_student = True
is_senior  = False

if is_student or is_senior:
    print("You get a 20% discount!")
else:
    print("No discount available.")

# 'not': reverses True to False and False to True
is_raining = False

if not is_raining:
    print("It is NOT raining. You can go outside!")


# ---------------------------------------------------------
# SECTION 5: NESTED IF (if inside another if)
# ---------------------------------------------------------
# You can put an if statement inside another if statement.
# This is called "nesting". Use it when your decision has layers.

print("\n--- Nested If ---")
has_ticket = True
vip = False

if has_ticket:
    print("You can enter the event.")
    if vip:
        print("Welcome to the VIP lounge!")
    else:
        print("Please go to the general seating area.")
else:
    print("Sorry, you need a ticket to enter.")


# ---------------------------------------------------------
# SECTION 6: ONE-LINE IF (Ternary / Conditional Expression)
# ---------------------------------------------------------
# For simple if/else, Python lets you write it in ONE line.
# Syntax: value_if_true  if  condition  else  value_if_false

print("\n--- One-Line If (Ternary) ---")
marks = 55
result = "Pass" if marks >= 50 else "Fail"
print(f"Student result: {result}")

number = -7
absolute_value = number if number >= 0 else -number
print(f"Absolute value of {number} is: {absolute_value}")


# ---------------------------------------------------------
# REAL LIFE EXAMPLE: Grade Calculator
# ---------------------------------------------------------
print("\n--- Real Life Example: Grade Calculator ---")
student_marks = int(input("Enter your marks (0-100): "))

if student_marks < 0 or student_marks > 100:
    print("Invalid marks. Please enter a number between 0 and 100.")
elif student_marks >= 90:
    grade = "A+"
    message = "Excellent! Outstanding performance!"
elif student_marks >= 80:
    grade = "A"
    message = "Very good!"
elif student_marks >= 70:
    grade = "B"
    message = "Good job!"
elif student_marks >= 60:
    grade = "C"
    message = "Satisfactory. Keep it up!"
elif student_marks >= 50:
    grade = "D"
    message = "Passed, but try harder next time."
else:
    grade = "F"
    message = "Failed. Don't give up! Study more."

if student_marks >= 0 and student_marks <= 100:
    print(f"Your grade: {grade}")
    print(f"Comment: {message}")

# ============================================================
# SUMMARY:
# - if checks a condition. If True, the block runs.
# - else runs when the if condition is False.
# - elif adds more conditions in between.
# - Comparison: ==  !=  >  <  >=  <=
# - Logical: and (both true), or (one true), not (reverse)
# - One-line: result = "Yes" if condition else "No"
# - INDENTATION is critical — use 4 spaces inside blocks!
# ============================================================
