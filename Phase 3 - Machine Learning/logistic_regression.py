"""
 LOGISTIC REGRESSION - Binary Classification
===============================================

What is Logistic Regression?
----------------------------
Despite the name, it's for CLASSIFICATION, not regression!

The Problem:
- You want to predict YES/NO, TRUE/FALSE, 0/1
- Examples: spam/not spam, disease/healthy, pass/fail

Why not Linear Regression?
- Linear regression outputs any number (-∞ to +∞)
- We need outputs between 0 and 1 (probability!)
- Linear regression for classification fails badly

The Solution: Sigmoid Function!
- Takes any number and squashes it between 0 and 1
- σ(x) = 1 / (1 + e^(-x))
- Output close to 1 → Class 1 (Positive)
- Output close to 0 → Class 0 (Negative)

Real World Example: Email Spam Detection
- Features: word counts, sender, links, etc.
- Output: probability of being spam
- If P(spam) > 0.5 → Classify as spam
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.metrics import roc_curve, roc_auc_score
import seaborn as sns

print("=" * 70)
print("LOGISTIC REGRESSION - Binary Classification")
print("=" * 70)

# ============================================================
# PART 1: Understanding the Sigmoid Function
# ============================================================
print("\n PART 1: The Sigmoid Function - The Heart of Logistic Regression")
print("-" * 70)

def sigmoid(x):
    """The magic function that converts any number to probability (0 to 1)"""
    return 1 / (1 + np.exp(-x))

# Visualize sigmoid
x_values = np.linspace(-10, 10, 100)
y_values = sigmoid(x_values)

plt.figure(figsize=(10, 6))
plt.plot(x_values, y_values, linewidth=3, color='blue')
plt.axhline(y=0.5, color='r', linestyle='--', alpha=0.7, label='Decision Boundary (0.5)')
plt.axvline(x=0, color='gray', linestyle='--', alpha=0.5)
plt.xlabel('Input Value (z)', fontsize=12)
plt.ylabel('Sigmoid Output σ(z)', fontsize=12)
plt.title('Sigmoid Function: Converts Any Number to Probability', fontsize=14, fontweight='bold')
plt.grid(True, alpha=0.3)
plt.legend(fontsize=11)
plt.tight_layout()
plt.savefig('sigmoid_function.png', dpi=150)
print(" Saved plot: sigmoid_function.png")

print(f"\n Sigmoid Function Examples:")
test_values = [-5, -2, 0, 2, 5]
for val in test_values:
    prob = sigmoid(val)
    print(f"   sigmoid({val:2d}) = {prob:.4f} → {'Negative (0)' if prob < 0.5 else 'Positive (1)'}")

print(f"\n Key Properties:")
print(f"   - sigmoid(-∞) → 0 (definitely class 0)")
print(f"   - sigmoid(0) → 0.5 (uncertain)")
print(f"   - sigmoid(+∞) → 1 (definitely class 1)")
print(f"   - Output is ALWAYS between 0 and 1!")

# ============================================================
# PART 2: Creating a Binary Classification Dataset
# ============================================================
print("\n\n PART 2: Creating a Binary Classification Dataset")
print("-" * 70)

print("""
 Problem: Predicting Student Admission to University

Features:
- Exam 1 Score (0-100)
- Exam 2 Score (0-100)

Target:
- Admitted: 1 (Yes)
- Not Admitted: 0 (No)

Goal: Can we predict if a student gets admitted based on exam scores?
""")

# Generate synthetic data
np.random.seed(42)

# Admitted students (higher scores)
n_admitted = 60
exam1_admitted = np.random.normal(75, 10, n_admitted)
exam2_admitted = np.random.normal(75, 10, n_admitted)
admitted_labels = np.ones(n_admitted)

# Not admitted students (lower scores)
n_not_admitted = 40
exam1_not_admitted = np.random.normal(50, 10, n_not_admitted)
exam2_not_admitted = np.random.normal(50, 10, n_not_admitted)
not_admitted_labels = np.zeros(n_not_admitted)

# Combine datasets
exam1_scores = np.concatenate([exam1_admitted, exam1_not_admitted])
exam2_scores = np.concatenate([exam2_admitted, exam2_not_admitted])
admission_status = np.concatenate([admitted_labels, not_admitted_labels])

# Create DataFrame
df = pd.DataFrame({
    'Exam1': exam1_scores,
    'Exam2': exam2_scores,
    'Admitted': admission_status
})

print(f"\n Dataset Overview:")
print(df.head(10))
print(f"\n Statistics:")
print(df.describe())
print(f"\n Class Distribution:")
print(f"   Admitted: {sum(admission_status == 1)} students")
print(f"   Not Admitted: {sum(admission_status == 0)} students")

# Visualize the data
plt.figure(figsize=(10, 6))
plt.scatter(df[df['Admitted'] == 1]['Exam1'],
            df[df['Admitted'] == 1]['Exam2'],
            c='green', marker='o', s=100, alpha=0.7, label='Admitted')
plt.scatter(df[df['Admitted'] == 0]['Exam1'],
            df[df['Admitted'] == 0]['Exam2'],
            c='red', marker='x', s=100, alpha=0.7, label='Not Admitted')
plt.xlabel('Exam 1 Score', fontsize=12)
plt.ylabel('Exam 2 Score', fontsize=12)
plt.title('Student Admission Data', fontsize=14, fontweight='bold')
plt.legend(fontsize=11)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('admission_data.png', dpi=150)
print("\n Saved plot: admission_data.png")
print("  Green circles = Admitted, Red X = Not Admitted")
print("  Notice: Higher scores → more likely to be admitted!")

# ============================================================
# PART 3: Preparing Data for Training
# ============================================================
print("\n\n PART 3: Preparing Data for Training")
print("-" * 70)

# Separate features and target
X = df[['Exam1', 'Exam2']].values
y = df['Admitted'].values

print(f"Features shape: {X.shape}")
print(f"Target shape: {y.shape}")

# Split into train and test sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42
)

print(f"\n️ Train-Test Split:")
print(f"   Training samples: {len(X_train)} ({len(X_train)/len(X)*100:.0f}%)")
print(f"   Test samples: {len(X_test)} ({len(X_test)/len(X)*100:.0f}%)")

# ============================================================
# PART 4: Training Logistic Regression Model
# ============================================================
print("\n\n PART 4: Training Logistic Regression Model")
print("-" * 70)

# Create and train the model
log_reg = LogisticRegression(random_state=42)
print("\n Training the model...")
log_reg.fit(X_train, y_train)
print("   Training complete! ")

# Display learned parameters
print(f"\n Learned Parameters:")
print(f"   Coefficients: {log_reg.coef_[0]}")
print(f"   Intercept: {log_reg.intercept_[0]:.4f}")

print(f"\n Decision Function:")
print(f"   z = {log_reg.coef_[0][0]:.4f} × Exam1 + {log_reg.coef_[0][1]:.4f} × Exam2 + {log_reg.intercept_[0]:.4f}")
print(f"   P(Admitted) = sigmoid(z)")
print(f"\n   Positive coefficient = feature helps admission")
print(f"   Larger absolute value = more important feature")

# ============================================================
# PART 5: Making Predictions
# ============================================================
print("\n\n PART 5: Making Predictions")
print("-" * 70)

# Predict classes (0 or 1)
y_pred = log_reg.predict(X_test)

# Predict probabilities (0.0 to 1.0)
y_pred_proba = log_reg.predict_proba(X_test)

print("\n Prediction Examples (Test Set):")
print(f"{'Exam1':<8} {'Exam2':<8} {'P(Not)':<10} {'P(Admit)':<10} {'Predicted':<12} {'Actual':<8}")
print("-" * 70)
for i in range(min(10, len(X_test))):
    exam1, exam2 = X_test[i]
    prob_not_admitted = y_pred_proba[i, 0]
    prob_admitted = y_pred_proba[i, 1]
    predicted = 'Admitted' if y_pred[i] == 1 else 'Not Admitted'
    actual = 'Admitted' if y_test[i] == 1 else 'Not Admitted'
    match = '' if y_pred[i] == y_test[i] else ''
    print(f"{exam1:<8.1f} {exam2:<8.1f} {prob_not_admitted:<10.4f} {prob_admitted:<10.4f} "
          f"{predicted:<12} {actual:<8} {match}")

print(f"\n Understanding Probabilities:")
print(f"   - P(Admit) > 0.5 → Predict 'Admitted'")
print(f"   - P(Admit) < 0.5 → Predict 'Not Admitted'")
print(f"   - You can change this threshold (e.g., 0.7) for stricter admission")

# ============================================================
# PART 6: Model Evaluation - Accuracy
# ============================================================
print("\n\n PART 6: Model Evaluation - Accuracy")
print("-" * 70)

# Calculate accuracy
train_accuracy = log_reg.score(X_train, y_train)
test_accuracy = log_reg.score(X_test, y_test)

print(f"\n Accuracy Scores:")
print(f"   Training Accuracy: {train_accuracy:.4f} ({train_accuracy*100:.2f}%)")
print(f"   Test Accuracy: {test_accuracy:.4f} ({test_accuracy*100:.2f}%)")

if test_accuracy >= 0.85:
    print(f"    Excellent! Model predicts well on unseen data!")
elif test_accuracy >= 0.70:
    print(f"    Good! Model has decent predictive power")
else:
    print(f"   ️ Model needs improvement")

print(f"\n What is Accuracy?")
print(f"   Accuracy = (Correct Predictions) / (Total Predictions)")
print(f"   But accuracy alone doesn't tell the full story...")

# ============================================================
# PART 7: Confusion Matrix - The Full Picture
# ============================================================
print("\n\n PART 7: Confusion Matrix - Understanding All Errors")
print("-" * 70)

print("""
 What is a Confusion Matrix?

A table showing all 4 possible outcomes:

                    Predicted
                    No      Yes
Actual  No      [  TN  |  FP  ]   TN = True Negative (Correct!)
                [-------+------]   FP = False Positive (Type I Error)
        Yes     [  FN  |  TP  ]   FN = False Negative (Type II Error)
                                   TP = True Positive (Correct!)

- True Positive (TP): Predicted admitted, actually admitted 
- True Negative (TN): Predicted not admitted, actually not admitted 
- False Positive (FP): Predicted admitted, but actually not admitted 
- False Negative (FN): Predicted not admitted, but actually admitted 
""")

# Calculate confusion matrix
cm = confusion_matrix(y_test, y_pred)

print(f"\n Confusion Matrix:")
print(f"\n                  Predicted")
print(f"                  Not Admit  Admitted")
print(f"Actual Not Admit  {cm[0, 0]:^10d} {cm[0, 1]:^9d}")
print(f"       Admitted   {cm[1, 0]:^10d} {cm[1, 1]:^9d}")

tn, fp, fn, tp = cm.ravel()
print(f"\n Breakdown:")
print(f"   True Negatives (TN): {tn}  (Correctly predicted not admitted)")
print(f"   False Positives (FP): {fp}  (Wrong: predicted admitted but wasn't)")
print(f"   False Negatives (FN): {fn}  (Wrong: predicted not admitted but was)")
print(f"   True Positives (TP): {tp}  (Correctly predicted admitted)")

# Visualize confusion matrix
plt.figure(figsize=(8, 6))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', cbar=False,
            xticklabels=['Not Admitted', 'Admitted'],
            yticklabels=['Not Admitted', 'Admitted'])
plt.xlabel('Predicted Label', fontsize=12)
plt.ylabel('True Label', fontsize=12)
plt.title('Confusion Matrix', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.savefig('confusion_matrix.png', dpi=150)
print("\n Saved plot: confusion_matrix.png")

# ============================================================
# PART 8: Classification Metrics
# ============================================================
print("\n\n PART 8: Important Classification Metrics")
print("-" * 70)

print("""
 Key Metrics Explained:

1. PRECISION: Of all predicted positives, how many are actually positive?
   Precision = TP / (TP + FP)
   High precision = Few false alarms

2. RECALL (Sensitivity): Of all actual positives, how many did we find?
   Recall = TP / (TP + FN)
   High recall = We catch most positive cases

3. F1-SCORE: Harmonic mean of precision and recall
   F1 = 2 × (Precision × Recall) / (Precision + Recall)
   Balances precision and recall

Example: Disease Detection
- High Precision needed: Don't want to scare healthy people
- High Recall needed: Don't want to miss sick people
""")

# Get detailed classification report
print(f"\n Classification Report:")
print(classification_report(y_test, y_pred,
                          target_names=['Not Admitted', 'Admitted']))

# Calculate individual metrics
precision_admitted = tp / (tp + fp) if (tp + fp) > 0 else 0
recall_admitted = tp / (tp + fn) if (tp + fn) > 0 else 0
f1_admitted = 2 * (precision_admitted * recall_admitted) / (precision_admitted + recall_admitted) if (precision_admitted + recall_admitted) > 0 else 0

print(f"\n For 'Admitted' class:")
print(f"   Precision: {precision_admitted:.3f} → When we predict 'admitted', we're right {precision_admitted*100:.1f}% of the time")
print(f"   Recall: {recall_admitted:.3f} → We correctly identify {recall_admitted*100:.1f}% of admitted students")
print(f"   F1-Score: {f1_admitted:.3f} → Overall balance score")

# ============================================================
# PART 9: ROC Curve and AUC
# ============================================================
print("\n\n PART 9: ROC Curve and AUC Score")
print("-" * 70)

print("""
 What is ROC Curve?

ROC (Receiver Operating Characteristic) shows the trade-off between:
- True Positive Rate (Recall): Finding all positives
- False Positive Rate: Mistakenly classifying negatives as positive

AUC (Area Under Curve):
- AUC = 1.0 → Perfect classifier! 
- AUC = 0.9-1.0 → Excellent
- AUC = 0.8-0.9 → Very good
- AUC = 0.7-0.8 → Good
- AUC = 0.5 → No better than random guessing (useless!)
- AUC < 0.5 → Worse than random (doing something wrong!)
""")

# Calculate ROC curve
y_pred_proba_positive = y_pred_proba[:, 1]  # Probabilities of positive class
fpr, tpr, thresholds = roc_curve(y_test, y_pred_proba_positive)
auc_score = roc_auc_score(y_test, y_pred_proba_positive)

print(f"\n AUC Score: {auc_score:.4f}")
if auc_score >= 0.9:
    print(f"    Excellent! Model has outstanding discriminative ability!")
elif auc_score >= 0.8:
    print(f"    Very good! Model distinguishes classes well!")
elif auc_score >= 0.7:
    print(f"    Good! Model has useful predictive power")
else:
    print(f"   ️ Fair. Model needs improvement")

# Plot ROC curve
plt.figure(figsize=(10, 6))
plt.plot(fpr, tpr, linewidth=3, label=f'ROC Curve (AUC = {auc_score:.3f})')
plt.plot([0, 1], [0, 1], 'k--', linewidth=2, label='Random Classifier (AUC = 0.5)')
plt.xlabel('False Positive Rate', fontsize=12)
plt.ylabel('True Positive Rate (Recall)', fontsize=12)
plt.title('ROC Curve - Model Performance', fontsize=14, fontweight='bold')
plt.legend(fontsize=11)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('roc_curve.png', dpi=150)
print("\n Saved plot: roc_curve.png")
print("  The further the curve from the diagonal, the better!")

# ============================================================
# PART 10: Decision Boundary Visualization
# ============================================================
print("\n\n PART 10: Decision Boundary Visualization")
print("-" * 70)

print("""
 What is a Decision Boundary?

The line (or curve) that separates the two classes.
- On one side: Model predicts class 0
- On the other side: Model predicts class 1

For logistic regression with 2 features, it's a straight line!
""")

# Create mesh for decision boundary
x_min, x_max = X[:, 0].min() - 10, X[:, 0].max() + 10
y_min, y_max = X[:, 1].min() - 10, X[:, 1].max() + 10
xx, yy = np.meshgrid(np.linspace(x_min, x_max, 200),
                     np.linspace(y_min, y_max, 200))

# Predict for each point in mesh
Z = log_reg.predict(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)

# Plot
plt.figure(figsize=(12, 7))
plt.contourf(xx, yy, Z, alpha=0.3, cmap='RdYlGn')
plt.scatter(X_test[y_test == 0][:, 0], X_test[y_test == 0][:, 1],
            c='red', marker='x', s=100, linewidths=2, label='Not Admitted (Test)')
plt.scatter(X_test[y_test == 1][:, 0], X_test[y_test == 1][:, 1],
            c='green', marker='o', s=100, linewidths=2, label='Admitted (Test)')
plt.xlabel('Exam 1 Score', fontsize=12)
plt.ylabel('Exam 2 Score', fontsize=12)
plt.title('Decision Boundary - Logistic Regression', fontsize=14, fontweight='bold')
plt.legend(fontsize=11)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('decision_boundary.png', dpi=150)
print("\n Saved plot: decision_boundary.png")
print("  Green region = Predicted 'Admitted'")
print("  Red region = Predicted 'Not Admitted'")
print("  The boundary is a straight line!")

# ============================================================
# PART 11: Changing the Decision Threshold
# ============================================================
print("\n\n PART 11: Adjusting the Decision Threshold")
print("-" * 70)

print("""
️ Threshold Tuning

Default threshold: 0.5
- If P(admitted) > 0.5 → Predict admitted

But you can change this!
- Strict admission (0.7): Admit only high-confidence students
- Lenient admission (0.3): Give more students a chance
""")

# Try different thresholds
thresholds_to_test = [0.3, 0.5, 0.7]

print(f"\n Effect of Different Thresholds:")
print(f"{'Threshold':<12} {'Accuracy':<10} {'Precision':<11} {'Recall':<8} {'F1-Score':<10}")
print("-" * 60)

for threshold in thresholds_to_test:
    y_pred_threshold = (y_pred_proba[:, 1] >= threshold).astype(int)
    acc = accuracy_score(y_test, y_pred_threshold)
    cm_t = confusion_matrix(y_test, y_pred_threshold)
    tn_t, fp_t, fn_t, tp_t = cm_t.ravel()

    prec = tp_t / (tp_t + fp_t) if (tp_t + fp_t) > 0 else 0
    rec = tp_t / (tp_t + fn_t) if (tp_t + fn_t) > 0 else 0
    f1 = 2 * (prec * rec) / (prec + rec) if (prec + rec) > 0 else 0

    print(f"{threshold:<12.1f} {acc:<10.4f} {prec:<11.4f} {rec:<8.4f} {f1:<10.4f}")

print(f"\n Trade-offs:")
print(f"   Low threshold (0.3): More admissions, but more false positives")
print(f"   High threshold (0.7): Fewer admissions, but more confidence in decisions")

# ============================================================
# WHY THIS MATTERS
# ============================================================
print("\n\n WHY LOGISTIC REGRESSION MATTERS")
print("=" * 70)
print("""
1. FOUNDATION OF CLASSIFICATION:
   - Understanding logistic regression helps you understand neural networks
   - Final layer of neural networks often uses sigmoid function
   - Same concepts: weights, bias, gradient descent

2. FAST AND INTERPRETABLE:
   - Trains quickly even on large datasets
   - Coefficients show feature importance
   - Easy to explain to non-technical people

3. WORKS WELL IN PRACTICE:
   - Used in production at many companies
   - Great baseline model (try this first!)
   - Often good enough for many problems

4. PROBABILISTIC OUTPUT:
   - Gives you confidence scores (probabilities)
   - You can tune the decision threshold
   - Can handle imbalanced classes

5. REAL WORLD APPLICATIONS:
   - Email spam detection
   - Credit card fraud detection
   - Disease diagnosis
   - Customer churn prediction
   - Click-through rate prediction (ads)

 KEY TAKEAWAYS:
    Logistic regression is for CLASSIFICATION (not regression!)
    Sigmoid function converts any value to probability (0-1)
    Confusion matrix shows all types of errors
    Precision and recall measure different aspects of performance
    ROC-AUC score summarizes overall discrimination ability
    You can tune the decision threshold based on your needs

️ LIMITATIONS:
   - Only works for linearly separable data
   - Assumes features are independent
   - Can't capture complex non-linear patterns
   - For complex patterns, use: Decision Trees, Random Forests, Neural Networks

 Next Steps:
   - Learn K-Nearest Neighbors (KNN) - non-parametric classification
   - Learn Decision Trees - can capture non-linear patterns
   - Learn multiclass classification (more than 2 classes)
   - Practice with real datasets (Titanic, Breast Cancer, etc.)
""")

print("\n Logistic Regression Complete!")
print("Next: knn.py - K-Nearest Neighbors algorithm")
