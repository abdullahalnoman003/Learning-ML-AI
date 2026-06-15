"""
 DECISION TREES - Making Decisions Like a Human
===================================================

What is a Decision Tree?
------------------------
A flowchart-like model that makes decisions by asking YES/NO questions!

Real Life Example: Deciding What to Wear
└─ Is it raining?
   ├─ YES → Is it cold?
   │   ├─ YES → Wear raincoat + sweater
   │   └─ NO → Wear raincoat
   └─ NO → Is it cold?
       ├─ YES → Wear sweater
       └─ NO → Wear t-shirt

Machine Learning Version:
The computer automatically learns which questions to ask and in what order!

How it Works:
1. Start with all data at the root
2. Find the best question to split the data
3. Create branches for each answer
4. Repeat for each branch
5. Stop when nodes are "pure" (mostly one class)

The Best Part: It's INTERPRETABLE! You can see exactly how it makes decisions!
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier, DecisionTreeRegressor
from sklearn.tree import plot_tree
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.datasets import load_iris
import seaborn as sns

print("=" * 70)
print("DECISION TREES - Making Decisions Like a Human")
print("=" * 70)

# ============================================================
# PART 1: Understanding Information Gain and Entropy
# ============================================================
print("\n PART 1: How Trees Choose the Best Split")
print("-" * 70)

print("""
 How does the tree decide which question to ask first?

Key Concept: ENTROPY (measure of impurity/disorder)

Entropy Formula:
   H = -Σ(p × log₂(p))
   where p = probability of each class

Examples:
   Pure node (all same class): Entropy = 0 (no disorder!)
   50/50 split: Entropy = 1 (maximum disorder!)

INFORMATION GAIN = Parent Entropy - Weighted Children Entropy
→ Choose the split with HIGHEST information gain!

Analogy: You're playing 20 questions
- Ask questions that eliminate the most possibilities
- "Is it bigger than a breadbox?" is better than "Is it blue?"
""")

def calculate_entropy(labels):
    """Calculate entropy of a set of labels"""
    _, counts = np.unique(labels, return_counts=True)
    probabilities = counts / counts.sum()
    entropy = -np.sum(probabilities * np.log2(probabilities + 1e-9))
    return entropy

# Example
dataset1 = np.array([0, 0, 0, 0, 0])  # All same class
dataset2 = np.array([0, 0, 0, 1, 1])  # Mixed
dataset3 = np.array([0, 0, 1, 1, 1])  # More mixed
dataset4 = np.array([0, 1, 0, 1, 0])  # Very mixed

print(f"\n Entropy Examples:")
print(f"   All class 0: {dataset1} → Entropy = {calculate_entropy(dataset1):.4f} (pure!)")
print(f"   Mostly 0: {dataset2} → Entropy = {calculate_entropy(dataset2):.4f}")
print(f"   More mixed: {dataset3} → Entropy = {calculate_entropy(dataset3):.4f}")
print(f"   Very mixed: {dataset4} → Entropy = {calculate_entropy(dataset4):.4f}")
print(f"\n Lower entropy = More pure = Better for classification!")

# ============================================================
# PART 2: Simple Classification Example
# ============================================================
print("\n\n PART 2: Building Your First Decision Tree")
print("-" * 70)

print("""
 Problem: Should I Play Tennis Today?

Features:
- Outlook: Sunny, Overcast, Rainy
- Temperature: Hot, Mild, Cool
- Humidity: High, Normal
- Windy: True, False

Target: Play Tennis? (Yes/No)
""")

# Create weather dataset
weather_data = pd.DataFrame({
    'Outlook': ['Sunny', 'Sunny', 'Overcast', 'Rainy', 'Rainy', 'Rainy', 'Overcast',
                'Sunny', 'Sunny', 'Rainy', 'Sunny', 'Overcast', 'Overcast', 'Rainy'],
    'Temperature': ['Hot', 'Hot', 'Hot', 'Mild', 'Cool', 'Cool', 'Cool',
                    'Mild', 'Cool', 'Mild', 'Mild', 'Mild', 'Hot', 'Mild'],
    'Humidity': ['High', 'High', 'High', 'High', 'Normal', 'Normal', 'Normal',
                 'High', 'Normal', 'Normal', 'Normal', 'High', 'Normal', 'High'],
    'Windy': [False, True, False, False, False, True, True,
              False, False, False, True, True, False, True],
    'Play': ['No', 'No', 'Yes', 'Yes', 'Yes', 'No', 'Yes',
             'No', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'No']
})

print(f"\n Weather Dataset:")
print(weather_data)

# Convert categorical to numerical (Decision Trees can handle this, but let's encode)
from sklearn.preprocessing import LabelEncoder

weather_encoded = weather_data.copy()
le = LabelEncoder()

for col in ['Outlook', 'Temperature', 'Humidity', 'Windy', 'Play']:
    weather_encoded[col] = le.fit_transform(weather_data[col])

print(f"\n Encoded Dataset (for ML):")
print(weather_encoded)

# Prepare data
X = weather_encoded[['Outlook', 'Temperature', 'Humidity', 'Windy']].values
y = weather_encoded['Play'].values

# Create and train decision tree
dt_clf = DecisionTreeClassifier(max_depth=3, random_state=42)
dt_clf.fit(X, y)

print(f"\n Decision Tree Created!")
print(f"   Tree depth: {dt_clf.get_depth()}")
print(f"   Number of leaves: {dt_clf.get_n_leaves()}")

# Visualize the tree
plt.figure(figsize=(20, 10))
plot_tree(dt_clf,
          feature_names=['Outlook', 'Temperature', 'Humidity', 'Windy'],
          class_names=['No', 'Yes'],
          filled=True,
          rounded=True,
          fontsize=10)
plt.title('Decision Tree: Play Tennis?', fontsize=16, fontweight='bold')
plt.tight_layout()
plt.savefig('decision_tree_simple.png', dpi=150)
print("\n Saved plot: decision_tree_simple.png")
print("  Look at the tree! It learned to make decisions automatically!")

# ============================================================
# PART 3: Real Dataset - Iris Flowers
# ============================================================
print("\n\n PART 3: Real World Example - Iris Flower Classification")
print("-" * 70)

print("""
 Famous Dataset: Iris Flowers

3 Species:
- Setosa
- Versicolor
- Virginica

4 Features:
- Sepal Length (cm)
- Sepal Width (cm)
- Petal Length (cm)
- Petal Width (cm)

Can a tree learn to identify the species?
""")

# Load iris dataset
iris = load_iris()
X_iris = iris.data
y_iris = iris.target
feature_names = iris.feature_names
target_names = iris.target_names

# Create DataFrame for easy viewing
iris_df = pd.DataFrame(X_iris, columns=feature_names)
iris_df['species'] = [target_names[i] for i in y_iris]

print(f"\n Iris Dataset:")
print(iris_df.head(10))
print(f"\n Dataset Info:")
print(f"   Samples: {len(X_iris)}")
print(f"   Features: {len(feature_names)}")
print(f"   Classes: {len(target_names)}")

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X_iris, y_iris, test_size=0.3, random_state=42
)

print(f"\n️ Data Split:")
print(f"   Training: {len(X_train)} samples")
print(f"   Testing: {len(X_test)} samples")

# ============================================================
# PART 4: Training Decision Tree
# ============================================================
print("\n\n PART 4: Training Decision Tree on Iris")
print("-" * 70)

# Train tree with limited depth
dt = DecisionTreeClassifier(max_depth=3, random_state=42)
print("\n Training Decision Tree...")
dt.fit(X_train, y_train)
print("   Training complete! ")

# Make predictions
y_pred = dt.predict(X_test)

# Evaluate
accuracy = accuracy_score(y_test, y_pred)
print(f"\n Model Performance:")
print(f"   Accuracy: {accuracy:.4f} ({accuracy*100:.2f}%)")

# Detailed report
print(f"\n Classification Report:")
print(classification_report(y_test, y_pred, target_names=target_names))

# Confusion matrix
cm = confusion_matrix(y_test, y_pred)
plt.figure(figsize=(8, 6))
sns.heatmap(cm, annot=True, fmt='d', cmap='Greens', cbar=False,
            xticklabels=target_names, yticklabels=target_names)
plt.xlabel('Predicted', fontsize=12)
plt.ylabel('Actual', fontsize=12)
plt.title('Confusion Matrix - Iris Classification', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.savefig('decision_tree_confusion_matrix.png', dpi=150)
print("\n Saved plot: decision_tree_confusion_matrix.png")

# ============================================================
# PART 5: Visualizing the Decision Tree
# ============================================================
print("\n\n PART 5: Visualizing the Decision Tree")
print("-" * 70)

plt.figure(figsize=(25, 12))
plot_tree(dt,
          feature_names=feature_names,
          class_names=target_names,
          filled=True,
          rounded=True,
          fontsize=11)
plt.title('Decision Tree for Iris Classification', fontsize=18, fontweight='bold')
plt.tight_layout()
plt.savefig('decision_tree_iris.png', dpi=150)
print("\n Saved plot: decision_tree_iris.png")

print(f"\n Understanding the Tree Visualization:")
print(f"""
Each box shows:
   - Decision rule (e.g., "petal length <= 2.45")
   - Gini impurity (lower = purer)
   - Samples: number of training samples reaching this node
   - Value: [count for each class]
   - Class: predicted class (if leaf node)

How to read it:
   1. Start at top (root)
   2. Follow the decision rules
   3. End at a leaf (final prediction)

Example: A flower with petal length 1.5 cm
   → Goes LEFT (1.5 <= 2.45)
   → Predicted as Setosa!
""")

# ============================================================
# PART 6: Feature Importance
# ============================================================
print("\n\n PART 6: Feature Importance - Which Features Matter Most?")
print("-" * 70)

# Get feature importances
feature_importance = dt.feature_importances_
importance_df = pd.DataFrame({
    'Feature': feature_names,
    'Importance': feature_importance
}).sort_values('Importance', ascending=False)

print(f"\n Feature Importance:")
print(importance_df.to_string(index=False))

# Visualize
plt.figure(figsize=(10, 6))
plt.barh(importance_df['Feature'], importance_df['Importance'], color='forestgreen')
plt.xlabel('Importance', fontsize=12)
plt.ylabel('Feature', fontsize=12)
plt.title('Feature Importance in Decision Tree', fontsize=14, fontweight='bold')
plt.grid(axis='x', alpha=0.3)
plt.tight_layout()
plt.savefig('decision_tree_feature_importance.png', dpi=150)
print("\n Saved plot: decision_tree_feature_importance.png")

print(f"\n Most Important Feature: {importance_df.iloc[0]['Feature']}")
print(f"   This feature provides the most information for classification!")

# ============================================================
# PART 7: Overfitting Problem
# ============================================================
print("\n\n PART 7: The Overfitting Problem")
print("-" * 70)

print("""
️ DANGER: Decision Trees Can Memorize!

Without constraints, a tree will grow until every training sample
is in its own leaf. This is OVERFITTING!

Result:
- Training accuracy: 100% (perfect!)
- Test accuracy: 70% (terrible!)
- The tree memorized noise instead of learning patterns

Solution: Pruning (limit tree growth)
""")

# Train trees with different depths
depths = [1, 2, 3, 5, 10, None]  # None = unlimited
train_accuracies = []
test_accuracies = []
n_leaves = []

print(f"\n Effect of Tree Depth:")
print(f"{'Depth':<10} {'Leaves':<10} {'Train Acc':<12} {'Test Acc':<12} {'Status':<20}")
print("-" * 70)

for depth in depths:
    dt_temp = DecisionTreeClassifier(max_depth=depth, random_state=42)
    dt_temp.fit(X_train, y_train)

    train_acc = dt_temp.score(X_train, y_train)
    test_acc = dt_temp.score(X_test, y_test)
    leaves = dt_temp.get_n_leaves()

    train_accuracies.append(train_acc)
    test_accuracies.append(test_acc)
    n_leaves.append(leaves)

    # Determine status
    if abs(train_acc - test_acc) < 0.05:
        status = "Good balance "
    elif train_acc > test_acc + 0.1:
        status = "Overfitting ️"
    else:
        status = "Underfitting ️"

    depth_str = "Unlimited" if depth is None else str(depth)
    print(f"{depth_str:<10} {leaves:<10} {train_acc:<12.4f} {test_acc:<12.4f} {status:<20}")

# Plot
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

# Plot 1: Accuracy vs Depth
depth_labels = [str(d) if d is not None else 'Unlimited' for d in depths]
x_pos = range(len(depths))
ax1.plot(x_pos, train_accuracies, 'bo-', linewidth=2, markersize=8, label='Training')
ax1.plot(x_pos, test_accuracies, 'ro-', linewidth=2, markersize=8, label='Testing')
ax1.set_xticks(x_pos)
ax1.set_xticklabels(depth_labels)
ax1.set_xlabel('Tree Depth', fontsize=12)
ax1.set_ylabel('Accuracy', fontsize=12)
ax1.set_title('Overfitting: Train vs Test Accuracy', fontsize=13, fontweight='bold')
ax1.legend(fontsize=11)
ax1.grid(True, alpha=0.3)

# Plot 2: Number of leaves
ax2.bar(x_pos, n_leaves, color='green', alpha=0.7)
ax2.set_xticks(x_pos)
ax2.set_xticklabels(depth_labels)
ax2.set_xlabel('Tree Depth', fontsize=12)
ax2.set_ylabel('Number of Leaves', fontsize=12)
ax2.set_title('Tree Complexity (Leaf Count)', fontsize=13, fontweight='bold')
ax2.grid(axis='y', alpha=0.3)

plt.tight_layout()
plt.savefig('decision_tree_overfitting.png', dpi=150)
print("\n Saved plot: decision_tree_overfitting.png")
print("  Notice: Unlimited depth has perfect training but lower test accuracy!")

# ============================================================
# PART 8: Hyperparameters for Controlling Trees
# ============================================================
print("\n\n PART 8: Hyperparameters - Controlling Tree Growth")
print("-" * 70)

print("""
️ Key Hyperparameters:

1. max_depth: Maximum tree depth
   - Lower = simpler tree (may underfit)
   - Higher = complex tree (may overfit)

2. min_samples_split: Minimum samples to split a node
   - Higher = prevents splitting on small groups

3. min_samples_leaf: Minimum samples in each leaf
   - Higher = smoother predictions

4. max_features: Number of features to consider for best split
   - Lower = more randomness, prevents overfitting

5. criterion: 'gini' or 'entropy'
   - Gini: faster to compute
   - Entropy: theoretically better, but similar in practice
""")

# Example with different parameters
dt_pruned = DecisionTreeClassifier(
    max_depth=4,
    min_samples_split=10,
    min_samples_leaf=5,
    random_state=42
)

dt_pruned.fit(X_train, y_train)
train_acc_pruned = dt_pruned.score(X_train, y_train)
test_acc_pruned = dt_pruned.score(X_test, y_test)

print(f"\n Well-Tuned Tree:")
print(f"   Parameters: max_depth=4, min_samples_split=10, min_samples_leaf=5")
print(f"   Training Accuracy: {train_acc_pruned:.4f}")
print(f"   Test Accuracy: {test_acc_pruned:.4f}")
print(f"   Tree Depth: {dt_pruned.get_depth()}")
print(f"   Number of Leaves: {dt_pruned.get_n_leaves()}")

# ============================================================
# PART 9: Decision Trees for Regression
# ============================================================
print("\n\n PART 9: Decision Trees for Regression")
print("-" * 70)

print("""
 Trees Work for Regression Too!

Instead of voting for a class, leaves contain the AVERAGE value
of training samples in that leaf.

Example: Predicting house prices
- Tree splits based on features (size, bedrooms, etc.)
- Each leaf predicts average price of houses in that region
""")

# Generate regression data
np.random.seed(42)
X_reg = np.sort(5 * np.random.rand(100, 1), axis=0)
y_reg = np.sin(X_reg).ravel() + np.random.normal(0, 0.1, 100)

# Train regression tree
dt_reg = DecisionTreeRegressor(max_depth=5, random_state=42)
dt_reg.fit(X_reg, y_reg)

# Predict
X_test_reg = np.linspace(0, 5, 300).reshape(-1, 1)
y_pred_reg = dt_reg.predict(X_test_reg)

# Evaluate
from sklearn.metrics import mean_squared_error, r2_score
y_pred_train_reg = dt_reg.predict(X_reg)
mse = mean_squared_error(y_reg, y_pred_train_reg)
r2 = r2_score(y_reg, y_pred_train_reg)

print(f"\n Regression Tree Performance:")
print(f"   R² Score: {r2:.4f}")
print(f"   MSE: {mse:.4f}")

# Plot
plt.figure(figsize=(10, 6))
plt.scatter(X_reg, y_reg, c='blue', s=50, alpha=0.6, label='Data')
plt.plot(X_test_reg, y_pred_reg, 'r-', linewidth=3, label='Decision Tree Prediction')
plt.xlabel('X', fontsize=12)
plt.ylabel('y', fontsize=12)
plt.title('Decision Tree Regression', fontsize=14, fontweight='bold')
plt.legend(fontsize=11)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('decision_tree_regression.png', dpi=150)
print("\n Saved plot: decision_tree_regression.png")
print("  Notice: The prediction is piecewise constant (step function)")
print("  Each horizontal segment = one leaf node's prediction")

# ============================================================
# WHY THIS MATTERS
# ============================================================
print("\n\n WHY DECISION TREES MATTER")
print("=" * 70)
print("""
1. INTERPRETABILITY:
   - You can SEE exactly how decisions are made
   - Easy to explain to stakeholders
   - Can be converted to business rules
   - "If petal length < 2.5, then it's Setosa"

2. NO FEATURE SCALING NEEDED:
   - Doesn't care about feature ranges
   - Works with raw data (unlike KNN, SVM)
   - Saves preprocessing time

3. HANDLES NON-LINEAR RELATIONSHIPS:
   - Can capture complex patterns
   - No need to assume linear relationships
   - Automatically finds interactions between features

4. WORKS WITH MIXED DATA:
   - Handles both numerical and categorical features
   - Can handle missing values (with modifications)

5. FOUNDATION FOR POWERFUL MODELS:
   - Random Forests = Multiple trees (more accurate!)
   - Gradient Boosting = Sequential trees (even better!)
   - XGBoost, LightGBM = State-of-the-art models

6. REAL WORLD APPLICATIONS:
   - Medical diagnosis (interpretable!)
   - Credit approval (explain decisions to customers)
   - Customer segmentation
   - Fraud detection
   - Recommendation systems

 KEY TAKEAWAYS:
    Decision trees ask YES/NO questions to classify
    Information gain determines best splits
    Feature importance shows which features matter
    Must control tree depth to prevent overfitting
    Works for both classification and regression
    No feature scaling needed!
    Highly interpretable (you can see the logic)

️ LIMITATIONS:
   - Prone to overfitting (grows too complex)
   - Unstable (small data changes → different tree)
   - Biased toward features with many values
   - Creates step functions (not smooth predictions)
   - Can create overly complex trees (hard to interpret)

 Best Practices:
    Always limit max_depth (start with 3-5)
    Use min_samples_split and min_samples_leaf
    Compare train vs test accuracy (check overfitting)
    Visualize the tree (if small enough)
    Check feature importance
    Don't use unlimited depth trees in production!

 Next Steps:
   - Learn Random Forests (ensemble of trees = more stable!)
   - Learn Gradient Boosting (sequential improvement)
   - Practice with real datasets
   - Learn about tree pruning techniques
""")

print("\n Decision Trees Complete!")
print("Next: random_forest.py - Ensemble learning with multiple trees")
