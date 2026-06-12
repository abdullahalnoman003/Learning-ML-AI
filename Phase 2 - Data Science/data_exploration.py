"""
 DATA EXPLORATION - Complete EDA (Exploratory Data Analysis) Workflow
==========================================================================

What is EDA?
------------
EDA is the first thing you do when you get a new dataset!
It's like being a detective - you investigate the data to understand:
- What's in the data?
- What's the quality?
- What patterns exist?
- What relationships matter?

This Complete workflow file shows you how to analyze ANY dataset from scratch.

Steps we'll follow:
1. Load data
2. Understand structure
3. Check data quality
4. Analyze distributions
5. Find relationships
6. Detect outliers
7. Answer questions
8. Document findings
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

print("=" * 70)
print("COMPLETE EXPLORATORY DATA ANALYSIS (EDA) WORKFLOW")
print("=" * 70)

# Set visualization style
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (12, 6)

# ============================================================
# STEP 1: Load the Data
# ============================================================
print("\n STEP 1: Load the Dataset")
print("-" * 70)

# We'll use the Titanic dataset (classic EDA example)
# Loading from seaborn's built-in datasets
titanic = sns.load_dataset('titanic')

print(" Dataset loaded successfully!")
print(f"   Source: Titanic passenger data")
print(f"   Purpose: Predict survival based on passenger features")

# ============================================================
# STEP 2: First Look
# ============================================================
print("\n STEP 2: First Look at the Data")
print("-" * 70)

print("\n First 5 rows:")
print(titanic.head())

print("\n Last 5 rows:")
print(titanic.tail())

print("\n Random 3 rows:")
print(titanic.sample(3))

# ============================================================
# STEP 3: Understand Structure
# ============================================================
print("\n\n STEP 3: Understanding Data Structure")
print("-" * 70)

print(f"\n Dataset Dimensions:")
print(f"   Rows (samples): {titanic.shape[0]}")
print(f"   Columns (features): {titanic.shape[1]}")
print(f"   Total cells: {titanic.size}")

print(f"\n Column Names:")
print(f"   {titanic.columns.tolist()}")

print(f"\n Data Types:")
print(titanic.dtypes)
print("\n int64/float64 = numbers, object = text, bool = True/False, category = categories")

print(f"\n Detailed Info:")
titanic.info()

# ============================================================
# STEP 4: Check Data Quality
# ============================================================
print("\n\n STEP 4: Data Quality Check")
print("-" * 70)

# Missing values
print("\n Missing Values Count:")
missing = titanic.isnull().sum()
print(missing[missing > 0])

print("\n Missing Values Percentage:")
missing_pct = (titanic.isnull().sum() / len(titanic) * 100).round(2)
print(missing_pct[missing_pct > 0])

# Visualize missing data
plt.figure(figsize=(12, 6))
sns.heatmap(titanic.isnull(), cbar=True, yticklabels=False, cmap='viridis')
plt.title('Missing Data Pattern (Yellow = Missing)', fontsize=14, fontweight='bold')
plt.savefig('missing_data_heatmap.png', dpi=300, bbox_inches='tight')
print("\n Created: missing_data_heatmap.png")
plt.close()

# Duplicates
duplicates = titanic.duplicated().sum()
print(f"\n Duplicate rows: {duplicates}")

# ============================================================
# STEP 5: Statistical Summary
# ============================================================
print("\n\n STEP 5: Statistical Summary")
print("-" * 70)

print("\n Numeric Columns Summary:")
print(titanic.describe())
print("\n Shows: count, mean, std, min, 25%, 50%, 75%, max")

print("\n Categorical Columns Summary:")
categorical_cols = titanic.select_dtypes(include=['object', 'category']).columns
for col in categorical_cols:
    print(f"\n{col}:")
    print(titanic[col].value_counts())

# ============================================================
# STEP 6: Distribution Analysis
# ============================================================
print("\n\n STEP 6: Analyzing Distributions")
print("-" * 70)

# Numeric distributions
numeric_cols = ['age', 'fare', 'parch', 'sibsp']

fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle('Distribution of Numeric Features', fontsize=16, fontweight='bold')

for idx, col in enumerate(numeric_cols):
    row = idx // 2
    col_idx = idx % 2

    axes[row, col_idx].hist(titanic[col].dropna(), bins=30, color='steelblue',
                             edgecolor='black', alpha=0.7)
    axes[row, col_idx].set_title(f'{col.title()} Distribution')
    axes[row, col_idx].set_xlabel(col.title())
    axes[row, col_idx].set_ylabel('Frequency')
    axes[row, col_idx].grid(axis='y', alpha=0.3)

plt.tight_layout()
plt.savefig('numeric_distributions.png', dpi=300, bbox_inches='tight')
print(" Created: numeric_distributions.png")
plt.close()

# ============================================================
# STEP 7: Target Variable Analysis
# ============================================================
print("\n\n STEP 7: Target Variable (What We Want to Predict)")
print("-" * 70)

survival_counts = titanic['survived'].value_counts()
survival_pct = titanic['survived'].value_counts(normalize=True) * 100

print(f"\n Survival Statistics:")
print(f"   Survived (1): {survival_counts[1]} ({survival_pct[1]:.1f}%)")
print(f"   Died (0): {survival_counts[0]} ({survival_pct[0]:.1f}%)")

# Visualize
fig, axes = plt.subplots(1, 2, figsize=(14, 5))
fig.suptitle('Survival Analysis', fontsize=16, fontweight='bold')

# Count plot
axes[0].bar(['Died', 'Survived'], survival_counts.values,
            color=['#FF6B6B', '#4ECDC4'], edgecolor='black', alpha=0.7)
axes[0].set_ylabel('Count')
axes[0].set_title('Survival Counts')
axes[0].grid(axis='y', alpha=0.3)

# Pie chart
axes[1].pie(survival_counts.values, labels=['Died', 'Survived'],
            autopct='%1.1f%%', colors=['#FF6B6B', '#4ECDC4'],
            startangle=90, explode=(0.05, 0))
axes[1].set_title('Survival Proportion')

plt.tight_layout()
plt.savefig('survival_analysis.png', dpi=300, bbox_inches='tight')
print(" Created: survival_analysis.png")
plt.close()

# ============================================================
# STEP 8: Relationship Analysis
# ============================================================
print("\n\n STEP 8: Relationships Between Variables")
print("-" * 70)

# Survival by categorical features
categorical_features = ['sex', 'class', 'embarked', 'who']

fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle('Survival Rate by Category', fontsize=16, fontweight='bold')

for idx, feature in enumerate(categorical_features):
    row = idx // 2
    col_idx = idx % 2

    # Calculate survival rate
    survival_rate = titanic.groupby(feature)['survived'].mean() * 100

    survival_rate.plot(kind='bar', ax=axes[row, col_idx],
                       color='steelblue', edgecolor='black', alpha=0.7)
    axes[row, col_idx].set_title(f'Survival Rate by {feature.title()}')
    axes[row, col_idx].set_ylabel('Survival Rate (%)')
    axes[row, col_idx].set_xlabel(feature.title())
    axes[row, col_idx].grid(axis='y', alpha=0.3)
    axes[row, col_idx].tick_params(axis='x', rotation=45)

plt.tight_layout()
plt.savefig('survival_by_category.png', dpi=300, bbox_inches='tight')
print(" Created: survival_by_category.png")
plt.close()

# Age vs Survival
plt.figure(figsize=(12, 6))
titanic[titanic['survived'] == 0]['age'].hist(bins=30, alpha=0.5, label='Died', color='red')
titanic[titanic['survived'] == 1]['age'].hist(bins=30, alpha=0.5, label='Survived', color='green')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.title('Age Distribution by Survival', fontsize=14, fontweight='bold')
plt.legend()
plt.grid(axis='y', alpha=0.3)
plt.savefig('age_vs_survival.png', dpi=300, bbox_inches='tight')
print(" Created: age_vs_survival.png")
plt.close()

# ============================================================
# STEP 9: Correlation Analysis
# ============================================================
print("\n\n STEP 9: Correlation Analysis")
print("-" * 70)

# Select only numeric columns
numeric_data = titanic.select_dtypes(include=[np.number])

# Correlation matrix
correlation_matrix = numeric_data.corr()

print("\n Correlation with Survival:")
survival_corr = correlation_matrix['survived'].sort_values(ascending=False)
print(survival_corr)

# Visualize
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', center=0,
            fmt='.2f', square=True, linewidths=1)
plt.title('Correlation Matrix', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.savefig('correlation_matrix.png', dpi=300, bbox_inches='tight')
print("\n Created: correlation_matrix.png")
plt.close()

# ============================================================
# STEP 10: Outlier Detection
# ============================================================
print("\n\n STEP 10: Outlier Detection")
print("-" * 70)

# Box plots for numeric features
fig, axes = plt.subplots(1, 2, figsize=(14, 6))
fig.suptitle('Outlier Detection (Box Plots)', fontsize=16, fontweight='bold')

axes[0].boxplot([titanic['age'].dropna()], tick_labels=['Age'])
axes[0].set_ylabel('Years')
axes[0].set_title('Age Outliers')
axes[0].grid(axis='y', alpha=0.3)

axes[1].boxplot([titanic['fare'].dropna()], tick_labels=['Fare'])
axes[1].set_ylabel('Fare ($)')
axes[1].set_title('Fare Outliers')
axes[1].grid(axis='y', alpha=0.3)

plt.tight_layout()
plt.savefig('outliers_boxplot.png', dpi=300, bbox_inches='tight')
print(" Created: outliers_boxplot.png")
plt.close()

# IQR method for fare
Q1 = titanic['fare'].quantile(0.25)
Q3 = titanic['fare'].quantile(0.75)
IQR = Q3 - Q1
outliers = titanic[(titanic['fare'] < Q1 - 1.5*IQR) | (titanic['fare'] > Q3 + 1.5*IQR)]

print(f"\n Fare outliers detected: {len(outliers)}")
print(f"   Outlier range: < {Q1 - 1.5*IQR:.2f} or > {Q3 + 1.5*IQR:.2f}")

# ============================================================
# STEP 11: Answer Key Questions
# ============================================================
print("\n\n STEP 11: Answering Business Questions")
print("-" * 70)

print("\n Question 1: Did women survive more than men?")
gender_survival = titanic.groupby('sex')['survived'].mean() * 100
print(f"   Female survival rate: {gender_survival['female']:.1f}%")
print(f"   Male survival rate: {gender_survival['male']:.1f}%")
print(f"   → Answer: YES! Women survived at {gender_survival['female'] - gender_survival['male']:.1f}% higher rate")

print("\n Question 2: Did class affect survival?")
class_survival = titanic.groupby('class')['survived'].mean() * 100
print(class_survival)
print(f"   → Answer: YES! First class had {class_survival['First']:.1f}% survival vs {class_survival['Third']:.1f}% in third")

print("\n Question 3: What was the average age of survivors vs non-survivors?")
avg_age_died = titanic[titanic['survived'] == 0]['age'].mean()
avg_age_survived = titanic[titanic['survived'] == 1]['age'].mean()
print(f"   Average age (died): {avg_age_died:.1f} years")
print(f"   Average age (survived): {avg_age_survived:.1f} years")

print("\n Question 4: Did having family affect survival?")
titanic['family_size'] = titanic['sibsp'] + titanic['parch']
family_survival = titanic.groupby('family_size')['survived'].mean() * 100
print(family_survival)
print(f"   → Answer: Small families (1-3) had highest survival rates")

# ============================================================
# STEP 12: Key Findings Summary
# ============================================================
print("\n\n STEP 12: Key Findings & Insights")
print("=" * 70)

findings = """
 KEY FINDINGS FROM TITANIC DATASET:

 SURVIVAL RATE
    Overall: 38.4% survived, 61.6% died
    More passengers died than survived

 GENDER IMPACT
    ** Females had 74% survival rate**
    Males had only 19% survival rate
    Gender was the STRONGEST predictor

 CLASS IMPACT
    First class: 63% survival
    Second class: 47% survival
    Third class: 24% survival
    Wealth/class significantly affected survival

 AGES DISTRIBUTION
    Passengers aged 20-40 were majority
    Children had higher survival rates
    Very elderly had lower survival rates

 FAMILY SIZE
    Traveling alone: lower survival
    Small families (2-4): highest survival
    Large families: lower survival

 MISSING DATA
    Age: 20% missing
    Cabin: 77% missing (might need to drop)
    Embarked: <1% missing (can fill)

 FOR MACHINE LEARNING:
    Most important features: sex, class, age, fare
    Need to handle missing ages
    Consider dropping cabin column
    Create feature: family_size = sibsp + parch
    Target imbalanced (62% died, 38% survived)
    Should use stratified sampling
"""

print(findings)

# Save summary to file
with open('EDA_findings.txt', 'w') as f:
    f.write(findings)
print(" Saved findings to: EDA_findings.txt")

# ============================================================
# FINAL CHECKLIST
# ============================================================
print("\n\n EDA CHECKLIST - Always Do These Steps!")
print("=" * 70)
print("""
 EDA COMPLETE WORKFLOW:

1.   Load data
2.   Check shape (rows × columns)
3.   View first/last/random rows
4.   Check data types
5.   Identify missing values
6.   Check for duplicates
7.   Statistical summary (describe())
8.   Visualize distributions
9.   Analyze target variable
10.  Check relationships with target
11.  Correlation analysis
12.  Detect outliers
13.  Answer business questions
14.  Document findings
15.  Plan next steps (cleaning, feature engineering)

 FILES CREATED:
    missing_data_heatmap.png
    numeric_distributions.png
    survival_analysis.png
    survival_by_category.png
    age_vs_survival.png
    correlation_matrix.png
    outliers_boxplot.png
    EDA_findings.txt

 NEXT STEPS AFTER EDA:
   1. Clean data (handle missing, outliers)
   2. Feature engineering (create new features)
   3. Split data (train/test)
   4. Choose ML model
   5. Train and evaluate

 Remember: Good EDA = Better Models!
   "Garbage in, garbage out" - Clean data is everything!
""")

print("\n Exploratory Data Analysis Complete!")
print(" Phase 2 - Data Science Complete!")
print("\nNext phase: Phase 3 - Machine Learning")
print("Start with: Phase 3 - Machine Learning/ml_concepts.py")
