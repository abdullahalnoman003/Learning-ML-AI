# Experiment Log Template

This template helps you track ML experiments systematically. Copy this template for each major experiment series.

---

# Experiment Series: [Name]

**Project:** Project Name
**Researcher:** Your Name
**Start Date:** YYYY-MM-DD
**Status:**  In Progress /  Complete /  Abandoned
**Goal:** Brief description of what you're trying to achieve

---

## Hypothesis

What do you expect to happen? What are you testing?

Example: "Adding attention mechanism will improve accuracy by 5% because it allows the model to focus on relevant features."

---

## Background & Motivation

### Problem
What problem are you trying to solve?

### Current Baseline
What's the current best approach/result?

### Proposed Improvement
What change are you proposing?

### Why This Might Work
Theoretical or empirical justification.

---

## Experimental Setup

### Dataset
- **Name:** Dataset name
- **Size:** Train/Val/Test splits
- **Source:** Where it's from
- **Preprocessing:** What preprocessing is applied
- **Version:** Dataset version or date

### Model
- **Architecture:** Model architecture
- **Framework:** PyTorch / TensorFlow / JAX
- **Input:** Input format and shape
- **Output:** Output format and shape

### Training Configuration
```yaml
model:
  architecture: "resnet50"
  pretrained: true

training:
  epochs: 100
  batch_size: 32
  optimizer: "adam"
  learning_rate: 0.001
  lr_scheduler: "cosine"
  weight_decay: 0.0001

data:
  augmentation: true
  normalization: "imagenet"

system:
  device: "cuda"
  mixed_precision: true
  num_workers: 4
  seed: 42
```

### Evaluation Metrics
- Metric 1 (e.g., Accuracy)
- Metric 2 (e.g., F1 Score)
- Metric 3 (e.g., Loss)

### Compute Resources
- **Hardware:** GPU model, RAM, CPU
- **Estimated Time:** Expected training time
- **Cost:** If using cloud compute

---

## Experiments

### Experiment 1: [Short Description]

**Date:** YYYY-MM-DD
**Researcher:** Name
**Status:**  Complete /  Running /  Failed

#### Configuration
What's different from the baseline?
```python
config = {
    "learning_rate": 0.001,
    "batch_size": 32,
    # Other relevant parameters
}
```

#### Hypothesis
What do you expect?

#### Results
| Metric | Train | Validation | Test |
|--------|-------|------------|------|
| Accuracy | 95.2% | 87.3% | - |
| Loss | 0.15 | 0.42 | - |

#### Observations
- Training converged after 50 epochs
- Validation accuracy plateaued at epoch 40
- Some overfitting observed

#### Analysis
What do the results tell you?

#### Visualizations
- Training curve: `figures/exp1_training_curve.png`
- Confusion matrix: `figures/exp1_confusion_matrix.png`

#### Files
- Code: `src/experiments/exp1_baseline.py`
- Model: `models/exp1_baseline.pth`
- Logs: `logs/exp1_baseline.json`
- Weights & Biases: [link]

#### Conclusion
Did it work? Why or why not?

#### Next Steps
- [ ] Try larger learning rate
- [ ] Add more regularization
- [ ] Test on different dataset

---

### Experiment 2: [Short Description]

**Date:** YYYY-MM-DD
**Status:**  Running

#### What Changed
Compared to Experiment 1:
- Increased learning rate from 0.001 to 0.005
- Added dropout (p=0.3)

#### Hypothesis
Higher learning rate should speed up convergence without hurting final performance.

#### Current Progress
- Epoch 25/100
- Current val accuracy: 85.1%
- Looking promising but need to wait for completion

#### Preliminary Observations
- Faster initial convergence
- More noisy training curve
- Need to monitor for overfitting

---

### Experiment 3: [Short Description]

**Date:** YYYY-MM-DD
**Status:**  Failed

#### What Changed
Attempted to use a more complex architecture.

#### Results
Training diverged after 10 epochs.

#### Error Analysis
- Loss became NaN
- Likely due to gradient explosion
- Learning rate too high for this architecture

#### Lessons Learned
- Need to adjust learning rate for different architectures
- Should have used gradient clipping
- Start with smaller learning rate for complex models

#### Next Steps
- Retry with 10x smaller learning rate
- Add gradient clipping

---

## Experiment Comparison

### Summary Table

| Exp | Description | Val Acc | Test Acc | Training Time | Notes |
|-----|-------------|---------|----------|---------------|-------|
| 1 | Baseline | 87.3% | - | 2 hours | Overfitting |
| 2 | Higher LR | 85.1% | - | Running | In progress |
| 3 | Complex arch | Failed | - | 30 min | Diverged |

### Best Performing
Experiment 1 is currently the best with 87.3% validation accuracy.

### Key Insights
1. Baseline is strong but overfits
2. Complex architectures need careful tuning
3. Need better regularization

---

## Ablation Studies

Testing the contribution of individual components.

### Ablation 1: Remove Component X

**Results:**
- Accuracy dropped from 87.3% to 82.1%
- **Conclusion:** Component X contributes 5.2% to performance

### Ablation 2: Remove Component Y

**Results:**
- Accuracy dropped from 87.3% to 85.8%
- **Conclusion:** Component Y contributes 1.5% to performance

### Ablation Summary
Components ranked by importance:
1. Component X: +5.2%
2. Component Y: +1.5%

---

## Error Analysis

### Failure Cases
Where does the model fail?

#### Category 1: [Description]
- Example 1: Description
- Example 2: Description
- **Possible Fix:** Suggestion

#### Category 2: [Description]
- Example 1: Description
- **Possible Fix:** Suggestion

### Confusion Analysis
Common misclassifications:
- Class A often confused with Class B (15% of errors)
- Possible reason: Visual similarity

---

## Hyperparameter Tuning

### Grid Search Results

| LR | Batch Size | Dropout | Val Acc |
|----|------------|---------|---------|
| 0.001 | 32 | 0.2 | 87.3% |
| 0.001 | 64 | 0.2 | 86.5% |
| 0.005 | 32 | 0.2 | 85.1% |
| 0.001 | 32 | 0.3 | **88.1%** |

**Best Configuration:** LR=0.001, Batch=32, Dropout=0.3

### Hyperparameter Importance
Ranked by impact on performance:
1. Learning rate (high impact)
2. Dropout (medium impact)
3. Batch size (low impact)

---

## Reproducibility Checklist

- [x] Random seeds set (Python, NumPy, PyTorch)
- [x] All hyperparameters documented
- [x] Library versions recorded (requirements.txt)
- [x] Data preprocessing steps documented
- [x] Model architecture fully specified
- [x] Training procedure documented
- [x] Evaluation protocol documented
- [x] Hardware specifications noted
- [ ] Code cleaned and commented
- [ ] Reproduction script provided

---

## Code & Artifacts

### Repository
- **Git Repo:** [link]
- **Branch:** experiment/series-name
- **Commit:** abc123def456

### Key Files
- Main script: `src/train.py`
- Model definition: `src/models/model.py`
- Data loader: `src/data/dataloader.py`
- Config: `configs/experiment_config.yaml`

### Saved Models
- Best model: `models/best_model.pth`
- Final model: `models/final_model.pth`
- Checkpoint: `models/checkpoint_epoch50.pth`

### Logs & Tracking
- Experiment tracking: [Weights & Biases link]
- TensorBoard logs: `logs/tensorboard/`
- JSON logs: `logs/experiments.json`

---

## Timeline

| Date | Event | Notes |
|------|-------|-------|
| 2024-01-01 | Started experiments | Initial baseline |
| 2024-01-03 | Completed Exp 1 | Baseline complete |
| 2024-01-05 | Started Exp 2 | Testing higher LR |
| 2024-01-06 | Exp 3 failed | Training diverged |
| 2024-01-08 | Completed Exp 2 | Worse than baseline |

---

## Results & Conclusions

### Summary
Brief summary of what you learned from this experiment series.

### Key Findings
1. Finding 1
2. Finding 2
3. Finding 3

### Best Model
- **Configuration:** Description
- **Performance:** Val: X%, Test: Y%
- **Location:** `models/best_model.pth`

### Lessons Learned
1. Lesson 1
2. Lesson 2
3. Lesson 3

### What Worked
- Approach 1
- Approach 2

### What Didn't Work
- Approach 3 (reason)
- Approach 4 (reason)

### Surprises
Unexpected findings or behaviors.

---

## Future Work

### Immediate Next Steps
- [ ] Action item 1
- [ ] Action item 2
- [ ] Action item 3

### Long-term Ideas
- Idea 1
- Idea 2

### Questions to Explore
1. Question 1
2. Question 2

---

## References

Papers or resources that informed this experiment:
1. [Paper 1](url) - Relevant aspect
2. [Paper 2](url) - Relevant aspect

---

## Discussion & Notes

### Meeting Notes (Date)
Discussion with advisor/collaborators:
- Point 1
- Point 2
- Decisions made

### Personal Reflections
Your thoughts and observations during the experiment.

---

## Appendix

### Detailed Configuration

Full configuration file:
```yaml
# Complete config
```

### Additional Visualizations
- Figure 1: Description
- Figure 2: Description

### Raw Data
Link to raw experimental data if needed.

---

## Quick Reference Commands

```bash
# Train model
python train.py --config configs/exp1.yaml

# Evaluate model
python evaluate.py --model models/best_model.pth --data data/test/

# Resume training
python train.py --resume models/checkpoint.pth

# Track with W&B
python train.py --wandb --project my-project
```

---

**Last Updated:** YYYY-MM-DD
**Next Review:** YYYY-MM-DD
