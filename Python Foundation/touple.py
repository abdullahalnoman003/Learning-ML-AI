##  What is a Tuple?
###  Description A **tuple** is like a list, but **cannot be changed** after creation.

colors = ("red", "green", "blue")

## Access Tuple Items

print(colors[0])
print(colors[-1])

## Tuple Cannot Be Modified ❌

#colors[0] = "yellow"   # ERROR

# This is the main difference from lists.

## Loop Through Tuple

for color in colors:
    print(color)


## Tuple with One Item (Important!)

single = (10,)

#Without comma → it’s not a tuple.

# PART 2: SETS

## What is a Set?
### A **set** is a collection of: Unique values ,Unordered, No duplicates

### Example

numbers = {1, 2, 3, 4}


##  8. Duplicate Values Removed Automatically

nums = {1, 2, 2, 3, 3, 4}
print(nums)


## Add & Remove Items in Set

numbers.add(10)
numbers.remove(10)


## Loop Through Set

for n in numbers:
    print(n)


## Set Operations (VERY IMPORTANT)

## Union

a = {1, 2, 3}
b = {3, 4, 5}

print(a | b)


### Intersection

print(a & b)


### Difference

print(a - b)


##  12. Real-Life Example (Unique Students)

students = ["Noman", "Ali", "Noman", "Rahim"]
unique_students = set(students)

print(unique_students)


