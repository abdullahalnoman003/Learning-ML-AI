"""
📊 NUMPY BASICS - Your First Step into Data Science
=====================================================

What is NumPy?
--------------
NumPy (Numerical Python) is like a supercharged calculator for Python.
Imagine you have 1 million numbers and want to add 10 to each one:
- Regular Python list: SLOW (loops through each number)
- NumPy array: FAST (processes all at once using optimized C code)

Why does every Data Scientist use NumPy?
- It's 50x faster than regular Python lists
- Every ML library (pandas, scikit-learn, TensorFlow) is built on top of NumPy
- Makes math operations super simple and readable

Think of NumPy arrays like Excel spreadsheets, but much more powerful!
"""

import numpy as np

print("=" * 60)
print("WELCOME TO NUMPY - THE FOUNDATION OF DATA SCIENCE")
print("=" * 60)

# ============================================================
# PART 1: Creating NumPy Arrays
# ============================================================
print("\n📌 PART 1: Creating Arrays (like lists, but better)")
print("-" * 60)

# Regular Python list
python_list = [1, 2, 3, 4, 5]
print(f"Regular Python list: {python_list}")
print(f"Type: {type(python_list)}")

# NumPy array - created from a list
numpy_array = np.array([1, 2, 3, 4, 5])
print(f"\nNumPy array: {numpy_array}")
print(f"Type: {type(numpy_array)}")

# What's the difference?
print("\n🤔 Why use NumPy arrays instead of lists?")
print("   ✓ Math operations are MUCH faster")
print("   ✓ You can do operations on the entire array at once")
print("   ✓ They use less memory")

# Example: Add 10 to every number
print("\n🔢 Adding 10 to every element:")
print(f"   Regular way (list): {[x + 10 for x in python_list]}")
print(f"   NumPy way (easy!): {numpy_array + 10}")
print("   👆 No loop needed! NumPy does it automatically!")

# ============================================================
# PART 2: Array Properties
# ============================================================
print("\n\n📌 PART 2: Understanding Your Array")
print("-" * 60)

# 1D array (like a single row in Excel)
arr_1d = np.array([10, 20, 30, 40, 50])
print(f"1D Array: {arr_1d}")
print(f"   Shape: {arr_1d.shape}  👈 (5,) means 5 elements in 1 dimension")
print(f"   Size: {arr_1d.size}  👈 Total number of elements")
print(f"   Data type: {arr_1d.dtype}  👈 What kind of numbers (int, float, etc.)")

# 2D array (like a table with rows and columns)
arr_2d = np.array([[1, 2, 3],
                   [4, 5, 6]])
print(f"\n2D Array:\n{arr_2d}")
print(f"   Shape: {arr_2d.shape}  👈 (2, 3) means 2 rows, 3 columns")
print(f"   Size: {arr_2d.size}  👈 2×3 = 6 total elements")

# 3D array (like multiple tables stacked)
arr_3d = np.array([[[1, 2], [3, 4]],
                   [[5, 6], [7, 8]]])
print(f"\n3D Array:\n{arr_3d}")
print(f"   Shape: {arr_3d.shape}  👈 (2, 2, 2) means 2 layers, 2 rows, 2 columns")
print("   💡 Think of this like 2 pages of a book, each with a 2×2 table")

# ============================================================
# PART 3: Special Array Creation Functions
# ============================================================
print("\n\n📌 PART 3: Quick Ways to Create Arrays")
print("-" * 60)

# Array of zeros (like blank cells in Excel)
zeros = np.zeros((3, 4))  # 3 rows, 4 columns
print(f"Array of zeros (3 rows × 4 columns):\n{zeros}\n")

# Array of ones
ones = np.ones((2, 3))
print(f"Array of ones (2 rows × 3 columns):\n{ones}\n")

# Identity matrix (diagonal of 1s, rest 0s - important in math!)
identity = np.eye(4)
print(f"Identity matrix (4×4):\n{identity}\n")

# Array with a range of numbers
range_arr = np.arange(0, 10, 2)  # Start at 0, stop before 10, step by 2
print(f"Range array (0 to 10, step 2): {range_arr}")
print("   💡 Like Python's range(), but creates a NumPy array")

# Array with evenly spaced numbers
linspace_arr = np.linspace(0, 1, 5)  # 5 numbers evenly spaced between 0 and 1
print(f"\nLinspace (5 numbers from 0 to 1): {linspace_arr}")
print("   💡 Perfect for creating smooth curves in graphs!")

# Random numbers (super useful for machine learning!)
random_arr = np.random.random((2, 3))  # Random numbers between 0 and 1
print(f"\nRandom array (2×3):\n{random_arr}")

random_int = np.random.randint(1, 100, size=(3, 3))  # Random integers
print(f"\nRandom integers (1-100, 3×3):\n{random_int}")

# ============================================================
# PART 4: Basic Math Operations
# ============================================================
print("\n\n📌 PART 4: Math Operations (Easy Mode)")
print("-" * 60)

a = np.array([1, 2, 3, 4])
b = np.array([10, 20, 30, 40])

print(f"Array a: {a}")
print(f"Array b: {b}")

# Element-wise operations (match each element)
print(f"\na + b = {a + b}  👈 [1+10, 2+20, 3+30, 4+40]")
print(f"a - b = {a - b}")
print(f"a * b = {a * b}  👈 Element-wise multiplication (NOT matrix multiplication!)")
print(f"a / b = {a / b}")
print(f"a ** 2 = {a ** 2}  👈 Square each element")

# Operations with single numbers (broadcasting)
print(f"\na + 10 = {a + 10}  👈 Adds 10 to EVERY element")
print(f"a * 5  = {a * 5}  👈 Multiplies EVERY element by 5")
print("   💡 This is called 'broadcasting' - NumPy magic!")

# ============================================================
# PART 5: Useful Math Functions
# ============================================================
print("\n\n📌 PART 5: Statistical Functions (Know Your Data)")
print("-" * 60)

data = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
print(f"Data: {data}")

print(f"\n📊 Statistics:")
print(f"   Sum: {np.sum(data)}  👈 Add all numbers")
print(f"   Mean (Average): {np.mean(data)}  👈 Sum ÷ count")
print(f"   Median (Middle value): {np.median(data)}")
print(f"   Standard Deviation: {np.std(data):.2f}  👈 How spread out the data is")
print(f"   Minimum: {np.min(data)}")
print(f"   Maximum: {np.max(data)}")
print(f"   Range: {np.ptp(data)}  👈 Max - Min")

# Where is the min/max?
print(f"\n📍 Locations:")
print(f"   Index of minimum: {np.argmin(data)}  👈 Position of smallest value")
print(f"   Index of maximum: {np.argmax(data)}")

# ============================================================
# PART 6: Indexing and Slicing
# ============================================================
print("\n\n📌 PART 6: Accessing Elements (Like Excel Cell References)")
print("-" * 60)

arr = np.array([10, 20, 30, 40, 50])
print(f"Array: {arr}")

# Single element
print(f"\nFirst element arr[0]: {arr[0]}")
print(f"Last element arr[-1]: {arr[-1]}")

# Slicing (getting a range)
print(f"\nFirst 3 elements arr[0:3]: {arr[0:3]}")
print(f"From index 2 to end arr[2:]: {arr[2:]}")
print(f"Every other element arr[::2]: {arr[::2]}")

# 2D array indexing
matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])
print(f"\n2D Array:\n{matrix}")
print(f"\nElement at row 0, column 1: {matrix[0, 1]}  👈 Value is 2")
print(f"Element at row 2, column 2: {matrix[2, 2]}  👈 Value is 9")
print(f"\nFirst row: {matrix[0, :]}  👈 : means 'all columns'")
print(f"First column: {matrix[:, 0]}  👈 : means 'all rows'")
print(f"\nTop-left 2×2 block:\n{matrix[0:2, 0:2]}")

# ============================================================
# PART 7: Boolean Indexing (Filtering Data)
# ============================================================
print("\n\n📌 PART 7: Boolean Indexing (Finding Data That Matches)")
print("-" * 60)

scores = np.array([45, 78, 92, 34, 88, 56, 91, 67])
print(f"Test Scores: {scores}")

# Create a boolean mask (True/False for each element)
passing_mask = scores >= 60
print(f"\nWhich scores are ≥60? {passing_mask}")
print("   💡 True means PASS, False means FAIL")

# Get only the passing scores
passing_scores = scores[passing_mask]
print(f"\nPassing scores (≥60): {passing_scores}")

# Shortcut - do it in one line
print(f"\nScores above 80: {scores[scores > 80]}")
print(f"Scores between 50-70: {scores[(scores >= 50) & (scores <= 70)]}")
print("   💡 Use & for AND, | for OR when combining conditions")

# ============================================================
# PART 8: Reshaping Arrays
# ============================================================
print("\n\n📌 PART 8: Reshaping (Reorganizing Your Data)")
print("-" * 60)

arr = np.arange(1, 13)  # Numbers 1 to 12
print(f"Original (1D): {arr}")
print(f"   Shape: {arr.shape}")

# Reshape to 2D
matrix = arr.reshape(3, 4)  # 3 rows × 4 columns
print(f"\nReshaped to 3×4 matrix:\n{matrix}")

matrix = arr.reshape(4, 3)  # 4 rows × 3 columns
print(f"\nReshaped to 4×3 matrix:\n{matrix}")

# Flatten back to 1D
flattened = matrix.flatten()
print(f"\nFlattened back to 1D: {flattened}")

# ============================================================
# WHY THIS MATTERS FOR MACHINE LEARNING
# ============================================================
print("\n\n🎯 WHY NUMPY MATTERS FOR AI/ML")
print("=" * 60)
print("""
1. IMAGES are NumPy arrays!
   - Grayscale image: (height, width) array
   - Color image: (height, width, 3) array [Red, Green, Blue channels]

2. DATASETS are NumPy arrays!
   - Each row = one data sample
   - Each column = one feature
   - Shape (1000, 5) = 1000 samples with 5 features each

3. NEURAL NETWORK WEIGHTS are NumPy arrays!
   - Model learning = adjusting these arrays

4. Every ML calculation uses NumPy math!
   - Matrix multiplication, dot products, norms, etc.

💡 Master NumPy = Understand how ML really works under the hood!
""")

print("\n✅ NumPy Basics Complete!")
print("Next file: numpy_math.py - Learn about matrix operations for ML")
