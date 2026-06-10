# 🤖 Phase 3: Machine Learning - Detailed Guide

> Machine Learning = giving computers the ability to learn from data **without being explicitly programmed**.  
> This phase takes you from ML theory all the way to trained, evaluated models.

---

## 📋 Phase Overview

**Prerequisites:** Complete Phase 1 (Python) and Phase 2 (Data Science Tools) first.

| Topic Group | Files | 
|-------------|-------|
| Core Concepts | `ml_concepts.py` |
| Regression | `linear_regression_scratch.py`, `linear_regression_sklearn.py` |
| Classification | `logistic_regression.py`, `knn.py`, `decision_tree.py` |
| Ensemble | `random_forest.py` |
| Evaluation | `model_evaluation.py`, `cross_validation.py` |
| Data Prep | `feature_engineering.py` |

**Status:  Not Started**

---

##  Setup

```bash
pip install scikit-learn
```

---

##  Topic 1: ML Core Concepts
 File to create: `ml_concepts.py`

Before writing code, understand what ML actually is.

### Types of Machine Learning

```
Machine Learning
├── Supervised Learning      → Learn from labeled data
│   ├── Regression           → Predict a number (price, temperature)
│   └── Classification       → Predict a category (spam/not spam, cat/dog)
│
├── Unsupervised Learning    → Find patterns in unlabeled data
│   ├── Clustering           → Group similar items (K-Means)
│   └── Dimensionality Reduction → (PCA, t-SNE)
│
└── Reinforcement Learning   → Learn by trial and error (games, robots)
```

### Key Vocabulary

| Term | Meaning |
|------|---------|
| **Dataset** | The collection of data you learn from |
| **Feature** | An input variable (e.g., age, height) - also called X |
| **Label / Target** | The output you want to predict - also called y |
| **Training set** | Data used to train (teach) the model |
| **Test set** | Unseen data used to evaluate the model |
| **Model** | The mathematical function that makes predictions |
| **Parameters** | Values the model learns (weights, biases) |
| **Hyperparameters** | Settings YOU choose before training (learning rate, depth) |
| **Overfitting** | Model memorizes training data, fails on new data |
| **Underfitting** | Model is too simple, can't capture patterns |

### The ML Workflow (always this order)
```
1. Get Data
2. Explore Data (EDA)
3. Clean & Preprocess
4. Split → Train / Test
5. Choose a Model
6. Train the Model
7. Evaluate on Test Set
8. Improve & Repeat
9. Deploy
```

---

##  Topic 2: Linear Regression

### From Scratch First
 File to create: `linear_regression_scratch.py`

**What is it?** Predicts a **number** by fitting a straight line through data.

The equation: $y = mx + b$ (or $\hat{y} = w \cdot x + b$ in ML terms)

**Goal:** Find the best `w` (weight/slope) and `b` (bias/intercept) to minimize error.

**Cost Function** (Mean Squared Error):
$$MSE = \frac{1}{n}\sum_{i=1}^{n}(y_i - \hat{y}_i)^2$$

**Gradient Descent** - how we minimize cost:
```python
import numpy as np

# Simple linear regression from scratch
class LinearRegression:
    def __init__(self, learning_rate=0.01, epochs=1000):
        self.lr = learning_rate
        self.epochs = epochs
        self.w = 0   # weight
        self.b = 0   # bias

    def predict(self, X):
        return self.w * X + self.b

    def train(self, X, y):
        n = len(X)
        for epoch in range(self.epochs):
            y_pred = self.predict(X)
            error = y_pred - y

            # Gradient descent update
            dw = (2/n) * np.dot(X, error)
            db = (2/n) * np.sum(error)

            self.w -= self.lr * dw
            self.b -= self.lr * db
```

**Why from scratch?**
> Understanding the math makes you a better engineer.  
> When something breaks, you know WHERE to look.

### With Scikit-learn
 File to create: `linear_regression_sklearn.py`

```python
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import numpy as np

# Sample data
X = np.array([[1], [2], [3], [4], [5]])
y = np.array([2, 4, 5, 4, 5])

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

# Evaluate
mse = mean_squared_error(y_test, y_pred)
print(f"MSE: {mse:.2f}")
print(f"Weight: {model.coef_[0]:.2f}")
print(f"Bias: {model.intercept_:.2f}")
```

---

##  Topic 3: Logistic Regression (Classification)
 File to create: `logistic_regression.py`

**What is it?** Despite the name, it's a **classifier** - predicts a category (0 or 1, Yes or No).

Uses the **sigmoid function** to squash output between 0 and 1:
$$\sigma(z) = \frac{1}{1 + e^{-z}}$$

```python
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report

# Load data
iris = load_iris()
X, y = iris.data, iris.target

# Binary classification - only 2 classes
mask = y != 2
X, y = X[mask], y[mask]

# Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Train
model = LogisticRegression()
model.fit(X_train, y_train)

# Evaluate
y_pred = model.predict(X_test)
print(f"Accuracy: {accuracy_score(y_test, y_pred):.2%}")
print(classification_report(y_test, y_pred))
```

---

##  Topic 4: K-Nearest Neighbors (KNN)
 File to create: `knn.py`

**What is it?** To predict a new point's class, look at its K nearest neighbors and take a vote.

**No training phase** - it memorizes the data and computes at prediction time.

```
Choose K (e.g., 3)   →   Find 3 closest training points   →   Majority vote = prediction
```

```python
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

model = KNeighborsClassifier(n_neighbors=3)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
print(f"KNN Accuracy: {accuracy_score(y_test, y_pred):.2%}")
```

**Key question:** How to choose K?
> Try different values and pick the one with best validation accuracy. This is **hyperparameter tuning**.

---

##  Topic 5: Decision Trees
 File to create: `decision_tree.py`

**What is it?** A flowchart-like model. At each step, ask a yes/no question to split the data.

```
Is age > 30?
├── Yes → Is income > 50k?
│         ├── Yes → Approved
│         └── No  → Rejected
└── No  → Approved
```

```python
from sklearn.tree import DecisionTreeClassifier, export_text
from sklearn.datasets import load_iris

iris = load_iris()
X, y = iris.data, iris.target

model = DecisionTreeClassifier(max_depth=3)
model.fit(X, y)

# See the tree structure
print(export_text(model, feature_names=iris.feature_names))
```

**Key hyperparameter:** `max_depth` - deeper trees overfit, shallower trees underfit.

---

##  Topic 6: Random Forest
 File to create: `random_forest.py`

**What is it?** Build many decision trees on random subsets of data, then combine their predictions.

**Ensemble learning** - combining multiple weak models = stronger model.

```python
from sklearn.ensemble import RandomForestClassifier

model = RandomForestClassifier(n_estimators=100, max_depth=5, random_state=42)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

# Feature importance - which features matter most?
importances = model.feature_importances_
for name, importance in zip(feature_names, importances):
    print(f"{name}: {importance:.4f}")
```

---

##  Topic 7: Model Evaluation
 File to create: `model_evaluation.py`

**Never trust accuracy alone.** Use multiple metrics.

```python
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score,
    f1_score, confusion_matrix, classification_report
)
import matplotlib.pyplot as plt
import seaborn as sns

# Accuracy - what % of predictions were correct?
print(f"Accuracy:  {accuracy_score(y_test, y_pred):.2%}")

# Precision - of all predicted positives, how many were actually positive?
print(f"Precision: {precision_score(y_test, y_pred, average='macro'):.2%}")

# Recall - of all actual positives, how many did we find?
print(f"Recall:    {recall_score(y_test, y_pred, average='macro'):.2%}")

# F1 - harmonic mean of precision and recall
print(f"F1 Score:  {f1_score(y_test, y_pred, average='macro'):.2%}")

# Confusion Matrix - visual breakdown of predictions
cm = confusion_matrix(y_test, y_pred)
sns.heatmap(cm, annot=True, fmt="d")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.show()
```

**Understanding the confusion matrix:**
```
                Predicted: No   Predicted: Yes
Actual: No   |     TN          |    FP         |
Actual: Yes  |     FN          |    TP         |

TN = True Negative   FP = False Positive (Type I Error)
FN = False Negative  TP = True Positive
(Type II Error)
```

---

##  Topic 8: Feature Engineering
 File to create: `feature_engineering.py`

**Garbage in → Garbage out.** Better features = better models.

**Feature Scaling** - put all features on the same scale:
```python
from sklearn.preprocessing import StandardScaler, MinMaxScaler

# StandardScaler: mean=0, std=1
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X_train)

# MinMaxScaler: scales to [0, 1]
scaler = MinMaxScaler()
X_scaled = scaler.fit_transform(X_train)
```

**Encoding Categorical Data** - ML needs numbers, not text:
```python
from sklearn.preprocessing import LabelEncoder, OneHotEncoder

# LabelEncoder: "cat"→0, "dog"→1, "bird"→2
le = LabelEncoder()
y_encoded = le.fit_transform(["cat", "dog", "cat", "bird"])

# OneHotEncoder: better for models (no ordinal assumption)
# "cat" → [1, 0, 0], "dog" → [0, 1, 0], "bird" → [0, 0, 1]
```

---

##  Topic 9: Cross Validation
 File to create: `cross_validation.py`

**Problem with simple train/test split:** Your result depends on which data ended up in the test set.

**Solution:** K-Fold Cross Validation - split data into K parts, train K times.

```python
from sklearn.model_selection import cross_val_score, KFold
from sklearn.ensemble import RandomForestClassifier

model = RandomForestClassifier()

# K=5 means 5 different train/test splits → average the results
scores = cross_val_score(model, X, y, cv=5, scoring="accuracy")
print(f"CV Scores: {scores}")
print(f"Mean: {scores.mean():.2%}  ±  Std: {scores.std():.2%}")
```

---

##  Phase 3 Mini-Project (Choose One)

### Option A: House Price Predictor
- Dataset: [Boston Housing](https://scikit-learn.org/stable/datasets/toy_dataset.html#boston-house-prices-dataset) or [Kaggle Housing](https://www.kaggle.com/c/house-prices-advanced-regression-techniques)
- Model: Linear Regression, then Random Forest
- Predict: sale price

### Option B: Titanic Survivor Classifier
- Dataset: [Kaggle Titanic](https://www.kaggle.com/c/titanic)
- Model: Logistic Regression, Decision Tree, Random Forest
- Predict: survived (0 or 1)
- Submit to Kaggle - see your score on the leaderboard!

---


*Go to [LEARNING_PATH.md](../LEARNING_PATH.md) for the complete AI/ML roadmap.*  
*Previous phase: [Data Science Tools](../Phase%202%20-%20Data%20Science/GUIDE.md)*  
*Next phase: [Deep Learning](../Phase%204%20-%20Deep%20Learning/GUIDE.md)*
