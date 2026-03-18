# ============================================================
# FILE: oop_advanced.py
# TOPIC: Advanced OOP - Inheritance, Polymorphism, Encapsulation
# ============================================================
# You already know the basics of classes and objects (oop.py).
# Now let's learn the ADVANCED concepts that are widely used
# in professional software development!
#
# In this file you will learn:
#   1. Inheritance (child class inherits from parent class)
#   2. super() - to call the parent class's methods
#   3. Polymorphism (same method name, different behavior)
#   4. Encapsulation (hiding data with private attributes)
#   5. @property decorator (controlled access to attributes)
#   6. @staticmethod (method that doesn't need 'self')
#   7. @classmethod (method that works with the class itself)
# ============================================================


# ---------------------------------------------------------
# SECTION 1: INHERITANCE
# ---------------------------------------------------------
# Inheritance lets a CHILD class reuse all the code from a
# PARENT class, and then ADD or CHANGE whatever it needs.
#
# Real-life analogy:
# A child inherits traits from their parents (eye color, height),
# but can also have their own unique traits.
#
# Syntax: class ChildClass(ParentClass):

print("=" * 45)
print("SECTION 1: INHERITANCE")
print("=" * 45)

# ---- PARENT CLASS ----
class Animal:
    """This is the PARENT (base) class."""

    def __init__(self, name, species):
        self.name    = name     # Every animal has a name
        self.species = species  # Every animal has a species

    def speak(self):
        # A generic speak method - child classes will override this
        print(f"{self.name} makes a sound.")

    def describe(self):
        print(f"{self.name} is a {self.species}.")


# ---- CHILD CLASS: Dog ----
class Dog(Animal):     # Dog INHERITS from Animal
    """Dog extends Animal with dog-specific behavior."""

    def __init__(self, name, breed):
        # Call the PARENT's __init__ to set name and species:
        super().__init__(name, species="Dog")
        self.breed = breed  # Dog-specific attribute

    def speak(self):   # OVERRIDE the parent's speak method
        print(f"{self.name} says: Woof! Woof!")

    def fetch(self):   # NEW method specific to Dog
        print(f"{self.name} fetches the ball!")


# ---- CHILD CLASS: Cat ----
class Cat(Animal):     # Cat INHERITS from Animal
    """Cat extends Animal with cat-specific behavior."""

    def __init__(self, name, indoor):
        super().__init__(name, species="Cat")
        self.indoor = indoor   # Is the cat an indoor cat?

    def speak(self):   # OVERRIDE speak
        print(f"{self.name} says: Meow!")

    def purr(self):    # NEW method specific to Cat
        print(f"{self.name} purrs contentedly...")


# Testing inheritance:
dog = Dog("Rex", "German Shepherd")
cat = Cat("Whiskers", indoor=True)

print("\n--- Dog ---")
dog.describe()    # From Animal (INHERITED — didn't need to rewrite it!)
dog.speak()       # From Dog (OVERRIDDEN)
dog.fetch()       # Dog-specific
print("Breed:", dog.breed)

print("\n--- Cat ---")
cat.describe()    # From Animal (INHERITED)
cat.speak()       # From Cat (OVERRIDDEN)
cat.purr()        # Cat-specific
print("Indoor cat?", cat.indoor)

# isinstance() checks if an object is from a class (or subclass):
print()
print("Is dog a Dog?",    isinstance(dog, Dog))     # True
print("Is dog an Animal?",isinstance(dog, Animal))  # True  <- inheritance!
print("Is dog a Cat?",    isinstance(dog, Cat))     # False


# ---------------------------------------------------------
# SECTION 2: super() - CALLING THE PARENT CLASS
# ---------------------------------------------------------
# super() lets you access methods from the PARENT class.
# Most commonly used in __init__ to run the parent's setup
# before adding the child's own setup.

print("\n" + "=" * 45)
print("SECTION 2: super()")
print("=" * 45)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age  = age
        print(f"  Person created: {self.name}")

    def greet(self):
        print(f"  Hi, I'm {self.name} and I'm {self.age} years old.")


class Employee(Person):
    def __init__(self, name, age, company, salary):
        super().__init__(name, age)   # Run Person's __init__ first!
        self.company = company         # Then add Employee-specific data
        self.salary  = salary
        print(f"  Employee created: {self.name} at {self.company}")

    def greet(self):                   # Override + extend parent's greet
        super().greet()                # Call parent's greet first
        print(f"  I work at {self.company} and earn ${self.salary}/month.")


emp = Employee("Noman", 22, "TechCorp", 50000)
print()
emp.greet()


# ---------------------------------------------------------
# SECTION 3: POLYMORPHISM
# ---------------------------------------------------------
# Polymorphism = "many forms".
# Different classes can have methods with the SAME NAME but
# DIFFERENT behavior.
#
# This is powerful because you can write ONE loop that works
# for ALL the different types without knowing which type it is.

print("\n" + "=" * 45)
print("SECTION 3: POLYMORPHISM")
print("=" * 45)

class Shape:
    def area(self):
        return 0  # Default (base class)

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        import math
        return math.pi * self.radius ** 2   # Area = pi * r^2

    def __str__(self):
        return f"Circle(radius={self.radius})"

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width  = width
        self.height = height

    def area(self):
        return self.width * self.height      # Area = width * height

    def __str__(self):
        return f"Rectangle({self.width}x{self.height})"

class Triangle(Shape):
    def __init__(self, base, height):
        self.base   = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height  # Area = 0.5 * base * height

    def __str__(self):
        return f"Triangle(base={self.base}, height={self.height})"


# Polymorphism in action:
# ALL shapes have an area() method, but each calculates it differently!
shapes = [
    Circle(5),
    Rectangle(4, 6),
    Triangle(3, 8)
]

print("\nAreas of all shapes:")
for shape in shapes:                     # ONE loop handles ALL shape types!
    print(f"  {shape}: area = {shape.area():.2f}")


# ---------------------------------------------------------
# SECTION 4: ENCAPSULATION (Protecting Data)
# ---------------------------------------------------------
# Encapsulation means hiding the internal details of an object
# and only exposing what's necessary.
#
# In Python, we use naming conventions:
#   _attribute  (single underscore)  = "protected" - use with care
#   __attribute (double underscore)  = "private"   - harder to access

print("\n" + "=" * 45)
print("SECTION 4: ENCAPSULATION")
print("=" * 45)

class SecureBankAccount:
    """A bank account with protected balance (encapsulation)."""

    def __init__(self, owner, initial_balance):
        self.owner = owner
        self.__balance = initial_balance   # __ makes it private!

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"  Deposited ${amount}. Balance: ${self.__balance}")

    def withdraw(self, amount):
        if amount > self.__balance:
            print("  Insufficient funds!")
        else:
            self.__balance -= amount
            print(f"  Withdrew ${amount}. Balance: ${self.__balance}")

    def get_balance(self):
        """The ONLY safe way to check the balance from outside."""
        return self.__balance


account = SecureBankAccount("Noman", 1000)
account.deposit(500)
account.withdraw(200)
print(f"  Current balance: ${account.get_balance()}")

# Trying to access __balance directly from outside won't work properly:
# print(account.__balance)  # AttributeError! Python protects it.
# This is the whole point of encapsulation - protect the data!


# ---------------------------------------------------------
# SECTION 5: @property (Smart Attribute Access)
# ---------------------------------------------------------
# @property lets you access a method LIKE an attribute.
# It's also used to add validation when setting a value.

print("\n" + "=" * 45)
print("SECTION 5: @property")
print("=" * 45)

class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name  = last_name
        self.__age = age      # Private

    @property
    def full_name(self):
        """Computed property - combines first and last name."""
        return f"{self.first_name} {self.last_name}"

    @property
    def age(self):
        """Getter - returns the private __age like a normal attribute."""
        return self.__age

    @age.setter
    def age(self, new_age):
        """Setter - validates the age before storing it."""
        if new_age < 0 or new_age > 150:
            print("  Invalid age! Age must be between 0 and 150.")
        else:
            self.__age = new_age
            print(f"  Age updated to {new_age}.")


p = Person("Abdullah", "Noman", 22)
print("Full name:", p.full_name)  # Accessed like attribute, not method()
print("Age:",       p.age)

p.age = 23       # Calls the setter
p.age = -5       # Setter catches the invalid value!
print("Age after attempted invalid update:", p.age)


# ---------------------------------------------------------
# SECTION 6: @staticmethod and @classmethod
# ---------------------------------------------------------
# @staticmethod:  A utility function inside a class that doesn't
#                 need 'self'. Could be a regular function, but
#                 logically belongs inside the class.
#
# @classmethod:   Works with the CLASS itself (not a specific object).
#                 Has 'cls' as first parameter instead of 'self'.
#                 Often used to create objects in alternative ways.

print("\n" + "=" * 45)
print("SECTION 6: @staticmethod and @classmethod")
print("=" * 45)

class MathHelper:

    PI = 3.14159    # class attribute (shared by all instances)

    @staticmethod
    def add(a, b):
        """A simple add function. Doesn't need the object."""
        return a + b

    @staticmethod
    def is_prime(n):
        """Checks whether a number is prime."""
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    @classmethod
    def circle_area(cls, radius):
        """Uses the class's PI attribute to compute circle area."""
        return cls.PI * radius * radius


# You can call static methods WITHOUT creating an object:
print("3 + 7 =", MathHelper.add(3, 7))
print("Is 17 prime?", MathHelper.is_prime(17))   # True
print("Is 18 prime?", MathHelper.is_prime(18))   # False

# classmethod uses the class itself:
print(f"Circle area (r=5): {MathHelper.circle_area(5):.2f}")


# ---------------------------------------------------------
# REAL LIFE EXAMPLE: Complete School System
# ---------------------------------------------------------
print("\n" + "=" * 45)
print("REAL LIFE EXAMPLE: School System")
print("=" * 45)

class SchoolMember:
    """Parent class for anyone in the school."""
    total_members = 0    # class variable: shared by ALL instances

    def __init__(self, name, age):
        self.name = name
        self.age  = age
        SchoolMember.total_members += 1
        print(f"  New member registered: {self.name}")

    def describe(self):
        print(f"  Name: {self.name} | Age: {self.age}")

    @classmethod
    def get_total(cls):
        print(f"  Total school members: {cls.total_members}")


class Teacher(SchoolMember):
    def __init__(self, name, age, subject, salary):
        super().__init__(name, age)
        self.subject = subject
        self.salary  = salary

    def describe(self):
        super().describe()
        print(f"  Subject: {self.subject} | Salary: ${self.salary}")


class Pupil(SchoolMember):
    def __init__(self, name, age, grade, tuition):
        super().__init__(name, age)
        self.grade   = grade
        self.tuition = tuition

    def describe(self):
        super().describe()
        print(f"  Grade: {self.grade} | Tuition: ${self.tuition}")


print("\nCreating school members:")
t1 = Teacher("Mr. Rahman", 40, "Mathematics", 5000)
t2 = Teacher("Ms. Faria",  35, "English",     4500)
s1 = Pupil("Noman",  22, "A", 2000)
s2 = Pupil("Ali",    19, "B", 2000)

print("\nSchool Directory:")
for member in [t1, t2, s1, s2]:
    member.describe()
    print()

SchoolMember.get_total()   # How many members were created in total?

# ============================================================
# SUMMARY:
# - Inheritance: class Child(Parent) -> reuses parent code
# - super()     -> calls parent's method from child class
# - Polymorphism -> same method name, different behavior per class
# - Encapsulation -> __attribute hides data (make it private)
# - @property    -> access method like an attribute; add setters
# - @staticmethod-> utility function, no 'self' needed
# - @classmethod -> works with the class itself (cls parameter)
# ============================================================
