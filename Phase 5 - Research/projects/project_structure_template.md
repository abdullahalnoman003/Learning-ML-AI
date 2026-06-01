# ML Research Project Structure Template

This directory contains templates for organizing ML research projects with best practices.

---

## Standard Project Structure

Here's a recommended structure for ML research projects:

```
project-name/
│
├── README.md                 # Project overview, setup instructions, results
├── LICENSE                   # License file
├── .gitignore               # Git ignore file
├── requirements.txt         # Python dependencies
├── environment.yml          # Conda environment (alternative)
├── setup.py                # Package installation script
│
├── data/                   # Data directory (usually not committed)
│   ├── raw/               # Original, immutable data
│   ├── processed/         # Cleaned, processed data
│   ├── external/          # External datasets
│   └── README.md         # Data documentation
│
├── notebooks/            # Jupyter notebooks for exploration
│   ├── 01_eda.ipynb            # Exploratory data analysis
│   ├── 02_preprocessing.ipynb   # Data preprocessing
│   ├── 03_baseline.ipynb        # Baseline models
│   ├── 04_experiments.ipynb     # Experiments
│   └── figures/                 # Generated figures
│
├── src/                  # Source code
│   ├── __init__.py
│   ├── data/            # Data loading and preprocessing
│   │   ├── __init__.py
│   │   ├── dataset.py
│   │   ├── dataloader.py
│   │   └── transforms.py
│   │
│   ├── models/          # Model architectures
│   │   ├── __init__.py
│   │   ├── base_model.py
│   │   ├── custom_model.py
│   │   └── layers.py
│   │
│   ├── training/        # Training logic
│   │   ├── __init__.py
│   │   ├── trainer.py
│   │   ├── losses.py
│   │   └── metrics.py
│   │
│   ├── evaluation/      # Evaluation code
│   │   ├── __init__.py
│   │   ├── evaluator.py
│   │   └── visualize.py
│   │
│   └── utils/          # Utility functions
│       ├── __init__.py
│       ├── config.py
│       ├── logger.py
│       └── helpers.py
│
├── scripts/            # Executable scripts
│   ├── train.py               # Training script
│   ├── evaluate.py            # Evaluation script
│   ├── inference.py           # Inference script
│   ├── preprocess_data.sh     # Data preprocessing
│   └── reproduce_results.sh   # Reproduction script
│
├── configs/           # Configuration files
│   ├── default.yaml          # Default configuration
│   ├── experiment1.yaml      # Experiment-specific configs
│   └── model_configs/        # Model-specific configs
│
├── tests/            # Unit tests
│   ├── __init__.py
│   ├── test_data.py
│   ├── test_models.py
│   ├── test_training.py
│   └── test_utils.py
│
├── experiments/      # Experiment logs and results
│   ├── README.md
│   ├── experiment_log.md
│   └── results/
│       ├── exp001/
│       ├── exp002/
│       └── ...
│
├── models/          # Saved models (usually not committed)
│   ├── .gitkeep
│   ├── best_model.pth
│   └── checkpoints/
│
├── outputs/         # Generated outputs
│   ├── figures/
│   ├── predictions/
│   └── visualizations/
│
├── docs/           # Documentation
│   ├── setup.md
│   ├── usage.md
│   ├── api.md
│   └── paper/          # Paper writing
│       ├── paper.tex
│       ├── references.bib
│       └── figures/
│
└── .github/        # GitHub-specific files (optional)
    └── workflows/
        └── tests.yml      # CI/CD workflows
```

---

## Template Files

### 1. README.md Template

```markdown
# Project Title

Brief description of your research project.

## Overview

### Problem
What problem are you solving?

### Approach
High-level description of your approach.

### Results
Summary of main results.

## Installation

### Requirements
- Python 3.8+
- CUDA 11.0+ (for GPU support)

### Setup
\`\`\`bash
# Clone repository
git clone https://github.com/username/project-name.git
cd project-name

# Create environment
conda env create -f environment.yml
conda activate project-name

# Or use pip
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
pip install -r requirements.txt

# Install package in development mode
pip install -e .
\`\`\`

## Quick Start

\`\`\`bash
# Download data
python scripts/download_data.py

# Preprocess data
python scripts/preprocess.py

# Train model
python scripts/train.py --config configs/default.yaml

# Evaluate model
python scripts/evaluate.py --model models/best_model.pth

# Run inference
python scripts/inference.py --input data/test/ --output outputs/
\`\`\`

## Usage

### Training
\`\`\`bash
python scripts/train.py \\
    --config configs/experiment1.yaml \\
    --data data/processed/ \\
    --output experiments/exp001/ \\
    --gpu 0
\`\`\`

### Evaluation
\`\`\`bash
python scripts/evaluate.py \\
    --model models/best_model.pth \\
    --data data/test/ \\
    --output outputs/eval/
\`\`\`

## Project Structure

See [Project Structure](#standard-project-structure) above.

## Configuration

Configuration is managed through YAML files in `configs/`.

Example configuration:
\`\`\`yaml
model:
  architecture: "resnet50"
  num_classes: 10

training:
  epochs: 100
  batch_size: 32
  learning_rate: 0.001

data:
  train_path: "data/processed/train/"
  val_path: "data/processed/val/"
  augmentation: true
\`\`\`

## Experiments

Results from experiments are tracked in `experiments/`. See `experiments/README.md` for details.

| Experiment | Description | Val Acc | Test Acc | Notes |
|------------|-------------|---------|----------|-------|
| exp001 | Baseline | 85.2% | 84.8% | Simple CNN |
| exp002 | ResNet50 | 92.1% | 91.5% | Best so far |

## Results

### Main Results

Present your main results here with tables and figures.

### Visualizations

![Result 1](outputs/figures/result1.png)
![Result 2](outputs/figures/result2.png)

## Reproducibility

To reproduce the results:

\`\`\`bash
bash scripts/reproduce_results.sh
\`\`\`

This will:
1. Download data
2. Preprocess data
3. Train model with optimal hyperparameters
4. Evaluate on test set
5. Generate figures

### Random Seeds
All experiments use fixed random seeds:
- Python: 42
- NumPy: 42
- PyTorch: 42

## Citation

If you use this code in your research, please cite:

\`\`\`bibtex
@article{authorYYYY,
  title={Paper Title},
  author={Author Names},
  journal={Journal/Conference},
  year={YYYY}
}
\`\`\`

## License

This project is licensed under the MIT License - see LICENSE file.

## Acknowledgments

- Funding source
- Collaborators
- Resources used

## Contact

- **Author:** Your Name
- **Email:** your.email@example.com
- **Website:** https://yourwebsite.com
\`\`\`

---

### 2. requirements.txt Template

```
# Core
numpy>=1.21.0
pandas>=1.3.0
scipy>=1.7.0

# Deep Learning
torch>=2.0.0
torchvision>=0.15.0
torchaudio>=2.0.0

# Training & Evaluation
scikit-learn>=1.0.0
matplotlib>=3.4.0
seaborn>=0.11.0
tqdm>=4.62.0

# Experiment Tracking
wandb>=0.12.0
tensorboard>=2.10.0

# Configuration
pyyaml>=5.4.0
omegaconf>=2.1.0

# Utilities
pillow>=8.3.0
opencv-python>=4.5.0
albumentations>=1.1.0

# Testing
pytest>=7.0.0
pytest-cov>=3.0.0

# Code Quality
black>=22.0.0
flake8>=4.0.0
isort>=5.10.0
mypy>=0.950

# Jupyter
jupyter>=1.0.0
ipywidgets>=7.6.0
```

---

### 3. .gitignore Template

```
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg

# Virtual Environment
venv/
ENV/
env/
.venv

# Jupyter Notebook
.ipynb_checkpoints
*.ipynb_checkpoints/

# Data
data/raw/*
data/processed/*
data/external/*
!data/*/README.md
!data/*/.gitkeep

# Models
models/*.pth
models/*.pt
models/*.h5
models/*.ckpt
models/checkpoints/*
!models/.gitkeep

# Experiments
experiments/*/logs/
experiments/*/checkpoints/
experiments/*/outputs/

# Outputs
outputs/
results/
*.png
*.jpg
*.jpeg
!docs/paper/figures/*.png

# IDE
.vscode/
.idea/
*.swp
*.swo
*~
.DS_Store

# Logs
logs/
*.log
wandb/
mlruns/

# Temporary files
tmp/
temp/
*.tmp

# Environment
.env
.env.local

# OS
Thumbs.db
.DS_Store
```

---

### 4. setup.py Template

```python
from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="project-name",
    version="0.1.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="Brief description",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/username/project-name",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    python_requires=">=3.8",
    install_requires=requirements,
    extras_require={
        "dev": ["pytest", "black", "flake8", "mypy"],
    },
)
```

---

### 5. Config File Template (configs/default.yaml)

```yaml
# Project Configuration

project:
  name: "project-name"
  description: "Brief description"
  seed: 42

# Data Configuration
data:
  train_path: "data/processed/train/"
  val_path: "data/processed/val/"
  test_path: "data/processed/test/"
  num_classes: 10
  image_size: 224
  augmentation: true
  num_workers: 4

# Model Configuration
model:
  architecture: "resnet50"
  pretrained: true
  num_classes: ${data.num_classes}
  dropout: 0.5

# Training Configuration
training:
  epochs: 100
  batch_size: 32
  learning_rate: 0.001
  optimizer: "adam"
  weight_decay: 0.0001
  lr_scheduler:
    name: "cosine"
    warmup_epochs: 5

  # Loss
  loss: "cross_entropy"
  label_smoothing: 0.1

  # Regularization
  mixup: false
  cutmix: false

  # Checkpointing
  save_frequency: 5
  keep_last_n: 3

# Evaluation Configuration
evaluation:
  batch_size: 64
  metrics:
    - "accuracy"
    - "precision"
    - "recall"
    - "f1"

# Logging Configuration
logging:
  log_frequency: 10
  use_wandb: true
  wandb_project: "project-name"
  use_tensorboard: true

# System Configuration
system:
  device: "cuda"  # cuda, cpu, or specific cuda:0
  mixed_precision: true
  cudnn_benchmark: true
  deterministic: false
```

---

### 6. Training Script Template (scripts/train.py)

```python
"""
Training script for the model.

Usage:
    python scripts/train.py --config configs/default.yaml
"""

import argparse
import yaml
import torch
import torch.nn as nn
from pathlib import Path
import sys

# Add src to path
sys.path.append(str(Path(__file__).parent.parent))

from src.data.dataloader import create_dataloaders
from src.models.model import create_model
from src.training.trainer import Trainer
from src.utils.config import load_config, set_seed
from src.utils.logger import setup_logger


def parse_args():
    parser = argparse.ArgumentParser(description="Train model")
    parser.add_argument("--config", type=str, required=True, help="Path to config file")
    parser.add_argument("--output", type=str, default="experiments/", help="Output directory")
    parser.add_argument("--resume", type=str, default=None, help="Resume from checkpoint")
    parser.add_argument("--gpu", type=int, default=0, help="GPU device")
    return parser.parse_args()


def main():
    # Parse arguments
    args = parse_args()

    # Load configuration
    config = load_config(args.config)

    # Setup
    set_seed(config.project.seed)
    device = torch.device(f"cuda:{args.gpu}" if torch.cuda.is_available() else "cpu")
    logger = setup_logger(args.output)

    logger.info(f"Starting training with config: {args.config}")
    logger.info(f"Device: {device}")

    # Create dataloaders
    train_loader, val_loader = create_dataloaders(config)
    logger.info(f"Train samples: {len(train_loader.dataset)}")
    logger.info(f"Val samples: {len(val_loader.dataset)}")

    # Create model
    model = create_model(config)
    model = model.to(device)
    logger.info(f"Model: {config.model.architecture}")

    # Create trainer
    trainer = Trainer(
        model=model,
        train_loader=train_loader,
        val_loader=val_loader,
        config=config,
        device=device,
        output_dir=args.output
    )

    # Resume if specified
    if args.resume:
        trainer.load_checkpoint(args.resume)
        logger.info(f"Resumed from {args.resume}")

    # Train
    logger.info("Starting training...")
    trainer.train()

    logger.info("Training completed!")
    logger.info(f"Best model saved to: {args.output}/best_model.pth")


if __name__ == "__main__":
    main()
```

---

### 7. Data README Template (data/README.md)

```markdown
# Data Documentation

## Overview

Description of the datasets used in this project.

## Directory Structure

\`\`\`
data/
├── raw/          # Original, immutable data
├── processed/    # Cleaned, processed data
└── external/     # External datasets
\`\`\`

## Datasets

### Dataset 1: [Name]

- **Source:** URL or reference
- **Size:** Number of samples
- **Format:** Image/CSV/JSON/etc.
- **License:** License information
- **Download:** Instructions for downloading

#### Structure
\`\`\`
dataset1/
├── train/
│   ├── class1/
│   ├── class2/
│   └── ...
├── val/
└── test/
\`\`\`

#### Statistics
- Train: 10,000 samples
- Validation: 2,000 samples
- Test: 2,000 samples
- Classes: 10
- Image size: 224x224

#### Preprocessing
1. Resize to 224x224
2. Normalize with ImageNet statistics
3. Data augmentation (training only):
   - Random horizontal flip
   - Random rotation (±15°)
   - Color jitter

## Downloading Data

\`\`\`bash
# Download script
python scripts/download_data.py

# Or manually download from:
# https://example.com/dataset.zip
\`\`\`

## Data Processing

To process raw data:

\`\`\`bash
python scripts/preprocess.py --input data/raw/ --output data/processed/
\`\`\`

## Data Format

### Input Format
- Images: RGB, 224x224 pixels
- Labels: Integer class indices (0-9)

### Output Format
Processed data is stored in the following structure:
\`\`\`
processed/
├── train/
│   ├── images/
│   └── labels.csv
├── val/
└── test/
\`\`\`

## Citation

If using this dataset, cite:
\`\`\`bibtex
@dataset{datasetYYYY,
  title={Dataset Title},
  author={Author Names},
  year={YYYY}
}
\`\`\`
\`\`\`

---

### 8. Testing Template (tests/test_models.py)

```python
"""
Unit tests for models.
"""

import pytest
import torch
from src.models.model import create_model


def test_model_forward():
    """Test model forward pass."""
    # Create a simple config
    class Config:
        class model:
            architecture = "resnet18"
            num_classes = 10
            pretrained = False

    config = Config()
    model = create_model(config)

    # Test forward pass
    batch_size = 4
    x = torch.randn(batch_size, 3, 224, 224)
    output = model(x)

    # Check output shape
    assert output.shape == (batch_size, 10), f"Expected shape {(batch_size, 10)}, got {output.shape}"


def test_model_training_mode():
    """Test model can switch between train/eval modes."""
    class Config:
        class model:
            architecture = "resnet18"
            num_classes = 10
            pretrained = False

    config = Config()
    model = create_model(config)

    # Test train mode
    model.train()
    assert model.training is True

    # Test eval mode
    model.eval()
    assert model.training is False


def test_model_device_transfer():
    """Test model can be transferred to device."""
    class Config:
        class model:
            architecture = "resnet18"
            num_classes = 10
            pretrained = False

    config = Config()
    model = create_model(config)

    # Test CPU
    model = model.to("cpu")
    x = torch.randn(2, 3, 224, 224)
    output = model(x)
    assert output.device.type == "cpu"

    # Test CUDA if available
    if torch.cuda.is_available():
        model = model.to("cuda")
        x = x.to("cuda")
        output = model(x)
        assert output.device.type == "cuda"


if __name__ == "__main__":
    pytest.main([__file__])
```

---

## Best Practices

### 1. Code Organization
- Keep source code in `src/`
- Executable scripts in `scripts/`
- Tests in `tests/`
- Notebooks for exploration only

### 2. Configuration Management
- Use YAML for configs
- Don't hardcode parameters
- Use hierarchical configs
- Version your configs

### 3. Version Control
- Commit code, not data/models
- Use meaningful commit messages
- Tag important versions
- Use branches for experiments

### 4. Documentation
- README for overview
- Docstrings for functions
- Comments for complex logic
- Document decisions in experiments/

### 5. Testing
- Write unit tests
- Test critical functions
- Use CI/CD (GitHub Actions)
- Test before committing

### 6. Reproducibility
- Set random seeds
- Log all hyperparameters
- Version dependencies
- Document environment

### 7. Experiment Tracking
- Use experiment tracking tools
- Log to both local and cloud
- Compare experiments systematically
- Archive old experiments

---

## Quick Start

To start a new project:

```bash
# Create project directory
mkdir my-new-project
cd my-new-project

# Copy template structure
# (Or use this as reference)

# Initialize git
git init

# Create virtual environment
python -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Create necessary directories
mkdir -p data/{raw,processed,external}
mkdir -p models/checkpoints
mkdir -p experiments
mkdir -p outputs/{figures,predictions}
mkdir -p logs

# Add .gitkeep files
touch data/.gitkeep
touch models/.gitkeep
touch experiments/.gitkeep
touch outputs/.gitkeep

# Start coding!
```

---

## Resources

- [Cookiecutter Data Science](https://drivendata.github.io/cookiecutter-data-science/)
- [PyTorch Project Template](https://github.com/victoresque/pytorch-template)
- [ML Project Template](https://github.com/drivendata/cookiecutter-data-science)

---

**Remember:** Good project structure makes collaboration easier, code more maintainable, and results reproducible!
