"""
KAGGLE COMPETITION GUIDE
=========================

Complete guide to participating in Kaggle competitions, from beginner to advanced.
Includes workflow, tips, best practices, and code templates.

Author: ML Research Learning Path
"""

import json
from pathlib import Path


class KaggleGuide:
    """
    Comprehensive guide for Kaggle competitions.
    """

    def __init__(self):
        self.competition_workflow = []
        self.tips = {}

    def introduction(self):
        """Introduction to Kaggle."""
        print("=" * 80)
        print("KAGGLE COMPETITION GUIDE")
        print("=" * 80)
        print("\nWHAT IS KAGGLE?")
        print("-" * 80)
        print("Kaggle is a platform for data science competitions where you can:")
        print("• Compete in machine learning competitions")
        print("• Learn from community notebooks and discussions")
        print("• Build your data science portfolio")
        print("• Access free datasets")
        print("• Use free GPU/TPU compute resources")
        print()

        print("WHY PARTICIPATE IN KAGGLE COMPETITIONS?")
        print("-" * 80)
        benefits = [
            "• Practical experience with real-world data problems",
            "• Learn from top data scientists (public notebooks)",
            "• Build your portfolio and reputation",
            "• Practice feature engineering and model optimization",
            "• Learn to work under constraints (time, compute)",
            "• Networking with the ML community",
            "• Potential prizes and job opportunities"
        ]
        for benefit in benefits:
            print(benefit)
        print()

        print("KAGGLE PROGRESSION SYSTEM:")
        print("-" * 80)
        print("Novice → Contributor → Expert → Master → Grandmaster")
        print("\nEarn medals by placing well in competitions:")
        print("• Bronze: Top 40%")
        print("• Silver: Top 20%")
        print("• Gold: Top 10%")
        print()

    def getting_started(self):
        """Getting started guide."""
        print("=" * 80)
        print("GETTING STARTED WITH KAGGLE")
        print("=" * 80)

        print("\n1. SETUP:")
        print("-" * 80)
        steps = [
            "1. Create a Kaggle account at kaggle.com",
            "2. Complete your profile (helps with job opportunities)",
            "3. Install Kaggle API:",
            "   pip install kaggle",
            "4. Get API credentials:",
            "   - Go to Account → Create New API Token",
            "   - Save kaggle.json to ~/.kaggle/ (Linux/Mac) or C:\\Users\\<User>\\.kaggle\\ (Windows)",
            "   - Set permissions: chmod 600 ~/.kaggle/kaggle.json (Linux/Mac)",
            "5. Verify installation:",
            "   kaggle competitions list"
        ]
        for step in steps:
            print(step)

        print("\n2. CHOOSE YOUR FIRST COMPETITION:")
        print("-" * 80)
        print("For beginners, start with:")
        print()
        print("a) Getting Started Competitions:")
        print("   • Titanic: Machine Learning from Disaster")
        print("   • House Prices: Advanced Regression Techniques")
        print("   • Digit Recognizer (MNIST)")
        print("   These are permanent, beginner-friendly competitions")
        print()
        print("b) Playground Competitions:")
        print("   • Simpler datasets for learning")
        print("   • Less competitive, more educational")
        print("   • Good for trying new techniques")
        print()
        print("c) Active Competitions:")
        print("   • Once comfortable, join active competitions")
        print("   • Start 1-2 weeks after launch (less overwhelming)")
        print("   • Read discussions and public notebooks first")
        print()

        print("3. KAGGLE API BASICS:")
        print("-" * 80)
        api_commands = '''
# List competitions
kaggle competitions list

# Download competition data
kaggle competitions download -c competition-name

# Submit predictions
kaggle competitions submit -c competition-name -f submission.csv -m "Message"

# Check leaderboard
kaggle competitions leaderboard -c competition-name

# Download a dataset
kaggle datasets download -d dataset-name

# List your submissions
kaggle competitions submissions -c competition-name
'''
        print(api_commands)

    def competition_workflow(self):
        """Standard competition workflow."""
        print("=" * 80)
        print("KAGGLE COMPETITION WORKFLOW")
        print("=" * 80)

        workflow_steps = [
            {
                "phase": "1. UNDERSTAND THE PROBLEM",
                "duration": "Day 1-2",
                "tasks": [
                    "• Read competition overview and evaluation metric",
                    "• Understand the data (features, target, size)",
                    "• Review competition rules and timeline",
                    "• Check discussion forum for clarifications",
                    "• Look at public notebooks to understand baseline approaches",
                    "• Identify if it's classification, regression, or other task",
                    "• Understand business context (why does this problem matter?)"
                ]
            },
            {
                "phase": "2. EXPLORATORY DATA ANALYSIS (EDA)",
                "duration": "Day 2-4",
                "tasks": [
                    "• Load and examine the data",
                    "• Check data types, missing values, distributions",
                    "• Visualize features and target variable",
                    "• Identify correlations and patterns",
                    "• Detect outliers and anomalies",
                    "• Understand train/test distribution differences",
                    "• Document insights and hypotheses"
                ]
            },
            {
                "phase": "3. DATA PREPROCESSING",
                "duration": "Day 4-6",
                "tasks": [
                    "• Handle missing values",
                    "• Encode categorical variables",
                    "• Scale/normalize numerical features",
                    "• Remove or handle outliers",
                    "• Split data for validation (if not provided)",
                    "• Ensure consistent preprocessing for train/test"
                ]
            },
            {
                "phase": "4. FEATURE ENGINEERING",
                "duration": "Day 6-12",
                "tasks": [
                    "• Create new features from existing ones",
                    "• Feature interactions and transformations",
                    "• Domain-specific features",
                    "• Aggregate features (if applicable)",
                    "• Feature selection",
                    "• Validate new features improve performance"
                ]
            },
            {
                "phase": "5. BASELINE MODEL",
                "duration": "Day 7-8",
                "tasks": [
                    "• Build simple baseline (e.g., logistic regression, decision tree)",
                    "• Establish cross-validation strategy",
                    "• Make first submission to public leaderboard",
                    "• Set up experiment tracking",
                    "• Create reusable training/evaluation pipeline"
                ]
            },
            {
                "phase": "6. MODEL DEVELOPMENT",
                "duration": "Day 8-20",
                "tasks": [
                    "• Try different model types (GBM, Neural Networks, etc.)",
                    "• Hyperparameter tuning",
                    "• Feature selection/importance analysis",
                    "• Cross-validation to ensure robustness",
                    "• Iterate based on validation results",
                    "• Track all experiments systematically"
                ]
            },
            {
                "phase": "7. ENSEMBLE & OPTIMIZATION",
                "duration": "Day 20-28",
                "tasks": [
                    "• Create model ensembles (blending, stacking)",
                    "• Optimize ensemble weights",
                    "• Fine-tune best models",
                    "• Validate on multiple CV folds",
                    "• Check for overfitting (LB vs CV scores)",
                    "• Select final submission carefully"
                ]
            },
            {
                "phase": "8. FINAL SUBMISSION",
                "duration": "Last 2-3 days",
                "tasks": [
                    "• Select 2 final submissions (Kaggle rule)",
                    "• Choose based on CV score, not LB score",
                    "• Run final models on test set",
                    "• Double-check submission format",
                    "• Submit before deadline",
                    "• Document your approach for future reference"
                ]
            },
            {
                "phase": "9. POST-COMPETITION",
                "duration": "After results",
                "tasks": [
                    "• Review winning solutions",
                    "• Compare with your approach",
                    "• Read competition discussions",
                    "• Implement winning techniques to learn",
                    "• Share your solution (writeup/notebook)",
                    "• Document lessons learned"
                ]
            }
        ]

        for step in workflow_steps:
            print(f"\n{step['phase']}")
            print(f"Duration: {step['duration']}")
            print("-" * 80)
            for task in step['tasks']:
                print(task)

        print("\n" + "=" * 80)

    def code_templates(self):
        """Useful code templates for Kaggle."""
        print("=" * 80)
        print("KAGGLE CODE TEMPLATES")
        print("=" * 80)

        print("\n1. PROJECT STRUCTURE:")
        print("-" * 80)
        structure = '''
kaggle-competition/
│
├── data/                  # Downloaded competition data
│   ├── train.csv
│   ├── test.csv
│   └── sample_submission.csv
│
├── notebooks/            # Jupyter notebooks for EDA and experiments
│   ├── 01_eda.ipynb
│   ├── 02_baseline.ipynb
│   └── 03_models.ipynb
│
├── src/                  # Source code
│   ├── __init__.py
│   ├── data.py          # Data loading and preprocessing
│   ├── features.py      # Feature engineering
│   ├── models.py        # Model definitions
│   ├── train.py         # Training scripts
│   └── utils.py         # Utility functions
│
├── models/              # Saved models
│   └── model_v1.pkl
│
├── submissions/         # Submission files
│   └── submission_v1.csv
│
├── configs/            # Configuration files
│   └── config.yaml
│
├── experiments/        # Experiment logs
│   └── experiment_log.json
│
├── requirements.txt    # Dependencies
└── README.md          # Documentation
'''
        print(structure)

        print("\n2. DATA LOADING TEMPLATE:")
        print("-" * 80)
        data_template = '''
import pandas as pd
import numpy as np
from pathlib import Path

class DataLoader:
    """Load and preprocess competition data."""

    def __init__(self, data_dir="data"):
        self.data_dir = Path(data_dir)

    def load_train(self):
        """Load training data."""
        train = pd.read_csv(self.data_dir / "train.csv")
        print(f"Train shape: {train.shape}")
        return train

    def load_test(self):
        """Load test data."""
        test = pd.read_csv(self.data_dir / "test.csv")
        print(f"Test shape: {test.shape}")
        return test

    def load_all(self):
        """Load all data."""
        train = self.load_train()
        test = self.load_test()
        return train, test

# Usage
loader = DataLoader()
train, test = loader.load_all()
'''
        print(data_template)

        print("\n3. CROSS-VALIDATION TEMPLATE:")
        print("-" * 80)
        cv_template = '''
from sklearn.model_selection import KFold, StratifiedKFold
import numpy as np

def cross_validate(model, X, y, n_splits=5, stratified=True):
    """
    Cross-validation with proper tracking.

    Args:
        model: Model with fit/predict methods
        X: Features
        y: Target
        n_splits: Number of CV folds
        stratified: Use stratified split (for classification)

    Returns:
        CV scores and predictions
    """
    if stratified:
        kfold = StratifiedKFold(n_splits=n_splits, shuffle=True, random_state=42)
    else:
        kfold = KFold(n_splits=n_splits, shuffle=True, random_state=42)

    cv_scores = []
    oof_predictions = np.zeros(len(X))  # Out-of-fold predictions

    for fold, (train_idx, val_idx) in enumerate(kfold.split(X, y)):
        print(f"\\nFold {fold + 1}/{n_splits}")

        # Split data
        X_train, X_val = X.iloc[train_idx], X.iloc[val_idx]
        y_train, y_val = y.iloc[train_idx], y.iloc[val_idx]

        # Train
        model.fit(X_train, y_train)

        # Predict
        val_pred = model.predict(X_val)
        oof_predictions[val_idx] = val_pred

        # Score
        from sklearn.metrics import accuracy_score  # or appropriate metric
        score = accuracy_score(y_val, val_pred)
        cv_scores.append(score)

        print(f"Fold {fold + 1} Score: {score:.4f}")

    print(f"\\nMean CV Score: {np.mean(cv_scores):.4f} (+/- {np.std(cv_scores):.4f})")

    return cv_scores, oof_predictions

# Usage
from sklearn.ensemble import RandomForestClassifier

model = RandomForestClassifier(n_estimators=100, random_state=42)
cv_scores, oof_preds = cross_validate(model, X_train, y_train, n_splits=5)
'''
        print(cv_template)

        print("\n4. SUBMISSION TEMPLATE:")
        print("-" * 80)
        submission_template = '''
def create_submission(test_ids, predictions, filename="submission.csv"):
    """
    Create submission file in correct format.

    Args:
        test_ids: Test sample IDs
        predictions: Model predictions
        filename: Output filename
    """
    submission = pd.DataFrame({
        'id': test_ids,
        'target': predictions  # Change column name as per competition
    })

    submission.to_csv(filename, index=False)
    print(f"Submission saved to {filename}")
    print(f"Shape: {submission.shape}")
    print(submission.head())

    return submission

# Usage
predictions = model.predict(X_test)
create_submission(test['id'], predictions, "submissions/submission_v1.csv")

# Submit using Kaggle API
# !kaggle competitions submit -c competition-name -f submission_v1.csv -m "Model description"
'''
        print(submission_template)

        print("\n5. FEATURE ENGINEERING TEMPLATE:")
        print("-" * 80)
        feature_template = '''
class FeatureEngineer:
    """Feature engineering pipeline."""

    def __init__(self):
        self.features = []

    def create_features(self, df):
        """Create new features."""
        df = df.copy()

        # Numerical features
        df['feature_sum'] = df['col1'] + df['col2']
        df['feature_ratio'] = df['col1'] / (df['col2'] + 1)  # Avoid division by zero
        df['feature_interaction'] = df['col1'] * df['col2']

        # Categorical features
        df['cat_count'] = df.groupby('category')['id'].transform('count')
        df['cat_mean_target'] = df.groupby('category')['target'].transform('mean')

        # Date features (if applicable)
        if 'date' in df.columns:
            df['date'] = pd.to_datetime(df['date'])
            df['year'] = df['date'].dt.year
            df['month'] = df['date'].dt.month
            df['day'] = df['date'].dt.day
            df['dayofweek'] = df['date'].dt.dayofweek
            df['is_weekend'] = df['dayofweek'].isin([5, 6]).astype(int)

        # Text features (if applicable)
        if 'text' in df.columns:
            df['text_length'] = df['text'].str.len()
            df['word_count'] = df['text'].str.split().str.len()
            df['unique_words'] = df['text'].str.split().apply(lambda x: len(set(x)))

        return df

# Usage
engineer = FeatureEngineer()
train = engineer.create_features(train)
test = engineer.create_features(test)
'''
        print(feature_template)

    def tips_and_tricks(self):
        """Kaggle tips and tricks."""
        print("=" * 80)
        print("KAGGLE TIPS & TRICKS")
        print("=" * 80)

        print("\nGENERAL TIPS:")
        print("-" * 80)
        general_tips = [
            "• Start early: Join competition as soon as it starts",
            "• Read everything: Rules, data description, forum discussions",
            "• Trust your CV: Choose final submissions based on CV, not leaderboard",
            "• Public LB is noisy: Only 20-30% of test data, can be misleading",
            "• Keep it simple: Start with simple models before complex ones",
            "• Document everything: Track experiments, code versions, results",
            "• Learn from others: Read public notebooks and discussions",
            "• Share to learn: Post your insights (after competition or near end)",
            "• Team up: Collaborate in later stages for better results",
            "• Stay consistent: Regular participation builds skills over time"
        ]
        for tip in general_tips:
            print(tip)

        print("\nCROSS-VALIDATION STRATEGY:")
        print("-" * 80)
        cv_tips = [
            "• Match train/test distributions: Check if time-based, spatial, etc.",
            "• Use appropriate split: StratifiedKFold for classification, etc.",
            "• Multiple validation strategies: Try different splits to be robust",
            "• Check CV vs LB correlation: Should move in same direction",
            "• Use out-of-fold predictions: For meta-models and ensembles",
            "• Same random seed: Reproducibility is crucial"
        ]
        for tip in cv_tips:
            print(tip)

        print("\nMODEL SELECTION:")
        print("-" * 80)
        model_tips = [
            "• For tabular data: GradientBoosting (XGBoost, LightGBM, CatBoost)",
            "• For images: CNNs, Vision Transformers, pretrained models",
            "• For text: Transformers (BERT, RoBERTa, etc.)",
            "• For time series: LSTM, GRU, temporal CNNs, classical methods",
            "• Diversity in ensembles: Combine different model types",
            "• Start with strong baselines: Don't spend too long on weak models"
        ]
        for tip in model_tips:
            print(tip)

        print("\nFEATURE ENGINEERING:")
        print("-" * 80)
        feature_tips = [
            "• Domain knowledge: Understanding the problem helps create features",
            "• Feature interactions: Multiply, divide, combine features",
            "• Aggregations: Group-by statistics (mean, std, count, etc.)",
            "• Target encoding: Encode categories by target mean (with CV!)",
            "• Feature selection: Remove low-importance features",
            "• Validate features: Check if new features improve CV score"
        ]
        for tip in feature_tips:
            print(tip)

        print("\nENSEMBLE TECHNIQUES:")
        print("-" * 80)
        ensemble_tips = [
            "• Blending: Average predictions from multiple models",
            "• Stacking: Train meta-model on predictions of base models",
            "• Diversity: Ensemble different model types, features, preprocessing",
            "• Weighted average: Optimize weights based on CV performance",
            "• Out-of-fold predictions: Use for meta-model training",
            "• Simple often works: Start with simple average before complex ensembles"
        ]
        for tip in ensemble_tips:
            print(tip)

        print("\nCOMMON MISTAKES TO AVOID:")
        print("-" * 80)
        mistakes = [
            "• Overfitting to public LB: Public LB is small sample, can be misleading",
            "• Not validating properly: Data leakage, wrong CV split",
            "• Ignoring data distribution: Train/test differences",
            "• Submitting too many times: Limited submissions per day",
            "• Poor time management: Spend too long on EDA or single approach",
            "• Not reading rules: Miss important details about evaluation",
            "• Forgetting to select submissions: Must select 2 final submissions!",
            "• Data leakage: Using future information, improper CV"
        ]
        for mistake in mistakes:
            print(mistake)

        print("\nRESOURCES TO USE:")
        print("-" * 80)
        resources = [
            "• Kaggle Notebooks: Learn from public notebooks",
            "• Kaggle Discussions: Ask questions, read insights",
            "• Kaggle Datasets: Additional data for training",
            "• Kaggle Free GPU/TPU: Use Kaggle notebooks for compute",
            "• Past competitions: Learn from winning solutions",
            "• Kaggle Learn: Free micro-courses on various topics",
            "• Community: Join Kaggle Discord, Reddit, Twitter"
        ]
        for resource in resources:
            print(resource)

        print("\n" + "=" * 80)

    def example_competition_template(self):
        """Complete template for a competition."""
        print("=" * 80)
        print("COMPLETE COMPETITION TEMPLATE")
        print("=" * 80)

        template = '''
import pandas as pd
import numpy as np
from sklearn.model_selection import StratifiedKFold
from sklearn.metrics import accuracy_score
import lightgbm as lgb
import warnings
warnings.filterwarnings('ignore')

# ============================================================================
# 1. CONFIGURATION
# ============================================================================
class Config:
    # Paths
    DATA_DIR = "data/"
    OUTPUT_DIR = "submissions/"
    MODEL_DIR = "models/"

    # Competition
    COMPETITION_NAME = "competition-name"
    TARGET_COL = "target"
    ID_COL = "id"

    # CV
    N_FOLDS = 5
    RANDOM_STATE = 42

    # Model
    MODEL_PARAMS = {
        'objective': 'binary',
        'metric': 'auc',
        'boosting_type': 'gbdt',
        'num_leaves': 31,
        'learning_rate': 0.05,
        'feature_fraction': 0.9,
        'bagging_fraction': 0.8,
        'bagging_freq': 5,
        'verbose': -1,
        'random_state': RANDOM_STATE
    }

# ============================================================================
# 2. LOAD DATA
# ============================================================================
print("Loading data...")
train = pd.read_csv(Config.DATA_DIR + "train.csv")
test = pd.read_csv(Config.DATA_DIR + "test.csv")
print(f"Train shape: {train.shape}, Test shape: {test.shape}")

# ============================================================================
# 3. FEATURE ENGINEERING
# ============================================================================
def create_features(df):
    """Create features."""
    df = df.copy()

    # Your feature engineering here
    # Example:
    # df['new_feature'] = df['col1'] * df['col2']

    return df

print("\\nCreating features...")
train = create_features(train)
test = create_features(test)

# ============================================================================
# 4. PREPARE DATA
# ============================================================================
# Features and target
feature_cols = [col for col in train.columns if col not in [Config.ID_COL, Config.TARGET_COL]]
X = train[feature_cols]
y = train[Config.TARGET_COL]
X_test = test[feature_cols]

print(f"\\nNumber of features: {len(feature_cols)}")

# ============================================================================
# 5. CROSS-VALIDATION
# ============================================================================
print("\\nStarting cross-validation...")
kfold = StratifiedKFold(n_splits=Config.N_FOLDS, shuffle=True, random_state=Config.RANDOM_STATE)

oof_predictions = np.zeros(len(X))
test_predictions = np.zeros(len(X_test))
cv_scores = []

for fold, (train_idx, val_idx) in enumerate(kfold.split(X, y)):
    print(f"\\nFold {fold + 1}/{Config.N_FOLDS}")

    # Split
    X_train, X_val = X.iloc[train_idx], X.iloc[val_idx]
    y_train, y_val = y.iloc[train_idx], y.iloc[val_idx]

    # Create datasets
    train_data = lgb.Dataset(X_train, label=y_train)
    val_data = lgb.Dataset(X_val, label=y_val, reference=train_data)

    # Train
    model = lgb.train(
        Config.MODEL_PARAMS,
        train_data,
        num_boost_round=1000,
        valid_sets=[train_data, val_data],
        valid_names=['train', 'valid'],
        callbacks=[
            lgb.early_stopping(stopping_rounds=50, verbose=False),
            lgb.log_evaluation(period=100)
        ]
    )

    # Predict validation
    val_pred = model.predict(X_val, num_iteration=model.best_iteration)
    oof_predictions[val_idx] = val_pred

    # Predict test
    test_pred = model.predict(X_test, num_iteration=model.best_iteration)
    test_predictions += test_pred / Config.N_FOLDS

    # Score
    score = accuracy_score(y_val, (val_pred > 0.5).astype(int))
    cv_scores.append(score)
    print(f"Fold {fold + 1} Score: {score:.4f}")

    # Save model
    model.save_model(f"{Config.MODEL_DIR}/model_fold{fold}.txt")

# Overall CV score
print(f"\\nOverall CV Score: {np.mean(cv_scores):.4f} (+/- {np.std(cv_scores):.4f})")

# ============================================================================
# 6. CREATE SUBMISSION
# ============================================================================
submission = pd.DataFrame({
    Config.ID_COL: test[Config.ID_COL],
    Config.TARGET_COL: test_predictions
})

submission_file = f"{Config.OUTPUT_DIR}/submission_cv{np.mean(cv_scores):.4f}.csv"
submission.to_csv(submission_file, index=False)
print(f"\\nSubmission saved to: {submission_file}")
print(submission.head())

# ============================================================================
# 7. SUBMIT (optional)
# ============================================================================
# !kaggle competitions submit -c {Config.COMPETITION_NAME} -f {submission_file} -m "LightGBM baseline"
'''
        print(template)
        print("\n" + "=" * 80)


def main():
    """Main function."""
    guide = KaggleGuide()

    print("\n" + "=" * 80)
    print("KAGGLE COMPETITION GUIDE")
    print("=" * 80)
    print("\nWhat would you like to learn?")
    print("1. Introduction to Kaggle")
    print("2. Getting started")
    print("3. Competition workflow")
    print("4. Code templates")
    print("5. Tips and tricks")
    print("6. Complete competition template")
    print("7. View everything")
    print("8. Exit")

    choice = input("\nEnter your choice (1-8): ")

    if choice == "1":
        guide.introduction()
    elif choice == "2":
        guide.getting_started()
    elif choice == "3":
        guide.competition_workflow()
    elif choice == "4":
        guide.code_templates()
    elif choice == "5":
        guide.tips_and_tricks()
    elif choice == "6":
        guide.example_competition_template()
    elif choice == "7":
        guide.introduction()
        input("\nPress Enter to continue...")
        guide.getting_started()
        input("\nPress Enter to continue...")
        guide.competition_workflow()
        input("\nPress Enter to continue...")
        guide.code_templates()
        input("\nPress Enter to continue...")
        guide.tips_and_tricks()
        input("\nPress Enter to continue...")
        guide.example_competition_template()
    else:
        print("Exiting...")


if __name__ == "__main__":
    main()
