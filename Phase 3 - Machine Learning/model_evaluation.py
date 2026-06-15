"""
 MODEL EVALUATION - Measuring Success the Right Way
======================================================

What is Model Evaluation?
-------------------------
You trained a model... but is it actually GOOD?

The Danger: "My model is 99% accurate!"
Reality: The dataset has 99% of one class (imbalanced!)
Your model just predicts the majority class every time!

The Truth: Accuracy alone is NOT enough!

We need:
1. Multiple metrics (precision, recall, F1)
2. Confusion matrix (see all types of errors)
3. ROC curves (trade-offs)
4. Learning curves (detect overfitting)
5. Cross-validation (robust estimates)

Real World Analogy:
Judging a chef:
- Don't just count how many dishes they made 
- Taste the food, check presentation, speed, consistency 

This file covers ALL the evaluation techniques you need!
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split, learning_curve
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import make_classification
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score, f1_score,
    confusion_matrix, classification_report,
    roc_curve, roc_auc_score, precision_recall_curve,
    mean_squared_error, mean_absolute_error, r2_score
)

print("=" * 70)
print("MODEL EVALUATION - Comprehensive Guide to Metrics")
print("=" * 70)

# ============================================================
# PART 1: Classification Metrics Overview
# ============================================================
print("\n PART 1: Understanding Classification Metrics")
print("-" * 70)

print("""
 The Confusion Matrix - Foundation of All Metrics

                    Predicted
                    Negative  Positive
Actual  Negative  [   TN   |   FP   ]
                  [---------+--------]
        Positive  [   FN   |   TP   ]

TN = True Negative (correctly predicted negative) 
FP = False Positive (predicted positive, actually negative)  Type I Error
FN = False Negative (predicted negative, actually positive)  Type II Error
TP = True Positive (correctly predicted positive) 

From these 4 numbers, we derive ALL classification metrics!
""")

# ============================================================
# PART 2: Creating Example Dataset
# ============================================================
print("\n\n PART 2: Binary Classification Example")
print("-" * 70)

print("""
 Problem: Email Spam Detection

- Positive class: Spam (1)
- Negative class: Not Spam (0)

This is an imbalanced dataset (80% not spam, 20% spam)
→ Accuracy alone would be misleading!
""")

# Generate imbalanced dataset
np.random.seed(42)
X, y = make_classification(
    n_samples=1000,
    n_features=20,
    n_informative=15,
    n_redundant=5,
    n_classes=2,
    weights=[0.8, 0.2],  # 80% class 0, 20% class 1
    random_state=42
)

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

print(f"\n Dataset Info:")
print(f"   Total samples: {len(y)}")
print(f"   Training samples: {len(y_train)}")
print(f"   Test samples: {len(y_test)}")
print(f"   Features: {X.shape[1]}")

# Check class distribution
unique, counts = np.unique(y, return_counts=True)
print(f"\n Class Distribution:")
for cls, count in zip(unique, counts):
    label = "Not Spam" if cls == 0 else "Spam"
    print(f"   {label}: {count} ({count/len(y)*100:.1f}%)")

# Train a model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
y_pred_proba = model.predict_proba(X_test)[:, 1]

print(f"\n Model trained!")

# ============================================================
# PART 3: The Confusion Matrix
# ============================================================
print("\n\n PART 3: Confusion Matrix - Detailed Error Analysis")
print("-" * 70)

cm = confusion_matrix(y_test, y_pred)
tn, fp, fn, tp = cm.ravel()

print(f"\n Confusion Matrix:")
print(f"\n                  Predicted")
print(f"                  Not Spam   Spam")
print(f"Actual Not Spam   {tn:^10d} {fp:^8d}")
print(f"       Spam       {fn:^10d} {tp:^8d}")

print(f"\n Breaking it Down:")
print(f"   True Negatives (TN): {tn}")
print(f"      → Correctly identified {tn} non-spam emails ")
print(f"\n   False Positives (FP): {fp}")
print(f"      → Wrongly flagged {fp} good emails as spam ")
print(f"      → TYPE I ERROR: False alarm!")
print(f"      → COST: User misses important emails!")
print(f"\n   False Negatives (FN): {fn}")
print(f"      → Missed {fn} spam emails (they reached inbox) ")
print(f"      → TYPE II ERROR: Missed detection!")
print(f"      → COST: User sees spam!")
print(f"\n   True Positives (TP): {tp}")
print(f"      → Correctly caught {tp} spam emails ")

# Visualize
plt.figure(figsize=(8, 6))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', cbar=False,
            xticklabels=['Not Spam', 'Spam'],
            yticklabels=['Not Spam', 'Spam'])
plt.xlabel('Predicted Label', fontsize=12)
plt.ylabel('True Label', fontsize=12)
plt.title('Confusion Matrix - Email Spam Detection', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.savefig('eval_confusion_matrix.png', dpi=150)
print("\n Saved plot: eval_confusion_matrix.png")

# ============================================================
# PART 4: Core Metrics Explained
# ============================================================
print("\n\n PART 4: Core Classification Metrics")
print("-" * 70)

accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)

print("""
 ACCURACY: Overall correctness
   Formula: (TP + TN) / (TP + TN + FP + FN)
   Question: "What percentage of predictions are correct?"
""")
print(f"   Accuracy = ({tp} + {tn}) / {len(y_test)} = {accuracy:.4f} ({accuracy*100:.2f}%)")
print(f"   ️ Can be misleading with imbalanced data!")

print(f"""

 PRECISION: When we predict positive, how often are we right?
   Formula: TP / (TP + FP)
   Question: "Of all spam predictions, how many are actually spam?"
   High precision = Few false alarms
""")
print(f"   Precision = {tp} / ({tp} + {fp}) = {precision:.4f} ({precision*100:.2f}%)")
print(f"    When we flag an email as spam, we're right {precision*100:.1f}% of the time")

print(f"""

 RECALL (Sensitivity, True Positive Rate): Of all actual positives, how many did we catch?
   Formula: TP / (TP + FN)
   Question: "Of all actual spam, how many did we detect?"
   High recall = We catch most spam
""")
print(f"   Recall = {tp} / ({tp} + {fn}) = {recall:.4f} ({recall*100:.2f}%)")
print(f"    We catch {recall*100:.1f}% of all spam emails")

print(f"""

️ F1-SCORE: Harmonic mean of precision and recall
   Formula: 2 × (Precision × Recall) / (Precision + Recall)
   Question: "What's the balance between precision and recall?"
   Use when: You need both precision and recall to be good
""")
print(f"   F1 = 2 × ({precision:.4f} × {recall:.4f}) / ({precision:.4f} + {recall:.4f}) = {f1:.4f}")
print(f"    Overall balance score: {f1*100:.1f}%")

print(f"""

 SPECIFICITY (True Negative Rate): Of all actual negatives, how many did we correctly identify?
   Formula: TN / (TN + FP)
   Question: "Of all good emails, how many did we correctly leave alone?"
""")
specificity = tn / (tn + fp) if (tn + fp) > 0 else 0
print(f"   Specificity = {tn} / ({tn} + {fp}) = {specificity:.4f} ({specificity*100:.2f}%)")
print(f"    We correctly identify {specificity*100:.1f}% of legitimate emails")

# ============================================================
# PART 5: The Precision-Recall Trade-off
# ============================================================
print("\n\n PART 5: The Precision-Recall Trade-off")
print("-" * 70)

print("""
️ The Fundamental Trade-off:

Can't maximize both precision and recall simultaneously!

High Threshold (0.9):
   → Predict spam only when VERY confident
   → HIGH PRECISION (few false positives)
   → LOW RECALL (miss some spam)
   → Example: Conservative spam filter

Low Threshold (0.3):
   → Predict spam more liberally
   → LOW PRECISION (more false positives)
   → HIGH RECALL (catch most spam)
   → Example: Aggressive spam filter

Which is worse?
   False Positive: Good email marked as spam (user misses important email!)
   False Negative: Spam reaches inbox (user slightly annoyed)

For email: FALSE POSITIVES are WORSE!
→ Choose high precision (even if recall suffers)
""")

# Calculate precision-recall for different thresholds
precisions, recalls, thresholds_pr = precision_recall_curve(y_test, y_pred_proba)

# Plot Precision-Recall curve
plt.figure(figsize=(10, 6))
plt.plot(recalls, precisions, linewidth=3, color='blue')
plt.xlabel('Recall', fontsize=12)
plt.ylabel('Precision', fontsize=12)
plt.title('Precision-Recall Curve', fontsize=14, fontweight='bold')
plt.grid(True, alpha=0.3)
plt.axhline(y=precision, color='r', linestyle='--', alpha=0.7, label=f'Current (threshold=0.5)')
plt.axvline(x=recall, color='r', linestyle='--', alpha=0.7)
plt.legend(fontsize=11)
plt.tight_layout()
plt.savefig('eval_precision_recall_curve.png', dpi=150)
print("\n Saved plot: eval_precision_recall_curve.png")

# Show effect of different thresholds
thresholds_to_test = [0.3, 0.5, 0.7, 0.9]
print(f"\n Effect of Different Thresholds:")
print(f"{'Threshold':<12} {'Precision':<12} {'Recall':<10} {'F1-Score':<10} {'Best For':<30}")
print("-" * 80)

for thresh in thresholds_to_test:
    y_pred_thresh = (y_pred_proba >= thresh).astype(int)
    prec = precision_score(y_test, y_pred_thresh, zero_division=0)
    rec = recall_score(y_test, y_pred_thresh, zero_division=0)
    f1_thresh = f1_score(y_test, y_pred_thresh, zero_division=0)

    if thresh <= 0.3:
        best_for = "Aggressive filtering"
    elif thresh >= 0.7:
        best_for = "Conservative (avoid FP)"
    else:
        best_for = "Balanced"

    print(f"{thresh:<12.1f} {prec:<12.4f} {rec:<10.4f} {f1_thresh:<10.4f} {best_for:<30}")

# ============================================================
# PART 6: ROC Curve and AUC
# ============================================================
print("\n\n PART 6: ROC Curve - Overall Discrimination Ability")
print("-" * 70)

print("""
 ROC Curve (Receiver Operating Characteristic):

Plots:
   X-axis: False Positive Rate (FPR) = FP / (FP + TN)
   Y-axis: True Positive Rate (TPR) = TP / (TP + FN) = Recall

Shows trade-off between:
   - Catching positives (TPR)
   - Avoiding false alarms (1 - FPR)

AUC (Area Under Curve):
   - Perfect classifier: AUC = 1.0
   - Random guessing: AUC = 0.5
   - Worse than random: AUC < 0.5 (something's wrong!)

   AUC Interpretation:
   - 0.9-1.0: Excellent ⭐
   - 0.8-0.9: Very good 
   - 0.7-0.8: Good
   - 0.6-0.7: Fair
   - 0.5-0.6: Poor
""")

# Calculate ROC curve
fpr, tpr, thresholds_roc = roc_curve(y_test, y_pred_proba)
roc_auc = roc_auc_score(y_test, y_pred_proba)

print(f"\n AUC Score: {roc_auc:.4f}")
if roc_auc >= 0.9:
    print(f"   ⭐ Excellent! Model has outstanding discriminative ability!")
elif roc_auc >= 0.8:
    print(f"    Very good! Model distinguishes classes well!")
elif roc_auc >= 0.7:
    print(f"   Good! Model has useful predictive power")
else:
    print(f"   Fair. Model needs improvement")

# Plot ROC curve
plt.figure(figsize=(10, 6))
plt.plot(fpr, tpr, linewidth=3, label=f'Model (AUC = {roc_auc:.3f})', color='blue')
plt.plot([0, 1], [0, 1], 'k--', linewidth=2, label='Random Classifier (AUC = 0.5)')
plt.fill_between(fpr, tpr, alpha=0.2)
plt.xlabel('False Positive Rate', fontsize=12)
plt.ylabel('True Positive Rate (Recall)', fontsize=12)
plt.title('ROC Curve - Model Discrimination Ability', fontsize=14, fontweight='bold')
plt.legend(fontsize=11, loc='lower right')
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('eval_roc_curve.png', dpi=150)
print("\n Saved plot: eval_roc_curve.png")

# ============================================================
# PART 7: Classification Report
# ============================================================
print("\n\n PART 7: Complete Classification Report")
print("-" * 70)

print(f"\n Scikit-Learn Classification Report:")
print(classification_report(y_test, y_pred, target_names=['Not Spam', 'Spam']))

print("""
 Understanding the Report:

Precision: "When we predict this class, how often are we right?"
Recall: "Of all actual instances of this class, how many did we find?"
F1-Score: "Harmonic mean of precision and recall"

Support: Number of actual instances of each class

Macro Average: Simple average across classes (treats all classes equally)
Weighted Average: Weighted by support (accounts for imbalance)

For imbalanced data: Focus on weighted average!
""")

# ============================================================
# PART 8: Regression Metrics
# ============================================================
print("\n\n PART 8: Regression Metrics (Predicting Numbers)")
print("-" * 70)

print("""
 Regression Metrics:

When predicting continuous values (house prices, temperature, etc.),
we use different metrics!
""")

# Generate regression example
from sklearn.ensemble import RandomForestRegressor
from sklearn.datasets import make_regression

X_reg, y_reg = make_regression(n_samples=500, n_features=10, noise=10, random_state=42)
X_train_reg, X_test_reg, y_train_reg, y_test_reg = train_test_split(
    X_reg, y_reg, test_size=0.3, random_state=42
)

# Train model
reg_model = RandomForestRegressor(n_estimators=100, random_state=42)
reg_model.fit(X_train_reg, y_train_reg)
y_pred_reg = reg_model.predict(X_test_reg)

# Calculate metrics
mae = mean_absolute_error(y_test_reg, y_pred_reg)
mse = mean_squared_error(y_test_reg, y_pred_reg)
rmse = np.sqrt(mse)
r2 = r2_score(y_test_reg, y_pred_reg)

print(f"""
 Mean Absolute Error (MAE):
   Formula: (1/n) × Σ|actual - predicted|
   Meaning: Average absolute difference
   Units: Same as target variable
   Value: {mae:.2f}
    On average, predictions are off by {mae:.2f} units

 Mean Squared Error (MSE):
   Formula: (1/n) × Σ(actual - predicted)²
   Meaning: Average squared difference
   Units: Squared target units
   Value: {mse:.2f}
    Penalizes large errors more than MAE

 Root Mean Squared Error (RMSE):
   Formula: √MSE
   Meaning: Square root of MSE (back to original units)
   Units: Same as target variable
   Value: {rmse:.2f}
    Standard deviation of prediction errors

 R² Score (Coefficient of Determination):
   Formula: 1 - (SS_residual / SS_total)
   Range: -∞ to 1.0
   Value: {r2:.4f}
   Interpretation:
   - 1.0 = Perfect predictions
   - 0.0 = No better than predicting the mean
   - Negative = Worse than predicting the mean!
    Our model explains {r2*100:.1f}% of the variance
""")

# Visualize predictions
plt.figure(figsize=(10, 6))
plt.scatter(y_test_reg, y_pred_reg, alpha=0.6, s=50)
plt.plot([y_test_reg.min(), y_test_reg.max()],
         [y_test_reg.min(), y_test_reg.max()],
         'r--', linewidth=2, label='Perfect Predictions')
plt.xlabel('Actual Values', fontsize=12)
plt.ylabel('Predicted Values', fontsize=12)
plt.title(f'Regression Predictions (R² = {r2:.3f})', fontsize=14, fontweight='bold')
plt.legend(fontsize=11)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('eval_regression_scatter.png', dpi=150)
print("\n Saved plot: eval_regression_scatter.png")

# Residual plot
residuals = y_test_reg - y_pred_reg
plt.figure(figsize=(10, 6))
plt.scatter(y_pred_reg, residuals, alpha=0.6, s=50)
plt.axhline(y=0, color='r', linestyle='--', linewidth=2)
plt.xlabel('Predicted Values', fontsize=12)
plt.ylabel('Residuals (Actual - Predicted)', fontsize=12)
plt.title('Residual Plot - Check for Patterns', fontsize=14, fontweight='bold')
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('eval_residual_plot.png', dpi=150)
print(" Saved plot: eval_residual_plot.png")
print("  Good model: Residuals randomly scattered around zero")
print("  Bad model: Patterns in residuals (curved, fanning out)")

# ============================================================
# PART 9: Learning Curves - Diagnosing Overfitting/Underfitting
# ============================================================
print("\n\n PART 9: Learning Curves - Diagnosing Your Model")
print("-" * 70)

print("""
 Learning Curves: Train vs Validation Score as Dataset Size Increases

Use to diagnose:
1. OVERFITTING: Train score >> Val score
   → Model memorizing instead of learning
   → Solution: More data, regularization, simpler model

2. UNDERFITTING: Both scores low and close
   → Model too simple
   → Solution: More complex model, more features

3. GOOD FIT: Scores close and high
   → Model generalizes well!
   → Keep it!

4. MORE DATA HELPS: Val score still improving
   → Collect more data!
   → Model hasn't plateaued yet
""")

# Calculate learning curves
train_sizes, train_scores, val_scores = learning_curve(
    RandomForestClassifier(n_estimators=50, random_state=42),
    X_train, y_train,
    train_sizes=np.linspace(0.1, 1.0, 10),
    cv=5,
    scoring='accuracy',
    n_jobs=-1
)

# Calculate means and stds
train_mean = np.mean(train_scores, axis=1)
train_std = np.std(train_scores, axis=1)
val_mean = np.mean(val_scores, axis=1)
val_std = np.std(val_scores, axis=1)

# Plot
plt.figure(figsize=(10, 6))
plt.plot(train_sizes, train_mean, 'o-', linewidth=2, markersize=8, label='Training Score')
plt.fill_between(train_sizes, train_mean - train_std, train_mean + train_std, alpha=0.2)
plt.plot(train_sizes, val_mean, 'o-', linewidth=2, markersize=8, label='Validation Score')
plt.fill_between(train_sizes, val_mean - val_std, val_mean + val_std, alpha=0.2)
plt.xlabel('Training Set Size', fontsize=12)
plt.ylabel('Accuracy', fontsize=12)
plt.title('Learning Curve - Diagnosing Model Performance', fontsize=14, fontweight='bold')
plt.legend(fontsize=11)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('eval_learning_curve.png', dpi=150)
print("\n Saved plot: eval_learning_curve.png")

gap = train_mean[-1] - val_mean[-1]
if gap < 0.05:
    print(f"   Good fit! Train and validation scores are close")
elif gap < 0.15:
    print(f"  ️ Slight overfitting (gap = {gap:.3f})")
else:
    print(f"  ️ Overfitting detected! (gap = {gap:.3f})")

# ============================================================
# WHY THIS MATTERS
# ============================================================
print("\n\n WHY PROPER EVALUATION MATTERS")
print("=" * 70)
print("""
1. AVOID BEING FOOLED:
   - 99% accuracy sounds great... unless 99% of data is one class!
   - Always check multiple metrics
   - Always check confusion matrix

2. CHOOSE RIGHT METRIC FOR YOUR PROBLEM:
   - Email spam: Minimize false positives (high precision)
   - Cancer detection: Minimize false negatives (high recall)
   - Balanced problem: F1-score or accuracy

3. UNDERSTAND TRADE-OFFS:
   - Can't maximize everything simultaneously
   - Choose based on business cost
   - Tune threshold based on your needs

4. DIAGNOSE PROBLEMS:
   - Learning curves show overfitting/underfitting
   - Residual plots show regression problems
   - ROC curve shows overall discrimination

5. PRODUCTION READINESS:
   - Know your model's strengths and weaknesses
   - Set appropriate expectations
   - Monitor right metrics in production

 KEY TAKEAWAYS:
    Accuracy alone is NOT enough (especially for imbalanced data)
    Confusion matrix shows all types of errors
    Precision: "When I predict positive, how often am I right?"
    Recall: "Of all positives, how many did I catch?"
    F1-score: Balance between precision and recall
    ROC-AUC: Overall discrimination ability
    Choose metric based on business cost
    Learning curves diagnose overfitting/underfitting
    Always evaluate on held-out test set!

 Which Metric When?
   - Fraud detection: HIGH RECALL (catch all fraud, even with false alarms)
   - Spam filtering: HIGH PRECISION (avoid marking good emails as spam)
   - Medical diagnosis: HIGH RECALL (don't miss sick patients)
   - Recommendation systems: F1-SCORE (balance relevance and coverage)
   - Imbalanced data: F1-SCORE or ROC-AUC (not accuracy!)
   - Regression: RMSE (penalizes large errors) or MAE (robust to outliers)

 Next Steps:
   - Learn cross-validation (next file!)
   - Practice with real imbalanced datasets
   - Learn about class weights and SMOTE
   - Understand cost-sensitive learning
   - Learn about multi-class metrics
""")

print("\n Model Evaluation Complete!")
print("Next: feature_engineering.py - Preparing data for better models")
