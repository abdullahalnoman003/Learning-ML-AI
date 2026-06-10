#  Phase 1: Python Foundations — Detailed Guide

> Python is the #1 language for AI and Machine Learning.  
> Master this phase before moving to data science or ML libraries.

---



##  Topics Covered (With File References)

---

### 1. Hello World & Print Basics
 File: `first.py`

**What you learned:**
- How Python executes code line by line
- The `print()` function
- Running your first Python program

**Key concept:**
```python
print("Hello World!")   # This outputs text to the screen
```

---

### 2. Variables, Data Types & Input
 File: `basics.py`

**What you learned:**
- Variables store data (Python auto-detects the type)
- Core data types: `str`, `int`, `float`, `bool`
- Taking input from user with `input()`
- Typecasting: converting one type to another

**Key concept:**
```python
name = "Noman"          # str  → text
age = 22                # int  → whole number
cgpa = 3.92             # float → decimal
active = True           # bool → True/False

# Input always returns string — must typecast if needed
cgpa = float(input("Enter CGPA: "))

# Check type of any variable
print(type(name))       # <class 'str'>
```

**Why this matters for ML:**
> Data types are critical in ML. An image pixel is a `float`, a label is an `int`, a category is a `str`. Getting types wrong causes bugs in models.

---

### 3. Conditional Statements
 File: `IfElse.py`

**What you learned:**
- `if`, `elif`, `else` to make decisions
- Combine conditions with `and`, `or`, `not`

**Key concept:**
```python
if age >= 18:
    print("Adult")
elif age >= 13:
    print("Teenager")
else:
    print("Child")
```

**Why this matters for ML:**
> Conditions are used everywhere — thresholding predictions, splitting datasets, checking model accuracy.

---

### 4. Loops
 File: `loop.py`

**What you learned:**
- `for` loop: iterate a fixed number of times
- `range(start, stop, step)` controls the loop
- `while` loop: runs until a condition is False
- `break` to exit, `continue` to skip

**Key concept:**
```python
# for loop
for i in range(0, 10, 2):    # 0, 2, 4, 6, 8
    print(i)

# while loop
while condition:
    # do something
    break     # exit when done
```

**Why this matters for ML:**
> Training a neural network = running a loop thousands of times (called **epochs**). Every ML training loop uses these concepts.

---

### 5. Functions
 File: `functions.py`

**What you learned:**
- Define reusable blocks of code with `def`
- Pass data using **parameters**
- Call a function multiple times

**Key concept:**
```python
def add(a, b):
    print(a + b)

add(10, 20)    # Output: 30
add(5, 7)      # Output: 12
```

**Why this matters for ML:**
> Every ML pipeline is a chain of functions: `load_data()`, `preprocess()`, `train_model()`, `evaluate()`. Functions keep code clean and reusable.

---

### 6. Lists
 File: `list.py`

**What you learned:**
- Lists store multiple values in order
- Access by index (starts at 0)
- Negative indexing (`-1` = last item)
- Loop through lists
- Modify, add (`append`), remove items

**Key concept:**
```python
numbers = [10, 20, 30, 40, 50]

print(numbers[0])     # 10  (first)
print(numbers[-1])    # 50  (last)

numbers.append(60)    # Add to end
numbers.remove(10)    # Remove value

for num in numbers:
    print(num)
```

**Why this matters for ML:**
> Datasets are lists of data points. Features of each sample are stored in lists/arrays. NumPy arrays (Phase 2) are powered lists.

---

### 7. Tuples & Sets
 File: `touple.py`

**What you learned:**
- **Tuple**: ordered, **immutable** (cannot change after creation)
- **Set**: unordered, **unique values only**, no duplicates

**Key concept:**
```python
# Tuple — fixed, cannot change
colors = ("red", "green", "blue")
print(colors[0])    # red

# Set — unique values only
nums = {1, 2, 2, 3, 3, 4}
print(nums)         # {1, 2, 3, 4}  — duplicates removed
```

**Why this matters for ML:**
> Tuples are used for fixed configurations (e.g., image shape `(224, 224, 3)`). Sets are used to find unique class labels in a dataset.

---

### 8. Dictionaries
 File: `dictionary.py`

**What you learned:**
- Key → Value pairs (like JSON)
- Access values by key
- Safe access with `.get()`
- Add, update, delete keys
- Loop through keys and values

**Key concept:**
```python
student = {
    "name": "Noman",
    "age": 22,
    "cgpa": 3.7
}

print(student["name"])         # Noman
print(student.get("email"))    # None (no error)
student["department"] = "SE"   # Add new key

for key, value in student.items():
    print(key, ":", value)
```

**Why this matters for ML:**
> Model configuration, hyperparameters, class labels — all stored as dictionaries. JSON APIs return dictionaries.

---

##  Topics Remaining in Phase 1

---

### 9. String Methods ← **Do This Next**
 File to create: `strings.py`

**What to learn:**
- String slicing, indexing
- `.upper()`, `.lower()`, `.strip()`, `.split()`, `.replace()`
- f-strings for clean formatting: `f"Hello {name}"`
- String checking: `.startswith()`, `.endswith()`, `.find()`

**Practice goal:**
```python
name = "  Abdullah Al Noman  "
print(name.strip())             # "Abdullah Al Noman"
print(name.strip().upper())     # "ABDULLAH AL NOMAN"
print(f"My name is {name.strip()}, I am {age} years old.")
```

---

### 10. Advanced Functions
 File to create: `functions_advanced.py`

**What to learn:**
- `return` — getting values back from functions
- Default parameter values
- `*args` — accept any number of arguments
- `**kwargs` — accept keyword arguments
- Lambda functions (anonymous, one-line functions)

**Practice goal:**
```python
def multiply(a, b=2):     # default parameter
    return a * b

square = lambda x: x ** 2   # lambda function
print(square(5))             # 25
```

---

### 11. List Comprehension
 File to create: `list_comprehension.py`

**What to learn:**
- Shorter way to create lists
- `map()`, `filter()` functions
- Dictionary comprehension

**Practice goal:**
```python
# Traditional way
squares = []
for x in range(10):
    squares.append(x ** 2)

# List comprehension way
squares = [x ** 2 for x in range(10)]

# Filter — only even numbers
evens = [x for x in range(20) if x % 2 == 0]
```

**Why this matters for ML:**
> NumPy and Pandas use these patterns everywhere. Knowing comprehensions makes ML code much cleaner.

---

### 12. File Handling
 File to create: `file_handling.py`

**What to learn:**
- Write data to a file
- Read data back from a file
- Using `with` statement (auto-closes file)
- Modes: `"r"` read, `"w"` write, `"a"` append

**Practice goal:**
```python
# Write to file
with open("data.txt", "w") as f:
    f.write("Name: Noman\nCGPA: 3.92")

# Read from file
with open("data.txt", "r") as f:
    content = f.read()
    print(content)
```

**Why this matters for ML:**
> ML datasets are files (CSV, JSON, images). Saving/loading model weights = file handling. Logging training progress = writing to files.

---

### 13. Error Handling
 File to create: `error_handling.py`

**What to learn:**
- `try` / `except` — catch and handle errors
- `finally` — runs no matter what
- Common errors: `ValueError`, `TypeError`, `FileNotFoundError`
- Raising custom errors with `raise`

**Practice goal:**
```python
try:
    age = int(input("Enter age: "))
    print(f"Age: {age}")
except ValueError:
    print("That's not a number!")
finally:
    print("Program finished.")
```

**Why this matters for ML:**
> Real-world datasets have bad data. Models can crash mid-training. Error handling keeps your pipeline running and gives useful error messages.

---

### 14. OOP Basics (Classes & Objects)
 File to create: `oop.py`

**What to learn:**
- What is a class? What is an object?
- `__init__` method (constructor)
- Instance methods
- `self` keyword

**Practice goal:**
```python
class Student:
    def __init__(self, name, cgpa):
        self.name = name
        self.cgpa = cgpa

    def display(self):
        print(f"{self.name} — CGPA: {self.cgpa}")

s1 = Student("Noman", 3.92)
s1.display()
```

**Why this matters for ML:**
> PyTorch models are classes. Scikit-learn estimators are classes. Every advanced ML tool uses OOP. This is critical.

---

### 15. OOP Advanced
 File to create: `oop_advanced.py`

**What to learn:**
- **Inheritance** — one class extends another
- **Polymorphism** — same method, different behavior
- **Encapsulation** — private attributes
- `super()` to call parent class

**Practice goal:**
```python
class Animal:
    def speak(self):
        print("...")

class Dog(Animal):
    def speak(self):   # Overrides parent
        print("Woof!")

d = Dog()
d.speak()   # Woof!
```

---

### 16. Modules & Imports
 File to create: `modules.py`

**What to learn:**
- `import` built-in modules: `math`, `random`, `os`, `datetime`
- Import specific functions: `from math import sqrt`
- Create and import your own module
- Introduction to `pip` and external packages

**Practice goal:**
```python
import math
import random

print(math.sqrt(144))           # 12.0
print(random.randint(1, 100))   # random number
print(math.pi)                  # 3.14159...
```

---

##  Phase 1 Mini-Project: Student Grade Calculator

**Build this after completing all Phase 1 topics:**

**Features to implement:**
1. Input multiple student names and marks
2. Calculate average, grade (A/B/C/F)
3. Store all data in a dictionary
4. Save results to a file (`results.txt`)
5. Handle invalid input with error handling
6. Use a `Student` class (OOP)

**Skills it will use:**
- Variables, data types, input
- Conditionals (grade logic)
- Loops (multiple students)
- Functions (calculate_grade, display_result)
- Dictionaries (student data)
- File handling (save results)
- Error handling (bad input)
- OOP (Student class)

---

##  Common Mistakes to Avoid

| Mistake | Fix |
|---------|-----|
| Forgetting indentation | Python uses spaces — always indent inside functions, loops, if/else |
| Using `=` instead of `==` in conditions | `=` assigns, `==` compares |
| Not typecasting `input()` | `input()` always returns string — cast to `int()` or `float()` when needed |
| Mutable default arguments in functions | Never use `def f(data=[])` — use `def f(data=None)` |
| Off-by-one in `range()` | `range(1, 10)` gives 1 to 9, NOT 10 |

---

*Go to [LEARNING_PATH.md](../LEARNING_PATH.md) for the complete AI/ML roadmap.*
