# ============================================================
# FILE: dictionary.py
# TOPIC: Dictionaries in Python
# ============================================================
# A dictionary stores data as KEY : VALUE pairs.
# Think of it like a real dictionary:
#   Key   = the word you look up (e.g., "capital")
#   Value = the definition      (e.g., "Dhaka")
#
# Real-life example: A student profile has a name, age, GPA —
# instead of 3 separate variables, store them all in ONE dictionary.
#
# In this file you will learn:
#   1. Creating a dictionary
#   2. Accessing values
#   3. Safe access with .get()
#   4. Adding and changing values
#   5. Removing items
#   6. Looping through a dictionary
#   7. Checking if a key exists
#   8. Useful dictionary methods
#   9. Nested dictionaries
#  10. Real-life examples
# ============================================================


# ---------------------------------------------------------
# SECTION 1: CREATING A DICTIONARY
# ---------------------------------------------------------
# Use curly braces {} and separate key-value pairs with colons :.
# Multiple pairs are separated by commas.
# Keys are usually strings. Values can be ANYTHING.

print("--- Creating a Dictionary ---")

student = {
    "name": "Noman",             # Key: "name",  Value: "Noman"
    "age": 22,                    # Key: "age",   Value: 22
    "cgpa": 3.7,                  # Key: "cgpa",  Value: 3.7
    "active": True                # Key: "active", Value: True
}

print(student)   # Prints the whole dictionary
print("Type:", type(student))   # <class 'dict'>


# ---------------------------------------------------------
# SECTION 2: ACCESSING VALUES
# ---------------------------------------------------------
# Use the KEY inside square brackets [] to get the value.
# IMPORTANT: If the key doesn't exist, this causes an ERROR.

print("\n--- Accessing Values ---")
print("Name:", student["name"])     # Noman
print("Age:",  student["age"])      # 22
print("CGPA:", student["cgpa"])     # 3.7

# print(student["email"])  # This would cause a KeyError!


# ---------------------------------------------------------
# SECTION 3: SAFE ACCESS WITH .get()
# ---------------------------------------------------------
# .get(key) is SAFER than [key] because:
# - If the key exists, it returns the value.
# - If the key does NOT exist, it returns None (no error!).
# - You can also set a default: .get(key, default_value)

print("\n--- Safe Access with .get() ---")
print(student.get("name"))             # Noman
print(student.get("email"))            # None (key doesn't exist, no crash)
print(student.get("email", "No email provided"))  # Default value shown


# ---------------------------------------------------------
# SECTION 4: ADDING AND CHANGING VALUES
# ---------------------------------------------------------
# To ADD a new key-value: student["new_key"] = value
# To CHANGE an existing value: student["existing_key"] = new_value
# Python checks if the key exists: if yes, update; if no, add.

print("\n--- Adding and Changing Values ---")
print("Before:", student)

student["age"] = 23                        # CHANGE: update age from 22 to 23
student["department"] = "Software Eng"     # ADD: new key-value pair
student["email"] = "noman@example.com"     # ADD: another new pair

print("After changes:", student)


# ---------------------------------------------------------
# SECTION 5: REMOVING ITEMS
# ---------------------------------------------------------

print("\n--- Removing Items ---")

# .pop(key) → removes the item with that key, returns the value
removed_value = student.pop("active")
print(f"Removed 'active' key. Value was: {removed_value}")
print("After pop:", student)

# del keyword → deletes a key-value pair
del student["email"]
print("After del 'email':", student)

# .clear() → removes ALL items (empties the dictionary)
temp_dict = {"a": 1, "b": 2}
temp_dict.clear()
print("After .clear():", temp_dict)   # {}


# ---------------------------------------------------------
# SECTION 6: LOOPING THROUGH A DICTIONARY
# ---------------------------------------------------------
# There are 3 ways to loop through a dictionary.

print("\n--- Looping Through a Dictionary ---")
student = {"name": "Noman", "age": 22, "cgpa": 3.7, "dept": "SE"}

# Method 1: Loop through KEYS only (default behavior)
print("Keys only:")
for key in student:
    print(" ", key)

# Method 2: Loop through VALUES only
print("Values only:")
for value in student.values():
    print(" ", value)

# Method 3: Loop through KEY + VALUE pairs (most useful!)
print("Keys and Values:")
for key, value in student.items():
    print(f"  {key}: {value}")


# ---------------------------------------------------------
# SECTION 7: CHECKING IF A KEY EXISTS
# ---------------------------------------------------------

print("\n--- Checking if a Key Exists ---")

if "name" in student:
    print("'name' key exists! Value:", student["name"])

if "email" not in student:
    print("'email' key does NOT exist in the dictionary.")


# ---------------------------------------------------------
# SECTION 8: USEFUL DICTIONARY METHODS
# ---------------------------------------------------------

print("\n--- Useful Dictionary Methods ---")
profile = {"name": "Ali", "age": 25, "city": "Dhaka"}

print("All keys:    ", list(profile.keys()))    # List of all keys
print("All values:  ", list(profile.values()))  # List of all values
print("All items:   ", list(profile.items()))   # List of (key, value) tuples
print("Total items: ", len(profile))             # Number of key-value pairs

# .update() → merges another dictionary into this one
extra_info = {"job": "Developer", "age": 26}   # 'age' will override!
profile.update(extra_info)
print("After .update():", profile)


# ---------------------------------------------------------
# SECTION 9: NESTED DICTIONARY (Dictionary inside Dictionary)
# ---------------------------------------------------------
# A value can itself be a dictionary. This lets you model
# complex, real-world data structures.

print("\n--- Nested Dictionary ---")
company = {
    "name": "TechCorp",
    "address": {
        "city": "Dhaka",
        "country": "Bangladesh",
        "zip": "1200"
    },
    "employees": 150
}

print("Company:",        company["name"])
print("City:",           company["address"]["city"])      # Accessing nested value
print("Country:",        company["address"]["country"])
print("Employees:",      company["employees"])


# ---------------------------------------------------------
# SECTION 10: DICTIONARY INSIDE A LIST (Very Important!)
# ---------------------------------------------------------
# In real projects, you often have a LIST of dictionaries.
# Each dictionary represents one record (like one row in a table).

print("\n--- List of Dictionaries ---")
students = [
    {"name": "Noman", "cgpa": 3.7},
    {"name": "Ali",   "cgpa": 3.2},
    {"name": "Rahim", "cgpa": 2.9}
]

# Print all students
print("All students:")
for s in students:
    print(f"  {s['name']}: CGPA {s['cgpa']}")

# Only print students with CGPA >= 3.5 (Honor Roll)
print("Honor Roll students (CGPA >= 3.5):")
for s in students:
    if s["cgpa"] >= 3.5:
        print(" ", s["name"])


# ---------------------------------------------------------
# REAL LIFE EXAMPLE: Simple Login System
# ---------------------------------------------------------
print("\n--- Real Life Example: Login System ---")

# The dictionary stores username: password pairs
users = {
    "noman": "1234",
    "admin": "admin123",
    "ali": "pass456"
}

username = input("Enter username: ")
password = input("Enter password: ")

# Check: does username exist AND does the password match?
if username in users and users[username] == password:
    print(f"Welcome, {username}! Login successful.")
else:
    print("Invalid username or password. Please try again.")

# ============================================================
# SUMMARY:
# - Dictionary: {"key": value} → stores data as key-value pairs
# - Access: dict["key"] or .get("key") (safer)
# - Add/Change: dict["key"] = value
# - Remove: .pop("key") or del dict["key"]
# - Loop: keys, .values(), .items()
# - Check: "key" in dict
# - Nested: a value can be another dictionary
# - Real use: JSON data, records, user profiles, settings
# ============================================================
