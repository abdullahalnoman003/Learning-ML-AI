"""
 LINEAR REGRESSION WITH SCIKIT-LEARN - Professional ML
==========================================================

What is Scikit-Learn?
---------------------
Scikit-learn is THE standard library for machine learning in Python.
It's like going from building a car by hand to using a car factory!

Benefits:
- Optimized C code (FAST!)
- Consistent API (all models work the same way)
- Built-in validation and metrics
- Production-ready code

The Scikit-Learn Workflow (memorize this!):
1. Import the model class
2. Create an instance: model = Model()
3. Fit to data: model.fit(X, y)
4. Make predictions: model.predict(X_new)

That's it! 4 steps for ANY model in scikit-learn!
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
import seaborn as sns

print("=" * 70)
print("LINEAR REGRESSION WITH SCIKIT-LEARN - Professional ML")
print("=" * 70)

# ============================================================
# PART 1: Simple Linear Regression (One Feature)
# ============================================================
print("\n PART 1: Simple Linear Regression (One Feature)")
print("-" * 70)

# Generate sample data: house prices based on size
np.random.seed(42)
house_sizes = np.array([750, 800, 850, 900, 950, 1000, 1100, 1200, 1300, 1400,
                        1500, 1600, 1700, 1800, 1900, 2000, 2100, 2200, 2300, 2400])
noise = np.random.randn(20) * 10000
house_prices = 50 * house_sizes + 100000 + noise

print(f"Dataset: {len(house_sizes)} houses")
print(f"Feature: House size (sq ft)")
print(f"Target: Price ($)")

# Reshape for sklearn (must be 2D)
X = house_sizes.reshape(-1, 1)  # -1 means "figure out the size"
y = house_prices

print(f"\n Data shape:")
print(f"   X shape: {X.shape}   (samples, features)")
print(f"   y shape: {y.shape}   (samples,)")
print(f"    sklearn needs X to be 2D: (n_samples, n_features)")

# Create and train the model
print("\n️ Creating Linear Regression model...")
model = LinearRegression()
print("   Model created! ")

print("\n Training the model...")
model.fit(X, y)
print("   Training complete! ")
print("    Behind the scenes: gradient descent optimized the parameters")

# Get learned parameters
print(f"\n Learned Parameters:")
print(f"   Coefficient (slope): {model.coef_[0]:.2f}")
print(f"   Intercept (bias): {model.intercept_:.2f}")
print(f"   Equation: Price = {model.coef_[0]:.2f} × Size + {model.intercept_:.2f}")

# Make predictions
predictions = model.predict(X)

# Evaluate
r2 = r2_score(y, predictions)
rmse = np.sqrt(mean_squared_error(y, predictions))
mae = mean_absolute_error(y, predictions)

print(f"\n Model Performance:")
print(f"   R² Score: {r2:.4f} ({r2*100:.2f}% variance explained)")
print(f"   RMSE: ${rmse:,.2f}")
print(f"   MAE: ${mae:,.2f}")

# Visualize
plt.figure(figsize=(10, 6))
plt.scatter(X, y, color='blue', alpha=0.6, s=100, label='Actual Data')
plt.plot(X, predictions, 'r-', linewidth=3, label='Predictions')
plt.xlabel('House Size (sq ft)', fontsize=12)
plt.ylabel('Price ($)', fontsize=12)
plt.title('Simple Linear Regression with Scikit-Learn', fontsize=14, fontweight='bold')
plt.legend(fontsize=11)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('sklearn_simple_regression.png', dpi=150)
print("\n Saved plot: sklearn_simple_regression.png")

# ============================================================
# PART 2: Multiple Linear Regression (Multiple Features)
# ============================================================
print("\n\n PART 2: Multiple Linear Regression (Multiple Features)")
print("-" * 70)

print("""
 Real World Example: Predicting house prices with multiple factors!

Now we'll use:
- Size (sq ft)
- Number of bedrooms
- Age of house (years)
- Distance to city center (miles)

Equation: Price = w₁×Size + w₂×Bedrooms + w₃×Age + w₄×Distance + b
""")

# Generate more realistic dataset
np.random.seed(42)
n_samples = 100

data = {
    'Size': np.random.randint(800, 3000, n_samples),
    'Bedrooms': np.random.randint(1, 6, n_samples),
    'Age': np.random.randint(0, 50, n_samples),
    'Distance_to_City': np.random.uniform(0.5, 20, n_samples),
}

# Create target: price depends on all features
df = pd.DataFrame(data)
df['Price'] = (
    50 * df['Size'] +
    20000 * df['Bedrooms'] -
    1000 * df['Age'] -
    2000 * df['Distance_to_City'] +
    100000 +
    np.random.randn(n_samples) * 15000  # Add noise
)

print(f"\n Dataset Preview:")
print(df.head(10))
print(f"\n Dataset Info:")
print(f"   Samples: {len(df)}")
print(f"   Features: {len(df.columns) - 1}")
print(f"\n Statistical Summary:")
print(df.describe())

# ============================================================
# PART 3: Train-Test Split (CRUCIAL!)
# ============================================================
print("\n\n PART 3: Train-Test Split")
print("-" * 70)

print("""
 WHY Split Data?

Problem: If we test on the same data we trained on, the model might
         just MEMORIZE the answers instead of learning patterns!
         This is called OVERFITTING.

Solution: Split data into:
- Training set (80%): Model learns from this
- Test set (20%): Model is evaluated on this (unseen data)

It's like studying from practice problems, then taking a real exam!
""")

# Separate features (X) and target (y)
X = df[['Size', 'Bedrooms', 'Age', 'Distance_to_City']].values
y = df['Price'].values

print(f"\nOriginal data shape: {X.shape}")

# Split the data
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,     # 20% for testing
    random_state=42    # For reproducibility
)

print(f"\n️ After splitting:")
print(f"   Training set: {X_train.shape[0]} samples ({X_train.shape[0]/len(X)*100:.0f}%)")
print(f"   Test set: {X_test.shape[0]} samples ({X_test.shape[0]/len(X)*100:.0f}%)")
print(f"    Model will train on {X_train.shape[0]} houses")
print(f"    Model will be tested on {X_test.shape[0]} NEW houses")

# ============================================================
# PART 4: Training the Multiple Regression Model
# ============================================================
print("\n\n PART 4: Training Multiple Linear Regression")
print("-" * 70)

# Create and train model
model_multi = LinearRegression()
print("\n Training on multiple features...")
model_multi.fit(X_train, y_train)
print("   Training complete! ")

# Display learned parameters
print(f"\n Learned Parameters:")
print(f"   Intercept: ${model_multi.intercept_:,.2f}")
print(f"\n   Feature Coefficients:")
feature_names = ['Size', 'Bedrooms', 'Age', 'Distance_to_City']
for name, coef in zip(feature_names, model_multi.coef_):
    print(f"   - {name:20s}: {coef:10.2f}")

print(f"\n Interpretation:")
print(f"   - Each extra sq ft adds: ${model_multi.coef_[0]:.2f}")
print(f"   - Each extra bedroom adds: ${model_multi.coef_[1]:,.2f}")
print(f"   - Each year older reduces: ${abs(model_multi.coef_[2]):,.2f}")
print(f"   - Each mile from city reduces: ${abs(model_multi.coef_[3]):,.2f}")

# ============================================================
# PART 5: Making Predictions
# ============================================================
print("\n\n PART 5: Making Predictions")
print("-" * 70)

# Predict on training data
y_train_pred = model_multi.predict(X_train)

# Predict on test data (UNSEEN!)
y_test_pred = model_multi.predict(X_test)

print("\n Example Predictions (Test Set):")
print(f"{'Size':<8} {'Beds':<6} {'Age':<6} {'Dist':<8} {'Actual':<12} {'Predicted':<12} {'Error':<10}")
print("-" * 80)
for i in range(min(10, len(X_test))):
    actual = y_test[i]
    predicted = y_test_pred[i]
    error = abs(actual - predicted)
    print(f"{X_test[i, 0]:<8.0f} {X_test[i, 1]:<6.0f} {X_test[i, 2]:<6.0f} "
          f"{X_test[i, 3]:<8.1f} ${actual:<11,.0f} ${predicted:<11,.0f} ${error:<9,.0f}")

# ============================================================
# PART 6: Model Evaluation
# ============================================================
print("\n\n PART 6: Model Evaluation")
print("-" * 70)

# Training metrics
train_r2 = r2_score(y_train, y_train_pred)
train_rmse = np.sqrt(mean_squared_error(y_train, y_train_pred))
train_mae = mean_absolute_error(y_train, y_train_pred)

# Test metrics (MOST IMPORTANT!)
test_r2 = r2_score(y_test, y_test_pred)
test_rmse = np.sqrt(mean_squared_error(y_test, y_test_pred))
test_mae = mean_absolute_error(y_test, y_test_pred)

print(f"\n Training Set Performance:")
print(f"   R² Score: {train_r2:.4f}")
print(f"   RMSE: ${train_rmse:,.2f}")
print(f"   MAE: ${train_mae:,.2f}")

print(f"\n Test Set Performance (UNSEEN DATA!):")
print(f"   R² Score: {test_r2:.4f}")
print(f"   RMSE: ${test_rmse:,.2f}")
print(f"   MAE: ${test_mae:,.2f}")

print(f"\n Analysis:")
if abs(train_r2 - test_r2) < 0.05:
    print(f"    Train and test scores are similar!")
    print(f"    Model generalizes well (not overfitting)")
else:
    print(f"   ️ Train and test scores differ")
    if train_r2 > test_r2:
        print(f"   ️ Possible overfitting (memorizing training data)")
    else:
        print(f"   ️ Possible underfitting (model too simple)")

# ============================================================
# PART 7: Residual Analysis
# ============================================================
print("\n\n PART 7: Residual Analysis (Error Analysis)")
print("-" * 70)

print("""
 What are Residuals?
   Residual = Actual - Predicted (the error for each prediction)

   Good model: Residuals are:
   - Small (close to zero)
   - Randomly distributed (no patterns)
   - Normally distributed (bell curve)
""")

# Calculate residuals
residuals = y_test - y_test_pred

print(f"\n Residual Statistics:")
print(f"   Mean: ${np.mean(residuals):,.2f} (should be close to 0)")
print(f"   Std Dev: ${np.std(residuals):,.2f}")
print(f"   Min: ${np.min(residuals):,.2f}")
print(f"   Max: ${np.max(residuals):,.2f}")

# Visualize residuals
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# Plot 1: Predicted vs Actual
axes[0].scatter(y_test, y_test_pred, alpha=0.6, s=50)
axes[0].plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--', linewidth=2)
axes[0].set_xlabel('Actual Price ($)', fontsize=11)
axes[0].set_ylabel('Predicted Price ($)', fontsize=11)
axes[0].set_title('Predicted vs Actual Prices', fontsize=12, fontweight='bold')
axes[0].grid(True, alpha=0.3)

# Plot 2: Residual distribution
axes[1].hist(residuals, bins=20, edgecolor='black', alpha=0.7)
axes[1].set_xlabel('Residual ($)', fontsize=11)
axes[1].set_ylabel('Frequency', fontsize=11)
axes[1].set_title('Residual Distribution', fontsize=12, fontweight='bold')
axes[1].axvline(x=0, color='r', linestyle='--', linewidth=2)
axes[1].grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('sklearn_residual_analysis.png', dpi=150)
print("\n Saved plot: sklearn_residual_analysis.png")
print("  Left plot: Points should fall near the red line")
print("  Right plot: Should look like a bell curve centered at 0")

# ============================================================
# PART 8: Feature Importance
# ============================================================
print("\n\n PART 8: Feature Importance")
print("-" * 70)

# Get absolute coefficients (importance)
feature_importance = pd.DataFrame({
    'Feature': feature_names,
    'Coefficient': model_multi.coef_,
    'Abs_Coefficient': np.abs(model_multi.coef_)
})
feature_importance = feature_importance.sort_values('Abs_Coefficient', ascending=False)

print("\n Feature Importance (by absolute coefficient):")
print(feature_importance.to_string(index=False))
print(f"\n Most important feature: {feature_importance.iloc[0]['Feature']}")
print(f"   It has the largest impact on price!")

# Visualize
plt.figure(figsize=(10, 6))
plt.barh(feature_importance['Feature'], feature_importance['Abs_Coefficient'], color='steelblue')
plt.xlabel('Absolute Coefficient Value', fontsize=12)
plt.ylabel('Feature', fontsize=12)
plt.title('Feature Importance in House Price Prediction', fontsize=14, fontweight='bold')
plt.grid(axis='x', alpha=0.3)
plt.tight_layout()
plt.savefig('sklearn_feature_importance.png', dpi=150)
print("\n Saved plot: sklearn_feature_importance.png")

# ============================================================
# PART 9: Making Predictions on New Data
# ============================================================
print("\n\n PART 9: Making Predictions on Completely New Houses")
print("-" * 70)

# Create new house data
new_houses = np.array([
    [1500, 3, 5, 8.0],    # 1500 sq ft, 3 bed, 5 years old, 8 miles from city
    [2000, 4, 0, 2.0],    # 2000 sq ft, 4 bed, brand new, 2 miles from city
    [1200, 2, 20, 15.0],  # 1200 sq ft, 2 bed, 20 years old, 15 miles from city
])

predictions_new = model_multi.predict(new_houses)

print("\n New House Predictions:")
print(f"{'Size':<8} {'Beds':<6} {'Age':<6} {'Distance':<12} {'Predicted Price':<15}")
print("-" * 60)
for i, house in enumerate(new_houses):
    print(f"{house[0]:<8.0f} {house[1]:<6.0f} {house[2]:<6.0f} {house[3]:<12.1f} ${predictions_new[i]:>13,.2f}")

# ============================================================
# PART 10: Saving and Loading Models
# ============================================================
print("\n\n PART 10: Saving Your Trained Model")
print("-" * 70)

import pickle

# Save model to file
model_filename = 'house_price_model.pkl'
with open(model_filename, 'wb') as file:
    pickle.dump(model_multi, file)

print(f"\n Model saved to: house_price_model.pkl")
print("   You can now load it anytime without retraining!")

# Load model back
with open(model_filename, 'rb') as file:
    loaded_model = pickle.load(file)

print(f"\n Model loaded successfully!")

# Test loaded model
test_prediction = loaded_model.predict([[2000, 4, 10, 5.0]])
print(f"   Test prediction: ${test_prediction[0]:,.2f}")
print("    Loaded model works perfectly!")

# ============================================================
# WHY THIS MATTERS
# ============================================================
print("\n\n WHY SCIKIT-LEARN MATTERS")
print("=" * 70)
print("""
1. PRODUCTION READY:
   - Used by companies like Spotify, Booking.com, J.P. Morgan
   - Fast, tested, and reliable
   - Easy to deploy in real applications

2. CONSISTENT API:
   - Same workflow for ALL models (regression, classification, clustering)
   - fit() → train the model
   - predict() → make predictions
   - score() → evaluate performance

3. BATTERIES INCLUDED:
   - Built-in data splitting (train_test_split)
   - Built-in metrics (r2_score, accuracy, etc.)
   - Built-in preprocessing (scaling, encoding)
   - Built-in model selection (cross-validation, grid search)

4. WELL DOCUMENTED:
   - Excellent documentation with examples
   - Large community (Stack Overflow has tons of answers)
   - Used in most ML courses and books

5. INTEGRATES WITH EVERYTHING:
   - Works seamlessly with NumPy and Pandas
   - Can be saved with pickle or joblib
   - Easily deployed to web servers (Flask, FastAPI)

 KEY TAKEAWAYS:
    Always split your data (train/test)
    Evaluate on test set (unseen data)
    Check for overfitting (train vs test performance)
    Analyze residuals to diagnose problems
    Feature importance helps understand your model
    Save trained models for reuse

 Next Steps:
   - Learn other regression types (Ridge, Lasso, ElasticNet)
   - Try polynomial features for non-linear relationships
   - Learn cross-validation for better evaluation
   - Move to classification problems (Logistic Regression)
""")

print("\n Scikit-Learn Linear Regression Complete!")
print("Next: logistic_regression.py - Binary classification problems")
