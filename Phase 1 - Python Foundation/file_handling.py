# ============================================================
# FILE: file_handling.py
# TOPIC: File Handling in Python
# ============================================================
# Files let you SAVE data permanently on your computer.
# When a program runs, variables are lost when it stops.
# Files solve this problem - data written to a file stays there!
#
# In this file you will learn:
#   1. Opening and closing files
#   2. Writing to a file (creates or overwrites)
#   3. Appending to a file (adds without erasing)
#   4. Reading from a file
#   5. The 'with' statement (best practice)
#   6. Working with file paths
#   7. Checking if a file exists
#   8. Writing/reading structured data (CSV-style)
#   9. Real-life example
# ============================================================

import os   # We use 'os' to check if files exist and delete them


# ---------------------------------------------------------
# SECTION 1: FILE MODES
# ---------------------------------------------------------
# When you open a file, you specify a MODE:
#
#   "r"  = READ only (default). Error if file doesn't exist.
#   "w"  = WRITE. Creates file if needed. ERASES existing content!
#   "a"  = APPEND. Creates file if needed. Adds to the END.
#   "x"  = CREATE. Creates file. Error if it already exists.
#   "r+" = Read AND Write (file must exist).
#
# Add 'b' for binary files (e.g., images): "rb", "wb"

print("--- File Modes Overview ---")
print("r  = Read     (default, file must exist)")
print("w  = Write    (creates/overwrites file)")
print("a  = Append   (adds to end of file)")
print("x  = Create   (only if file doesn't exist)")


# ---------------------------------------------------------
# SECTION 2: WRITING TO A FILE
# ---------------------------------------------------------
# Use mode "w" to WRITE.
# WARNING: "w" will DELETE any existing content in the file!

print("\n--- Section 2: Writing to a File ---")

# Method 1: open() and close() manually
file = open("notes.txt", "w")        # Open for writing
file.write("Hello! This is my first file.\n")   # \n = new line
file.write("Python file handling is easy.\n")
file.write("Learning is fun!\n")
file.close()                           # IMPORTANT: always close the file!

print("File 'notes.txt' has been written successfully.")


# ---------------------------------------------------------
# SECTION 3: THE 'with' STATEMENT (Best Practice)
# ---------------------------------------------------------
# The 'with' statement automatically closes the file for you,
# even if an error occurs. This is the RECOMMENDED way.
# No need to call .close() manually!

print("\n--- Section 3: Using 'with' Statement (Best Practice) ---")

with open("students.txt", "w") as f:  # 'f' is the file object
    f.write("Name, Age, Grade\n")     # Header line
    f.write("Noman, 22, A\n")
    f.write("Ali, 19, B\n")
    f.write("Sara, 21, A+\n")
    f.write("Rahim, 20, C\n")
    # File is automatically closed here when 'with' block ends!

print("File 'students.txt' written with 'with' statement.")


# ---------------------------------------------------------
# SECTION 4: WRITING A LIST OF LINES
# ---------------------------------------------------------
# .writelines() writes a list of strings all at once.

print("\n--- Section 4: writelines() ---")

lines = [
    "Python is powerful.\n",
    "It is used in AI and Data Science.\n",
    "Let's keep learning!\n"
]

with open("facts.txt", "w") as f:
    f.writelines(lines)    # Write all lines at once

print("File 'facts.txt' written using writelines().")


# ---------------------------------------------------------
# SECTION 5: READING A FILE
# ---------------------------------------------------------
# There are 3 ways to READ a file:
#
#   .read()       -> reads the ENTIRE file as one big string
#   .readline()   -> reads ONE line at a time
#   .readlines()  -> reads ALL lines into a LIST

print("\n--- Section 5: Reading a File ---")

# --- .read() - Read entire file ---
print("\n[.read()] Entire contents of notes.txt:")
with open("notes.txt", "r") as f:
    content = f.read()   # Reads everything as one string
    print(content)

# --- .readline() - Read one line at a time ---
print("[.readline()] Reading one line at a time from notes.txt:")
with open("notes.txt", "r") as f:
    line1 = f.readline()   # First call reads line 1
    line2 = f.readline()   # Second call reads line 2
    print("Line 1:", line1.strip())  # .strip() removes the \n at end
    print("Line 2:", line2.strip())

# --- .readlines() - Read all lines into a list ---
print("\n[.readlines()] All lines as a list from students.txt:")
with open("students.txt", "r") as f:
    all_lines = f.readlines()   # Returns a list like ["line1\n", "line2\n"]
    for line in all_lines:
        print("-", line.strip())  # strip() removes \n from each line


# ---------------------------------------------------------
# SECTION 6: LOOPING THROUGH A FILE (Best Way to Read)
# ---------------------------------------------------------
# The most memory-efficient way to read a file is to loop
# through the file object directly (no need for readlines()).

print("\n--- Section 6: Looping Through a File ---")

print("Contents of facts.txt:")
with open("facts.txt", "r") as f:
    for line in f:              # Python reads one line at a time
        print(" >", line.strip())


# ---------------------------------------------------------
# SECTION 7: APPENDING TO A FILE (Adding Without Erasing)
# ---------------------------------------------------------
# Mode "a" adds new content to the END of the file.
# Existing content is preserved (unlike "w" which erases it)!

print("\n--- Section 7: Appending to a File ---")

print("Before appending, notes.txt contains:")
with open("notes.txt", "r") as f:
    print(f.read())

with open("notes.txt", "a") as f:   # Open in APPEND mode
    f.write("This line was added later!\n")
    f.write("Appending keeps existing content.\n")

print("After appending, notes.txt contains:")
with open("notes.txt", "r") as f:
    print(f.read())


# ---------------------------------------------------------
# SECTION 8: CHECKING IF A FILE EXISTS
# ---------------------------------------------------------
# Before reading a file, it's good practice to check if it exists.
# Use os.path.exists() to check.

print("\n--- Section 8: Checking File Existence ---")

if os.path.exists("notes.txt"):
    print("notes.txt EXISTS.")
else:
    print("notes.txt does NOT exist.")

if os.path.exists("nonexistent.txt"):
    print("nonexistent.txt EXISTS.")
else:
    print("nonexistent.txt does NOT exist.")

# Safe reading (check first, then read):
filename = "students.txt"
if os.path.exists(filename):
    with open(filename, "r") as f:
        print(f"\nContents of {filename}:")
        for line in f:
            print(" ", line.strip())
else:
    print(f"{filename} was not found. Cannot read.")


# ---------------------------------------------------------
# SECTION 9: FileNotFoundError Handling
# ---------------------------------------------------------
# Even better than os.path.exists() is using try/except
# to handle the error directly.

print("\n--- Section 9: Handle FileNotFoundError ---")

try:
    with open("missing_file.txt", "r") as f:
        content = f.read()
except FileNotFoundError:
    print("Error: 'missing_file.txt' was not found on disk.")
except PermissionError:
    print("Error: You don't have permission to read that file.")
else:
    print("File read successfully!")
    print(content)


# ---------------------------------------------------------
# REAL LIFE EXAMPLE: Simple Student Grade Logger
# ---------------------------------------------------------
print("\n--- Real Life Example: Grade Logger ---")

def save_grade(name, subject, mark):
    """Saves a student's grade to a file."""
    with open("grades.txt", "a") as f:
        grade = "Pass" if mark >= 50 else "Fail"
        f.write(f"{name},{subject},{mark},{grade}\n")
    print(f"  Saved: {name} | {subject} | {mark} | {grade}")

def show_all_grades():
    """Reads and displays all saved grades."""
    print("  --- All Saved Grades ---")
    if not os.path.exists("grades.txt"):
        print("  No grades saved yet.")
        return
    with open("grades.txt", "r") as f:
        for line in f:
            parts = line.strip().split(",")
            print(f"  Name: {parts[0]:<10} | Subject: {parts[1]:<10} | Mark: {parts[2]:<5} | Result: {parts[3]}")

# Save some grades:
print("Saving grades...")
save_grade("Noman", "Math",    92)
save_grade("Ali",   "Science", 45)
save_grade("Sara",  "English", 78)
save_grade("Noman", "Science", 85)

# Read and display all saved grades:
print()
show_all_grades()


# ---------------------------------------------------------
# CLEANUP: Remove test files (so re-running the script is clean)
# ---------------------------------------------------------
print("\n--- Cleaning up test files ---")
for filename in ["notes.txt", "students.txt", "facts.txt", "grades.txt"]:
    if os.path.exists(filename):
        os.remove(filename)
        print(f"  Deleted: {filename}")

# ============================================================
# SUMMARY:
# - open("file.txt", mode) -> opens a file
# - Modes: 'r'(read), 'w'(write/overwrite), 'a'(append), 'x'(create)
# - Always use 'with open(...)' -> auto-closes file for you
# - .read()       -> entire file as string
# - .readline()   -> one line at a time
# - .readlines()  -> all lines as a list
# - for line in f -> most efficient way to loop through file
# - .write("text") -> write a string to file
# - .writelines([]) -> write a list of strings
# - os.path.exists("file") -> check if file exists
# - Use try/except FileNotFoundError for safe reading
# ============================================================
