# Complete AI & Machine Learning Learning Path

> **Goal:** Take anyone from zero programming knowledge to being able to build, understand, and experiment with real AI/ML models — step by step.

> **Status:** All 5 phases are complete. This document serves as a permanent reference and roadmap for the full learning journey.

---

## How to Use This Guide

1. Follow the phases **in order** — each phase builds on the previous one.
2. Open each folder and read the `GUIDE.md` inside it for detailed topic breakdowns.
3. Read the code files — every line is **commented** for understanding.
4. Do not rush. **One concept per day is enough.**
5. After each phase, build the **mini-project** listed at the end.

---

## Full Roadmap Overview

```
Phase 1 -> Python Foundations  
Phase 2 -> Data Science Tools  
Phase 3 -> Machine Learning    
Phase 4 -> Deep Learning       
Phase 5 -> Research & Projects 
```

---

## Phase 1: Python Foundations

Folder: `Phase 1 - Python Foundation/`
Detailed Guide: [Phase 1 - Python Foundation/GUIDE.md](Phase%201%20-%20Python%20Foundation/GUIDE.md)

Python is the language of AI/ML. Before touching any library, you must understand the language deeply.

### Topics Covered

| File | Topic | 
|------|-------|
| `first.py` | Hello World, `print()` basics |
| `basics.py` | Variables, data types, input, typecasting |
| `IfElse.py` | Conditional statements (`if`, `elif`, `else`) |
| `loop.py` | `for` loop, `while` loop, `break`, `continue` |
| `functions.py` | Defining functions, parameters, return values |
| `list.py` | Lists, indexing, slicing, methods |
| `touple.py` | Tuples, sets |
| `dictionary.py` | Dictionaries, key-value pairs, looping |
| `strings.py` | String methods, f-strings, formatting |
| `functions_advanced.py` | `return`, `*args`, `**kwargs`, lambda |
| `list_comprehension.py` | List/dict comprehension, `map()`, `filter()` |
| `file_handling.py` | Read/write files, `with` statement |
| `error_handling.py` | `try`, `except`, `finally`, custom errors |
| `oop.py` | Classes, objects, `__init__`, methods |
| `oop_advanced.py` | Inheritance, polymorphism, encapsulation |
| `modules.py` | `import`, built-in modules, creating modules |

**16 / 16 topics complete**

### Phase 1 Mini-Project
> Build a **Student Grade Calculator** using:
> - Functions, lists, dictionaries, file handling
> - Input from user → Calculate average → Save to file → Display result

---

## Phase 2: Data Science Tools

Folder: `Phase 2 - Data Science/`
Detailed Guide: [Phase 2 - Data Science/GUIDE.md](Phase%202%20-%20Data%20Science/GUIDE.md)

These are the 3 essential libraries every AI/ML engineer uses daily.

### Topics Covered

| File | Topic | 
|------|-------|
| `numpy_basics.py` | Arrays, shapes, operations |
| `numpy_math.py` | Matrix operations, dot product, broadcasting |
| `pandas_basics.py` | DataFrames, Series, reading CSV |
| `pandas_cleaning.py` | Handling missing data, filtering, groupby |
| `matplotlib_basics.py` | Line plots, bar charts, histograms |
| `matplotlib_advanced.py` | Subplots, customization, seaborn intro |
| `data_exploration.py` | Full EDA workflow on the Titanic dataset |

**7 / 7 topics complete**

### Install Libraries
```bash
pip install numpy pandas matplotlib seaborn
```

### Phase 2 Mini-Project
> **Analyze a real dataset** (e.g., Titanic or Iris from Kaggle):
> - Load with Pandas → Clean data → Explore statistically → Visualize with Matplotlib

---

## Phase 3: Machine Learning

Folder: `Phase 3 - Machine Learning/`
Detailed Guide: [Phase 3 - Machine Learning/GUIDE.md](Phase%203%20-%20Machine%20Learning/GUIDE.md)

This is where AI starts. Learn the theory first, then implement from scratch, then use libraries.

### Topics Covered

| File | Topic | 
|------|-------|
| `ml_concepts.py` | What is ML? Supervised vs unsupervised |
| `linear_regression_scratch.py` | Build linear regression without libraries |
| `linear_regression_sklearn.py` | Same using scikit-learn |
| `logistic_regression.py` | Classification, sigmoid, decision boundary |
| `knn.py` | K-Nearest Neighbors algorithm |
| `decision_tree.py` | Decision tree classifier |
| `random_forest.py` | Ensemble learning |
| `model_evaluation.py` | Accuracy, precision, recall, F1, confusion matrix |
| `feature_engineering.py` | Feature scaling, encoding, selection |
| `cross_validation.py` | K-Fold, train/test split, overfitting |

**10 / 10 topics complete**

### Install Libraries
```bash
pip install scikit-learn
```

### Phase 3 Mini-Project
> **House Price Predictor** or **Spam Email Classifier**:
> - Load dataset → Clean → Train model → Evaluate → Improve

---

## Phase 4: Deep Learning

Folder: `Phase 4 - Deep Learning/`
Detailed Guide: [Phase 4 - Deep Learning/GUIDE.md](Phase%204%20-%20Deep%20Learning/GUIDE.md)

Neural networks are the backbone of modern AI — image recognition, NLP, generative AI.

### Topics Covered

| File | Topic | 
|------|-------|
| `neural_network_scratch.py` | Perceptron, forward pass from scratch |
| `backpropagation.py` | How networks learn — gradient descent |
| `tensorflow_basics.py` | Tensors, models, layers |
| `first_nn.py` | First neural network with Keras (MNIST, ~97% accuracy) |
| `cnn_basics.py` | Convolutional Neural Networks (~99% accuracy) |
| `rnn_basics.py` | Recurrent Networks, LSTM (sequence/text data) |
| `transfer_learning.py` | Use pretrained models (ResNet, VGG) |
| `nlp_basics.py` | Text preprocessing, tokenization, embeddings |
| `transformers_intro.py` | Attention mechanism, Transformer architecture |

**9 / 9 topics complete**

### Install Libraries
```bash
pip install tensorflow keras torch torchvision transformers
```

### Phase 4 Mini-Project
> **Handwritten Digit Recognizer** (MNIST dataset) or **Sentiment Analyzer**:
> - Build CNN/NN → Train → Evaluate → Test on real inputs

---

## Phase 5: Research & Experiments

Folder: `Phase 5 - Research/`
Detailed Guide: [Phase 5 - Research/GUIDE.md](Phase%205%20-%20Research/GUIDE.md) | Quick Start: [Phase 5 - Research/QUICKSTART.md](Phase%205%20-%20Research/QUICKSTART.md)

This is where you go beyond tutorials — reading papers, reproducing results, tracking experiments.

### Topics Covered

| File / Resource | Description | 
|-----------------|-------------|
| `paper_reading_guide.py` | Interactive 3-pass method for reading ML papers |
| `experiment_tracking.py` | Experiment logging, W&B integration |
| `kaggle_guide.py` | Complete Kaggle competition workflow |
| `research_workflow.py` | Paper reproduction and research methodology |
| `paper_notes/README.md` | How to use the paper notes system |
| `paper_notes/example_attention_is_all_you_need.md` | Example notes on "Attention Is All You Need" |
| `experiments/experiment_log_template.md` | Template for tracking ML experiments |
| `projects/project_structure_template.md` | Template for structuring ML projects |

**Complete research toolkit ready**

### Suggested Papers to Start With
1. *"A Few Useful Things to Know About Machine Learning"* — Pedro Domingos
2. *"Attention Is All You Need"* — Vaswani et al. (Transformer paper)
3. *"Deep Residual Learning for Image Recognition"* — He et al. (ResNet)

---

## Tools Used (by Phase)

| Tool | When | Purpose |
|------|------|---------|
| Python 3.x | Phase 1 | Core language |
| VS Code | All phases | Code editor |
| Git + GitHub | All phases | Track progress |
| NumPy | Phase 2+ | Math arrays |
| Pandas | Phase 2+ | Data tables |
| Matplotlib / Seaborn | Phase 2+ | Visualization |
| Scikit-learn | Phase 3+ | ML models |
| TensorFlow / Keras | Phase 4+ | Deep learning |
| PyTorch | Phase 4+ | Research DL |
| Jupyter Notebook | Phase 2+ | Interactive coding |
| Weights & Biases | Phase 5 | Experiment tracking |

---

## Recommended Free Resources

### Python
- [Python Official Docs](https://docs.python.org/3/)
- [Automate the Boring Stuff with Python](https://automatetheboringstuff.com/) — Free book

### Math for ML
- [3Blue1Brown — Linear Algebra](https://www.youtube.com/playlist?list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab)
- [3Blue1Brown — Calculus](https://www.youtube.com/playlist?list=PLZHQObOWTQDMsr9K-rj53DwVRMYO3t5Yr)
- [Khan Academy — Statistics](https://www.khanacademy.org/math/statistics-probability)

### Machine Learning
- [fast.ai — Practical Deep Learning](https://course.fast.ai/)
- [Andrew Ng — ML Specialization (Coursera)](https://www.coursera.org/specializations/machine-learning-introduction) — Audit for free
- [Kaggle Learn](https://www.kaggle.com/learn) — Free, hands-on

### Deep Learning
- [Deep Learning Book — Goodfellow](https://www.deeplearningbook.org/) — Free online
- [PyTorch Official Tutorials](https://pytorch.org/tutorials/)

---

## Math You Need for ML

You do not need to master these before starting, but learn them alongside:

| Topic | Why It Matters |
|-------|----------------|
| **Linear Algebra** | Matrix operations, neural network computations |
| **Calculus** | Gradient descent, backpropagation |
| **Probability & Statistics** | Model evaluation, distributions, Bayes |
| **Optimization** | How models learn and minimize error |

---

## Milestone Checklist

- [x] Phase 1 Complete — Can write clean Python programs
- [x] Phase 2 Complete — Can load, clean, and visualize data
- [x] Phase 3 Complete — Can train and evaluate ML models
- [x] Phase 4 Complete — Can build and train neural networks
- [x] Phase 5 Complete — Can read papers and reproduce results
- [x] Research toolkit built — paper notes, experiment logs, project templates

---

## Tips for Success

1. **Code every day** — Even 20 minutes is better than nothing
2. **Do not skip Phase 1** — Weak Python means weak everything else
3. **Build projects** — Theory alone will not teach you anything real
4. **Read error messages** — They tell you exactly what is wrong
5. **Use Kaggle** — Free GPUs, real datasets, competitions
6. **Visualize everything** — If you cannot plot it, you do not understand it
7. **Math matters** — Learn it slowly alongside coding, not before

---

*Started: January 2026 | Completed: June 2026*
*This repository documents a full AI/ML learning journey from scratch to research-level skills.*
