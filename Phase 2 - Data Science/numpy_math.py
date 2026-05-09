"""
🔢 NUMPY MATH - Matrix Operations for Machine Learning
=======================================================

What You'll Learn:
- Matrix multiplication (the heart of neural networks!)
- Dot products (used in EVERY ML algorithm)
- Transpose, inverse, and other linear algebra operations
- Broadcasting rules (NumPy's superpower)

Why This Matters:
In machine learning, almost everything is matrix math:
- Training a model = multiplying matrices
- Making predictions = more matrix multiplication
- Neural networks = stacks of matrix multiplications

Don't worry if you're not a math expert! We'll explain everything visually.
"""

import numpy as np

print("=" * 60)
print("NUMPY MATH - THE ENGINE OF MACHINE LEARNING")
print("=" * 60)

# ============================================================
# PART 1: Matrix Multiplication vs Element-wise Multiplication
# ============================================================
print("\n📌 PART 1: Matrix Multiplication (The Most Important Operation in ML!)")
print("-" * 60)

print("\n🤔 What's the difference?")
print("   Element-wise: Multiply matching positions")
print("   Matrix multiplication: Combine rows and columns")

A = np.array([[1, 2],
              [3, 4]])
B = np.array([[5, 6],
              [7, 8]])

print(f"\nMatrix A:\n{A}")
print(f"\nMatrix B:\n{B}")

# Element-wise multiplication (using *)
print(f"\nElement-wise (A * B):\n{A * B}")
print("   How it works: [1×5, 2×6]")
print("                 [3×7, 4×8]")

# Matrix multiplication (using @ or np.dot)
print(f"\nMatrix multiplication (A @ B):\n{A @ B}")
print("   How it works:")
print("   First row, first column:  (1×5) + (2×7) = 19")
print("   First row, second column: (1×6) + (2×8) = 22")
print("   Second row, first column:  (3×5) + (4×7) = 43")
print("   Second row, second column: (3×6) + (4×8) = 50")

print("\n💡 Rule: For A @ B to work:")
print("   A must have shape (m, n)")
print("   B must have shape (n, p)")
print("   Result will have shape (m, p)")

# ============================================================
# PART 2: The Dot Product
# ============================================================
print("\n\n📌 PART 2: Dot Product (Core of ML Algorithms)")
print("-" * 60)

print("\n📚 What is a dot product?")
print("   Take two vectors, multiply matching elements, then sum everything")

v1 = np.array([1, 2, 3])
v2 = np.array([4, 5, 6])

print(f"\nVector 1: {v1}")
print(f"Vector 2: {v2}")

dot_result = np.dot(v1, v2)
print(f"\nDot product: {dot_result}")
print(f"   Calculation: (1×4) + (2×5) + (3×6) = 4 + 10 + 18 = {dot_result}")

# Why this matters in ML
print("\n🤖 Why ML uses dot products:")
print("   In a neural network, each neuron computes:")
print("   output = dot(weights, inputs) + bias")
print("   Example: weights = [0.5, 0.3, 0.2], inputs = [2, 3, 1]")
weights = np.array([0.5, 0.3, 0.2])
inputs = np.array([2, 3, 1])
bias = 0.1
neuron_output = np.dot(weights, inputs) + bias
print(f"   Neuron output = {neuron_output:.2f}")

# ============================================================
# PART 3: Matrix Transpose
# ============================================================
print("\n\n📌 PART 3: Transpose (Flip Rows and Columns)")
print("-" * 60)

matrix = np.array([[1, 2, 3],
                   [4, 5, 6]])
print(f"Original matrix (2×3):\n{matrix}")
print(f"   Shape: {matrix.shape}")

transposed = matrix.T
print(f"\nTransposed matrix (3×2):\n{transposed}")
print(f"   Shape: {transposed.shape}")
print("   💡 Rows became columns, columns became rows!")

# Why transpose matters
print("\n🎯 Why use transpose?")
print("   In ML, you often need to change data shape to match matrix multiplication rules")
print("   Example: Shape (100, 3) @ Shape (3, 5) ✓ Works!")
print("            Shape (100, 3) @ Shape (100, 5) ✗ Doesn't work!")
print("            Shape (100, 3) @ Shape (5, 3).T ✓ Now it works!)

# ============================================================
# PART 4: Broadcasting
# ============================================================
print("\n\n📌 PART 4: Broadcasting (NumPy's Superpower)")
print("-" * 60)

print("\n📚 What is broadcasting?")
print("   NumPy automatically stretches smaller arrays to match larger ones")

matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])
print(f"Matrix (3×3):\n{matrix}")

# Add a single number (broadcasts to all elements)
result1 = matrix + 10
print(f"\nAdd 10 (broadcasts to all):\n{result1}")

# Add a row vector (broadcasts down)
row = np.array([10, 20, 30])
result2 = matrix + row
print(f"\nAdd row vector {row}:\n{result2}")
print("   💡 The row [10, 20, 30] gets added to EVERY row")

# Add a column vector (broadcasts across)
column = np.array([[100],
                   [200],
                   [300]])
result3 = matrix + column
print(f"\nAdd column vector:\n{column}")
print(f"Result:\n{result3}")
print("   💡 The column gets added to EVERY column")

# ============================================================
# PART 5: Aggregations Along Axes
# ============================================================
print("\n\n📌 PART 5: Aggregating Along Axes (Rows vs Columns)")
print("-" * 60)

data = np.array([[1, 2, 3],
                 [4, 5, 6],
                 [7, 8, 9]])
print(f"Data matrix:\n{data}")

# No axis = collapse everything
print(f"\nSum of ALL elements: {np.sum(data)}")

# Axis 0 = collapse DOWN (sum each column)
print(f"\nSum along axis 0 (down columns): {np.sum(data, axis=0)}")
print("   → [1+4+7, 2+5+8, 3+6+9] = [12, 15, 18]")

# Axis 1 = collapse RIGHT (sum each row)
print(f"\nSum along axis 1 (across rows): {np.sum(data, axis=1)}")
print("   → [1+2+3, 4+5+6, 7+8+9] = [6, 15, 24]")

# Other aggregations
print(f"\nMean of each column: {np.mean(data, axis=0)}")
print(f"Max of each row: {np.max(data, axis=1)}")

print("\n💡 Think of it this way:")
print("   axis=0: Operation goes DOWN ↓  (result has shape of columns)")
print("   axis=1: Operation goes RIGHT → (result has shape of rows)")

# ============================================================
# PART 6: Linear Algebra Operations
# ============================================================
print("\n\n📌 PART 6: Linear Algebra (Advanced but Important)")
print("-" * 60)

# Matrix inverse
A = np.array([[4, 7],
              [2, 6]])
print(f"Matrix A:\n{A}")

A_inv = np.linalg.inv(A)
print(f"\nInverse of A:\n{A_inv}")

# Check: A @ A_inv should give identity matrix
identity = A @ A_inv
print(f"\nA @ A_inv (should be identity):\n{np.round(identity, 2)}")
print("   💡 Used in solving linear equations in ML")

# Determinant
det = np.linalg.det(A)
print(f"\nDeterminant of A: {det:.2f}")
print("   💡 If determinant = 0, matrix is singular (not invertible)")

# Eigenvalues and eigenvectors (don't worry if this seems hard!)
eigenvalues, eigenvectors = np.linalg.eig(A)
print(f"\nEigenvalues: {eigenvalues}")
print(f"Eigenvectors:\n{eigenvectors}")
print("   💡 Used in PCA (dimensionality reduction) and other ML techniques")

# Matrix rank
rank = np.linalg.matrix_rank(A)
print(f"\nMatrix rank: {rank}")
print(f"   💡 Tells you how many independent rows/columns exist")

# ============================================================
# PART 7: Norms (Measuring Distance and Size)
# ============================================================
print("\n\n📌 PART 7: Norms (Measuring Vector Lengths)")
print("-" * 60)

v = np.array([3, 4])
print(f"Vector: {v}")

# L2 norm (Euclidean distance)
l2_norm = np.linalg.norm(v)
print(f"\nL2 norm (length): {l2_norm}")
print(f"   Calculation: √(3² + 4²) = √(9 + 16) = √25 = 5")
print("   💡 This is the straight-line distance from origin to point (3, 4)")

# L1 norm (Manhattan distance)
l1_norm = np.linalg.norm(v, ord=1)
print(f"\nL1 norm: {l1_norm}")
print(f"   Calculation: |3| + |4| = 7")
print("   💡 Distance if you can only move horizontally or vertically (like city blocks)")

# Why norms matter in ML
print("\n🎯 Why norms matter:")
print("   - Regularization (L1, L2) prevents overfitting")
print("   - Distance metrics for KNN, clustering")
print("   - Gradient clipping in deep learning")

# ============================================================
# PART 8: Real ML Example - Linear Regression
# ============================================================
print("\n\n📌 PART 8: Putting It All Together - Simple Linear Regression")
print("-" * 60)

print("\n🎯 Problem: Predict house prices based on size")
print("   House sizes (sq ft): [1000, 1500, 2000, 2500]")
print("   Prices ($1000s):      [200,  300,  400,  500]")

# Data (each row is one house)
X = np.array([[1, 1000],   # [bias term, size]
              [1, 1500],
              [1, 2000],
              [1, 2500]])
y = np.array([200, 300, 400, 500])

print(f"\nFeature matrix X (with bias column):\n{X}")
print(f"Target values y: {y}")

# Solve using linear algebra: weights = (X^T @ X)^(-1) @ X^T @ y
print("\n🧮 Solving using matrix operations...")

# Step 1: X transpose times X
XtX = X.T @ X
print(f"\n1. X^T @ X:\n{XtX}")

# Step 2: Inverse
XtX_inv = np.linalg.inv(XtX)
print(f"\n2. (X^T @ X)^(-1):\n{XtX_inv}")

# Step 3: Multiply by X^T @ y
weights = XtX_inv @ X.T @ y
print(f"\n3. Final weights: {weights}")
print(f"   Bias (intercept): {weights[0]:.2f}")
print(f"   Coefficient (per sq ft): {weights[1]:.4f}")

# Make predictions
predictions = X @ weights
print(f"\n🔮 Predictions: {predictions}")
print(f"Actual prices: {y}")
print(f"   👆 Pretty close!")

print("\n💡 This is EXACTLY how scikit-learn's LinearRegression works under the hood!")

# ============================================================
# SUMMARY
# ============================================================
print("\n\n🎯 NUMPY MATH SUMMARY")
print("=" * 60)
print("""
✅ What You Learned:
   1. Matrix multiplication (@) vs element-wise (*)
   2. Dot product - used in EVERY ML model
   3. Transpose - flipping dimensions
   4. Broadcasting - automatic size matching
   5. Aggregations - sum/mean along axes
   6. Linear algebra - inverse, determinant, eigenvalues
   7. Norms - measuring distances
   8. Real example - Linear Regression from scratch!

🚀 Next Steps:
   - Practice with different matrix sizes
   - Try implementing other ML algorithms using NumPy
   - Move on to Pandas for data manipulation

📝 Key Takeaway:
   Machine Learning = Matrix Math
   Master NumPy = Understand ML deeply
""")

print("\n✅ NumPy Math Complete!")
print("Next file: pandas_basics.py - Learn to work with real datasets")
