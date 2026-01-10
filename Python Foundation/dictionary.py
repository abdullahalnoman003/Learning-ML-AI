# Dictionary 

# A dictionary stores data as key : value pairs. like we use is json data. also like object in 

# 1. What is a Dictionary?

name = "Noman"
age = 22
cgpa = 3.7

student = {
    "name": "Noman",
    "age": 22,
    "cgpa": 3.7
}

# 2. Access Dictionary Values

print(student["name"])
print(student["age"])

# Key must exist, otherwise → error.

# 3. Using `get()` (Safer Way)

print(student.get("cgpa"))
print(student.get("email"))   # None (no error)

# 4. Change Dictionary Values

student["age"] = 23

# 5. Add New Key–Value Pair

student["department"] = "Software Engineering"

# 6. Remove Items
student.pop("cgpa")

# 7. Loop Through Dictionary

# Keys only

for key in student:
    print(key)

# Values only

for value in student.values():
    print(value)

# Key + Value (Most Used)

for key, value in student.items():
    print(key, ":", value)


# 8. Check Key Exists

if "age" in student:
    print("Age exists")

# 9. Real-Life Example (Login System)

users = {
    "noman": "1234",
    "admin": "admin123"
}

username = input("Username: ")
password = input("Password: ")

if username in users and users[username] == password:
    print("Login successful")
else:
    print("Invalid credentials")

# 10. Dictionary Inside List (Very Important)


students = [
    {"name": "Noman", "cgpa": 3.7},
    {"name": "Ali", "cgpa": 3.2},
    {"name": "Rahim", "cgpa": 2.9}
]
for s in students:
    if s["cgpa"] >= 3.5:
        print(s["name"])

