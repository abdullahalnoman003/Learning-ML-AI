"""
🤖 MACHINE LEARNING CONCEPTS - Understanding the Fundamentals
===============================================================

What is Machine Learning?
-------------------------
Instead of programming rules manually:
   Traditional: IF age > 65 THEN senior_citizen

Machine Learning: Show the computer examples, let IT figure out the rules!
   Examples: [age=70 → senior, age=25 → young, age=68 → senior...]
   Computer learns: "If age > ~60, probably senior"

Machine Learning = Teaching computers to learn from data

Think of it like teaching a child:
- Show them examples (training data)
- They learn patterns
- They can handle new situations (predictions)
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

print("=" * 70)
print("MACHINE LEARNING FOUNDATIONS - CONCEPTS & TERMINOLOGY")
print("=" * 70)

# ============================================================
# PART 1: Types of Machine Learning
# ============================================================
print("\n📌 PART 1: Three Types of Machine Learning")
print("-" * 70)

print("""
1️⃣ SUPERVISED LEARNING (Learn from labeled examples)
   You have: Input + Correct Output
   Goal: Learn to predict output for new inputs

   Example: Email spam detection
   - Training data: emails labeled as "spam" or "not spam"
   - Model learns: what makes an email spam
   - Prediction: classify new emails

   Two types:
   a) REGRESSION → Predict a NUMBER
      • House prices (features → $price)
      • Temperature forecast (date/location → degrees)
      • Stock prices (historical data → future price)

   b) CLASSIFICATION → Predict a CATEGORY
      • Spam detection (email → spam/not spam)
      • Disease diagnosis (symptoms → disease/healthy)
      • Image recognition (pixels → cat/dog/bird)

2️⃣ UNSUPERVISED LEARNING (Find patterns without labels)
   You have: Input only (no correct answers)
   Goal: Find hidden structure in data

   Types:
   a) CLUSTERING → Group similar items
      • Customer segmentation (group similar customers)
      • Document organization (group similar articles)

   b) DIMENSIONALITY REDUCTION → Compress data
      • PCA: Reduce 100 features to 10
      • t-SNE: Visualize high-D data in 2D

3️⃣ REINFORCEMENT LEARNING (Learn through trial & error)
   Agent takes actions → gets rewards/penalties → learns optimal behavior

   Examples:
   • Game AI (AlphaGo, Chess engines)
   • Robot control (walking, grasping)
   • Self-driving cars

   💡 This course focuses on SUPERVISED LEARNING (most common in practice)
""")

# ============================================================
# PART 2: Key Terminology
# ============================================================
print("\n📌 PART 2: Essential ML Vocabulary")
print("-" * 70)

vocab = {
    "Dataset": "Collection of data used for training/testing",
    "Sample/Instance": "One row of data (one example)",
    "Feature/Attribute": "Input variable (column) - what the model uses to learn",
    "Label/Target": "Output variable - what we want to predict",
    "Training Set": "Data used to teach the model (~70-80%)",
    "Test Set": "Data used to evaluate model on unseen examples (~20-30%)",
    "Validation Set": "Data used to tune model settings",
    "Model": "The learned function that makes predictions",
    "Parameters": "Values the model LEARNS (weights, biases)",
    "Hyperparameters": "Settings YOU choose BEFORE training (learning rate, tree depth)",
    "Overfitting": "Model memorizes training data → fails on new data",
    "Underfitting": "Model too simple → can't learn patterns",
    "Bias": "Error from wrong assumptions (underfitting)",
    "Variance": "Error from sensitivity to training data (overfitting)",
    "Accuracy": "% of correct predictions",
    "Loss/Cost": "How wrong the model's predictions are"
}

print("\n📚 ML Dictionary:")
for term, definition in vocab.items():
    print(f"\n• {term}:")
    print(f"  → {definition}")

# ============================================================
# PART 3: The ML Workflow
# ============================================================
print("\n\n📌 PART 3: The Complete ML Workflow (Always Follow This!)")
print("-" * 70)

workflow = """
┌─────────────────────────────────────────────────────────────┐
│                  MACHINE LEARNING WORKFLOW                  │
└─────────────────────────────────────────────────────────────┘

1️⃣ DEFINE THE PROBLEM
   • What are you trying to predict?
   • Regression or classification?
   • What's the business goal?

2️⃣ COLLECT DATA
   • Gather relevant data
   • More data = better model (usually!)
   • Quality > Quantity

3️⃣ EXPLORE DATA (EDA)
   • Load and inspect data
   • Visualize distributions
   • Find relationships
   • Check for missing values

4️⃣ PREPARE DATA
   • Handle missing values
   • Remove outliers
   • Encode categorical variables (text → numbers)
   • Scale/normalize features
   • Feature engineering (create new features)

5️⃣ SPLIT DATA
   • Training set (to learn)
   • Test set (to evaluate)
   • Optional: Validation set (to tune)

6️⃣ CHOOSE MODEL
   • Start simple (Linear/Logistic Regression)
   • Try multiple algorithms
   • Consider: interpretability vs performance

7️⃣ TRAIN MODEL
   • Feed training data to model
   • Model adjusts parameters to minimize error
   • This is where "learning" happens!

8️⃣ EVALUATE MODEL
   • Test on unseen test data
   • Calculate metrics (accuracy, precision, recall)
   • Check for overfitting/underfitting

9️⃣ IMPROVE MODEL
   • Try different algorithms
   • Feature engineering
   • Hyperparameter tuning
   • Get more/better data

🔟 DEPLOY MODEL
   • Put model into production
   • Monitor performance
   • Retrain when needed
"""

print(workflow)

# ============================================================
# PART 4: Practical Example - The Workflow in Action
# ============================================================
print("\n📌 PART 4: Hands-On Example - Predicting Student Performance")
print("-" * 70)

print("\n🎯 Problem: Predict if a student will pass based on study hours")

# Step 1: Create sample data
np.random.seed(42)
study_hours = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1.5, 3.5, 5.5, 7.5, 9.5])
exam_score = study_hours * 8 + np.random.randint(-5, 5, len(study_hours))
passed = (exam_score >= 50).astype(int)  # 1 = passed, 0 = failed

df = pd.DataFrame({
    'Study_Hours': study_hours,
    'Exam_Score': exam_score,
    'Passed': passed
})

print("\n📊 Our Dataset:")
print(df.head(10))

# Step 2: Visualize
plt.figure(figsize=(10, 6))
colors = ['red' if p == 0 else 'green' for p in passed]
plt.scatter(study_hours, exam_score, c=colors, s=100, alpha=0.6, edgecolors='black')
plt.axhline(y=50, color='blue', linestyle='--', linewidth=2, label='Passing Line (50)')
plt.xlabel('Study Hours')
plt.ylabel('Exam Score')
plt.title('Study Hours vs Exam Score')
plt.legend(['Passing Line', 'Failed', 'Passed'])
plt.grid(True, alpha=0.3)
plt.savefig('ml_example_data.png', dpi=300, bbox_inches='tight')
print("\n✓ Created: ml_example_data.png")
print("   Red = Failed, Green = Passed")
plt.close()

# Step 3: Prepare data
X = df[['Study_Hours']].values  # Features (input)
y = df['Passed'].values  # Target (output)

print(f"\n📊 Data Shape:")
print(f"   X (features): {X.shape} → {X.shape[0]} samples, {X.shape[1]} feature(s)")
print(f"   y (target): {y.shape} → {y.shape[0]} labels")

# Step 4: Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

print(f"\n📊 Train/Test Split:")
print(f"   Training samples: {len(X_train)} ({len(X_train)/len(X)*100:.0f}%)")
print(f"   Test samples: {len(X_test)} ({len(X_test)/len(X)*100:.0f}%)")
print(f"   💡 Train on 70%, evaluate on remaining 30%")

# ============================================================
# PART 5: Overfitting vs Underfitting
# ============================================================
print("\n\n📌 PART 5: Overfitting vs Underfitting (CRITICAL CONCEPT!)")
print("-" * 70)

print("""
🎯 THE GOLDILOCKS PROBLEM:

❌ UNDERFITTING (Too Simple)
   • Model too basic to capture patterns
   • High error on BOTH training and test data
   • Example: Predicting house prices using only "number of bedrooms"
   • Fix: Use more features, more complex model

✅ JUST RIGHT (Good Fit)
   • Model captures real patterns
   • Good performance on training data
   • Good performance on test data
   • This is our goal!

❌ OVERFITTING (Too Complex)
   • Model memorizes training data (including noise)
   • Great on training data
   • Terrible on test data
   • Example: Model memorizes every house price perfectly but fails on new houses
   • Fix: More data, simpler model, regularization

💡 Think of it like studying for an exam:
   • Underfitting = didn't study enough, fail both practice and real exam
   • Just right = understood concepts, do well on both
   • Overfitting = memorized answers to practice problems,
                   but can't solve new problems on real exam
""")

# Visualize
x_plot = np.linspace(0, 11, 100)

fig, axes = plt.subplots(1, 3, figsize=(15, 4))

# Underfitting - constant line
axes[0].scatter(study_hours, exam_score, c=colors, s=50, alpha=0.6)
axes[0].axhline(y=np.mean(exam_score), color='red', linewidth=2)
axes[0].set_title('UNDERFITTING\n(Too Simple)', fontweight='bold')
axes[0].set_xlabel('Study Hours')
axes[0].set_ylabel('Exam Score')
axes[0].grid(True, alpha=0.3)

# Good fit - linear
axes[1].scatter(study_hours, exam_score, c=colors, s=50, alpha=0.6)
coeffs = np.polyfit(study_hours, exam_score, 1)
axes[1].plot(x_plot, np.polyval(coeffs, x_plot), 'g-', linewidth=2)
axes[1].set_title('GOOD FIT\n(Just Right)', fontweight='bold')
axes[1].set_xlabel('Study Hours')
axes[1].grid(True, alpha=0.3)

# Overfitting - high degree polynomial
axes[2].scatter(study_hours, exam_score, c=colors, s=50, alpha=0.6)
coeffs_over = np.polyfit(study_hours, exam_score, 10)  # Degree 10!
axes[2].plot(x_plot, np.polyval(coeffs_over, x_plot), 'b-', linewidth=2)
axes[2].set_title('OVERFITTING\n(Too Complex)', fontweight='bold')
axes[2].set_xlabel('Study Hours')
axes[2].grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('overfitting_underfitting.png', dpi=300, bbox_inches='tight')
print("\n✓ Created: overfitting_underfitting.png")
plt.close()

# ============================================================
# PART 6: Bias-Variance Tradeoff
# ============================================================
print("\n\n📌 PART 6: Bias-Variance Tradeoff")
print("-" * 70)

print("""
📊 TOTAL ERROR = Bias² + Variance + Irreducible Error

• BIAS = Error from wrong assumptions
  - High bias → underfitting
  - Model consistently wrong in same direction
  - Example: Using straight line for curved data

• VARIANCE = Error from sensitivity to training data
  - High variance → overfitting
  - Model changes dramatically with different training data
  - Example: Fitting exact curve through noisy data

• IRREDUCIBLE ERROR = Random noise in data
  - Can't be reduced (it's in the data itself)

💡 THE TRADEOFF:
   ↓ More complex model → ↓ Bias (good!) but ↑ Variance (bad!)
   ↓ Simpler model → ↑ Bias (bad!) but ↓ Variance (good!)

   Goal: Find sweet spot where TOTAL ERROR is minimized
""")

# ============================================================
# SUMMARY
# ============================================================
print("\n\n🎯 ML CONCEPTS SUMMARY")
print("=" * 70)
print("""
✅ KEY TAKEAWAYS:

1️⃣ ML Types:
   • Supervised (labeled data) - MOST COMMON
     - Regression (predict numbers)
     - Classification (predict categories)
   • Unsupervised (no labels)
   • Reinforcement (rewards/penalties)

2️⃣ ML Workflow (ALWAYS follow):
   Define → Collect → Explore → Prepare → Split →
   Choose → Train → Evaluate → Improve → Deploy

3️⃣ Train/Test Split:
   • Train: Learn patterns (~70%)
   • Test: Evaluate generalization (~30%)
   • NEVER touch test data during training!

4️⃣ Overfitting vs Underfitting:
   • Underfitting: Too simple
   • Overfitting: Too complex (memorizes)
   • Goal: Just right (generalizes)

5️⃣ Evaluation:
   • Training accuracy HIGH, Test accuracy HIGH ✓
   • Training accuracy HIGH, Test accuracy LOW → Overfitting ✗
   • Training accuracy LOW, Test accuracy LOW → Underfitting ✗

🎓 YOU'RE READY FOR ML ALGORITHMS!

Next files to learn actual ML algorithms:
   • linear_regression_scratch.py - Build from scratch
   • linear_regression_sklearn.py - Use scikit-learn
   • logistic_regression.py - Classification
   • knn.py, decision_tree.py, random_forest.py
""")

print("\n✅ ML Concepts Complete!")
print("Next: linear_regression_scratch.py - Build your first ML algorithm from scratch!")
