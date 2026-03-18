# ============================================================
# FILE: error_handling.py
# TOPIC: Error Handling in Python (try / except / else / finally)
# ============================================================
# Errors (also called Exceptions) happen in every program.
# For example:
#   - User types a letter when you expected a number
#   - You try to open a file that doesn't exist
#   - You try to divide by zero
#
# Instead of letting the program CRASH, we can HANDLE errors
# gracefully using try/except blocks.
#
# Think of it like a safety net:
#   try    -> attempt the risky code
#   except -> catch the error if it fails
#   else   -> run if NO error occurred
#   finally-> ALWAYS runs, with or without error (cleanup code)
# ============================================================


# ---------------------------------------------------------
# SECTION 1: WHY ERRORS HAPPEN (Without Handling)
# ---------------------------------------------------------
# Let's understand what happens when an error is NOT caught.
# (We'll comment these out so they don't crash the program.)

print("--- Section 1: Common Errors ---")

# ZeroDivisionError:
# result = 10 / 0        # Cannot divide by zero!

# ValueError:
# number = int("hello")  # Cannot convert "hello" to an integer!

# NameError:
# print(unknown_var)     # Variable doesn't exist!

# IndexError:
# my_list = [1, 2, 3]
# print(my_list[10])     # Index 10 doesn't exist in a 3-item list!

print("(Errors shown as comments above to avoid crashing the program.)")


# ---------------------------------------------------------
# SECTION 2: BASIC try / except
# ---------------------------------------------------------
# Wrap the risky code inside 'try'. If an error occurs,
# Python jumps to 'except' instead of crashing.

print("\n--- Section 2: Basic try / except ---")

try:
    # This risky code might fail:
    number = int(input("Enter a whole number: "))   # What if user types "abc"?
    print("You entered:", number)
except:
    # This runs ONLY if the code inside 'try' caused an error:
    print("Oops! That was not a valid number. Please enter digits only.")

print("Program continues normally after the try/except block.")


# ---------------------------------------------------------
# SECTION 3: CATCHING SPECIFIC ERRORS
# ---------------------------------------------------------
# It's better to catch SPECIFIC error types so you can give
# more helpful messages depending on WHAT went wrong.
#
# Common error types:
#   ValueError          -> wrong type/format (e.g., int("hello"))
#   ZeroDivisionError   -> dividing by zero
#   FileNotFoundError   -> file doesn't exist
#   TypeError           -> wrong data type in operation
#   IndexError          -> list index out of range
#   KeyError            -> dictionary key doesn't exist
#   NameError           -> variable not defined

print("\n--- Section 3: Catching Specific Errors ---")

def safe_divide(a, b):
    """Divides two numbers safely, handling possible errors."""
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        print("  Error: Cannot divide by zero!")
        return None
    except TypeError:
        print("  Error: Both values must be numbers, not text!")
        return None

print("10 / 2:", safe_divide(10, 2))     # 5.0
print("10 / 0:", safe_divide(10, 0))     # ZeroDivisionError caught
print("10 / '2':", safe_divide(10, '2')) # TypeError caught


# ---------------------------------------------------------
# SECTION 4: else CLAUSE (runs if NO error)
# ---------------------------------------------------------
# The 'else' block runs ONLY when the try block succeeds
# (no exception was raised).

print("\n--- Section 4: else Clause ---")

try:
    age = int(input("Enter your age: "))
except ValueError:
    print("That's not a valid age. Please enter a number.")
else:
    # This only runs if the int() conversion succeeded:
    if age >= 18:
        print(f"You are {age} years old. You are an adult!")
    else:
        print(f"You are {age} years old. You are still young!")


# ---------------------------------------------------------
# SECTION 5: finally CLAUSE (ALWAYS runs)
# ---------------------------------------------------------
# 'finally' runs NO MATTER WHAT – whether an error occurred or not.
# Use it for "cleanup" code (e.g., closing files, releasing resources).

print("\n--- Section 5: finally Clause ---")

def attempt_connection(host):
    """Simulates connecting to a server."""
    print(f"  Attempting to connect to: {host}")
    try:
        if host == "":
            raise ValueError("Host cannot be empty!")  # Manually raise error
        print(f"  Successfully connected to {host}!")
    except ValueError as e:
        print(f"  Connection failed: {e}")
    finally:
        # This ALWAYS runs – good place to disconnect/cleanup
        print("  Connection closed. (finally block always runs)")

attempt_connection("Google.com")
print()
attempt_connection("")     # Empty host -> ValueError


# ---------------------------------------------------------
# SECTION 6: raise (Throwing Custom Errors)
# ---------------------------------------------------------
# You can CREATE and THROW your own errors using 'raise'.
# This is useful when you want to stop execution if some
# custom condition is violated.

print("\n--- Section 6: raise (Custom Errors) ---")

def set_age(age):
    """Sets an age after validating it."""
    if not isinstance(age, int):
        raise TypeError("Age must be an integer!")
    if age < 0:
        raise ValueError("Age cannot be negative!")
    if age > 150:
        raise ValueError("Age seems unrealistically high!")
    print(f"  Age set to: {age}")

# Test different scenarios:
for test_age in [25, -1, 200, "twenty"]:
    try:
        set_age(test_age)
    except (ValueError, TypeError) as error:
        # 'as error' lets us store and display the error message
        print(f"  Could not set age = {test_age!r}. Reason: {error}")


# ---------------------------------------------------------
# SECTION 7: Multiple except Blocks
# ---------------------------------------------------------
# You can handle multiple different errors separately with
# multiple except blocks, or catch several at once with a tuple.

print("\n--- Section 7: Multiple except Blocks ---")

def get_list_item(my_list, index):
    """Safely gets an item from a list at the given index."""
    try:
        value = my_list[index]
        print(f"  Item at index {index}: {value}")
    except IndexError:
        print(f"  Error: Index {index} is out of range! List has {len(my_list)} items.")
    except TypeError:
        print(f"  Error: Index must be an integer, not '{type(index).__name__}'!")
    except Exception as e:
        # 'Exception' is the GENERAL catch-all for any other error
        print(f"  Unexpected error: {e}")

my_list = ["apple", "banana", "cherry"]
get_list_item(my_list, 1)      # banana (works fine)
get_list_item(my_list, 10)     # IndexError
get_list_item(my_list, "abc")  # TypeError


# ---------------------------------------------------------
# REAL LIFE EXAMPLE: Input Validator
# ---------------------------------------------------------
print("\n--- Real Life Example: Safe User Input ---")

def get_positive_number(prompt):
    """Keeps asking until the user gives a valid positive number."""
    while True:    # Keep looping until we get valid input
        try:
            value = float(input(prompt))
            if value <= 0:
                raise ValueError("Number must be positive!")
            return value   # Return the valid number
        except ValueError as e:
            print(f"  Invalid input: {e}. Please try again.")

# Get two numbers safely and divide them:
num1 = get_positive_number("Enter the first positive number: ")
num2 = get_positive_number("Enter the second positive number: ")

try:
    result = num1 / num2
    print(f"  {num1} / {num2} = {result:.4f}")
except ZeroDivisionError:
    print("  Cannot divide by zero!")

# ============================================================
# SUMMARY:
# - try:      -> put risky code here
# - except ErrorType: -> handle that specific error
# - except (E1, E2):  -> handle multiple error types
# - except Exception as e: -> catch any error, store message in e
# - else:     -> runs ONLY if NO error occurred in try
# - finally:  -> runs ALWAYS (error or not) - use for cleanup
# - raise     -> manually throw an error
# - Common errors: ValueError, TypeError, ZeroDivisionError,
#                  FileNotFoundError, IndexError, KeyError
# ============================================================
