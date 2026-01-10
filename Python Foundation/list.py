# Now we will learn list
#  1. Creating a List


numbers = [1, 2, 3, 4, 5]
names = ["Noman", "Ali", "Rahim"]
mixed = [1, "Python", True, 3.5]


#  2. Accessing List Items (Index) it uses index based on 0

names = ["Noman", "Ali", "Rahim"]

print(names[0])   # Noman
print(names[1])   # Ali
print(names[2])   # Rahim
#print (names[3])  # Error

#  3. Negative Index (From End)

print(names[-1])  # Rahim
print(names[-2])  # Ali

#  4. Loop Through a List

# Method 1: Direct value


for name in names:
    print(name)


# Method 2: Using index


for i in range(len(names)):
    print(names[i])

#  5. Modify List Items

numbers = [10, 20, 30]
numbers[1] = 99
print(numbers)

[10, 99, 30]


#  6. Add Items to a List

# append()  add at end

numbers.append(40)

# insert()  add at specific index


numbers.insert(1, 15)

#  7. Remove Items from List

# remove() by value

numbers.remove(20)

# pop()  by index

numbers.pop()      # removes last
numbers.pop(1)     # removes index 1

#  8. List Length

print(len(numbers))

#  9. Check Item Exists

if 10 in numbers:
    print("Found")

#  10. Real-Life Example (Marks System)


marks = [45, 78, 90, 33, 67]

total = 0

for m in marks:
    total += m

average = total / len(marks)
print("Average:", average)
