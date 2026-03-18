# ============================================================
# FILE: strings.py
# TOPIC: Strings in Python
# ============================================================
# A "string" is simply a piece of text.
# In Python, any text inside quotes is a string.
# You can use single quotes ' ' or double quotes " ".
#
# In this file you will learn:
#   1. Creating strings
#   2. String indexing (accessing individual characters)
#   3. String slicing (getting a piece of the string)
#   4. Common string methods (built-in tools for strings)
#   5. f-strings (the modern way to format strings)
#   6. Checking and searching inside strings
# ============================================================


# ---------------------------------------------------------
# SECTION 1: CREATING STRINGS
# ---------------------------------------------------------
# A string is text surrounded by quotes.

greeting = "Hello, World!"          # Double quotes
city      = 'Dhaka'                  # Single quotes (both work the same)
long_text = """This is a
multi-line string.
Very useful for long paragraphs!"""  # Triple quotes for multiple lines

print("--- Creating Strings ---")
print(greeting)
print(city)
print(long_text)


# ---------------------------------------------------------
# SECTION 2: STRING INDEXING
# ---------------------------------------------------------
# Think of a string like a row of boxes, each holding one letter.
# Each box has a number called an "index", starting from 0.
#
#  H  e  l  l  o
#  0  1  2  3  4   ← Positive index (from the start)
# -5 -4 -3 -2 -1   ← Negative index (from the end)
#
# Use square brackets [] to access a character at a specific index.

word = "Hello"
print("\n--- String Indexing ---")
print(word[0])   # H  ← first character
print(word[1])   # e
print(word[4])   # o  ← last character (index 4)
print(word[-1])  # o  ← -1 always means the LAST character
print(word[-2])  # l  ← second from the end


# ---------------------------------------------------------
# SECTION 3: STRING SLICING
# ---------------------------------------------------------
# Slicing means extracting a PART of a string.
# Syntax: string[start : stop]
# It gives you characters from 'start' up to (but NOT including) 'stop'.
#
# You can also use: string[start : stop : step]
# 'step' controls how many characters to skip.

message = "Python is fun!"
print("\n--- String Slicing ---")
print(message[0:6])    # "Python"  ← index 0,1,2,3,4,5
print(message[7:9])    # "is"
print(message[10:])    # "fun!"    ← from index 10 to the end
print(message[:6])     # "Python"  ← from start up to index 6
print(message[-4:])    # "fun!"    ← last 4 characters
print(message[::2])    # every 2nd character (skips one each time)
print(message[::-1])   # "!nuf si nohtyP" ← reverses the string!


# ---------------------------------------------------------
# SECTION 4: COMMON STRING METHODS
# ---------------------------------------------------------
# Python has many built-in "methods" (tools) for strings.
# A method is called using a dot: string.method_name()

sentence = "  hello, python world!  "
print("\n--- Common String Methods ---")

# .upper() → converts ALL letters to UPPERCASE
print(sentence.upper())

# .lower() → converts ALL letters to lowercase
print(sentence.lower())

# .strip() → removes extra spaces from both sides
print(sentence.strip())          # removes spaces left and right
print(sentence.strip().upper())  # you can chain methods!

# .replace(old, new) → replaces every occurrence of 'old' with 'new'
print(sentence.replace("python", "AI"))

# .split(separator) → splits a string into a LIST of words
words = "apple,banana,cherry"
fruit_list = words.split(",")    # split at each comma
print(fruit_list)                # ['apple', 'banana', 'cherry']

# .join() → opposite of split, joins a list into one string
joined = " - ".join(fruit_list)
print(joined)                    # apple - banana - cherry

# .capitalize() → makes only the FIRST letter uppercase
print("python programming".capitalize())  # Python programming

# .title() → makes the First Letter Of Every Word uppercase
print("python programming".title())  # Python Programming

# len() → counts the number of characters (including spaces)
print("Length of 'Hello':", len("Hello"))  # 5


# ---------------------------------------------------------
# SECTION 5: f-STRINGS (FORMATTED STRINGS)
# ---------------------------------------------------------
# f-strings are the modern and cleanest way to include variable
# values inside a string. Just put 'f' before the opening quote,
# then put variables inside curly braces {}.

name  = "Noman"
age   = 22
gpa   = 3.92

print("\n--- f-Strings ---")
# Old way (messy):
print("My name is " + name + " and I am " + str(age) + " years old.")

# New way with f-string (clean & easy):
print(f"My name is {name} and I am {age} years old.")
print(f"My GPA is {gpa:.1f}")   # :.1f means round to 1 decimal place

# You can even put EXPRESSIONS inside {}:
print(f"Next year I will be {age + 1} years old.")
print(f"My GPA in percentage: {gpa * 25:.0f}%")


# ---------------------------------------------------------
# SECTION 6: CHECKING & SEARCHING INSIDE STRINGS
# ---------------------------------------------------------
# Python gives you tools to look inside strings.

phrase = "Learning Python is amazing"
print("\n--- String Checking & Searching ---")

# .startswith() → does the string BEGIN with this text?
print(phrase.startswith("Learning"))  # True
print(phrase.startswith("Python"))    # False

# .endswith() → does the string END with this text?
print(phrase.endswith("amazing"))     # True
print(phrase.endswith("boring"))      # False

# .find() → returns the INDEX of the first match
#           returns -1 if the text is NOT found
print(phrase.find("Python"))  # 9  (Python starts at index 9)
print(phrase.find("Java"))    # -1 (Java is not in the phrase)

# .count() → counts how many times something appears
print(phrase.count("i"))      # counts the letter 'i'
print(phrase.count("n"))      # counts the letter 'n'

# 'in' keyword → checks if something is inside the string (True/False)
print("Python" in phrase)     # True
print("Java" in phrase)       # False

# .isdigit() → True if ALL characters are numbers
print("12345".isdigit())      # True
print("123ab".isdigit())      # False

# .isalpha() → True if ALL characters are letters
print("Hello".isalpha())      # True
print("Hello123".isalpha())   # False


# ---------------------------------------------------------
# REAL LIFE EXAMPLE: Simple Name Formatter
# ---------------------------------------------------------
print("\n--- Real Life Example ---")
full_name = input("Enter your full name: ")

# Clean the input (remove extra spaces, fix capitalization)
clean_name = full_name.strip().title()

print(f"Formatted name: {clean_name}")
print(f"Total characters (including spaces): {len(clean_name)}")
print(f"Uppercase version: {clean_name.upper()}")

# Check if name starts with a specific letter
if clean_name.startswith("A"):
    print("Your name starts with the letter A!")
else:
    print(f"Your name starts with the letter: {clean_name[0]}")

# ============================================================
# SUMMARY:
# - Strings are text inside quotes: "Hello" or 'Hello'
# - Index starts at 0. Use [] to get one character.
# - Slicing: string[start:stop] to get a portion
# - Methods: .upper(), .lower(), .strip(), .replace(), .split()
# - f-strings: f"Hello {name}" → clean way to embed variables
# - .find(), .count(), .startswith(), .endswith() to search
# - 'in' keyword to check if something exists in the string
# ============================================================
