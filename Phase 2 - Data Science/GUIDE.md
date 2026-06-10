#  Phase 2: Data Science Tools — Detailed Guide

> Before building ML models, you must know how to **load, clean, and visualize data**.  
> These 3 libraries are used in every single AI/ML project.

---

##  Phase Overview

**Prerequisites:** Complete Phase 1 (Python Foundations) first.

| Library | Purpose | 
|---------|---------|
| NumPy | Fast math, arrays, matrix operations |  
| Pandas | Data tables, cleaning, filtering |  
| Matplotlib + Seaborn | Charts, graphs, visualization |  

**Status:  Not Started**

---

##  Setup — Install Everything First

```bash
pip install numpy pandas matplotlib seaborn jupyter
```

Run this in your terminal before starting.  
Verify installations:
```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
print("All libraries ready!")
```

---

##  Topic 1: NumPy
 File to create: `numpy_basics.py`

NumPy (Numerical Python) is the foundation of all ML math in Python.  
It gives you fast, powerful **arrays** (like supercharged lists).

### Why NumPy over regular Python lists?
```python
# Python list — slow for math
a = [1, 2, 3, 4, 5]

# NumPy array — 50x faster for large data
import numpy as np
a = np.array([1, 2, 3, 4, 5])
```

### What to Learn

**Basics:**
```python
import numpy as np

# Create arrays
arr = np.array([1, 2, 3, 4, 5])
matrix = np.array([[1, 2], [3, 4]])

# Shape = dimensions of the array
print(arr.shape)       # (5,)     → 1D, 5 elements
print(matrix.shape)    # (2, 2)   → 2 rows, 2 columns

# Data type
print(arr.dtype)       # int64
```

**Creating special arrays:**
```python
np.zeros((3, 3))           # 3x3 grid of zeros
np.ones((2, 4))            # 2x4 grid of ones
np.eye(3)                  # 3x3 identity matrix
np.random.random((3, 3))   # random values 0-1
np.arange(0, 10, 2)        # [0, 2, 4, 6, 8]
np.linspace(0, 1, 5)       # [0, 0.25, 0.5, 0.75, 1.0]
```

**Math operations:**
```python
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

# Element-wise operations
print(a + b)      # [5, 7, 9]
print(a * b)      # [4, 10, 18]
print(a ** 2)     # [1, 4, 9]

# Aggregate
print(np.sum(a))      # 6
print(np.mean(a))     # 2.0
print(np.max(a))      # 3
print(np.std(a))      # standard deviation
```

 File to create: `numpy_math.py`

**Matrix operations (critical for ML):**
```python
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

# Dot product (matrix multiplication)
print(np.dot(A, B))

# Transpose — flip rows and columns
print(A.T)

# Inverse (for linear algebra)
print(np.linalg.inv(A))

# Broadcasting — apply operation to all elements
print(A + 10)    # adds 10 to each element
```

**Indexing and slicing:**
```python
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

print(arr[0])        # First row: [1, 2, 3]
print(arr[:, 1])     # All rows, column 1: [2, 5, 8]
print(arr[0:2, 1:3]) # Rows 0-1, columns 1-2

# Boolean indexing
print(arr[arr > 5])  # Elements greater than 5
```

**Why this matters for ML:**
> Images are NumPy arrays (height × width × channels).  
> Your dataset's features are a NumPy matrix.  
> Every ML calculation is NumPy math under the hood.

---

##  Topic 2: Pandas
 File to create: `pandas_basics.py`

Pandas gives you **DataFrames** — spreadsheet-like tables in Python.  
This is how you load, explore, and manipulate real datasets.

### What to Learn

**Creating DataFrames:**
```python
import pandas as pd

# From a dictionary
data = {
    "name": ["Noman", "Ali", "Rahim"],
    "age":  [22, 24, 21],
    "cgpa": [3.9, 3.5, 3.7]
}
df = pd.DataFrame(data)
print(df)
```

**Loading real data (CSV):**
```python
df = pd.read_csv("dataset.csv")

# First look at data
print(df.head())          # first 5 rows
print(df.tail())          # last 5 rows
print(df.shape)           # (rows, columns)
print(df.columns)         # column names
print(df.dtypes)          # data types of each column
print(df.describe())      # statistics (mean, std, min, max)
print(df.info())          # overview of all columns
```

**Accessing data:**
```python
# Select one column
print(df["name"])

# Select multiple columns
print(df[["name", "cgpa"]])

# Select rows by index
print(df.iloc[0])         # first row
print(df.iloc[0:3])       # rows 0, 1, 2

# Filter rows by condition
high_cgpa = df[df["cgpa"] > 3.7]
```

 File to create: `pandas_cleaning.py`

**Handling missing data:**
```python
# Check for missing values
print(df.isnull().sum())

# Fill missing values
df["cgpa"].fillna(df["cgpa"].mean(), inplace=True)

# Drop rows with any missing value
df.dropna(inplace=True)
```

**Useful operations:**
```python
# Sort by column
df.sort_values("cgpa", ascending=False)

# Group and aggregate
df.groupby("department")["cgpa"].mean()

# Add new column
df["grade"] = df["cgpa"].apply(lambda x: "A" if x >= 3.7 else "B")

# Rename columns
df.rename(columns={"cgpa": "GPA"}, inplace=True)

# Drop a column
df.drop("unnecessary_column", axis=1, inplace=True)
```

**Why this matters for ML:**
> Every real ML project starts with a CSV or Excel file.  
> You use Pandas to explore, clean, and prepare data before feeding it to a model.

---

##  Topic 3: Matplotlib & Seaborn

 File to create: `matplotlib_basics.py`

**Visualization is understanding.** If you can't plot your data, you can't understand it.

**Basic plots:**
```python
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [10, 20, 15, 30, 25]

# Line plot
plt.plot(x, y)
plt.title("My First Plot")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.show()

# Bar chart
plt.bar(x, y, color="blue")
plt.show()

# Histogram
data = [22, 25, 21, 24, 23, 22, 26]
plt.hist(data, bins=5)
plt.show()

# Scatter plot
plt.scatter(x, y, color="red")
plt.show()
```

 File to create: `matplotlib_advanced.py`

**Subplots (multiple charts):**
```python
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

axes[0].plot(x, y)
axes[0].set_title("Line Plot")

axes[1].bar(x, y)
axes[1].set_title("Bar Chart")

plt.tight_layout()
plt.show()
```

**Seaborn (prettier + statistical plots):**
```python
import seaborn as sns

# Heatmap (great for correlation)
corr = df.corr()
sns.heatmap(corr, annot=True, cmap="coolwarm")
plt.show()

# Box plot
sns.boxplot(data=df, x="department", y="cgpa")

# Pair plot (relationships between all columns)
sns.pairplot(df)
plt.show()
```

---

##  Topic 4: Full EDA Workflow
 File to create: `data_exploration.py`

**EDA = Exploratory Data Analysis** — the first thing you do with any new dataset.

Standard EDA steps:
1. Load the data
2. Check shape and columns
3. Check for missing values
4. Check data types
5. Look at basic statistics
6. Check for duplicates
7. Visualize distributions
8. Check correlations
9. Draw conclusions

```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Step 1: Load
df = pd.read_csv("titanic.csv")

# Step 2: Shape
print(df.shape)

# Step 3: Missing values
print(df.isnull().sum())

# Step 4: Statistics
print(df.describe())

# Step 5: Correlation heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(df.corr(), annot=True)
plt.show()

# Step 6: Distribution of target
df["Survived"].value_counts().plot(kind="bar")
plt.show()
```

---

##  Phase 2 Mini-Project: Real Dataset Analysis

**Use the Titanic or Iris dataset (free on Kaggle/scikit-learn).**

**Tasks:**
1. Load the dataset with Pandas
2. Explore: shape, missing values, dtypes
3. Clean: fill or drop missing values
4. Answer 3 questions about the data using groupby
5. Create at least 5 visualizations
6. Write a short summary of what you found

**Starter code:**
```python
# Use scikit-learn's built-in datasets (no download needed)
from sklearn.datasets import load_iris
import pandas as pd

iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df["species"] = iris.target
print(df.head())
```

---



*Go to [LEARNING_PATH.md](../LEARNING_PATH.md) for the complete AI/ML roadmap.*  
*Previous phase: [Python Foundation](../Python%20Foundation/GUIDE.md)*
