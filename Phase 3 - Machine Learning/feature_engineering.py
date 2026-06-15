"""
 FEATURE ENGINEERING - Preparing Data for ML Success
=======================================================

What is Feature Engineering?
----------------------------
Transforming raw data into features that ML models can actually use!

The Truth: "Garbage In = Garbage Out"
- The BEST algorithm with BAD features → Poor results
- A SIMPLE algorithm with GOOD features → Great results!

Feature Engineering = 80% of ML Success!

What We'll Cover:
1. Handling missing values
2. Encoding categorical variables
3. Feature scaling/normalization
4. Creating new features
5. Feature selection
6. Handling outliers

Real World: Most ML time is spent on data preparation, not modeling!
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import (
    StandardScaler, MinMaxScaler, RobustScaler,
    LabelEncoder, OneHotEncoder, OrdinalEncoder
)
from sklearn.impute import SimpleImputer
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_selection import SelectKBest, f_classif, RFE

print("=" * 70)
print("FEATURE ENGINEERING - Turning Raw Data into ML Gold")
print("=" * 70)

# ============================================================
# PART 1: Creating Sample Dataset with Common Issues
# ============================================================
print("\n PART 1: Real-World Messy Data")
print("-" * 70)

print("""
 Example: Customer Purchase Prediction

Features:
- Age (numeric, has missing values)
- Income (numeric, different scale, has outliers)
- Education (categorical, ordered)
- City (categorical, unordered)
- Purchase_History (numeric)

Target: Will customer make a purchase? (Yes/No)

This dataset has all common real-world problems!
""")

# Create sample dataset
np.random.seed(42)
n_samples = 100

data = {
    'Age': np.random.randint(18, 70, n_samples).astype(float),
    'Income': np.random.normal(50000, 20000, n_samples),
    'Education': np.random.choice(['High School', 'Bachelor', 'Master', 'PhD'], n_samples),
    'City': np.random.choice(['New York', 'London', 'Paris', 'Tokyo'], n_samples),
    'Purchase_History': np.random.randint(0, 50, n_samples),
    'Purchased': np.random.choice([0, 1], n_samples, p=[0.6, 0.4])
}

df = pd.DataFrame(data)

# Introduce missing values
missing_indices = np.random.choice(df.index, size=10, replace=False)
df.loc[missing_indices, 'Age'] = np.nan

# Introduce outliers
outlier_indices = np.random.choice(df.index, size=5, replace=False)
df.loc[outlier_indices, 'Income'] = df.loc[outlier_indices, 'Income'] * 5

print(f"\n Dataset Preview:")
print(df.head(10))

print(f"\n Dataset Info:")
print(f"   Samples: {len(df)}")
print(f"   Features: {df.shape[1] - 1}")
print(f"   Missing values: {df.isnull().sum().sum()}")

print(f"\n Missing Values per Column:")
print(df.isnull().sum())

print(f"\n Data Types:")
print(df.dtypes)

# ============================================================
# PART 2: Handling Missing Values
# ============================================================
print("\n\n PART 2: Handling Missing Values")
print("-" * 70)

print("""
 Strategies for Missing Values:

1. REMOVE:
   - Drop rows with missing values
   - Pro: Simple
   - Con: Lose data (bad if many missing)

2. IMPUTE (Fill in):
   a) Mean/Median (numeric)
      - Mean: Affected by outliers
      - Median: Robust to outliers (better!)

   b) Mode (categorical)
      - Most frequent value

   c) Forward Fill / Backward Fill
      - Use previous/next value (time series)

   d) Predictive Imputation
      - Train model to predict missing values
      - Most sophisticated

3. CREATE INDICATOR:
   - Add binary column: "Was_Missing"
   - Sometimes missingness itself is informative!
""")

# Show missing data
print(f"\n Rows with Missing Age:")
print(df[df['Age'].isnull()][['Age', 'Income', 'Education']])

# Strategy 1: Mean imputation
imputer_mean = SimpleImputer(strategy='mean')
df['Age_Mean_Imputed'] = imputer_mean.fit_transform(df[['Age']])

# Strategy 2: Median imputation (better for outliers)
imputer_median = SimpleImputer(strategy='median')
df['Age_Median_Imputed'] = imputer_median.fit_transform(df[['Age']])

# Strategy 3: Add missing indicator
df['Age_Was_Missing'] = df['Age'].isnull().astype(int)

# Fill the original Age column
df['Age'] = df['Age_Median_Imputed']

print(f"\n Missing values handled!")
print(f"   Strategy: Median imputation (robust to outliers)")
print(f"   Added indicator: Age_Was_Missing (preserves information)")

# ============================================================
# PART 3: Encoding Categorical Variables
# ============================================================
print("\n\n PART 3: Encoding Categorical Variables")
print("-" * 70)

print("""
 Problem: ML models only understand numbers!

Categorical Variables:
- Education: ['High School', 'Bachelor', 'Master', 'PhD']
- City: ['New York', 'London', 'Paris', 'Tokyo']

Encoding Strategies:

1. LABEL ENCODING:
   Convert to integers: High School=0, Bachelor=1, Master=2, PhD=3
   ️ Problem: Implies order (Bachelor > High School)
    Use when: Ordinal data (Small < Medium < Large)
    Don't use when: Nominal data (no order)

2. ONE-HOT ENCODING:
   Create binary column for each category:
   City_NewYork  City_London  City_Paris  City_Tokyo
   1             0            0           0
   0             1            0           0
    Use when: Nominal data (no order)
   ️ Problem: Many categories → Many columns (curse of dimensionality)

3. ORDINAL ENCODING:
   Like label encoding but YOU specify the order
   Small=0, Medium=1, Large=2
    Use when: Clear ordering exists
""")

# Education: Ordinal (has order)
print(f"\n Education Encoding (Ordinal):")
print(f"   Original values: {df['Education'].unique()}")

education_order = {'High School': 0, 'Bachelor': 1, 'Master': 2, 'PhD': 3}
df['Education_Encoded'] = df['Education'].map(education_order)

print(f"   Encoded: High School=0, Bachelor=1, Master=2, PhD=3")
print(f"\nSample:")
print(df[['Education', 'Education_Encoded']].head())

# City: Nominal (no order) → One-Hot Encoding
print(f"\n\n City Encoding (One-Hot):")
print(f"   Original values: {df['City'].unique()}")

# One-hot encode
city_dummies = pd.get_dummies(df['City'], prefix='City', drop_first=True)
df = pd.concat([df, city_dummies], axis=1)

print(f"   Created {len(city_dummies.columns)} new binary columns:")
print(f"   {city_dummies.columns.tolist()}")
print(f"\n drop_first=True: Avoid multicollinearity (one column is redundant)")
print(f"\nSample:")
print(df[['City'] + city_dummies.columns.tolist()].head())

# ============================================================
# PART 4: Feature Scaling
# ============================================================
print("\n\n PART 4: Feature Scaling - CRITICAL for Many Algorithms!")
print("-" * 70)

print("""
️ Why Scale Features?

Problem: Different features have different ranges
- Age: 18-70 (range ≈ 50)
- Income: 20,000-300,000 (range ≈ 280,000)

Algorithms affected by scale:
    KNN (uses distance)
    SVM (uses distance)
    Neural Networks (gradient descent)
    Linear/Logistic Regression (when using regularization)

Algorithms NOT affected:
    Decision Trees
    Random Forest
    Gradient Boosting

Scaling Methods:

1. STANDARDIZATION (Z-score normalization):
   Formula: z = (x - mean) / std_dev
   Result: Mean=0, Std=1
   Range: Typically -3 to +3
   Use when: Data is normally distributed
    Most common! Works well in general

2. MIN-MAX SCALING (Normalization):
   Formula: x_scaled = (x - min) / (max - min)
   Result: Values between 0 and 1
   Use when: Need bounded range (e.g., neural networks)
   ️ Sensitive to outliers!

3. ROBUST SCALING:
   Formula: x_scaled = (x - median) / IQR
   Result: Robust to outliers
   Use when: Data has many outliers
    Best for messy real-world data
""")

# Compare scaling methods
print(f"\n Original Data Statistics:")
print(f"   Age: mean={df['Age'].mean():.1f}, std={df['Age'].std():.1f}, min={df['Age'].min():.1f}, max={df['Age'].max():.1f}")
print(f"   Income: mean={df['Income'].mean():.1f}, std={df['Income'].std():.1f}, min={df['Income'].min():.1f}, max={df['Income'].max():.1f}")

# Prepare data for scaling
features_to_scale = ['Age', 'Income', 'Purchase_History']
X_original = df[features_to_scale].copy()

# Method 1: StandardScaler
scaler_standard = StandardScaler()
X_standard = scaler_standard.fit_transform(X_original)
X_standard_df = pd.DataFrame(X_standard, columns=[f'{col}_Standard' for col in features_to_scale])

# Method 2: MinMaxScaler
scaler_minmax = MinMaxScaler()
X_minmax = scaler_minmax.fit_transform(X_original)
X_minmax_df = pd.DataFrame(X_minmax, columns=[f'{col}_MinMax' for col in features_to_scale])

# Method 3: RobustScaler
scaler_robust = RobustScaler()
X_robust = scaler_robust.fit_transform(X_original)
X_robust_df = pd.DataFrame(X_robust, columns=[f'{col}_Robust' for col in features_to_scale])

print(f"\n After StandardScaler (mean=0, std=1):")
print(f"   Age: mean={X_standard[:, 0].mean():.4f}, std={X_standard[:, 0].std():.4f}")
print(f"   Income: mean={X_standard[:, 1].mean():.4f}, std={X_standard[:, 1].std():.4f}")

print(f"\n After MinMaxScaler (range: 0-1):")
print(f"   Age: min={X_minmax[:, 0].min():.4f}, max={X_minmax[:, 0].max():.4f}")
print(f"   Income: min={X_minmax[:, 1].min():.4f}, max={X_minmax[:, 1].max():.4f}")

print(f"\n After RobustScaler (uses median and IQR):")
print(f"   Age: median={np.median(X_robust[:, 0]):.4f}")
print(f"   Income: median={np.median(X_robust[:, 1]):.4f}")

# Visualize scaling effects
fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# Original
axes[0, 0].hist(df['Income'], bins=30, edgecolor='black', alpha=0.7)
axes[0, 0].set_title('Original Income', fontweight='bold')
axes[0, 0].set_xlabel('Income ($)')

# StandardScaler
axes[0, 1].hist(X_standard[:, 1], bins=30, edgecolor='black', alpha=0.7, color='orange')
axes[0, 1].set_title('StandardScaler', fontweight='bold')
axes[0, 1].set_xlabel('Standardized Income')

# MinMaxScaler
axes[1, 0].hist(X_minmax[:, 1], bins=30, edgecolor='black', alpha=0.7, color='green')
axes[1, 0].set_title('MinMaxScaler', fontweight='bold')
axes[1, 0].set_xlabel('Normalized Income (0-1)')

# RobustScaler
axes[1, 1].hist(X_robust[:, 1], bins=30, edgecolor='black', alpha=0.7, color='red')
axes[1, 1].set_title('RobustScaler', fontweight='bold')
axes[1, 1].set_xlabel('Robust Scaled Income')

plt.tight_layout()
plt.savefig('feature_scaling_comparison.png', dpi=150)
print("\n Saved plot: feature_scaling_comparison.png")

# ============================================================
# PART 5: Handling Outliers
# ============================================================
print("\n\n PART 5: Handling Outliers")
print("-" * 70)

print("""
 Outliers: Data points that are FAR from others

Detection Methods:

1. Z-SCORE METHOD:
   - Points with |z-score| > 3 are outliers
   - Assumes normal distribution

2. IQR METHOD (Interquartile Range):
   - Q1 = 25th percentile, Q3 = 75th percentile
   - IQR = Q3 - Q1
   - Outliers: < Q1 - 1.5×IQR or > Q3 + 1.5×IQR
   - More robust than z-score

Handling Strategies:
1. REMOVE: Drop outliers (if they're errors)
2. CAP: Set to maximum acceptable value (winsorization)
3. TRANSFORM: Log transform, square root
4. KEEP: They might be important! (fraud detection)
5. SEPARATE MODEL: Train different model for outliers
""")

# Detect outliers using IQR method
Q1 = df['Income'].quantile(0.25)
Q3 = df['Income'].quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

outliers = df[(df['Income'] < lower_bound) | (df['Income'] > upper_bound)]

print(f"\n Outlier Detection (IQR Method):")
print(f"   Q1 (25th percentile): ${Q1:,.0f}")
print(f"   Q3 (75th percentile): ${Q3:,.0f}")
print(f"   IQR: ${IQR:,.0f}")
print(f"   Lower bound: ${lower_bound:,.0f}")
print(f"   Upper bound: ${upper_bound:,.0f}")
print(f"   Number of outliers: {len(outliers)}")

if len(outliers) > 0:
    print(f"\n Outliers found:")
    print(outliers[['Age', 'Income', 'Education']])

# Visualize outliers
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# Box plot
axes[0].boxplot(df['Income'], vert=True)
axes[0].set_ylabel('Income ($)', fontsize=12)
axes[0].set_title('Box Plot - Outliers Visible', fontsize=13, fontweight='bold')
axes[0].grid(axis='y', alpha=0.3)

# Histogram
axes[1].hist(df['Income'], bins=30, edgecolor='black', alpha=0.7)
axes[1].axvline(x=upper_bound, color='r', linestyle='--', linewidth=2, label='Upper Bound')
axes[1].axvline(x=lower_bound, color='r', linestyle='--', linewidth=2, label='Lower Bound')
axes[1].set_xlabel('Income ($)', fontsize=12)
axes[1].set_ylabel('Frequency', fontsize=12)
axes[1].set_title('Income Distribution with Outlier Bounds', fontsize=13, fontweight='bold')
axes[1].legend()
axes[1].grid(axis='y', alpha=0.3)

plt.tight_layout()
plt.savefig('feature_outliers.png', dpi=150)
print("\n Saved plot: feature_outliers.png")

# Strategy: Cap outliers
df['Income_Capped'] = df['Income'].clip(lower=lower_bound, upper=upper_bound)
print(f"\n Outliers capped!")
print(f"   Values below ${lower_bound:,.0f} → ${lower_bound:,.0f}")
print(f"   Values above ${upper_bound:,.0f} → ${upper_bound:,.0f}")

# ============================================================
# PART 6: Feature Creation (Feature Engineering)
# ============================================================
print("\n\n PART 6: Creating New Features")
print("-" * 70)

print("""
 Sometimes the magic is in CREATING new features!

Common Techniques:

1. MATHEMATICAL OPERATIONS:
   - Ratios: Income / Age (income per year of life)
   - Differences: Current - Previous
   - Products: Price × Quantity

2. BINNING (Discretization):
   - Convert continuous → categorical
   - Age → Age_Group (Young, Middle, Senior)

3. DATE/TIME FEATURES:
   - Extract: Year, Month, Day, Hour, Day_of_Week
   - Create: Is_Weekend, Is_Holiday

4. DOMAIN KNOWLEDGE:
   - Use your understanding of the problem!
   - Example: BMI = Weight / (Height²)

5. POLYNOMIAL FEATURES:
   - x, x², x³ (for non-linear relationships)
   - Interactions: x₁ × x₂
""")

# Create new features
df['Income_Per_Age'] = df['Income'] / df['Age']
df['High_Spender'] = (df['Purchase_History'] > df['Purchase_History'].median()).astype(int)

# Age groups (binning)
df['Age_Group'] = pd.cut(df['Age'],
                         bins=[0, 30, 50, 100],
                         labels=['Young', 'Middle', 'Senior'])

print(f"\n New Features Created:")
print(f"   1. Income_Per_Age: Income divided by Age")
print(f"   2. High_Spender: Binary (1 if above median purchase history)")
print(f"   3. Age_Group: Categorical bins (Young, Middle, Senior)")

print(f"\n Sample of new features:")
print(df[['Age', 'Income', 'Income_Per_Age', 'Purchase_History', 'High_Spender', 'Age_Group']].head())

# ============================================================
# PART 7: Feature Selection
# ============================================================
print("\n\n PART 7: Feature Selection - Less is More!")
print("-" * 70)

print("""
 Why Remove Features?

Problems with too many features:
    Overfitting (model memorizes noise)
    Slower training
    Curse of dimensionality
    Harder to interpret

Methods:

1. FILTER METHODS:
   - Statistical tests (correlation, chi-square, ANOVA)
   - Fast and simple
   - Independent of model

2. WRAPPER METHODS:
   - Recursive Feature Elimination (RFE)
   - Forward/Backward selection
   - Uses model performance
   - Slow but accurate

3. EMBEDDED METHODS:
   - Feature importance from tree models
   - L1 regularization (Lasso)
   - Built into training
""")

# Prepare data for feature selection
df_clean = df.copy()

# Select numeric features for modeling
numeric_features = ['Age', 'Income_Capped', 'Purchase_History', 'Education_Encoded',
                   'Age_Was_Missing', 'Income_Per_Age', 'High_Spender']

# Add one-hot encoded city features
city_cols = [col for col in df.columns if col.startswith('City_')]
all_features = numeric_features + city_cols

X = df_clean[all_features].fillna(0)
y = df_clean['Purchased']

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

print(f"\n Feature Selection Setup:")
print(f"   Total features: {X.shape[1]}")
print(f"   Features: {all_features}")

# Method 1: SelectKBest (Filter method)
print(f"\n Method 1: SelectKBest (ANOVA F-value)")
selector = SelectKBest(score_func=f_classif, k=5)
selector.fit(X_train, y_train)

# Get scores
feature_scores = pd.DataFrame({
    'Feature': all_features,
    'Score': selector.scores_
}).sort_values('Score', ascending=False)

print(f"\n Feature Importance Scores:")
print(feature_scores.to_string(index=False))

selected_features = feature_scores.head(5)['Feature'].tolist()
print(f"\n Top 5 features selected:")
for i, feat in enumerate(selected_features, 1):
    print(f"   {i}. {feat}")

# Method 2: Feature importance from Random Forest
print(f"\n\n Method 2: Random Forest Feature Importance")
rf = RandomForestClassifier(n_estimators=100, random_state=42)
rf.fit(X_train, y_train)

feature_importance_rf = pd.DataFrame({
    'Feature': all_features,
    'Importance': rf.feature_importances_
}).sort_values('Importance', ascending=False)

print(f"\n Feature Importance from Random Forest:")
print(feature_importance_rf.to_string(index=False))

# Visualize
plt.figure(figsize=(10, 6))
plt.barh(feature_importance_rf['Feature'][:10], feature_importance_rf['Importance'][:10], color='forestgreen')
plt.xlabel('Importance', fontsize=12)
plt.ylabel('Feature', fontsize=12)
plt.title('Top 10 Most Important Features', fontsize=14, fontweight='bold')
plt.grid(axis='x', alpha=0.3)
plt.tight_layout()
plt.savefig('feature_importance.png', dpi=150)
print("\n Saved plot: feature_importance.png")

# ============================================================
# PART 8: Complete Pipeline Example
# ============================================================
print("\n\n PART 8: Putting It All Together - Complete Pipeline")
print("-" * 70)

print("""
 Complete Feature Engineering Pipeline:

1. Handle missing values → Impute
2. Detect and handle outliers → Cap or remove
3. Encode categorical variables → One-hot or label encoding
4. Create new features → Domain knowledge
5. Scale features → StandardScaler
6. Select features → Remove unimportant ones
7. Train model → Random Forest
8. Evaluate → Accuracy, precision, recall

This is what you do in EVERY real ML project!
""")

# Simplified pipeline example
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer

print(f"\n Building sklearn Pipeline...")

# Define transformers
numeric_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='median')),
    ('scaler', StandardScaler())
])

# Create preprocessor
numeric_features_simple = ['Age', 'Income', 'Purchase_History']
preprocessor = ColumnTransformer(
    transformers=[
        ('num', numeric_transformer, numeric_features_simple)
    ])

# Create pipeline
pipeline = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('classifier', RandomForestClassifier(n_estimators=100, random_state=42))
])

# Prepare simple data
X_simple = df[numeric_features_simple]
y_simple = df['Purchased']

X_train_s, X_test_s, y_train_s, y_test_s = train_test_split(
    X_simple, y_simple, test_size=0.3, random_state=42
)

# Train pipeline
print(f"   Training pipeline...")
pipeline.fit(X_train_s, y_train_s)

# Evaluate
train_score = pipeline.score(X_train_s, y_train_s)
test_score = pipeline.score(X_test_s, y_test_s)

print(f"\n Pipeline Performance:")
print(f"   Training Accuracy: {train_score:.4f}")
print(f"   Test Accuracy: {test_score:.4f}")
print(f"\n Pipeline successfully applies all transformations automatically!")
print(f"   This is production-ready code!")

# ============================================================
# WHY THIS MATTERS
# ============================================================
print("\n\n WHY FEATURE ENGINEERING MATTERS")
print("=" * 70)
print("""
1. MOST IMPORTANT STEP:
   - "Data and features determine the upper bound on performance"
   - Algorithm choice is secondary!
   - Great features + simple model > poor features + complex model

2. REAL WORLD IS MESSY:
   - Missing values are common
   - Outliers exist
   - Wrong data types
   - Different scales
   - You MUST clean data!

3. DOMAIN KNOWLEDGE WINS:
   - Understanding your problem → Better features
   - Example: Using "BMI" instead of just weight and height
   - Creative feature engineering beats fancy algorithms

4. ALGORITHM REQUIREMENTS:
   - KNN, SVM, Neural Networks → NEED scaling
   - Tree-based → Don't need scaling
   - All algorithms → Need proper encoding

5. PRODUCTION CONSIDERATIONS:
   - Use sklearn Pipeline for reproducibility
   - Save fitted transformers (same transform on new data)
   - Document all transformations

 KEY TAKEAWAYS:
    Handle missing values (don't just drop!)
    Encode categorical variables properly
    Scale features for distance-based algorithms
    Create new features from domain knowledge
    Remove unimportant features (less is more)
    Handle outliers (detect and treat)
    Use sklearn Pipeline for reproducibility
    80% of ML is data preparation!

 Best Practices:
    Always split data BEFORE scaling (prevent data leakage!)
    Fit transformers on training set only
    Apply same transformation to test set
    Document all decisions
    Create reproducible pipelines
    Start simple, add complexity if needed

️ Common Mistakes:
    Scaling before train-test split (DATA LEAKAGE!)
    Using mean imputation without checking distribution
    One-hot encoding high cardinality features (too many columns)
    Not handling outliers
    Ignoring domain knowledge
    Over-engineering features (keep it simple!)

 Next Steps:
   - Learn about data leakage (next: cross_validation.py)
   - Practice with real messy datasets
   - Learn about time series features
   - Learn about text features (TF-IDF, embeddings)
   - Learn about image features (CNNs)
""")

print("\n Feature Engineering Complete!")
print("Next: cross_validation.py - Robust model evaluation")
