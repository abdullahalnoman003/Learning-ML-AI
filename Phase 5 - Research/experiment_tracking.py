"""
EXPERIMENT TRACKING FOR MACHINE LEARNING
=========================================

This guide teaches you how to track ML experiments effectively using:
1. Simple logging with Python
2. Weights & Biases (W&B) integration
3. MLflow basics
4. Best practices for reproducibility

Author: ML Research Learning Path
"""

import json
import os
import time
from datetime import datetime
from pathlib import Path
import hashlib


class SimpleExperimentTracker:
    """
    Simple experiment tracker that logs experiments to JSON files.
    Useful for small projects or when you don't need a full tracking platform.
    """

    def __init__(self, experiment_dir="experiments"):
        """
        Initialize the experiment tracker.

        Args:
            experiment_dir: Directory to store experiment logs
        """
        self.experiment_dir = Path(experiment_dir)
        self.experiment_dir.mkdir(parents=True, exist_ok=True)
        self.current_experiment = None
        self.start_time = None

    def start_experiment(self, name, description="", tags=None):
        """Start a new experiment."""
        self.start_time = time.time()

        self.current_experiment = {
            "name": name,
            "description": description,
            "tags": tags or [],
            "timestamp": datetime.now().isoformat(),
            "config": {},
            "metrics": {},
            "artifacts": [],
            "status": "running",
            "duration_seconds": 0
        }

        print(f"Started experiment: {name}")
        return self

    def log_config(self, config):
        """Log experiment configuration/hyperparameters."""
        if self.current_experiment is None:
            raise ValueError("No active experiment. Call start_experiment() first.")

        self.current_experiment["config"].update(config)
        print(f"Logged config: {list(config.keys())}")

    def log_metric(self, name, value, step=None):
        """Log a single metric value."""
        if self.current_experiment is None:
            raise ValueError("No active experiment. Call start_experiment() first.")

        if name not in self.current_experiment["metrics"]:
            self.current_experiment["metrics"][name] = []

        metric_entry = {"value": value}
        if step is not None:
            metric_entry["step"] = step
        metric_entry["timestamp"] = datetime.now().isoformat()

        self.current_experiment["metrics"][name].append(metric_entry)

    def log_metrics(self, metrics, step=None):
        """Log multiple metrics at once."""
        for name, value in metrics.items():
            self.log_metric(name, value, step)

    def log_artifact(self, filepath, artifact_type="file"):
        """Log an artifact (model checkpoint, plot, etc.)."""
        if self.current_experiment is None:
            raise ValueError("No active experiment. Call start_experiment() first.")

        self.current_experiment["artifacts"].append({
            "filepath": str(filepath),
            "type": artifact_type,
            "timestamp": datetime.now().isoformat()
        })

        print(f"Logged artifact: {filepath}")

    def end_experiment(self, status="completed"):
        """End the current experiment and save results."""
        if self.current_experiment is None:
            raise ValueError("No active experiment.")

        self.current_experiment["status"] = status
        self.current_experiment["duration_seconds"] = time.time() - self.start_time

        # Generate experiment ID based on timestamp and name
        exp_id = hashlib.md5(
            f"{self.current_experiment['timestamp']}_{self.current_experiment['name']}".encode()
        ).hexdigest()[:8]

        # Save to file
        filename = self.experiment_dir / f"experiment_{exp_id}.json"
        with open(filename, 'w') as f:
            json.dump(self.current_experiment, f, indent=2)

        print(f"\nExperiment '{self.current_experiment['name']}' ended.")
        print(f"Duration: {self.current_experiment['duration_seconds']:.2f} seconds")
        print(f"Saved to: {filename}")

        # Reset
        result = self.current_experiment
        self.current_experiment = None
        self.start_time = None

        return result

    def list_experiments(self):
        """List all logged experiments."""
        experiments = []
        for filepath in self.experiment_dir.glob("experiment_*.json"):
            with open(filepath, 'r') as f:
                exp = json.load(f)
                exp["filepath"] = str(filepath)
                experiments.append(exp)

        # Sort by timestamp
        experiments.sort(key=lambda x: x["timestamp"], reverse=True)
        return experiments

    def print_experiment_summary(self, experiment):
        """Print a summary of an experiment."""
        print("\n" + "=" * 80)
        print(f"Experiment: {experiment['name']}")
        print("=" * 80)
        print(f"Description: {experiment.get('description', 'N/A')}")
        print(f"Status: {experiment['status']}")
        print(f"Timestamp: {experiment['timestamp']}")
        print(f"Duration: {experiment.get('duration_seconds', 0):.2f} seconds")
        print(f"Tags: {', '.join(experiment.get('tags', []))}")

        print("\nConfiguration:")
        for key, value in experiment.get('config', {}).items():
            print(f"  {key}: {value}")

        print("\nFinal Metrics:")
        for name, values in experiment.get('metrics', {}).items():
            if values:
                final_value = values[-1]['value']
                print(f"  {name}: {final_value}")

        if experiment.get('artifacts'):
            print("\nArtifacts:")
            for artifact in experiment['artifacts']:
                print(f"  {artifact['type']}: {artifact['filepath']}")

        print("=" * 80)


class WandBExampleTracker:
    """
    Example wrapper for Weights & Biases experiment tracking.
    Shows how to use W&B for more advanced tracking.

    Install: pip install wandb
    """

    def __init__(self):
        """Initialize W&B tracker."""
        self.wandb_available = False
        try:
            import wandb
            self.wandb = wandb
            self.wandb_available = True
        except ImportError:
            print("Weights & Biases not installed. Install with: pip install wandb")

    def setup_guide(self):
        """Display setup guide for W&B."""
        print("=" * 80)
        print("WEIGHTS & BIASES (W&B) SETUP GUIDE")
        print("=" * 80)
        print("\n1. INSTALLATION:")
        print("   pip install wandb")
        print()
        print("2. LOGIN:")
        print("   wandb login")
        print("   (This will open browser for API key)")
        print()
        print("3. INITIALIZE IN CODE:")
        print("   import wandb")
        print("   wandb.init(project='my-project', name='experiment-1')")
        print()
        print("4. LOG METRICS:")
        print("   wandb.log({'accuracy': 0.95, 'loss': 0.05})")
        print()
        print("5. FINISH:")
        print("   wandb.finish()")
        print()
        print("6. VIEW RESULTS:")
        print("   Visit: https://wandb.ai/")
        print("=" * 80)

    def example_usage(self):
        """Show example usage of W&B."""
        print("\n" + "=" * 80)
        print("EXAMPLE: Using Weights & Biases")
        print("=" * 80)

        code_example = '''
import wandb
import numpy as np

# 1. Initialize W&B
wandb.init(
    project="my-ml-project",
    name="experiment-1",
    config={
        "learning_rate": 0.001,
        "batch_size": 32,
        "epochs": 10,
        "architecture": "resnet50"
    },
    tags=["baseline", "resnet"]
)

# 2. Access config
config = wandb.config

# 3. Training loop
for epoch in range(config.epochs):
    # Your training code here
    train_loss = np.random.random()  # Placeholder
    val_loss = np.random.random()    # Placeholder
    val_acc = np.random.random()     # Placeholder

    # Log metrics
    wandb.log({
        "epoch": epoch,
        "train_loss": train_loss,
        "val_loss": val_loss,
        "val_accuracy": val_acc
    })

# 4. Log artifacts (model, plots, etc.)
# Save model
model_path = "model.pth"
# torch.save(model.state_dict(), model_path)
wandb.save(model_path)

# Log table
table = wandb.Table(
    columns=["id", "prediction", "ground_truth"],
    data=[[0, 0.9, 1.0], [1, 0.7, 0.0]]
)
wandb.log({"predictions": table})

# Log images
# wandb.log({"examples": [wandb.Image(img) for img in images]})

# 5. Finish
wandb.finish()
'''
        print(code_example)

    def advanced_features(self):
        """Show advanced W&B features."""
        print("\n" + "=" * 80)
        print("ADVANCED W&B FEATURES")
        print("=" * 80)

        print("\n1. HYPERPARAMETER SWEEPS:")
        print("-" * 80)
        sweep_example = '''
# Define sweep configuration
sweep_config = {
    'method': 'bayes',  # or 'grid', 'random'
    'metric': {
        'name': 'val_accuracy',
        'goal': 'maximize'
    },
    'parameters': {
        'learning_rate': {
            'min': 0.0001,
            'max': 0.1
        },
        'batch_size': {
            'values': [16, 32, 64]
        },
        'optimizer': {
            'values': ['adam', 'sgd']
        }
    }
}

# Initialize sweep
sweep_id = wandb.sweep(sweep_config, project="my-project")

# Run sweep agent
wandb.agent(sweep_id, function=train_function, count=10)
'''
        print(sweep_example)

        print("\n2. ARTIFACT TRACKING:")
        print("-" * 80)
        artifact_example = '''
# Save dataset as artifact
artifact = wandb.Artifact('my-dataset', type='dataset')
artifact.add_file('data.csv')
wandb.log_artifact(artifact)

# Use artifact in another run
artifact = wandb.use_artifact('my-dataset:latest')
artifact_dir = artifact.download()
'''
        print(artifact_example)

        print("\n3. CUSTOM PLOTS:")
        print("-" * 80)
        plot_example = '''
# Log confusion matrix
wandb.log({"confusion_matrix": wandb.plot.confusion_matrix(
    probs=None,
    y_true=y_true,
    preds=predictions,
    class_names=class_names
)})

# Log PR curve
wandb.log({"pr_curve": wandb.plot.pr_curve(
    y_true,
    y_probas,
    labels=class_names
)})

# Log ROC curve
wandb.log({"roc_curve": wandb.plot.roc_curve(
    y_true,
    y_probas,
    labels=class_names
)})
'''
        print(plot_example)

        print("\n4. MODEL VERSIONING:")
        print("-" * 80)
        model_example = '''
# Link model to W&B Model Registry
run = wandb.init()
artifact = wandb.Artifact('my-model', type='model')
artifact.add_file('model.pth')
run.log_artifact(artifact)

# Later: Load specific model version
artifact = wandb.use_artifact('my-model:v0')
artifact_dir = artifact.download()
'''
        print(model_example)


class MLflowExampleTracker:
    """
    Example for MLflow experiment tracking.
    MLflow is another popular open-source platform.

    Install: pip install mlflow
    """

    def setup_guide(self):
        """Display setup guide for MLflow."""
        print("=" * 80)
        print("MLFLOW SETUP GUIDE")
        print("=" * 80)
        print("\n1. INSTALLATION:")
        print("   pip install mlflow")
        print()
        print("2. START UI:")
        print("   mlflow ui")
        print("   (Visit http://localhost:5000)")
        print()
        print("3. BASIC USAGE:")
        print("-" * 80)

        example = '''
import mlflow

# Start a run
with mlflow.start_run():
    # Log parameters
    mlflow.log_param("learning_rate", 0.001)
    mlflow.log_param("batch_size", 32)

    # Log metrics
    mlflow.log_metric("accuracy", 0.95)
    mlflow.log_metric("loss", 0.05)

    # Log model
    mlflow.sklearn.log_model(model, "model")

    # Log artifacts
    mlflow.log_artifact("plot.png")
'''
        print(example)
        print("=" * 80)


def experiment_tracking_best_practices():
    """Display best practices for experiment tracking."""
    print("=" * 80)
    print("EXPERIMENT TRACKING BEST PRACTICES")
    print("=" * 80)

    print("\n1. WHAT TO TRACK:")
    print("-" * 80)
    to_track = [
        "• Hyperparameters (learning rate, batch size, architecture, etc.)",
        "• Metrics (loss, accuracy, F1, etc.) - log every epoch",
        "• System info (GPU type, library versions, random seeds)",
        "• Dataset info (version, size, splits, preprocessing)",
        "• Model checkpoints (best model, final model, intermediate)",
        "• Visualizations (learning curves, confusion matrices, samples)",
        "• Code version (git commit hash, branch)",
        "• Training time and resource usage"
    ]
    for item in to_track:
        print(item)

    print("\n2. ORGANIZATION:")
    print("-" * 80)
    org_tips = [
        "• Use descriptive experiment names (not 'exp1', 'exp2')",
        "• Group related experiments with tags",
        "• Use hierarchical project structure",
        "• Document what you're testing in descriptions",
        "• Keep a research notebook/log",
        "• Link experiments to code commits"
    ]
    for tip in org_tips:
        print(tip)

    print("\n3. REPRODUCIBILITY:")
    print("-" * 80)
    repro_tips = [
        "• Set and log random seeds (Python, NumPy, PyTorch, etc.)",
        "• Log exact library versions (requirements.txt or conda env)",
        "• Save data preprocessing steps",
        "• Document hardware used (GPU model, CPU, RAM)",
        "• Save exact command used to run experiment",
        "• Version your datasets",
        "• Save full config files, not just changed parameters"
    ]
    for tip in repro_tips:
        print(tip)

    print("\n4. EFFICIENCY:")
    print("-" * 80)
    efficiency_tips = [
        "• Don't log too frequently (every 10-100 steps, not every step)",
        "• Use async logging when possible",
        "• Compress large artifacts",
        "• Clean up failed experiments",
        "• Archive old experiments",
        "• Use early stopping to save compute"
    ]
    for tip in efficiency_tips:
        print(tip)

    print("\n5. ANALYSIS:")
    print("-" * 80)
    analysis_tips = [
        "• Regularly review experiment results",
        "• Compare experiments side-by-side",
        "• Look for patterns across experiments",
        "• Share results with team members",
        "• Document insights and learnings",
        "• Create summary reports for project milestones"
    ]
    for tip in analysis_tips:
        print(tip)

    print("\n6. COMMON PITFALLS TO AVOID:")
    print("-" * 80)
    pitfalls = [
        "• Not tracking random seeds (non-reproducible results)",
        "• Forgetting to log important hyperparameters",
        "• Overwriting previous experiment results",
        "• Not saving the best model (only saving final)",
        "• Inconsistent metric names across experiments",
        "• Not documenting why experiments failed",
        "• Manual tracking in spreadsheets (error-prone)"
    ]
    for pitfall in pitfalls:
        print(pitfall)

    print("\n" + "=" * 80)


def complete_example():
    """Complete example of experiment tracking workflow."""
    print("=" * 80)
    print("COMPLETE EXPERIMENT TRACKING EXAMPLE")
    print("=" * 80)

    example_code = '''
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader
import wandb
import random
import numpy as np

# ============================================================================
# 1. SET RANDOM SEEDS FOR REPRODUCIBILITY
# ============================================================================
def set_seed(seed=42):
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)
    torch.backends.cudnn.deterministic = True
    torch.backends.cudnn.benchmark = False

set_seed(42)

# ============================================================================
# 2. DEFINE CONFIGURATION
# ============================================================================
config = {
    # Model
    "architecture": "resnet18",
    "pretrained": True,
    "num_classes": 10,

    # Training
    "learning_rate": 0.001,
    "batch_size": 32,
    "epochs": 50,
    "optimizer": "adam",
    "weight_decay": 0.0001,

    # Data
    "dataset": "CIFAR10",
    "augmentation": True,
    "train_split": 0.8,

    # System
    "seed": 42,
    "device": "cuda" if torch.cuda.is_available() else "cpu",
    "num_workers": 4,

    # Tracking
    "log_interval": 10,  # Log every N batches
    "save_checkpoint_interval": 5  # Save every N epochs
}

# ============================================================================
# 3. INITIALIZE EXPERIMENT TRACKING
# ============================================================================
run = wandb.init(
    project="image-classification",
    name=f"resnet18_lr{config['learning_rate']}_bs{config['batch_size']}",
    config=config,
    tags=["baseline", "resnet"],
    notes="Baseline ResNet18 with default hyperparameters"
)

# Update config with any sweep parameters
config = wandb.config

# ============================================================================
# 4. LOG SYSTEM INFO
# ============================================================================
import sys
import torch

system_info = {
    "python_version": sys.version,
    "pytorch_version": torch.__version__,
    "cuda_available": torch.cuda.is_available(),
    "cuda_version": torch.version.cuda if torch.cuda.is_available() else None,
    "gpu_name": torch.cuda.get_device_name(0) if torch.cuda.is_available() else None,
}

wandb.config.update(system_info)

# ============================================================================
# 5. TRAINING LOOP WITH LOGGING
# ============================================================================
def train_epoch(model, train_loader, criterion, optimizer, epoch):
    model.train()
    running_loss = 0.0
    correct = 0
    total = 0

    for batch_idx, (inputs, targets) in enumerate(train_loader):
        inputs, targets = inputs.to(config.device), targets.to(config.device)

        optimizer.zero_grad()
        outputs = model(inputs)
        loss = criterion(outputs, targets)
        loss.backward()
        optimizer.step()

        running_loss += loss.item()
        _, predicted = outputs.max(1)
        total += targets.size(0)
        correct += predicted.eq(targets).sum().item()

        # Log batch metrics
        if batch_idx % config.log_interval == 0:
            wandb.log({
                "batch_loss": loss.item(),
                "batch": epoch * len(train_loader) + batch_idx
            })

    # Return epoch metrics
    epoch_loss = running_loss / len(train_loader)
    epoch_acc = 100. * correct / total
    return epoch_loss, epoch_acc

def validate(model, val_loader, criterion):
    model.eval()
    running_loss = 0.0
    correct = 0
    total = 0

    with torch.no_grad():
        for inputs, targets in val_loader:
            inputs, targets = inputs.to(config.device), targets.to(config.device)
            outputs = model(inputs)
            loss = criterion(outputs, targets)

            running_loss += loss.item()
            _, predicted = outputs.max(1)
            total += targets.size(0)
            correct += predicted.eq(targets).sum().item()

    val_loss = running_loss / len(val_loader)
    val_acc = 100. * correct / total
    return val_loss, val_acc

# Main training loop
best_acc = 0.0

for epoch in range(config.epochs):
    # Train
    train_loss, train_acc = train_epoch(
        model, train_loader, criterion, optimizer, epoch
    )

    # Validate
    val_loss, val_acc = validate(model, val_loader, criterion)

    # Log epoch metrics
    wandb.log({
        "epoch": epoch,
        "train_loss": train_loss,
        "train_accuracy": train_acc,
        "val_loss": val_loss,
        "val_accuracy": val_acc,
        "learning_rate": optimizer.param_groups[0]['lr']
    })

    # Save best model
    if val_acc > best_acc:
        best_acc = val_acc
        torch.save({
            'epoch': epoch,
            'model_state_dict': model.state_dict(),
            'optimizer_state_dict': optimizer.state_dict(),
            'accuracy': best_acc,
        }, 'best_model.pth')

        # Log to W&B
        wandb.save('best_model.pth')
        wandb.run.summary["best_accuracy"] = best_acc
        wandb.run.summary["best_epoch"] = epoch

    # Save checkpoint periodically
    if (epoch + 1) % config.save_checkpoint_interval == 0:
        torch.save({
            'epoch': epoch,
            'model_state_dict': model.state_dict(),
            'optimizer_state_dict': optimizer.state_dict(),
        }, f'checkpoint_epoch_{epoch}.pth')
        wandb.save(f'checkpoint_epoch_{epoch}.pth')

    print(f'Epoch {epoch}: Train Loss: {train_loss:.4f}, Train Acc: {train_acc:.2f}%, '
          f'Val Loss: {val_loss:.4f}, Val Acc: {val_acc:.2f}%')

# ============================================================================
# 6. FINAL EVALUATION AND LOGGING
# ============================================================================
# Load best model
checkpoint = torch.load('best_model.pth')
model.load_state_dict(checkpoint['model_state_dict'])

# Evaluate on test set
test_loss, test_acc = validate(model, test_loader, criterion)

wandb.run.summary["test_accuracy"] = test_acc
wandb.run.summary["test_loss"] = test_loss

# Log confusion matrix
# ... (generate predictions and confusion matrix)
# wandb.log({"confusion_matrix": wandb.plot.confusion_matrix(...)})

# ============================================================================
# 7. FINISH EXPERIMENT
# ============================================================================
wandb.finish()

print(f"\\nTraining completed! Best validation accuracy: {best_acc:.2f}%")
print(f"Test accuracy: {test_acc:.2f}%")
'''

    print(example_code)
    print("\n" + "=" * 80)


if __name__ == "__main__":
    print("EXPERIMENT TRACKING GUIDE FOR MACHINE LEARNING")
    print("=" * 80)
    print("\nWhat would you like to learn about?")
    print("1. Simple experiment tracking (no external tools)")
    print("2. Weights & Biases (W&B) guide")
    print("3. MLflow guide")
    print("4. Best practices")
    print("5. Complete example")
    print("6. Run simple tracking demo")
    print("7. Exit")

    choice = input("\nEnter your choice (1-7): ")

    if choice == "1":
        print("\n" + "=" * 80)
        print("SIMPLE EXPERIMENT TRACKING DEMO")
        print("=" * 80)

        # Demo simple tracker
        tracker = SimpleExperimentTracker()

        tracker.start_experiment(
            name="baseline_model",
            description="Baseline model with default hyperparameters",
            tags=["baseline", "cnn"]
        )

        tracker.log_config({
            "learning_rate": 0.001,
            "batch_size": 32,
            "epochs": 10,
            "architecture": "resnet18"
        })

        # Simulate training
        for epoch in range(10):
            train_loss = 2.0 - epoch * 0.15
            val_loss = 2.0 - epoch * 0.12
            val_acc = 0.5 + epoch * 0.04

            tracker.log_metrics({
                "train_loss": train_loss,
                "val_loss": val_loss,
                "val_accuracy": val_acc
            }, step=epoch)

        tracker.log_artifact("model.pth", "model")
        result = tracker.end_experiment()

        print("\nListing all experiments:")
        experiments = tracker.list_experiments()
        for exp in experiments[:5]:  # Show last 5
            tracker.print_experiment_summary(exp)

    elif choice == "2":
        wandb_tracker = WandBExampleTracker()
        wandb_tracker.setup_guide()
        wandb_tracker.example_usage()
        wandb_tracker.advanced_features()

    elif choice == "3":
        mlflow_tracker = MLflowExampleTracker()
        mlflow_tracker.setup_guide()

    elif choice == "4":
        experiment_tracking_best_practices()

    elif choice == "5":
        complete_example()

    elif choice == "6":
        # Interactive demo
        tracker = SimpleExperimentTracker()

        name = input("Experiment name: ")
        description = input("Description: ")

        tracker.start_experiment(name, description)

        print("\nLog some configurations:")
        lr = input("Learning rate (e.g., 0.001): ")
        batch_size = input("Batch size (e.g., 32): ")

        tracker.log_config({
            "learning_rate": float(lr),
            "batch_size": int(batch_size)
        })

        print("\nSimulating training for 5 epochs...")
        import random
        for epoch in range(5):
            tracker.log_metric("loss", random.uniform(0.1, 2.0), epoch)
            tracker.log_metric("accuracy", random.uniform(0.5, 0.99), epoch)

        tracker.end_experiment()

    else:
        print("Exiting...")
