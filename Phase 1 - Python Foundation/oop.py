# ============================================================
# FILE: oop.py
# TOPIC: Object-Oriented Programming (OOP) Basics
# ============================================================
# OOP is a way of writing code that models real-world things.
# Instead of just writing step-by-step instructions, we create
# "blueprints" (called Classes) that describe objects.
#
# Think of it like this:
#   - A CLASS is a blueprint (like an architectural plan for a house)
#   - An OBJECT is a real thing built from the blueprint (the actual house)
#   - You can build MANY houses from ONE blueprint!
#
# In this file you will learn:
#   1. What is a class and how to define one
#   2. What is the __init__ method (constructor)
#   3. What is the 'self' keyword
#   4. Instance attributes (data stored in an object)
#   5. Instance methods (actions an object can perform)
#   6. Creating and using objects
#   7. Real-life example
# ============================================================


# ---------------------------------------------------------
# SECTION 1: DEFINING A CLASS
# ---------------------------------------------------------
# Use the 'class' keyword, then the class name (by convention,
# class names start with a Capital Letter), then a colon :.
# Everything inside the class is indented.

print("--- Section 1: Defining a Class ---")

class Dog:
    # This is the simplest possible class.
    # It currently has no data or behavior.
    pass  # 'pass' means: this block is intentionally empty

# Even like this, we can create Dog 'objects':
my_dog = Dog()
print("Created a dog object:", my_dog)
print("Type:", type(my_dog))  # <class '__main__.Dog'>


# ---------------------------------------------------------
# SECTION 2: __init__ METHOD (The Constructor)
# ---------------------------------------------------------
# __init__ is a special method that runs AUTOMATICALLY whenever
# you create a new object from the class.
# It is used to give the object its starting data (attributes).
#
# Think of __init__ as the "setup" step when you build a new object.
#
# 'self' refers to the CURRENT OBJECT being created.
# Always pass 'self' as the first parameter in every method.

print("\n--- Section 2: __init__ Method ---")

class Student:

    def __init__(self, name, age, department):
        # This method is called automatically when you do: Student(...)
        # It stores the given values inside the object.
        self.name       = name        # Store 'name' in the object
        self.age        = age         # Store 'age' in the object
        self.department = department  # Store 'department' in the object
        print(f"  --> A new Student object created: {self.name}")

# Creating objects (instances) from the Student class:
# Python automatically calls __init__ when you do this:
student1 = Student("Noman", 22, "Software Engineering")
student2 = Student("Ali",   19, "Computer Science")
student3 = Student("Sara",  21, "Data Science")


# ---------------------------------------------------------
# SECTION 3: ACCESSING ATTRIBUTES
# ---------------------------------------------------------
# After creating an object, access its stored data using a dot (.)
# Syntax: object.attribute_name

print("\n--- Section 3: Accessing Attributes ---")
print("Name:",       student1.name)        # Noman
print("Age:",        student1.age)         # 22
print("Department:", student1.department)  # Software Engineering

print()
print("Name:",       student2.name)        # Ali
print("Age:",        student2.age)         # 19

# Each object has its OWN copy of the attributes.
# Changing student1's data does NOT affect student2.
student1.age = 23    # Update student1's age
print("\nAfter update:")
print("student1 age:", student1.age)  # 23
print("student2 age:", student2.age)  # 19 (unchanged)


# ---------------------------------------------------------
# SECTION 4: INSTANCE METHODS (Actions Objects Can Do)
# ---------------------------------------------------------
# A method is a function that belongs to a class.
# It always has 'self' as the first parameter.
# Methods define what an object CAN DO.

print("\n--- Section 4: Instance Methods ---")

class BankAccount:

    def __init__(self, owner, balance=0):
        """Set up the bank account with an owner and starting balance."""
        self.owner   = owner
        self.balance = balance
        print(f"Account created for {self.owner} with balance: ${self.balance}")

    def deposit(self, amount):
        """Add money to the account."""
        if amount > 0:
            self.balance += amount   # Add to balance
            print(f"  Deposited ${amount}. New balance: ${self.balance}")
        else:
            print("  Deposit amount must be positive!")

    def withdraw(self, amount):
        """Remove money from the account."""
        if amount > self.balance:
            print(f"  Not enough funds! Balance is only ${self.balance}.")
        elif amount <= 0:
            print("  Withdrawal amount must be positive!")
        else:
            self.balance -= amount   # Subtract from balance
            print(f"  Withdrew ${amount}. New balance: ${self.balance}")

    def show_balance(self):
        """Display the current balance."""
        print(f"  [{self.owner}] Current balance: ${self.balance}")

# Create a BankAccount object:
account = BankAccount("Noman", 1000)

# Call methods on the object using dot notation:
account.show_balance()
account.deposit(500)
account.withdraw(200)
account.withdraw(2000)   # Should fail (not enough funds)
account.show_balance()


# ---------------------------------------------------------
# SECTION 5: THE __str__ METHOD (String Representation)
# ---------------------------------------------------------
# __str__ is another special method that controls what happens
# when you print() an object. Without it, you get an ugly
# memory address. With it, you get a nice, readable description.

print("\n--- Section 5: __str__ Method ---")

class Book:

    def __init__(self, title, author, pages):
        self.title  = title
        self.author = author
        self.pages  = pages

    def __str__(self):
        # This is called automatically when you use print(object)
        return f"'{self.title}' by {self.author} ({self.pages} pages)"

    def is_long_book(self):
        """Returns True if the book has more than 300 pages."""
        return self.pages > 300

book1 = Book("Python Crash Course", "Eric Matthes", 544)
book2 = Book("The Alchemist",       "Paulo Coelho", 197)

print(book1)                        # Uses __str__ automatically
print(book2)
print("Is book1 long?", book1.is_long_book())  # True
print("Is book2 long?", book2.is_long_book())  # False


# ---------------------------------------------------------
# REAL LIFE EXAMPLE: Student Report Card
# ---------------------------------------------------------
print("\n--- Real Life Example: Student Report Card ---")

class StudentReport:

    def __init__(self, name, marks_list):
        """Create a student report with a name and a list of marks."""
        self.name       = name
        self.marks_list = marks_list  # e.g., [85, 90, 72, 68]

    def get_total(self):
        """Returns the sum of all marks."""
        return sum(self.marks_list)

    def get_average(self):
        """Returns the average mark."""
        return self.get_total() / len(self.marks_list)

    def get_grade(self):
        """Returns a letter grade based on average."""
        avg = self.get_average()
        if avg >= 90:   return "A+"
        elif avg >= 80: return "A"
        elif avg >= 70: return "B"
        elif avg >= 60: return "C"
        else:           return "F"

    def print_report(self):
        """Prints a formatted report card."""
        print(f"  Student:  {self.name}")
        print(f"  Marks:    {self.marks_list}")
        print(f"  Total:    {self.get_total()}")
        print(f"  Average:  {self.get_average():.1f}")
        print(f"  Grade:    {self.get_grade()}")
        print()

# Create student report objects:
report1 = StudentReport("Noman", [92, 88, 95, 85])
report2 = StudentReport("Ali",   [65, 70, 60, 55])
report3 = StudentReport("Sara",  [78, 82, 79, 88])

print("=== REPORT CARDS ===")
report1.print_report()
report2.print_report()
report3.print_report()

# ============================================================
# SUMMARY:
# - class ClassName:   → defines a blueprint
# - __init__(self, ...) → runs automatically when object is created
# - self.attribute      → stores data inside the object
# - def method(self):  → defines what the object can do
# - object = ClassName(args) → creates a new object (instance)
# - object.attribute   → reads stored data
# - object.method()    → calls an action
# - __str__(self)      → controls what print(object) shows
# ============================================================
