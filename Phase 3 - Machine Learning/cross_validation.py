"""
 CROSS-VALIDATION - Robust Model Evaluation
==============================================

What is Cross-Validation?
--------------------------
Testing your model on multiple different train/test splits!

The Problem with Single Train-Test Split:
- You might get lucky (easy test set → overestimate performance)
- You might get unlucky (hard test set → underestimate performance)
- Results depend on random split → Not reliable!

The Solution: K-Fold Cross-Validation
1. Split data into K equal parts (folds)
2. Train on K-1 folds, test on 1 fold
3. Repeat K times (each fold is test set once)
4. Average the K results → More reliable estimate!

Real World Analogy:
Testing a student:
- Single exam: Might get lucky/unlucky questions
- 5 different exams: Average score is more reliable!

Benefits:
- More reliable performance estimate
- Uses all data for both training and testing
- Detects overfitting better
- Standard practice in ML!
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import (
    KFold, StratifiedKFold, cross_val_score, cross_validate,
    GridSearchCV, RandomizedSearchCV
)
from sklearn.datasets import make_classification, load_breast_cancer
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline

print("=" * 70)
print("CROSS-VALIDATION - Getting Reliable Performance Estimates")
print("=" * 70)

# ============================================================
# PART 1: The Problem with Single Train-Test Split
# ============================================================
print("\n PART 1: Why Single Split is Unreliable")
print("-" * 70)

print("""
 The Randomness Problem:

Imagine splitting data 10 times and getting these accuracies:
   Split 1: 95%  ← Got lucky!
   Split 2: 78%  ← Got unlucky!
   Split 3: 85%
   Split 4: 82%
   Split 5: 88%
   ...

Which accuracy should you report?
→ You need the AVERAGE to get a reliable estimate!

Cross-validation solves this by systematically using different splits.
""")

# Generate dataset
np.random.seed(42)
X, y = make_classification(
    n_samples=200,
    n_features=20,
    n_informative=15,
    n_redundant=5,
    n_classes=2,
    random_state=42
)

# Demonstrate variability in single splits
from sklearn.model_selection import train_test_split

print(f"\n Testing with 10 Different Random Splits:")
print(f"{'Split':<8} {'Train Acc':<12} {'Test Acc':<12} {'Difference':<12}")
print("-" * 50)

model = RandomForestClassifier(n_estimators=50, random_state=42)
test_accuracies = []

for i in range(10):
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, random_state=i
    )
    model.fit(X_train, y_train)
    train_acc = model.score(X_train, y_train)
    test_acc = model.score(X_test, y_test)
    test_accuracies.append(test_acc)

    print(f"{i+1:<8} {train_acc:<12.4f} {test_acc:<12.4f} {abs(train_acc - test_acc):<12.4f}")

print(f"\n Statistics:")
print(f"   Mean test accuracy: {np.mean(test_accuracies):.4f}")
print(f"   Std deviation: {np.std(test_accuracies):.4f}")
print(f"   Min: {np.min(test_accuracies):.4f}")
print(f"   Max: {np.max(test_accuracies):.4f}")
print(f"   Range: {np.max(test_accuracies) - np.min(test_accuracies):.4f}")
print(f"\n️ Huge variability! Which score do you trust?")

# ============================================================
# PART 2: K-Fold Cross-Validation Explained
# ============================================================
print("\n\n PART 2: K-Fold Cross-Validation Step-by-Step")
print("-" * 70)

print("""
 How K-Fold Works (Example: K=5):

Original data: [■■■■■■■■■■■■■■■■■■■■] (20 samples)

Fold 1: [Test][Train][Train][Train][Train]
Fold 2: [Train][Test][Train][Train][Train]
Fold 3: [Train][Train][Test][Train][Train]
Fold 4: [Train][Train][Train][Test][Train]
Fold 5: [Train][Train][Train][Train][Test]

Each sample is used:
- 4 times for training (80%)
- 1 time for testing (20%)

Final score: Average of all 5 test scores
→ Uses ALL data efficiently!

Common K values:
- K=5: Standard choice (fast, good balance)
- K=10: More reliable but slower
- K=n (Leave-One-Out): Most thorough but very slow
""")

# Demonstrate K-Fold
kfold = KFold(n_splits=5, shuffle=True, random_state=42)

print(f"\n 5-Fold Cross-Validation Splits:")
print(f"{'Fold':<8} {'Train Size':<15} {'Test Size':<15} {'Test Indices':<30}")
print("-" * 75)

for fold, (train_idx, test_idx) in enumerate(kfold.split(X), 1):
    print(f"{fold:<8} {len(train_idx):<15} {len(test_idx):<15} {test_idx[:5].tolist()}...")

# ============================================================
# PART 3: Performing Cross-Validation
# ============================================================
print("\n\n PART 3: Performing Cross-Validation with Scikit-Learn")
print("-" * 70)

# Simple cross-validation
model = RandomForestClassifier(n_estimators=100, random_state=42)
cv_scores = cross_val_score(model, X, y, cv=5, scoring='accuracy')

print(f"\n 5-Fold Cross-Validation Results:")
for fold, score in enumerate(cv_scores, 1):
    print(f"   Fold {fold}: {score:.4f} ({score*100:.2f}%)")

print(f"\n Summary Statistics:")
print(f"   Mean: {cv_scores.mean():.4f} ({cv_scores.mean()*100:.2f}%)")
print(f"   Std Dev: {cv_scores.std():.4f}")
print(f"   95% Confidence Interval: {cv_scores.mean():.4f} ± {1.96 * cv_scores.std():.4f}")
print(f"\n Much more reliable than single split!")
print(f"   We can say: 'Model accuracy is {cv_scores.mean()*100:.1f}% ± {cv_scores.std()*100:.1f}%'")

# ============================================================
# PART 4: Stratified K-Fold (For Imbalanced Data)
# ============================================================
print("\n\n PART 4: Stratified K-Fold - Better for Imbalanced Data")
print("-" * 70)

print("""
️ Stratified K-Fold:

Problem with regular K-Fold:
   If you have imbalanced classes (90% class A, 10% class B),
   some folds might get NO examples of class B!

Stratified K-Fold:
   Ensures each fold has the SAME class distribution as original data
   → Each fold has ~90% class A, ~10% class B

When to use:
    Classification with imbalanced classes (always!)
    Regression (stratification doesn't make sense)
""")

# Create imbalanced dataset
X_imb, y_imb = make_classification(
    n_samples=200,
    n_features=20,
    n_classes=2,
    weights=[0.9, 0.1],  # 90% class 0, 10% class 1
    random_state=42
)

print(f"\n Imbalanced Dataset:")
unique, counts = np.unique(y_imb, return_counts=True)
for cls, count in zip(unique, counts):
    print(f"   Class {cls}: {count} samples ({count/len(y_imb)*100:.1f}%)")

# Compare regular vs stratified
print(f"\n Regular K-Fold Class Distribution:")
kfold_regular = KFold(n_splits=5, shuffle=True, random_state=42)

for fold, (train_idx, test_idx) in enumerate(kfold_regular.split(X_imb), 1):
    y_test_fold = y_imb[test_idx]
    class_1_pct = (y_test_fold == 1).sum() / len(y_test_fold) * 100
    print(f"   Fold {fold}: {class_1_pct:.1f}% class 1 (should be 10%)")

print(f"\n Stratified K-Fold Class Distribution:")
skfold = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)

for fold, (train_idx, test_idx) in enumerate(skfold.split(X_imb, y_imb), 1):
    y_test_fold = y_imb[test_idx]
    class_1_pct = (y_test_fold == 1).sum() / len(y_test_fold) * 100
    print(f"   Fold {fold}: {class_1_pct:.1f}% class 1 (perfectly balanced!)")

# Compare performance
scores_regular = cross_val_score(model, X_imb, y_imb, cv=kfold_regular)
scores_stratified = cross_val_score(model, X_imb, y_imb, cv=skfold)

print(f"\n Performance Comparison:")
print(f"   Regular K-Fold: {scores_regular.mean():.4f} ± {scores_regular.std():.4f}")
print(f"   Stratified K-Fold: {scores_stratified.mean():.4f} ± {scores_stratified.std():.4f}")
print(f"\n Stratified is more reliable for imbalanced data!")

# ============================================================
# PART 5: Multiple Metrics with cross_validate
# ============================================================
print("\n\n PART 5: Evaluating Multiple Metrics")
print("-" * 70)

print("""
 cross_validate: Get multiple metrics at once!

Instead of just accuracy, get:
- Accuracy
- Precision
- Recall
- F1-score
- Training time
- Scoring time
""")

# Load real dataset
data = load_breast_cancer()
X_real = data.data
y_real = data.target

print(f"\n Dataset: Breast Cancer Wisconsin")
print(f"   Samples: {X_real.shape[0]}")
print(f"   Features: {X_real.shape[1]}")
print(f"   Classes: {len(np.unique(y_real))} (Malignant, Benign)")

# Cross-validate with multiple metrics
scoring = ['accuracy', 'precision', 'recall', 'f1', 'roc_auc']
cv_results = cross_validate(
    model, X_real, y_real,
    cv=5,
    scoring=scoring,
    return_train_score=True
)

print(f"\n Cross-Validation Results (5-fold):")
print(f"{'Metric':<20} {'Mean':<12} {'Std':<10}")
print("-" * 45)

for metric in scoring:
    test_scores = cv_results[f'test_{metric}']
    print(f"{'Test ' + metric:<20} {test_scores.mean():<12.4f} {test_scores.std():<10.4f}")

print(f"\n️ Timing:")
print(f"   Fit time: {cv_results['fit_time'].mean():.4f}s ± {cv_results['fit_time'].std():.4f}s")
print(f"   Score time: {cv_results['score_time'].mean():.4f}s ± {cv_results['score_time'].std():.4f}s")

# ============================================================
# PART 6: Comparing Multiple Models
# ============================================================
print("\n\n PART 6: Comparing Multiple Models")
print("-" * 70)

print("""
 Use cross-validation to choose the best model!

Fair comparison:
- Same data splits for all models
- Same evaluation metrics
- Report mean ± std dev
""")

# Define models
models = {
    'Logistic Regression': LogisticRegression(max_iter=1000, random_state=42),
    'Decision Tree': DecisionTreeClassifier(max_depth=10, random_state=42),
    'Random Forest': RandomForestClassifier(n_estimators=100, random_state=42),
    'SVM': SVC(kernel='rbf', random_state=42)
}

# Create pipeline with scaling (important for LR and SVM)
results = []

print(f"\n Model Comparison (5-Fold CV):")
print(f"{'Model':<25} {'Accuracy':<20} {'Precision':<20} {'Recall':<15}")
print("-" * 85)

for name, model in models.items():
    # Create pipeline
    pipeline = Pipeline([
        ('scaler', StandardScaler()),
        ('model', model)
    ])

    # Cross-validate
    cv_scores = cross_validate(
        pipeline, X_real, y_real,
        cv=5,
        scoring=['accuracy', 'precision', 'recall']
    )

    acc_mean = cv_scores['test_accuracy'].mean()
    acc_std = cv_scores['test_accuracy'].std()
    prec_mean = cv_scores['test_precision'].mean()
    prec_std = cv_scores['test_precision'].std()
    rec_mean = cv_scores['test_recall'].mean()
    rec_std = cv_scores['test_recall'].std()

    results.append({
        'Model': name,
        'Accuracy': acc_mean,
        'Precision': prec_mean,
        'Recall': rec_mean
    })

    print(f"{name:<25} {acc_mean:.4f}±{acc_std:.4f} "f"{prec_mean:.4f}±{prec_std:.4f} "f"{rec_mean:.4f}±{rec_std:.4f}")

# Find best model
best_model = max(results, key=lambda x: x['Accuracy'])
print(f"\n Best Model: {best_model['Model']}")
print(f"   Accuracy: {best_model['Accuracy']:.4f}")

# Visualize comparison
results_df = pd.DataFrame(results)
fig, ax = plt.subplots(figsize=(10, 6))
x = np.arange(len(results_df))
width = 0.25

ax.bar(x - width, results_df['Accuracy'], width, label='Accuracy', alpha=0.8)
ax.bar(x, results_df['Precision'], width, label='Precision', alpha=0.8)
ax.bar(x + width, results_df['Recall'], width, label='Recall', alpha=0.8)

ax.set_xlabel('Model', fontsize=12)
ax.set_ylabel('Score', fontsize=12)
ax.set_title('Model Comparison - Cross-Validation Results', fontsize=14, fontweight='bold')
ax.set_xticks(x)
ax.set_xticklabels(results_df['Model'], rotation=45, ha='right')
ax.legend()
ax.grid(axis='y', alpha=0.3)
plt.tight_layout()
plt.savefig('D:/', dpi=150)
print("\n Saved plot: cross_validation_model_comparison.png")

# ============================================================
# PART 7: Hyperparameter Tuning with GridSearchCV
# ============================================================
print("\n\n PART 7: Hyperparameter Tuning with GridSearchCV")
print("-" * 70)

print("""
️ GridSearchCV: Find the best hyperparameters!

Process:
1. Define parameter grid (all combinations to try)
2. For each combination:
   - Perform cross-validation
   - Calculate average score
3. Return best parameters

Example: Random Forest
   n_estimators: [50, 100, 200]
   max_depth: [5, 10, 15]
   → 3 × 3 = 9 combinations
   → With 5-fold CV = 45 total model fits!
""")

# Define parameter grid
param_grid = {
    'n_estimators': [50, 100, 200],
    'max_depth': [5, 10, 15],
    'min_samples_split': [2, 5]
}

print(f"\n Parameter Grid:")
for param, values in param_grid.items():
    print(f"   {param}: {values}")

total_combinations = np.prod([len(v) for v in param_grid.values()])
print(f"\n   Total combinations: {total_combinations}")
print(f"   With 5-fold CV: {total_combinations * 5} model fits!")

# Perform grid search
grid_search = GridSearchCV(
    RandomForestClassifier(random_state=42),
    param_grid,
    cv=5,
    scoring='accuracy',
    n_jobs=-1,
    verbose=0
)

print(f"\n Running GridSearchCV...")
grid_search.fit(X_real, y_real)
print(f"   Search complete! ")

# Results
print(f"\n Best Parameters:")
for param, value in grid_search.best_params_.items():
    print(f"   {param}: {value}")

print(f"\n Best Cross-Validation Score: {grid_search.best_score_:.4f}")
print(f"\n These are the optimal hyperparameters!")

# Show top 5 parameter combinations
results_df = pd.DataFrame(grid_search.cv_results_)
top_5 = results_df.nsmallest(5, 'rank_test_score')[['params', 'mean_test_score', 'std_test_score', 'rank_test_score']]

print(f"\n Top 5 Parameter Combinations:")
for idx, row in top_5.iterrows():
    print(f"   Rank {int(row['rank_test_score'])}: Score={row['mean_test_score']:.4f}±{row['std_test_score']:.4f}")
    print(f"      Params: {row['params']}")

# ============================================================
# PART 8: RandomizedSearchCV (Faster Alternative)
# ============================================================
print("\n\n PART 8: RandomizedSearchCV - When GridSearch is Too Slow")
print("-" * 70)

print("""
 RandomizedSearchCV: Sample random combinations!

Problem with GridSearch:
   100 parameters → 100^5 = 10 billion combinations! 

RandomizedSearchCV:
   - Randomly sample N combinations (e.g., 50)
   - Much faster than exhaustive search
   - Often finds good parameters quickly

Use when:
   - Large parameter space
   - Limited computational resources
   - Want quick results
""")

# Define distributions for random sampling
from scipy.stats import randint, uniform

param_distributions = {
    'n_estimators': randint(50, 300),
    'max_depth': randint(5, 30),
    'min_samples_split': randint(2, 20),
    'min_samples_leaf': randint(1, 10)
}

print(f"\n Parameter Distributions:")
for param, dist in param_distributions.items():
    print(f"   {param}: Random integers or uniform distribution")

# Perform random search
random_search = RandomizedSearchCV(
    RandomForestClassifier(random_state=42),
    param_distributions,
    n_iter=20,  # Try 20 random combinations
    cv=5,
    scoring='accuracy',
    n_jobs=-1,
    random_state=42,
    verbose=0
)

print(f"\n Running RandomizedSearchCV (20 iterations)...")
random_search.fit(X_real, y_real)
print(f"   Search complete! ")

print(f"\n Best Parameters Found:")
for param, value in random_search.best_params_.items():
    print(f"   {param}: {value}")

print(f"\n Best Cross-Validation Score: {random_search.best_score_:.4f}")

# Compare with GridSearch
print(f"\n️ GridSearch vs RandomizedSearch:")
print(f"   GridSearch best score: {grid_search.best_score_:.4f}")
print(f"   RandomSearch best score: {random_search.best_score_:.4f}")
print(f"   Difference: {abs(grid_search.best_score_ - random_search.best_score_):.4f}")
print(f"\n RandomSearch found similar results much faster!")

# ============================================================
# PART 9: Nested Cross-Validation (The Right Way)
# ============================================================
print("\n\n PART 9: Nested Cross-Validation - Unbiased Performance Estimate")
print("-" * 70)

print("""
️ IMPORTANT: GridSearchCV gives OPTIMISTIC estimates!

Problem:
   1. GridSearch finds best params on CV
   2. Reports the best CV score
   → This score is BIASED (overfits to the CV folds!)

Solution: NESTED Cross-Validation
   Outer loop: Estimate true performance
   Inner loop: Tune hyperparameters

Think of it as:
   Outer CV = Final exam (unbiased evaluation)
   Inner CV = Practice exams (hyperparameter tuning)
""")

# Nested CV (simplified example)
outer_cv = KFold(n_splits=5, shuffle=True, random_state=42)
inner_cv = KFold(n_splits=3, shuffle=True, random_state=42)

nested_scores = []

print(f"\n Performing Nested Cross-Validation...")
print(f"   Outer folds: 5")
print(f"   Inner folds: 3")

for fold, (train_idx, test_idx) in enumerate(outer_cv.split(X_real), 1):
    X_train_outer, X_test_outer = X_real[train_idx], X_real[test_idx]
    y_train_outer, y_test_outer = y_real[train_idx], y_real[test_idx]

    # Inner loop: Hyperparameter tuning
    grid_search_inner = GridSearchCV(
        RandomForestClassifier(random_state=42),
        {'n_estimators': [50, 100], 'max_depth': [5, 10]},
        cv=inner_cv,
        n_jobs=-1
    )
    grid_search_inner.fit(X_train_outer, y_train_outer)

    # Outer loop: Evaluate with best params
    score = grid_search_inner.score(X_test_outer, y_test_outer)
    nested_scores.append(score)

    print(f"   Fold {fold}: {score:.4f}")

print(f"\n Nested CV Results:")
print(f"   Mean: {np.mean(nested_scores):.4f}")
print(f"   Std: {np.std(nested_scores):.4f}")
print(f"\n This is the UNBIASED estimate of your model's performance!")

# ============================================================
# WHY THIS MATTERS
# ============================================================
print("\n\n WHY CROSS-VALIDATION MATTERS")
print("=" * 70)
print("""
1. RELIABLE PERFORMANCE ESTIMATES:
   - Single split = Noisy estimate (lucky/unlucky)
   - Cross-validation = Robust estimate (averages out luck)
   - Report: Mean ± Std Dev

2. EFFICIENT DATA USAGE:
   - Uses all data for training AND testing
   - Especially important for small datasets
   - No data is "wasted"

3. MODEL SELECTION:
   - Fair comparison between models
   - Same splits for all models
   - Choose best model objectively

4. HYPERPARAMETER TUNING:
   - GridSearchCV: Exhaustive search
   - RandomizedSearchCV: Random sampling (faster)
   - Finds optimal hyperparameters automatically

5. DETECTS OVERFITTING:
   - High variance in CV scores = Overfitting
   - Train score >> CV score = Overfitting
   - Helps diagnose model problems

6. PRODUCTION READINESS:
   - Confident in reported performance
   - Know the variance (± std dev)
   - Better than cherry-picking best split

 KEY TAKEAWAYS:
    Always use cross-validation (not single split!)
    Use StratifiedKFold for classification
    Report mean ± std dev
    K=5 or K=10 is standard
    Use GridSearchCV to find best hyperparameters
    Use nested CV for unbiased performance estimate
    Compare models on same CV splits
    More folds = More reliable, but slower

 Best Practices:
    Start with 5-fold CV (good balance)
    Use stratified for imbalanced data
    Scale inside CV (prevent data leakage!)
    Use same CV splits for model comparison
    Report confidence intervals
    Use nested CV for publication-ready results

️ Common Mistakes:
    Not using CV (just single train-test split)
    Using GridSearch CV score as final estimate (optimistic!)
    Scaling before CV (data leakage!)
    Not using stratified CV for imbalanced data
    Using K=n (leave-one-out) on large datasets (too slow)
    Not reporting standard deviation

️ Computational Cost:
   - K=5: 5× slower than single split
   - K=10: 10× slower
   - GridSearch × CV: Very slow!
   - Use n_jobs=-1 for parallel processing

 Next Steps:
   - Practice on real datasets
   - Learn about time series CV (different!)
   - Learn about bootstrap sampling
   - Learn about permutation testing
   - Use cross-validation in ALL your projects!
""")

print("\n Cross-Validation Complete!")
print("\n Congratulations! You've completed all 9 ML files!")
print("=" * 70)
print("""
 What You've Learned:

1. linear_regression_scratch.py → How ML really works (gradient descent!)
2. linear_regression_sklearn.py → Using professional tools
3. logistic_regression.py → Binary classification
4. knn.py → Distance-based learning
5. decision_tree.py → Interpretable models
6. random_forest.py → Ensemble learning (wisdom of crowds)
7. model_evaluation.py → Measuring success correctly
8. feature_engineering.py → Preparing data (80% of ML!)
9. cross_validation.py → Robust evaluation

 You're now ready to:
    Build real ML projects
    Participate in Kaggle competitions
    Apply ML to your own problems
    Move on to deep learning (neural networks)

Next recommended steps:
   1. Practice with Kaggle datasets
   2. Build an end-to-end project
   3. Learn deep learning (Phase 4!)
   4. Read research papers
   5. Contribute to open source

Happy Learning! 
""")
