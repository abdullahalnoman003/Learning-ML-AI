#  Phase 5: Research & Experiments - Detailed Guide

> This is where you go beyond courses and tutorials.  
> You read real papers, reproduce results, build original projects, and contribute to the field.

---

##  Phase Overview

**Prerequisites:** Complete Phases 1-4 first.

**Status: ⏳ Not Started**

---

##  Topic 1: How to Read a Research Paper

Research papers are dense - but you don't have to read them linearly.

### The 3-Pass Method

**Pass 1 (5 minutes) - Bird's eye view:**
- Read: Title, Abstract, Introduction, Conclusion, Figure captions
- Answer: What problem does this solve? What is the main contribution?

**Pass 2 (1 hour) - Understand the approach:**
- Read: Rest of the paper, skip math proofs and code details
- Answer: How does their method work? What datasets did they use? What were the results?

**Pass 3 (Several hours) - Deep dive:**
- Read: Everything, including all math
- Reproduce: Try to implement it yourself
- Critique: What are the limitations? What would you try differently?

### Where to Find Papers

| Source | URL | Type |
|--------|-----|------|
| **arXiv** | arxiv.org | Free preprints of all ML papers |
| **Papers With Code** | paperswithcode.com | Papers + official code |
| **Semantic Scholar** | semanticscholar.org | Search + summaries |
| **Google Scholar** | scholar.google.com | Academic search |
| **Hugging Face** | huggingface.co/papers | Trending AI papers |

### Recommended Starting Papers

| Paper | Year | Why Read It |
|-------|------|------------|
| *A Few Useful Things to Know About ML* - Pedro Domingos | 2012 | Best intro to ML thinking |
| *Attention Is All You Need* - Vaswani et al. | 2017 | The Transformer paper - basis of all LLMs |
| *Deep Residual Learning* - He et al. (ResNet) | 2015 | Revolutionary CNN architecture |
| *Dropout: Preventing Overfitting* - Srivastava et al. | 2014 | Simple but powerful technique |
| *Adam Optimizer* - Kingma & Ba | 2014 | The optimizer used in almost every model |
| *BERT* - Devlin et al. | 2018 | Language model that changed NLP |

---

##  Topic 2: Experiment Tracking

When training models, you need to track:
- What hyperparameters did you use?
- What was the training curve?
- How does this run compare to previous ones?

### Option 1: Simple File Logging

```python
import json
from datetime import datetime

experiment = {
    "date": str(datetime.now()),
    "model": "Random Forest",
    "hyperparams": {"n_estimators": 100, "max_depth": 5},
    "train_accuracy": 0.95,
    "test_accuracy": 0.89,
    "notes": "Overfitting - try reducing depth"
}

with open("experiments_log.json", "a") as f:
    f.write(json.dumps(experiment) + "\n")
```

### Option 2: Weights & Biases (WandB) - Professional Tool

```bash
pip install wandb
wandb login
```

```python
import wandb

wandb.init(project="my-ml-project", name="run-1")

wandb.config = {
    "learning_rate": 0.001,
    "epochs": 50,
    "batch_size": 32
}

for epoch in range(50):
    # ... train ...
    wandb.log({"loss": loss, "accuracy": acc, "epoch": epoch})

wandb.finish()
```

---

##  Topic 3: Working with Real Datasets

### Finding Datasets

| Source | What You'll Find |
|--------|-----------------|
| [Kaggle](https://kaggle.com/datasets) | Thousands of real-world datasets |
| [UCI ML Repository](https://archive.ics.uci.edu/) | Classic academic datasets |
| [Google Dataset Search](https://datasetsearch.research.google.com/) | Any dataset on the web |
| [Hugging Face Datasets](https://huggingface.co/datasets) | NLP / ML datasets |
| [AWS Open Data](https://registry.opendata.aws/) | Large-scale datasets |

### Dataset Annotation

When you can't find the right dataset, you collect your own:

```python
# Label Studio - free open source annotation tool
# pip install label-studio
# label-studio start

# For image datasets:
# Organize: /dataset/class_name/image.jpg

import os
from pathlib import Path

def check_dataset_structure(root_path):
    """Check how many images per class"""
    root = Path(root_path)
    for class_dir in sorted(root.iterdir()):
        if class_dir.is_dir():
            count = len(list(class_dir.glob("*.jpg")))
            print(f"{class_dir.name}: {count} images")
```

---

##  Topic 4: Reproducing a Paper

This is the most valuable exercise in ML research.

### Steps

1. **Choose a paper** - start with papers that have official code
2. **Read the paper** (all 3 passes)  
3. **Choose a dataset** - use the same one from the paper if possible
4. **Implement from description** - try BEFORE looking at official code
5. **Compare your results** to the numbers in the paper
6. **Look at official code** - see where your implementation differed
7. **Experiment** - change something and see what happens

### Good Papers to Reproduce First

| Paper | Difficulty | Skills Needed |
|-------|-----------|---------------|
| Linear Regression from scratch | ⭐ | NumPy, calculus basics |
| Logistic Regression from scratch | ⭐⭐ | NumPy, sigmoid |
| 2-layer Neural Network on MNIST | ⭐⭐ | NumPy, backpropagation |
| CNN on CIFAR-10 | ⭐⭐⭐ | TensorFlow/PyTorch |
| LSTM for text classification | ⭐⭐⭐⭐ | PyTorch, NLP |
| Transformer (simplified) | ⭐⭐⭐⭐⭐ | Advanced PyTorch |

---

##  Topic 5: Kaggle Competitions

Kaggle is the best place to practice real ML skills.

### How to Start

1. Create a [Kaggle account](https://kaggle.com)
2. Start with **Getting Started** competitions:
   - [Titanic (Classification)](https://www.kaggle.com/c/titanic)
   - [House Prices (Regression)](https://www.kaggle.com/c/house-prices-advanced-regression-techniques)
   - [MNIST Digit Recognizer (CNN)](https://www.kaggle.com/c/digit-recognizer)
3. Read top-rated notebooks to learn from others
4. Iterate and improve your score

### Kaggle Workflow Template

```python
# 1. Load data
import pandas as pd
train = pd.read_csv("/kaggle/input/competition-name/train.csv")
test  = pd.read_csv("/kaggle/input/competition-name/test.csv")

# 2. EDA
print(train.shape)
print(train.isnull().sum())

# 3. Feature engineering

# 4. Train model

# 5. Generate submission
submission = pd.DataFrame({
    "Id": test["Id"],
    "Prediction": model.predict(X_test)
})
submission.to_csv("submission.csv", index=False)
```

---

##  Topic 6: Writing Technical Documentation

Good researchers communicate clearly. Document your experiments.

### Standard Experiment README Template

```markdown
# Experiment: [Name]

## Goal
What are you trying to do or prove?

## Dataset
- Name:
- Size:
- Source:
- Features:

## Model
- Architecture:
- Hyperparameters:

## Results
| Metric | Train | Validation | Test |
|--------|-------|------------|------|
| Accuracy | % | % | % |
| F1 Score | | | |

## Observations
What worked? What didn't? What would you try next?

## Files
- `train.py` - Training script
- `model.py` - Model definition
- `results/` - Plots and saved models
```

---

##  Phase 5 Project Ideas

### Beginner Research Projects

1. **Reproduce AlexNet on CIFAR-10** - Classic CNN paper from 2012
2. **Implement Word2Vec from scratch** - Word embeddings
3. **Compare 5 ML algorithms on a dataset** - Write up results

### Intermediate Projects

4. **Build a mini ChatBot** - LSTM + seq2seq
5. **Medical Image Classification** - X-ray / skin lesion datasets
6. **Time Series Forecasting** - Stock prices or weather data

### Advanced / Research-Level Projects

7. **Reproduce a 2024 research paper** - Find one on arXiv with code
8. **Propose a modification** - Change something in a model and see if it works better
9. **Submit to Kaggle** - Get competitive with your models
10. **Write a technical blog post** - Explain what you learned

---

##  Research Paper Templates

### How to summarize a paper (your notes format):

```
Paper: [Title]
Authors: [Names]
Year: [Year], Published: [Conference/Journal]
Link: [URL]

─── WHAT PROBLEM ────────────────────────────────
[1-2 sentences - what challenge are they tackling?]

─── THEIR SOLUTION ──────────────────────────────
[2-3 sentences - what did they propose?]

─── KEY IDEA ────────────────────────────────────
[The one thing that makes this paper special]

─── RESULTS ─────────────────────────────────────
[Key metrics from their experiments]

─── MY THOUGHTS ─────────────────────────────────
[What I found interesting / confusing / want to try]

─── STATUS ──────────────────────────────────────
[ ] Read pass 1  [ ] Read pass 2  [ ] Read fully  [ ] Reproduced
```

---


*Go to [LEARNING_PATH.md](../LEARNING_PATH.md) for the complete AI/ML roadmap.*  
*Previous phase: [Deep Learning](../Phase%204%20-%20Deep%20Learning/GUIDE.md)*
