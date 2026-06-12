"""
 PANDAS BASICS - Working with Real Data
==========================================

What is Pandas?
---------------
Pandas is like Excel for Python, but WAY more powerful!
- Load CSV, Excel, SQL databases, JSON files
- Filter, sort, group, and analyze data
- Handle missing values
- Prepare data for machine learning

Think of it as your data manipulation Swiss Army knife!

Key Concept: DataFrame = A table with rows and columns (like a spreadsheet)
"""

import pandas as pd
import numpy as np

print("=" * 60)
print("WELCOME TO PANDAS - YOUR DATA MANIPULATION TOOLKIT")
print("=" * 60)

# ============================================================
# PART 1: Creating DataFrames
# ============================================================
print("\n PART 1: Creating DataFrames (Your Data Tables)")
print("-" * 60)

# Method 1: From a dictionary
print("\n Method 1: Creating from a dictionary")
data = {
    "Name": ["Alice", "Bob", "Charlie", "Diana", "Eve"],
    "Age": [24, 27, 22, 32, 29],
    "City": ["New York", "London", "Paris", "Tokyo", "Berlin"],
    "Salary": [70000, 80000, 65000, 90000, 75000]
}

df = pd.DataFrame(data)
print(df)
print("\n Each key becomes a column, values become rows")

# Method 2: From a list of lists
print("\n\n Method 2: Creating from lists")
data_list = [
    ["Alice", 24, "New York"],
    ["Bob", 27, "London"],
    ["Charlie", 22, "Paris"]
]
df2 = pd.DataFrame(data_list, columns=["Name", "Age", "City"])
print(df2)

# Method 3: From NumPy array
print("\n\n Method 3: Creating from NumPy array")
array = np.array([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]])
df3 = pd.DataFrame(array, columns=["A", "B", "C"])
print(df3)

# ============================================================
# PART 2: Exploring Your DataFrame
# ============================================================
print("\n\n PART 2: First Look at Your Data (EDA Basics)")
print("-" * 60)

print("\n Let's explore our employee data:")
print(df)

# Basic info
print(f"\n Shape: {df.shape}   ({df.shape[0]} rows, {df.shape[1]} columns)")
print(f"Size: {df.size}   Total cells = rows × columns")

# Column names and types
print(f"\n Column names: {df.columns.tolist()}")
print("\n Data types of each column:")
print(df.dtypes)
print("    object = text, int64 = whole numbers, float64 = decimals")

# First few rows
print("\n First 3 rows (head):")
print(df.head(3))  # Default is 5 rows

# Last few rows
print("\n Last 2 rows (tail):")
print(df.tail(2))

# Random sample
print("\n Random 2 rows:")
print(df.sample(2))

# ============================================================
# PART 3: Getting Information
# ============================================================
print("\n\n PART 3: Understanding Your Data")
print("-" * 60)

# Summary statistics
print("\n Statistical Summary:")
print(df.describe())
print("    Count, mean, std, min, max, quartiles for numeric columns")

# Info about the DataFrame
print("\n DataFrame Info:")
df.info()
print("    Columns, data types, non-null counts, memory usage")

# Check for missing values
print(f"\n Missing values per column:")
print(df.isnull().sum())
print(f"\nTotal missing values: {df.isnull().sum().sum()}")

# Value counts
print(f"\n How many people in each city?")
print(df["City"].value_counts())

# ============================================================
# PART 4: Selecting Data
# ============================================================
print("\n\n PART 4: Selecting Data (Rows and Columns)")
print("-" * 60)

# Select a single column (returns Series)
print("\n Select 'Name' column:")
names = df["Name"]
print(names)
print(f"Type: {type(names)}   Series = single column")

# Select multiple columns (returns DataFrame)
print("\n Select 'Name' and 'Salary' columns:")
subset = df[["Name", "Salary"]]
print(subset)

# Select rows by index position (.iloc)
print("\n Select row 0 (first row) using .iloc:")
print(df.iloc[0])
print("    .iloc uses position (0, 1, 2, ...)")

print("\n Select rows 1-3:")
print(df.iloc[1:4])  # Remember: end index is exclusive

# Select rows by label (.loc)
print("\n Select specific rows and columns with .loc:")
print(df.loc[0:2, ["Name", "Age"]])  # Rows 0-2, specific columns
print("    .loc uses labels (and end index is inclusive!)")

# Select with boolean condition
print("\n Select all rows where Age >= 27:")
adults = df[df["Age"] >= 27]
print(adults)

print("\n People earning more than $70k:")
high_earners = df[df["Salary"] > 70000]
print(high_earners[["Name", "Salary"]])

# Multiple conditions
print("\n Age >= 25 AND Salary > 70000:")
result = df[(df["Age"] >= 25) & (df["Salary"] > 70000)]
print(result[["Name", "Age", "Salary"]])
print("    Use & for AND, | for OR, ~ for NOT")
print("   ️ Always use parentheses around each condition!")

# ============================================================
# PART 5: Adding and Modifying Data
# ============================================================
print("\n\n PART 5: Adding and Modifying Data")
print("-" * 60)

# Create a copy to avoid modifying original
df_copy = df.copy()

# Add a new column
print("\n Adding 'Bonus' column (10% of salary):")
df_copy["Bonus"] = df_copy["Salary"] * 0.10
print(df_copy[["Name", "Salary", "Bonus"]])

# Add column based on condition
print("\n Adding 'Seniority' based on age:")
df_copy["Seniority"] = df_copy["Age"].apply(
    lambda x: "Senior" if x >= 30 else "Junior"
)
print(df_copy[["Name", "Age", "Seniority"]])

# Modify existing values
print("\n️ Give everyone a $5000 raise:")
df_copy["Salary"] = df_copy["Salary"] + 5000
print(df_copy[["Name", "Salary"]])

# Modify specific values
print("\n️ Update Alice's age to 25:")
df_copy.loc[0, "Age"] = 25
print(df_copy.loc[0])

# ============================================================
# PART 6: Sorting and Ranking
# ============================================================
print("\n\n PART 6: Sorting Your Data")
print("-" * 60)

# Sort by one column
print("\n Sort by Age (ascending):")
sorted_df = df.sort_values("Age")
print(sorted_df[["Name", "Age"]])

print("\n Sort by Salary (descending):")
sorted_df = df.sort_values("Salary", ascending=False)
print(sorted_df[["Name", "Salary"]])

# Sort by multiple columns
print("\n Sort by City, then by Age:")
sorted_df = df.sort_values(["City", "Age"])
print(sorted_df[["Name", "City", "Age"]])

# Reset index after sorting
sorted_df = sorted_df.reset_index(drop=True)
print("\n After resetting index:")
print(sorted_df[["Name", "Salary"]])
print("    drop=True removes the old index")

# ============================================================
# PART 7: Filtering with Query
# ============================================================
print("\n\n PART 7: Filtering with .query() (Cleaner Syntax)")
print("-" * 60)

# Using query (more readable for complex conditions)
print("\n Find people aged 25-30:")
result = df.query("25 <= Age <= 30")
print(result[["Name", "Age"]])

print("\n Find people in New York or London:")
result = df.query("City == 'New York' or City == 'London'")
print(result[["Name", "City"]])

print("\n Salary > 70000 and Age < 30:")
result = df.query("Salary > 70000 and Age < 30")
print(result)

# ============================================================
# PART 8: Grouping and Aggregating
# ============================================================
print("\n\n PART 8: Group By - Analyzing Categories")
print("-" * 60)

# Create more sample data for grouping
employees = pd.DataFrame({
    "Name": ["Alice", "Bob", "Charlie", "Diana", "Eve", "Frank", "Grace", "Henry"],
    "Department": ["Sales", "Sales", "IT", "IT", "Sales", "IT", "HR", "HR"],
    "Salary": [70000, 80000, 65000, 90000, 75000, 72000, 68000, 85000],
    "Age": [24, 27, 22, 32, 29, 26, 31, 35]
})

print("\n Employee data:")
print(employees)

# Group by department and calculate mean
print("\n Average salary by department:")
dept_avg = employees.groupby("Department")["Salary"].mean()
print(dept_avg)

# Multiple aggregations
print("\n Multiple statistics by department:")
dept_stats = employees.groupby("Department")["Salary"].agg(["count", "mean", "min", "max"])
print(dept_stats)

# Group by and get multiple columns
print("\n Department summary:")
summary = employees.groupby("Department").agg({
    "Salary": ["mean", "max"],
    "Age": "mean"
})
print(summary)
print("    Super useful for data analysis!")

# ============================================================
# PART 9: Working with Dates
# ============================================================
print("\n\n PART 9: Working with Dates and Times")
print("-" * 60)

# Create date data
dates_df = pd.DataFrame({
    "Date": ["2024-01-15", "2024-02-20", "2024-03-10"],
    "Sales": [5000, 6000, 5500]
})

print("\n Original data:")
print(dates_df)
print(f"Date column type: {dates_df['Date'].dtype}   It's just text!")

# Convert to datetime
dates_df["Date"] = pd.to_datetime(dates_df["Date"])
print("\n After conversion:")
print(dates_df)
print(f"Date column type: {dates_df['Date'].dtype}   Now it's datetime!")

# Extract date components
dates_df["Year"] = dates_df["Date"].dt.year
dates_df["Month"] = dates_df["Date"].dt.month
dates_df["Day"] = dates_df["Date"].dt.day
dates_df["Day_Name"] = dates_df["Date"].dt.day_name()

print("\n With extracted date components:")
print(dates_df)

# ============================================================
# PART 10: Reading and Writing Files
# ============================================================
print("\n\n PART 10: Reading and Writing Files")
print("-" * 60)

print("\n Saving DataFrame to CSV:")
df.to_csv("employees.csv", index=False)
print("    Saved to 'employees.csv' (index=False means don't save row numbers)")

print("\n Reading CSV back:")
df_loaded = pd.read_csv("employees.csv")
print(df_loaded.head())

print("\n Other file formats:")
print("   • Excel: df.to_excel('file.xlsx')")
print("   • JSON: df.to_json('file.json')")
print("   • SQL: df.to_sql('table_name', connection)")

# ============================================================
# REAL WORLD EXAMPLE
# ============================================================
print("\n\n REAL WORLD EXAMPLE: Analyzing Sales Data")
print("-" * 60)

# Simulated sales data
sales_data = pd.DataFrame({
    "Date": pd.date_range("2024-01-01", periods=10, freq="D"),
    "Product": ["A", "B", "A", "C", "B", "A", "C", "B", "A", "C"],
    "Units_Sold": [5, 3, 7, 2, 4, 6, 1, 5, 8, 3],
    "Price": [100, 150, 100, 200, 150, 100, 200, 150, 100, 200]
})

sales_data["Revenue"] = sales_data["Units_Sold"] * sales_data["Price"]

print("\n Sales data:")
print(sales_data)

print("\n Total revenue by product:")
product_revenue = sales_data.groupby("Product")["Revenue"].sum().sort_values(ascending=False)
print(product_revenue)

print("\n Best selling day:")
best_day = sales_data.loc[sales_data["Units_Sold"].idxmax()]
print(f"   Date: {best_day['Date'].date()}")
print(f"   Product: {best_day['Product']}")
print(f"   Units: {best_day['Units_Sold']}")

# ============================================================
# SUMMARY
# ============================================================
print("\n\n PANDAS BASICS SUMMARY")
print("=" * 60)
print("""
 What You Learned:
   1. Creating DataFrames from dictionaries, lists, numpy arrays
   2. Exploring data: head(), tail(), describe(), info()
   3. Selecting data: [], .loc[], .iloc[], boolean indexing
   4. Adding/modifying columns and values
   5. Sorting: sort_values()
   6. Filtering: query()
   7. Grouping: groupby() with aggregations
   8. Working with dates
   9. Reading/writing CSV files
   10. Real-world data analysis example

 Key Functions to Remember:
   • df.head() - First few rows
   • df.info() - Data types and missing values
   • df.describe() - Statistics
   • df["column"] - Select column
   • df[df["Age"] > 25] - Filter rows
   • df.groupby("Category").mean() - Group and aggregate
   • df.sort_values("Column") - Sort data

 Next Steps:
   - Practice with real datasets (Kaggle, UCI ML Repository)
   - Learn data cleaning techniques
   - Move on to pandas_cleaning.py
""")

print("\n Pandas Basics Complete!")
print("Next file: pandas_cleaning.py - Learn to clean messy real-world data")
