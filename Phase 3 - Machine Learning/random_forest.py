"""
 RANDOM FOREST - Wisdom of the Crowd
===========================================

What is a Random Forest?
------------------------
A collection of Decision Trees that vote together!

The Wisdom of Crowds Principle:
- One expert might be wrong
- But ask 100 experts and take the majority vote → More accurate!

Real Life Analogy:
Medical Diagnosis:
- 1 doctor: 80% accurate
- 100 doctors voting: 95% accurate!

Random Forest = 100+ Decision Trees + Majority Vote

Why "Random"?
1. Each tree trains on a RANDOM subset of data (bootstrap sampling)
2. Each split considers a RANDOM subset of features
→ Trees are different from each other (diversity!)
→ When combined, they're more robust and accurate!

The Magic: Reduces overfitting while keeping interpretability!
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.datasets import load_iris, make_classification, make_moons
import seaborn as sns

print("=" * 70)
print("RANDOM FOREST - Ensemble Learning with Multiple Trees")
print("=" * 70)

# ============================================================
# PART 1: Understanding Ensemble Learning
# ============================================================
print("\n PART 1: The Power of Ensemble Learning")
print("-" * 70)

print("""
 Core Idea: Combine Multiple Weak Models → Strong Model!

Types of Ensemble Methods:

1. BAGGING (Bootstrap Aggregating):
   - Train models on different random subsets
   - Average predictions (regression) or vote (classification)
   - Random Forest uses this!

2. BOOSTING:
   - Train models sequentially
   - Each model focuses on previous model's mistakes
   - XGBoost, AdaBoost use this

3. STACKING:
   - Train different types of models
   - Another model learns to combine their predictions

Why Ensemble Works:
- Reduces variance (less overfitting)
- More stable predictions
- Better generalization
- "Averages out" individual model errors
""")

# ============================================================
# PART 2: Single Tree vs Random Forest
# ============================================================
print("\n\n PART 2: Single Tree vs Random Forest Comparison")
print("-" * 70)

# Load iris dataset
iris = load_iris()
X = iris.data
y = iris.target
feature_names = iris.feature_names
target_names = iris.target_names

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

print(f" Dataset: Iris Flowers")
print(f"   Training samples: {len(X_train)}")
print(f"   Test samples: {len(X_test)}")
print(f"   Features: {len(feature_names)}")
print(f"   Classes: {len(target_names)}")

# Train a single decision tree
dt = DecisionTreeClassifier(random_state=42)
dt.fit(X_train, y_train)
dt_train_acc = dt.score(X_train, y_train)
dt_test_acc = dt.score(X_test, y_test)

# Train a random forest
rf = RandomForestClassifier(n_estimators=100, random_state=42)
print("\n Training Random Forest (100 trees)...")
rf.fit(X_train, y_train)
rf_train_acc = rf.score(X_train, y_train)
rf_test_acc = rf.score(X_test, y_test)
print("   Training complete! ")

print(f"\n Performance Comparison:")
print(f"{'Model':<20} {'Train Accuracy':<18} {'Test Accuracy':<18} {'Difference':<12}")
print("-" * 70)
print(f"{'Single Tree':<20} {dt_train_acc:<18.4f} {dt_test_acc:<18.4f} {abs(dt_train_acc - dt_test_acc):<12.4f}")
print(f"{'Random Forest':<20} {rf_train_acc:<18.4f} {rf_test_acc:<18.4f} {abs(rf_train_acc - rf_test_acc):<12.4f}")

print(f"\n Analysis:")
if rf_test_acc > dt_test_acc:
    print(f"    Random Forest is more accurate!")
    print(f"   Improvement: {(rf_test_acc - dt_test_acc)*100:.1f}%")
if abs(rf_train_acc - rf_test_acc) < abs(dt_train_acc - dt_test_acc):
    print(f"    Random Forest generalizes better (less overfitting)!")

# ============================================================
# PART 3: How Random Forest Works (Bootstrap + Random Features)
# ============================================================
print("\n\n PART 3: How Random Forest Creates Diversity")
print("-" * 70)

print("""
 Two Sources of Randomness:

1. BOOTSTRAP SAMPLING (Row Sampling):
   Original dataset: 100 samples
   Each tree trains on: 100 samples (randomly sampled WITH replacement)

   Example:
   Original: [1, 2, 3, 4, 5]
   Tree 1 sees: [1, 1, 3, 4, 5]  ← Sample 1 appears twice, 2 is missing
   Tree 2 sees: [1, 2, 2, 3, 5]  ← Different samples!
   Tree 3 sees: [2, 3, 4, 4, 5]  ← Different again!

2. FEATURE RANDOMNESS (Column Sampling):
   At each split, only consider √n_features random features

   Example with 4 features:
   Split 1: Consider features [A, C] only
   Split 2: Consider features [B, D] only
   Split 3: Consider features [A, B] only

   → Each tree makes different decisions!
   → Trees are DECORRELATED!
""")

# Demonstrate with a simple example
print(f"\n Random Forest Configuration:")
print(f"   Number of trees: {rf.n_estimators}")
print(f"   Max features per split: {rf.max_features}")
print(f"   Bootstrap sampling: {rf.bootstrap}")
print(f"   Out-of-bag samples used: {rf.oob_score if hasattr(rf, 'oob_score_') else 'Not enabled'}")

# ============================================================
# PART 4: Detailed Classification Example
# ============================================================
print("\n\n PART 4: Detailed Classification with Random Forest")
print("-" * 70)

# Make predictions
y_pred = rf.predict(X_test)
y_pred_proba = rf.predict_proba(X_test)

# Show some predictions
print(f"\n Sample Predictions:")
print(f"{'Actual':<15} {'Predicted':<15} {'Confidence':<12} {'Correct':<8}")
print("-" * 60)
for i in range(min(10, len(X_test))):
    actual_name = target_names[y_test[i]]
    pred_name = target_names[y_pred[i]]
    confidence = np.max(y_pred_proba[i])
    correct = '' if y_test[i] == y_pred[i] else ''
    print(f"{actual_name:<15} {pred_name:<15} {confidence:<12.4f} {correct:<8}")

# Classification report
print(f"\n Classification Report:")
print(classification_report(y_test, y_pred, target_names=target_names))

# Confusion matrix
cm = confusion_matrix(y_test, y_pred)
plt.figure(figsize=(8, 6))
sns.heatmap(cm, annot=True, fmt='d', cmap='Greens', cbar=False,
            xticklabels=target_names, yticklabels=target_names)
plt.xlabel('Predicted', fontsize=12)
plt.ylabel('Actual', fontsize=12)
plt.title('Confusion Matrix - Random Forest', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.savefig('random_forest_confusion_matrix.png', dpi=150)
print("\n Saved plot: random_forest_confusion_matrix.png")

# ============================================================
# PART 5: Feature Importance in Random Forest
# ============================================================
print("\n\n PART 5: Feature Importance - Aggregated Across All Trees")
print("-" * 70)

print("""
 How Feature Importance is Calculated:

For each tree:
1. Calculate how much each feature reduces impurity
2. Weight by number of samples passing through

Random Forest:
- Average importance across ALL trees
- More robust than single tree importance
- Less affected by outliers or noise
""")

# Get feature importances
importances = rf.feature_importances_
indices = np.argsort(importances)[::-1]

print(f"\n Feature Importance Ranking:")
for i, idx in enumerate(indices):
    print(f"   {i+1}. {feature_names[idx]:25s}: {importances[idx]:.4f}")

# Visualize
plt.figure(figsize=(10, 6))
plt.barh(range(len(feature_names)), importances[indices], color='forestgreen')
plt.yticks(range(len(feature_names)), [feature_names[i] for i in indices])
plt.xlabel('Importance', fontsize=12)
plt.ylabel('Feature', fontsize=12)
plt.title('Feature Importance in Random Forest', fontsize=14, fontweight='bold')
plt.grid(axis='x', alpha=0.3)
plt.tight_layout()
plt.savefig('random_forest_feature_importance.png', dpi=150)
print("\n Saved plot: random_forest_feature_importance.png")

print(f"\n Most important feature: {feature_names[indices[0]]}")
print(f"   This feature is consistently important across all 100 trees!")

# ============================================================
# PART 6: Number of Trees - How Many is Enough?
# ============================================================
print("\n\n PART 6: Choosing the Number of Trees")
print("-" * 70)

print("""
 How many trees should we use?

More trees:
    More stable predictions
    Better accuracy (up to a point)
    Less variance
    Slower training
    More memory

General Rule:
   - Start with 100 trees (default)
   - Increase if you have lots of data
   - 500-1000 often enough
   - Diminishing returns after that
""")

# Test different numbers of trees
n_trees_list = [1, 5, 10, 25, 50, 100, 200, 500]
train_scores = []
test_scores = []

print(f"\n Testing Different Numbers of Trees:")
print(f"{'Trees':<10} {'Train Acc':<12} {'Test Acc':<12} {'Time (rel)':<12}")
print("-" * 55)

import time

for n_trees in n_trees_list:
    start_time = time.time()
    rf_temp = RandomForestClassifier(n_estimators=n_trees, random_state=42, n_jobs=-1)
    rf_temp.fit(X_train, y_train)
    elapsed = time.time() - start_time

    train_acc = rf_temp.score(X_train, y_train)
    test_acc = rf_temp.score(X_test, y_test)

    train_scores.append(train_acc)
    test_scores.append(test_acc)

    print(f"{n_trees:<10} {train_acc:<12.4f} {test_acc:<12.4f} {elapsed:<12.3f}s")

# Plot
plt.figure(figsize=(10, 6))
plt.plot(n_trees_list, train_scores, 'bo-', linewidth=2, markersize=8, label='Training')
plt.plot(n_trees_list, test_scores, 'ro-', linewidth=2, markersize=8, label='Testing')
plt.xlabel('Number of Trees', fontsize=12)
plt.ylabel('Accuracy', fontsize=12)
plt.title('Effect of Number of Trees on Accuracy', fontsize=14, fontweight='bold')
plt.xscale('log')
plt.legend(fontsize=11)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('random_forest_n_trees.png', dpi=150)
print("\n Saved plot: random_forest_n_trees.png")
print("  Notice: Accuracy improves quickly, then plateaus")
print("  Diminishing returns after ~100 trees!")

# ============================================================
# PART 7: Visualizing Individual Trees
# ============================================================
print("\n\n PART 7: Looking Inside: Individual Trees in the Forest")
print("-" * 70)

print(f"\n Let's examine the first 3 trees:")

# Get first 3 trees
from sklearn.tree import plot_tree

fig, axes = plt.subplots(1, 3, figsize=(24, 6))

for i in range(3):
    tree = rf.estimators_[i]
    plot_tree(tree,
              feature_names=feature_names,
              class_names=target_names,
              filled=True,
              rounded=True,
              fontsize=8,
              ax=axes[i])
    axes[i].set_title(f'Tree {i+1} (of 100)', fontsize=12, fontweight='bold')

plt.tight_layout()
plt.savefig('random_forest_individual_trees.png', dpi=150)
print("\n Saved plot: random_forest_individual_trees.png")
print("  Each tree is different due to randomness!")
print("  Together, they make better predictions!")

# ============================================================
# PART 8: Hyperparameters
# ============================================================
print("\n\n PART 8: Important Hyperparameters")
print("-" * 70)

print("""
️ Key Hyperparameters to Tune:

1. n_estimators (default: 100)
   - Number of trees
   - More = better, but slower
   - Start with 100, increase if needed

2. max_depth (default: None)
   - Maximum tree depth
   - Limit to prevent overfitting
   - Try: 10, 20, 30

3. min_samples_split (default: 2)
   - Minimum samples to split a node
   - Higher = simpler trees
   - Try: 2, 5, 10

4. min_samples_leaf (default: 1)
   - Minimum samples in leaf node
   - Higher = smoother predictions
   - Try: 1, 2, 4

5. max_features (default: 'sqrt')
   - Features to consider per split
   - 'sqrt': √n_features (classification default)
   - 'log2': log₂(n_features)
   - Integer: specific number

6. bootstrap (default: True)
   - Use bootstrap sampling?
   - Keep True for randomness!

7. n_jobs (default: None)
   - Number of CPU cores to use
   - -1 = use all cores (faster!)
""")

# Example of tuning
rf_tuned = RandomForestClassifier(
    n_estimators=200,
    max_depth=10,
    min_samples_split=5,
    min_samples_leaf=2,
    max_features='sqrt',
    random_state=42,
    n_jobs=-1
)

rf_tuned.fit(X_train, y_train)
tuned_train_acc = rf_tuned.score(X_train, y_train)
tuned_test_acc = rf_tuned.score(X_test, y_test)

print(f"\n Tuned Random Forest:")
print(f"   Training Accuracy: {tuned_train_acc:.4f}")
print(f"   Test Accuracy: {tuned_test_acc:.4f}")

# ============================================================
# PART 9: Random Forest for Regression
# ============================================================
print("\n\n PART 9: Random Forest for Regression")
print("-" * 70)

print("""
 Random Forest works for regression too!

Instead of voting:
- Each tree predicts a number
- Final prediction = AVERAGE of all trees

Benefits:
- Smoother predictions than single tree
- Less affected by outliers
- Better generalization
""")

# Generate regression data
np.random.seed(42)
X_reg = np.sort(5 * np.random.rand(200, 1), axis=0)
y_reg = np.sin(X_reg).ravel() + np.random.normal(0, 0.1, 200)

# Split
X_train_reg, X_test_reg, y_train_reg, y_test_reg = train_test_split(
    X_reg, y_reg, test_size=0.3, random_state=42
)

# Train random forest regressor
rf_reg = RandomForestRegressor(n_estimators=100, max_depth=10, random_state=42)
rf_reg.fit(X_train_reg, y_train_reg)

# Also train single tree for comparison
from sklearn.tree import DecisionTreeRegressor
dt_reg = DecisionTreeRegressor(max_depth=10, random_state=42)
dt_reg.fit(X_train_reg, y_train_reg)

# Predict
X_plot = np.linspace(0, 5, 500).reshape(-1, 1)
y_rf_pred = rf_reg.predict(X_plot)
y_dt_pred = dt_reg.predict(X_plot)

# Evaluate
from sklearn.metrics import mean_squared_error, r2_score
rf_r2 = r2_score(y_test_reg, rf_reg.predict(X_test_reg))
dt_r2 = r2_score(y_test_reg, dt_reg.predict(X_test_reg))

print(f"\n Regression Performance:")
print(f"   Single Tree R²: {dt_r2:.4f}")
print(f"   Random Forest R²: {rf_r2:.4f}")
print(f"   Improvement: {(rf_r2 - dt_r2)*100:.1f}%")

# Plot
plt.figure(figsize=(12, 6))
plt.scatter(X_train_reg, y_train_reg, c='blue', s=30, alpha=0.4, label='Training Data')
plt.scatter(X_test_reg, y_test_reg, c='red', s=30, alpha=0.4, label='Test Data')
plt.plot(X_plot, y_dt_pred, 'orange', linewidth=2, label='Single Tree', alpha=0.7)
plt.plot(X_plot, y_rf_pred, 'green', linewidth=3, label='Random Forest')
plt.xlabel('X', fontsize=12)
plt.ylabel('y', fontsize=12)
plt.title('Random Forest Regression vs Single Tree', fontsize=14, fontweight='bold')
plt.legend(fontsize=11)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('random_forest_regression.png', dpi=150)
print("\n Saved plot: random_forest_regression.png")
print("  Random Forest (green) = smoother, more stable")
print("  Single Tree (orange) = jagged, overfits")

# ============================================================
# PART 10: Out-of-Bag (OOB) Evaluation
# ============================================================
print("\n\n PART 10: Out-of-Bag (OOB) Score - Free Validation!")
print("-" * 70)

print("""
 FREE Validation Set!

Remember: Each tree trains on a bootstrap sample (sampling WITH replacement)
→ About 37% of samples are NOT used for each tree
→ These are "out-of-bag" (OOB) samples

Clever Trick:
- For each sample, predict using only trees that didn't see it
- Aggregate these predictions = OOB prediction
- Compare to true labels = OOB score

Benefit: Like having a validation set WITHOUT splitting your data!
""")

# Train with OOB
rf_oob = RandomForestClassifier(n_estimators=100, oob_score=True, random_state=42)
rf_oob.fit(X_train, y_train)

print(f"\n Out-of-Bag Evaluation:")
print(f"   OOB Score: {rf_oob.oob_score_:.4f}")
print(f"   Test Score: {rf_oob.score(X_test, y_test):.4f}")
print(f"   Difference: {abs(rf_oob.oob_score_ - rf_oob.score(X_test, y_test)):.4f}")
print(f"\n OOB score is close to test score!")
print(f"   This validates our model without a separate validation set!")

# ============================================================
# WHY THIS MATTERS
# ============================================================
print("\n\n WHY RANDOM FOREST MATTERS")
print("=" * 70)
print("""
1. PRODUCTION READY:
   - Used by top companies (Uber, Netflix, Airbnb)
   - Reliable and robust
   - Handles real-world messy data well

2. STRONG PERFORMANCE:
   - Often wins Kaggle competitions
   - Great out-of-the-box performance
   - Minimal tuning needed

3. VERSATILE:
   - Works for classification and regression
   - Handles non-linear relationships
   - Works with mixed data types
   - Resistant to outliers

4. BUILT-IN VALIDATION:
   - OOB score for free validation
   - Feature importance included
   - No need for separate validation set

5. REDUCED OVERFITTING:
   - Ensemble averaging reduces variance
   - More stable than single tree
   - Better generalization

6. INTERPRETABILITY:
   - Feature importance available
   - Can inspect individual trees
   - More interpretable than neural networks

7. REAL WORLD APPLICATIONS:
   - Credit card fraud detection
   - Stock market prediction
   - Medical diagnosis
   - Customer churn prediction
   - Recommendation systems

 KEY TAKEAWAYS:
    Random Forest = Ensemble of Decision Trees
    Uses bootstrap sampling + feature randomness
    Majority vote (classification) or average (regression)
    More accurate and stable than single tree
    Less prone to overfitting
    Feature importance shows what matters
    OOB score provides free validation
    Parallelizable (fast with multiple cores)

️ LIMITATIONS:
   - Slower than single tree (trains many trees)
   - More memory (stores all trees)
   - Less interpretable than single tree (black box)
   - Predictions can be slow (query all trees)
   - Not great for very high dimensional data (>1000 features)

 When to use Random Forest:
    Tabular data (not images/text)
    Need high accuracy
    Have mixed feature types
    Want feature importance
    Need robust model (production)
    Need single interpretable rule
    Need real-time predictions (milliseconds)

 Next Steps:
   - Learn Gradient Boosting (XGBoost, LightGBM)
   - Learn hyperparameter tuning (GridSearch, RandomSearch)
   - Practice with Kaggle competitions
   - Learn about stacking and blending
   - Compare with neural networks for your data
""")

print("\n Random Forest Complete!")
print("Next: model_evaluation.py - Comprehensive model evaluation techniques")
