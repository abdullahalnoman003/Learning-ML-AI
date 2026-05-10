"""
🧹 PANDAS DATA CLEANING - Making Messy Data Usable
===================================================

Why Data Cleaning Matters:
--------------------------
Real-world data is NEVER perfect! You'll encounter:
- Missing values (NaN, blank cells)
- Duplicates
- Wrong data types
- Outliers
- Inconsistent formats

Data scientists spend 80% of their time cleaning data!
This file teaches you how to handle all these issues.

Remember: "Garbage in, garbage out"
Good ML models need clean data!
"""

import pandas as pd
import numpy as np

print("=" * 60)
print("DATA CLEANING - FROM MESSY TO MACHINE-LEARNING READY")
print("=" * 60)

# ============================================================
# PART 1: Creating Messy Data (Simulating Real Life!)
# ============================================================
print("\n📌 PART 1: Understanding Messy Data")
print("-" * 60)

# Create a deliberately messy dataset
messy_data = pd.DataFrame({
    "Name": ["Alice", "Bob", "Charlie", np.nan, "Eve", "Frank", "Bob", "Grace", "  Diana  "],
    "Age": [25, 30, np.nan, 28, 150, 35, 30, 27, 32],  # 150 is an outlier, duplicate Bob
    "Salary": ["50000", "60000", "55000", "70000", np.nan, "65000", "60000", "58000", "72000"],
    "Department": ["sales", "IT", "Sales", "it", "HR", np.nan, "IT", "hr", "Sales"],
    "Join_Date": ["2020-01-15", "2019/03/20", "2021-07-10", "Not Available", "2022-01", "2020-12-25", "2019/03/20", "2023-05-18", "2018-11-30"]
})

print("\n❌ Messy dataset (has many problems!):")
print(messy_data)

print("\n🔍 Let's identify the problems:")
print("✗ Missing values (NaN)")
print("✗ Duplicate rows (Bob appears twice)")
print("✗ Age outlier (150 is impossible!)")
print("✗ Salary is stored as text instead of numbers")
print("✗ Inconsistent text (sales vs Sales, IT vs it)")
print("✗ Leading/trailing spaces in names")
print("✗ Inconsistent date formats")

# ============================================================
# PART 2: Handling Missing Values
# ============================================================
print("\n\n📌 PART 2: Handling Missing Data (NaN)")
print("-" * 60)

print("\n🔍 Step 1: Find missing values")
print(f"\nMissing values per column:")
print(messy_data.isnull().sum())

print(f"\n📊 Percentage missing per column:")
print((messy_data.isnull().sum() / len(messy_data) * 100).round(2))

# Visualize missing patterns
print("\n📍 Which rows have missing data?")
print(messy_data[messy_data.isnull().any(axis=1)])

print("\n\n🛠️ Step 2: Strategy for handling missing data")
print("=" * 60)

# Make a copy to work with
df_clean = messy_data.copy()

# Strategy 1: Drop rows with ANY missing value
print("\n1️⃣ Option: Drop ALL rows with missing data")
df_dropped = df_clean.dropna()
print(f"   Original rows: {len(df_clean)}")
print(f"   After dropping: {len(df_dropped)}")
print("   ⚠️ Lost 4 rows! Use only if you have lots of data")

# Strategy 2: Drop rows with missing values in specific columns
print("\n2️⃣ Option: Drop rows with missing Name only")
df_dropped_name = df_clean.dropna(subset=["Name"])
print(f"   After dropping rows with missing Name: {len(df_dropped_name)}")

# Strategy 3: Fill missing values
print("\n3️⃣ Option: Fill missing values (BETTER!)")

# Fill Age with mean
mean_age = df_clean["Age"].mean()
df_clean["Age"] = df_clean["Age"].fillna(mean_age)
print(f"   ✓ Filled missing Age with mean: {mean_age:.1f}")

# Fill Department with mode (most common)
mode_dept = df_clean["Department"].mode()[0]  # mode() returns Series
df_clean["Department"] = df_clean["Department"].fillna(mode_dept)
print(f"   ✓ Filled missing Department with mode: {mode_dept}")

# Fill Salary with forward fill (use previous value)
df_clean["Salary"] = df_clean["Salary"].fillna(method="ffill")
print(f"   ✓ Filled missing Salary using forward fill")

# Fill Name with placeholder
df_clean["Name"] = df_clean["Name"].fillna("Unknown")
print(f"   ✓ Filled missing Name with 'Unknown'")

print("\n📊 After filling missing values:")
print(df_clean.isnull().sum())
print("   ✓ No more missing values!")

# ============================================================
# PART 3: Handling Duplicates
# ============================================================
print("\n\n📌 PART 3: Finding and Removing Duplicates")
print("-" * 60)

print("\n🔍 Check for duplicates:")
print(f"Total duplicate rows: {df_clean.duplicated().sum()}")

print("\n📍 Show duplicate rows:")
duplicates = df_clean[df_clean.duplicated(keep=False)]  # keep=False shows all duplicates
print(duplicates.sort_values("Name"))

print("\n🧹 Remove duplicates:")
df_clean = df_clean.drop_duplicates()
print(f"   Rows before: {len(messy_data)}")
print(f"   Rows after: {len(df_clean)}")
print("   ✓ Duplicates removed! Only keeping first occurrence")

# ============================================================
# PART 4: Fixing Data Types
# ============================================================
print("\n\n📌 PART 4: Fixing Data Types")
print("-" * 60)

print("\n🔍 Current data types:")
print(df_clean.dtypes)

# Salary is 'object' (text) but should be numeric
print("\n🛠️ Converting Salary from text to integer:")
df_clean["Salary"] = pd.to_numeric(df_clean["Salary"], errors="coerce")
print(f"   ✓ Salary is now: {df_clean['Salary'].dtype}")
print("   💡 'coerce' turns invalid values to NaN")

print("\n📊 Updated data types:")
print(df_clean.dtypes)

# ============================================================
# PART 5: Handling Outliers
# ============================================================
print("\n\n📌 PART 5: Detecting and Handling Outliers")
print("-" * 60)

print("\n🔍 Age statistics:")
print(df_clean["Age"].describe())
print("   ⚠️ Max = 150! That's impossible!")

# Method 1: Visual inspection
print("\n1️⃣ Detect outliers using IQR (Interquartile Range)")
Q1 = df_clean["Age"].quantile(0.25)
Q3 = df_clean["Age"].quantile(0.75)
IQR = Q3 - Q1

lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

print(f"   Q1 (25th percentile): {Q1}")
print(f"   Q3 (75th percentile): {Q3}")
print(f"   IQR: {IQR}")
print(f"   Valid range: {lower_bound:.1f} to {upper_bound:.1f}")

# Find outliers
outliers = df_clean[(df_clean["Age"] < lower_bound) | (df_clean["Age"] > upper_bound)]
print(f"\n📍 Outliers found:")
print(outliers[["Name", "Age"]])

# Strategy: Replace outliers with median
print("\n🛠️ Fix: Replace outlier with median")
median_age = df_clean["Age"].median()
df_clean.loc[df_clean["Age"] > upper_bound, "Age"] = median_age
print(f"   ✓ Replaced Age outliers with median: {median_age}")

print("\n📊 Age after fixing:")
print(df_clean["Age"].describe())

# ============================================================
# PART 6: Text Cleaning
# ============================================================
print("\n\n📌 PART 6: Cleaning Text Data")
print("-" * 60)

print("\n🔍 Original Department values:")
print(df_clean["Department"].unique())
print("   ⚠️ Inconsistent: 'sales' vs 'Sales', 'IT' vs 'it'")

# Make all text consistent (lowercase)
df_clean["Department"] = df_clean["Department"].str.lower()
print("\n✓ After converting to lowercase:")
print(df_clean["Department"].unique())

# Standardize values
df_clean["Department"] = df_clean["Department"].str.title()  # First letter caps
print("\n✓ After title case:")
print(df_clean["Department"].unique())

# Remove leading/trailing whitespace
print("\n🔍 Names with spaces:")
print(df_clean["Name"].tolist())

df_clean["Name"] = df_clean["Name"].str.strip()
print("\n✓ After removing spaces:")
print(df_clean["Name"].tolist())

# Replace specific values
df_clean["Department"] = df_clean["Department"].replace({
    "Hr": "Human Resources",
    "It": "Information Technology"
})
print("\n✓ After standardizing department names:")
print(df_clean["Department"].unique())

# ============================================================
# PART 7: Date Cleaning
# ============================================================
print("\n\n📌 PART 7: Cleaning Date Formats")
print("-" * 60)

print("\n🔍 Original Join_Date (mixed formats):")
print(df_clean["Join_Date"].tolist())

# Convert to datetime (handles multiple formats automatically)
df_clean["Join_Date"] = pd.to_datetime(df_clean["Join_Date"], errors="coerce")
print("\n✓ After conversion to datetime:")
print(df_clean["Join_Date"])
print(f"   Data type: {df_clean['Join_Date'].dtype}")
print("   💡 Invalid dates became NaT (Not a Time)")

# Handle invalid dates
df_clean["Join_Date"] = df_clean["Join_Date"].fillna(pd.Timestamp("2020-01-01"))
print("\n✓ Filled invalid dates with default date:")
print(df_clean["Join_Date"])

# ============================================================
# PART 8: Creating New Features
# ============================================================
print("\n\n📌 PART 8: Feature Engineering (Creating Useful Columns)")
print("-" * 60)

# Calculate years of experience
current_year = pd.Timestamp.now().year
df_clean["Years_Experience"] = current_year - df_clean["Join_Date"].dt.year

print("\n➕ Added 'Years_Experience' column:")
print(df_clean[["Name", "Join_Date", "Years_Experience"]])

# Categorize age
def categorize_age(age):
    if age < 25:
        return "Junior"
    elif age < 35:
        return "Mid-Level"
    else:
        return "Senior"

df_clean["Career_Level"] = df_clean["Age"].apply(categorize_age)

print("\n➕ Added 'Career_Level' based on age:")
print(df_clean[["Name", "Age", "Career_Level"]])

# ============================================================
# PART 9: Validation and Final Check
# ============================================================
print("\n\n📌 PART 9: Final Data Validation")
print("-" * 60)

print("\n✓ CLEANED DATASET:")
print(df_clean)

print("\n📊 Data Quality Report:")
print(f"   Total rows: {len(df_clean)}")
print(f"   Total columns: {len(df_clean.columns)}")
print(f"   Missing values: {df_clean.isnull().sum().sum()}")
print(f"   Duplicate rows: {df_clean.duplicated().sum()}")

print("\n📈 Data type summary:")
print(df_clean.dtypes)

print("\n📊 Statistical summary:")
print(df_clean.describe())

# ============================================================
# PART 10: Save Cleaned Data
# ============================================================
print("\n\n📌 PART 10: Saving Cleaned Data")
print("-" * 60)

# Save to CSV
df_clean.to_csv("employees_cleaned.csv", index=False)
print("✓ Saved cleaned data to 'employees_cleaned.csv'")

# ============================================================
# DATA CLEANING CHECKLIST
# ============================================================
print("\n\n🎯 DATA CLEANING CHECKLIST")
print("=" * 60)
print("""
✅ Always Do These Steps (in order):

1. ❓ UNDERSTAND THE DATA
   - df.info() - data types and missing values
   - df.describe() - statistics
   - df.head() - first few rows

2. 🔍 FIND MISSING VALUES
   - df.isnull().sum() - count missing
   - Decide: drop or fill?

3. 🧹 REMOVE DUPLICATES
   - df.duplicated().sum()
   - df.drop_duplicates()

4. 🔢 FIX DATA TYPES
   - Convert strings to numbers: pd.to_numeric()
   - Convert to datetime: pd.to_datetime()

5. 🎯 HANDLE OUTLIERS
   - Use IQR method or domain knowledge
   - Remove or cap values

6. 📝 CLEAN TEXT
   - .str.lower() or .str.upper()
   - .str.strip() to remove spaces
   - Standardize categories

7. 📅 FIX DATES
   - pd.to_datetime() with errors='coerce'
   - Fill invalid dates appropriately

8. ➕ FEATURE ENGINEERING
   - Create new columns from existing ones
   - Categorize continuous variables

9. ✓ VALIDATE
   - Check: no missing, no duplicates
   - Verify data types are correct
   - Inspect value ranges

10. 💾 SAVE
    - Save cleaned data to new file

💡Common Strategies for Missing Data:
   • Numeric: Fill with mean, median, or mode
   • Categorical: Fill with mode or 'Unknown'
   • Drop if >70% of row is missing
   • Drop if column is not important

⚠️ NEVER modify original data directly!
   Always work on a copy: df_clean = df.copy()
""")

print("\n✅ Data Cleaning Complete!")
print("Next file: matplotlib_basics.py - Visualize your cleaned data")
