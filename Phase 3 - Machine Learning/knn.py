"""
👥 K-NEAREST NEIGHBORS (KNN) - Learning from Similarity
========================================================

What is KNN?
------------
The simplest ML algorithm that actually works!

Core Idea: "You are the average of your 5 closest friends"
- To classify a new point, look at its K nearest neighbors
- Take a vote: majority class wins!
- No training phase - just memorize the data!

Real World Analogy:
Imagine you're house hunting and want to know the price:
1. Find 5 most similar houses (size, bedrooms, location)
2. Average their prices
3. That's your estimate!

How it Works:
1. Choose K (number of neighbors)
2. Calculate distance to all training points
3. Find K nearest neighbors
4. For classification: Take majority vote
5. For regression: Take average

The Magic: It's "lazy learning" - no training, just stores data!
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier, KNeighborsRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import make_classification, make_moons
import seaborn as sns

print("=" * 70)
print("K-NEAREST NEIGHBORS (KNN) - Learning from Similarity")
print("=" * 70)

# ============================================================
# PART 1: Understanding Distance
# ============================================================
print("\n📌 PART 1: Understanding Distance - The Heart of KNN")
print("-" * 70)

print("""
🎯 How do we measure "closeness"?

Euclidean Distance (most common):
   d = √[(x₁-x₂)² + (y₁-y₂)²]

   Like measuring with a ruler - straight line distance!

Example:
   Point A: (2, 3)
   Point B: (5, 7)
   Distance = √[(5-2)² + (7-3)²] = √[9 + 16] = √25 = 5
""")

def euclidean_distance(point1, point2):
    """Calculate Euclidean distance between two points"""
    return np.sqrt(np.sum((point1 - point2) ** 2))

# Example points
pointA = np.array([2, 3])
pointB = np.array([5, 7])
pointC = np.array([1, 3])

dist_AB = euclidean_distance(pointA, pointB)
dist_AC = euclidean_distance(pointA, pointC)

print(f"\n📏 Distance Examples:")
print(f"   Point A: {pointA}")
print(f"   Point B: {pointB}")
print(f"   Point C: {pointC}")
print(f"\n   Distance A to B: {dist_AB:.2f}")
print(f"   Distance A to C: {dist_AC:.2f}")
print(f"   → Point C is closer to A than B is!")

# Visualize
plt.figure(figsize=(8, 8))
plt.scatter(*pointA, s=200, c='red', marker='o', label='Point A', edgecolors='black', linewidths=2)
plt.scatter(*pointB, s=200, c='blue', marker='s', label='Point B', edgecolors='black', linewidths=2)
plt.scatter(*pointC, s=200, c='green', marker='^', label='Point C', edgecolors='black', linewidths=2)
plt.plot([pointA[0], pointB[0]], [pointA[1], pointB[1]], 'b--', linewidth=2, alpha=0.7)
plt.plot([pointA[0], pointC[0]], [pointA[1], pointC[1]], 'g--', linewidth=2, alpha=0.7)
plt.text((pointA[0]+pointB[0])/2, (pointA[1]+pointB[1])/2 + 0.3, f'd={dist_AB:.2f}', fontsize=11, fontweight='bold')
plt.text((pointA[0]+pointC[0])/2, (pointA[1]+pointC[1])/2 - 0.5, f'd={dist_AC:.2f}', fontsize=11, fontweight='bold')
plt.xlabel('X coordinate', fontsize=12)
plt.ylabel('Y coordinate', fontsize=12)
plt.title('Euclidean Distance Between Points', fontsize=14, fontweight='bold')
plt.legend(fontsize=11)
plt.grid(True, alpha=0.3)
plt.axis('equal')
plt.tight_layout()
plt.savefig('D:/Language Learning/AI ML/Learning-ML-AI/Phase 3 - Machine Learning/knn_distance.png', dpi=150)
print("\n✓ Saved plot: knn_distance.png")

# ============================================================
# PART 2: Creating Classification Dataset
# ============================================================
print("\n\n📌 PART 2: Binary Classification with KNN")
print("-" * 70)

print("""
🎯 Problem: Classifying Fruits (Apple vs Orange)

Features:
- Weight (grams)
- Diameter (cm)

Can KNN learn the difference?
""")

# Generate fruit data
np.random.seed(42)

# Apples: lighter and smaller
n_apples = 50
apple_weights = np.random.normal(150, 20, n_apples)
apple_diameters = np.random.normal(7, 1, n_apples)
apple_labels = np.zeros(n_apples)  # 0 = Apple

# Oranges: heavier and larger
n_oranges = 50
orange_weights = np.random.normal(200, 25, n_oranges)
orange_diameters = np.random.normal(9, 1, n_oranges)
orange_labels = np.ones(n_oranges)  # 1 = Orange

# Combine
weights = np.concatenate([apple_weights, orange_weights])
diameters = np.concatenate([apple_diameters, orange_diameters])
labels = np.concatenate([apple_labels, orange_labels])

df = pd.DataFrame({
    'Weight': weights,
    'Diameter': diameters,
    'Fruit': ['Apple' if label == 0 else 'Orange' for label in labels]
})

print(f"\n📊 Dataset Overview:")
print(df.head(10))
print(f"\n📈 Class Distribution:")
print(df['Fruit'].value_counts())

# Visualize
plt.figure(figsize=(10, 6))
plt.scatter(df[df['Fruit'] == 'Apple']['Weight'],
            df[df['Fruit'] == 'Apple']['Diameter'],
            c='red', marker='o', s=100, alpha=0.7, label='Apple', edgecolors='black')
plt.scatter(df[df['Fruit'] == 'Orange']['Weight'],
            df[df['Fruit'] == 'Orange']['Diameter'],
            c='orange', marker='s', s=100, alpha=0.7, label='Orange', edgecolors='black')
plt.xlabel('Weight (grams)', fontsize=12)
plt.ylabel('Diameter (cm)', fontsize=12)
plt.title('Fruit Classification Dataset', fontsize=14, fontweight='bold')
plt.legend(fontsize=11)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('D:/Language Learning/AI ML/Learning-ML-AI/Phase 3 - Machine Learning/knn_fruit_data.png', dpi=150)
print("\n✓ Saved plot: knn_fruit_data.png")

# ============================================================
# PART 3: Training KNN Classifier
# ============================================================
print("\n\n📌 PART 3: Training KNN Classifier")
print("-" * 70)

# Prepare data
X = df[['Weight', 'Diameter']].values
y = labels

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42
)

print(f"Training samples: {len(X_train)}")
print(f"Test samples: {len(X_test)}")

# Create KNN model with K=5
k = 5
knn = KNeighborsClassifier(n_neighbors=k)

print(f"\n🎓 Training KNN with K={k}...")
knn.fit(X_train, y_train)
print("   Training complete! ✓")
print("   💡 Actually, KNN doesn't 'train' - it just memorizes the data!")

# Make predictions
y_pred = knn.predict(X_test)

# Evaluate
accuracy = accuracy_score(y_test, y_pred)
print(f"\n📊 Model Performance:")
print(f"   Accuracy: {accuracy:.4f} ({accuracy*100:.2f}%)")

# Classification report
print(f"\n📋 Detailed Classification Report:")
print(classification_report(y_test, y_pred, target_names=['Apple', 'Orange']))

# Confusion matrix
cm = confusion_matrix(y_test, y_pred)
plt.figure(figsize=(7, 5))
sns.heatmap(cm, annot=True, fmt='d', cmap='Oranges', cbar=False,
            xticklabels=['Apple', 'Orange'],
            yticklabels=['Apple', 'Orange'])
plt.xlabel('Predicted', fontsize=12)
plt.ylabel('Actual', fontsize=12)
plt.title(f'Confusion Matrix (K={k})', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.savefig('D:/Language Learning/AI ML/Learning-ML-AI/Phase 3 - Machine Learning/knn_confusion_matrix.png', dpi=150)
print("\n✓ Saved plot: knn_confusion_matrix.png")

# ============================================================
# PART 4: How KNN Makes a Prediction (Visual Example)
# ============================================================
print("\n\n📌 PART 4: How KNN Makes a Prediction")
print("-" * 70)

# Pick a new fruit to classify
new_fruit = np.array([[180, 8.5]])  # Weight: 180g, Diameter: 8.5cm

print(f"\n🍎 New fruit to classify:")
print(f"   Weight: {new_fruit[0][0]} grams")
print(f"   Diameter: {new_fruit[0][1]} cm")

# Predict
prediction = knn.predict(new_fruit)
prediction_proba = knn.predict_proba(new_fruit)

fruit_name = 'Apple' if prediction[0] == 0 else 'Orange'
print(f"\n🎯 Prediction: {fruit_name}")
print(f"   Probability of Apple: {prediction_proba[0][0]:.4f}")
print(f"   Probability of Orange: {prediction_proba[0][1]:.4f}")

# Find the K nearest neighbors
distances, indices = knn.kneighbors(new_fruit, n_neighbors=k)

print(f"\n👥 The {k} nearest neighbors are:")
for i, (dist, idx) in enumerate(zip(distances[0], indices[0])):
    neighbor_weight = X_train[idx][0]
    neighbor_diameter = X_train[idx][1]
    neighbor_class = 'Apple' if y_train[idx] == 0 else 'Orange'
    print(f"   {i+1}. {neighbor_class:6s} - Weight: {neighbor_weight:6.1f}g, Diameter: {neighbor_diameter:4.1f}cm, Distance: {dist:.2f}")

# Visualize
plt.figure(figsize=(12, 7))
# Plot training data
plt.scatter(X_train[y_train == 0][:, 0], X_train[y_train == 0][:, 1],
            c='red', marker='o', s=80, alpha=0.5, label='Apple (Training)', edgecolors='black')
plt.scatter(X_train[y_train == 1][:, 0], X_train[y_train == 1][:, 1],
            c='orange', marker='s', s=80, alpha=0.5, label='Orange (Training)', edgecolors='black')
# Plot new point
plt.scatter(new_fruit[0][0], new_fruit[0][1],
            c='green', marker='*', s=500, label='New Fruit', edgecolors='black', linewidths=2)
# Highlight nearest neighbors
for idx in indices[0]:
    plt.scatter(X_train[idx][0], X_train[idx][1],
                c='lime', marker='o', s=200, alpha=0.7, edgecolors='black', linewidths=2)
    # Draw line to neighbor
    plt.plot([new_fruit[0][0], X_train[idx][0]],
             [new_fruit[0][1], X_train[idx][1]],
             'g--', linewidth=1, alpha=0.5)
plt.xlabel('Weight (grams)', fontsize=12)
plt.ylabel('Diameter (cm)', fontsize=12)
plt.title(f'KNN Prediction: Finding the {k} Nearest Neighbors', fontsize=14, fontweight='bold')
plt.legend(fontsize=10)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('D:/Language Learning/AI ML/Learning-ML-AI/Phase 3 - Machine Learning/knn_prediction_example.png', dpi=150)
print("\n✓ Saved plot: knn_prediction_example.png")
print("  Green star = new fruit")
print("  Bright green circles = K nearest neighbors")
print("  Dashed lines = distances to neighbors")

# ============================================================
# PART 5: Choosing the Right K
# ============================================================
print("\n\n📌 PART 5: Choosing the Right K Value")
print("-" * 70)

print("""
🤔 How to choose K?

K=1: Look at only 1 nearest neighbor
- Very sensitive to noise (outliers)
- Overfits (memorizes training data)
- Decision boundary is jagged

K=100: Look at 100 nearest neighbors
- Too smooth, ignores local patterns
- Underfits (too simple)
- Poor accuracy

Sweet spot: Usually K=3 to K=10
- Odd numbers preferred (avoid ties in voting)
- Rule of thumb: K = √(number of samples)
""")

# Test different K values
k_values = [1, 3, 5, 7, 9, 15, 20, 30]
train_accuracies = []
test_accuracies = []

print(f"\n📊 Testing different K values:")
print(f"{'K':<6} {'Train Accuracy':<16} {'Test Accuracy':<15} {'Status':<20}")
print("-" * 70)

for k in k_values:
    knn_temp = KNeighborsClassifier(n_neighbors=k)
    knn_temp.fit(X_train, y_train)

    train_acc = knn_temp.score(X_train, y_train)
    test_acc = knn_temp.score(X_test, y_test)

    train_accuracies.append(train_acc)
    test_accuracies.append(test_acc)

    # Determine status
    if abs(train_acc - test_acc) < 0.05:
        status = "Good balance ✓"
    elif train_acc > test_acc + 0.1:
        status = "Overfitting ⚠️"
    else:
        status = "Underfitting ⚠️"

    print(f"{k:<6} {train_acc:<16.4f} {test_acc:<15.4f} {status:<20}")

# Find best K
best_k_idx = np.argmax(test_accuracies)
best_k = k_values[best_k_idx]
print(f"\n🏆 Best K value: {best_k} (Test Accuracy: {test_accuracies[best_k_idx]:.4f})")

# Plot K vs Accuracy
plt.figure(figsize=(10, 6))
plt.plot(k_values, train_accuracies, 'bo-', linewidth=2, markersize=8, label='Training Accuracy')
plt.plot(k_values, test_accuracies, 'ro-', linewidth=2, markersize=8, label='Test Accuracy')
plt.axvline(x=best_k, color='green', linestyle='--', linewidth=2, label=f'Best K={best_k}')
plt.xlabel('K (Number of Neighbors)', fontsize=12)
plt.ylabel('Accuracy', fontsize=12)
plt.title('KNN: Effect of K on Accuracy', fontsize=14, fontweight='bold')
plt.legend(fontsize=11)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('D:/Language Learning/AI ML/Learning-ML-AI/Phase 3 - Machine Learning/knn_k_selection.png', dpi=150)
print("\n✓ Saved plot: knn_k_selection.png")

# ============================================================
# PART 6: Feature Scaling - CRUCIAL for KNN!
# ============================================================
print("\n\n📌 PART 6: Why Feature Scaling is CRUCIAL for KNN")
print("-" * 70)

print("""
⚠️ THE TRAP: Different Feature Scales!

Imagine predicting house prices:
- Feature 1: Bedrooms (range: 1-5)
- Feature 2: Square feet (range: 500-5000)

Distance calculation:
   d = √[(bed₁-bed₂)² + (sqft₁-sqft₂)²]
   d = √[(3-4)² + (2000-2500)²]
   d = √[1 + 250,000]
   d ≈ 500

The square feet DOMINATES! Bedrooms are ignored!

Solution: STANDARDIZATION (Scale all features to similar ranges)
""")

# Create dataset with different scales
np.random.seed(42)
X_unscaled = np.column_stack([
    np.random.randint(1, 6, 100),      # Bedrooms: 1-5
    np.random.randint(500, 5000, 100)  # Square feet: 500-5000
])
y_scale = (X_unscaled[:, 0] > 3).astype(int)  # Target based on bedrooms

X_train_us, X_test_us, y_train_s, y_test_s = train_test_split(
    X_unscaled, y_scale, test_size=0.25, random_state=42
)

# Without scaling
knn_unscaled = KNeighborsClassifier(n_neighbors=5)
knn_unscaled.fit(X_train_us, y_train_s)
acc_unscaled = knn_unscaled.score(X_test_us, y_test_s)

# With scaling
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train_us)
X_test_scaled = scaler.transform(X_test_us)

knn_scaled = KNeighborsClassifier(n_neighbors=5)
knn_scaled.fit(X_train_scaled, y_train_s)
acc_scaled = knn_scaled.score(X_test_scaled, y_test_s)

print(f"\n📊 Impact of Scaling:")
print(f"   Without scaling: {acc_unscaled:.4f} accuracy")
print(f"   With scaling: {acc_scaled:.4f} accuracy")
print(f"   Improvement: {(acc_scaled - acc_unscaled)*100:.1f}%")

print(f"\n🔍 What StandardScaler does:")
print(f"   Formula: z = (x - mean) / std_dev")
print(f"   Result: All features have mean=0, std=1")
print(f"\n   Before scaling:")
print(f"      Bedrooms: mean={X_train_us[:, 0].mean():.1f}, std={X_train_us[:, 0].std():.1f}")
print(f"      Sq Feet: mean={X_train_us[:, 1].mean():.1f}, std={X_train_us[:, 1].std():.1f}")
print(f"\n   After scaling:")
print(f"      Bedrooms: mean={X_train_scaled[:, 0].mean():.4f}, std={X_train_scaled[:, 0].std():.4f}")
print(f"      Sq Feet: mean={X_train_scaled[:, 1].mean():.4f}, std={X_train_scaled[:, 1].std():.4f}")

# ============================================================
# PART 7: Decision Boundaries
# ============================================================
print("\n\n📌 PART 7: Visualizing Decision Boundaries")
print("-" * 70)

# Create non-linear dataset
X_moons, y_moons = make_moons(n_samples=200, noise=0.15, random_state=42)
X_train_m, X_test_m, y_train_m, y_test_m = train_test_split(
    X_moons, y_moons, test_size=0.25, random_state=42
)

# Try different K values
k_values_viz = [1, 5, 15]
fig, axes = plt.subplots(1, 3, figsize=(15, 4))

for idx, k in enumerate(k_values_viz):
    knn_viz = KNeighborsClassifier(n_neighbors=k)
    knn_viz.fit(X_train_m, y_train_m)
    acc_viz = knn_viz.score(X_test_m, y_test_m)

    # Create mesh
    x_min, x_max = X_moons[:, 0].min() - 0.5, X_moons[:, 0].max() + 0.5
    y_min, y_max = X_moons[:, 1].min() - 0.5, X_moons[:, 1].max() + 0.5
    xx, yy = np.meshgrid(np.linspace(x_min, x_max, 200),
                         np.linspace(y_min, y_max, 200))

    Z = knn_viz.predict(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)

    axes[idx].contourf(xx, yy, Z, alpha=0.3, cmap='RdYlBu')
    axes[idx].scatter(X_train_m[:, 0], X_train_m[:, 1], c=y_train_m,
                     cmap='RdYlBu', edgecolors='black', s=50, alpha=0.8)
    axes[idx].set_xlabel('Feature 1', fontsize=11)
    axes[idx].set_ylabel('Feature 2', fontsize=11)
    axes[idx].set_title(f'K={k} (Accuracy: {acc_viz:.3f})', fontsize=12, fontweight='bold')
    axes[idx].grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('D:/Language Learning/AI ML/Learning-ML-AI/Phase 3 - Machine Learning/knn_decision_boundaries.png', dpi=150)
print("\n✓ Saved plot: knn_decision_boundaries.png")
print("  K=1: Very complex boundary (overfitting)")
print("  K=5: Balanced boundary")
print("  K=15: Too smooth boundary (underfitting)")

# ============================================================
# PART 8: KNN for Regression
# ============================================================
print("\n\n📌 PART 8: KNN for Regression (Predicting Continuous Values)")
print("-" * 70)

print("""
💡 KNN works for regression too!

Classification: Take majority vote
Regression: Take average of K neighbors

Example: Predicting house prices
""")

# Generate regression data
np.random.seed(42)
X_reg = np.random.uniform(0, 10, 100).reshape(-1, 1)
y_reg = 2 * X_reg.ravel() + np.sin(X_reg.ravel() * 2) * 3 + np.random.randn(100) * 0.5

# Split
X_train_reg, X_test_reg, y_train_reg, y_test_reg = train_test_split(
    X_reg, y_reg, test_size=0.25, random_state=42
)

# Train KNN regressor
knn_reg = KNeighborsRegressor(n_neighbors=5)
knn_reg.fit(X_train_reg, y_train_reg)

# Predict
X_plot = np.linspace(0, 10, 300).reshape(-1, 1)
y_plot = knn_reg.predict(X_plot)

# Evaluate
from sklearn.metrics import mean_squared_error, r2_score
y_pred_reg = knn_reg.predict(X_test_reg)
mse = mean_squared_error(y_test_reg, y_pred_reg)
r2 = r2_score(y_test_reg, y_pred_reg)

print(f"\n📊 KNN Regression Performance:")
print(f"   R² Score: {r2:.4f}")
print(f"   MSE: {mse:.4f}")

# Plot
plt.figure(figsize=(10, 6))
plt.scatter(X_train_reg, y_train_reg, c='blue', s=50, alpha=0.6, label='Training Data')
plt.scatter(X_test_reg, y_test_reg, c='red', s=50, alpha=0.6, label='Test Data')
plt.plot(X_plot, y_plot, 'g-', linewidth=3, label='KNN Prediction')
plt.xlabel('X', fontsize=12)
plt.ylabel('y', fontsize=12)
plt.title('KNN Regression', fontsize=14, fontweight='bold')
plt.legend(fontsize=11)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('D:/Language Learning/AI ML/Learning-ML-AI/Phase 3 - Machine Learning/knn_regression.png', dpi=150)
print("\n✓ Saved plot: knn_regression.png")

# ============================================================
# WHY THIS MATTERS
# ============================================================
print("\n\n🎯 WHY KNN MATTERS")
print("=" * 70)
print("""
1. SIMPLEST ALGORITHM:
   - No training phase! (Lazy learning)
   - Just memorizes the data
   - Easy to understand and explain

2. NO ASSUMPTIONS:
   - Doesn't assume linear relationships
   - Doesn't assume feature independence
   - Can capture complex patterns

3. VERSATILE:
   - Works for classification AND regression
   - Works for multi-class problems
   - Naturally handles non-linear patterns

4. INTUITIVE:
   - Mimics human reasoning ("similar things should be similar")
   - Easy to explain to non-technical people
   - Good baseline model

5. REAL WORLD APPLICATIONS:
   - Recommendation systems (find similar users/products)
   - Pattern recognition
   - Missing value imputation
   - Anomaly detection

🔑 KEY TAKEAWAYS:
   ✓ KNN is "lazy learning" - no training, just memorize
   ✓ Distance metric is crucial (usually Euclidean)
   ✓ ALWAYS scale features (different units = wrong distances!)
   ✓ K value matters: too small = overfitting, too large = underfitting
   ✓ Odd K values avoid ties in voting
   ✓ Works for both classification and regression

⚠️ LIMITATIONS:
   - SLOW for large datasets (must calculate distance to ALL points!)
   - Memory intensive (stores entire training set)
   - Sensitive to irrelevant features
   - Suffers from "curse of dimensionality" (too many features)
   - Needs feature scaling

💡 When to use KNN:
   ✓ Small to medium datasets
   ✓ Non-linear patterns
   ✓ Need interpretable results
   ✗ Large datasets (use tree-based models instead)
   ✗ Many features (use dimensionality reduction first)

🚀 Next Steps:
   - Learn Decision Trees (better for large datasets)
   - Learn about curse of dimensionality
   - Try different distance metrics (Manhattan, Minkowski)
   - Learn dimensionality reduction (PCA) for high-dimensional data
""")

print("\n✅ K-Nearest Neighbors Complete!")
print("Next: decision_tree.py - Learning tree-based models")
