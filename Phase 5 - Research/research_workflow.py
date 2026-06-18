"""
RESEARCH WORKFLOW GUIDE
=======================

Complete workflow for conducting ML research, reproducing papers,
and running experiments systematically.

Author: ML Research Learning Path
"""

import json
import os
from datetime import datetime
from pathlib import Path


class ResearchWorkflow:
    """
    Guide for systematic research workflow in machine learning.
    """

    def __init__(self):
        self.project_name = ""
        self.research_log = []

    def introduction(self):
        """Introduction to research workflow."""
        print("=" * 80)
        print("MACHINE LEARNING RESEARCH WORKFLOW")
        print("=" * 80)
        print("\nThis guide covers the complete workflow for:")
        print("• Conducting original research")
        print("• Reproducing published papers")
        print("• Running systematic experiments")
        print("• Documenting and sharing results")
        print()

        print("KEY PRINCIPLES:")
        print("-" * 80)
        principles = [
            "1. Reproducibility: Every result should be reproducible",
            "2. Systematicity: Follow a consistent process",
            "3. Documentation: Record everything (code, data, results, decisions)",
            "4. Iteration: Research is iterative, not linear",
            "5. Validation: Always validate claims rigorously",
            "6. Collaboration: Share findings and learn from others"
        ]
        for principle in principles:
            print(principle)
        print()

    def research_project_workflow(self):
        """Complete research project workflow."""
        print("=" * 80)
        print("RESEARCH PROJECT WORKFLOW")
        print("=" * 80)

        phases = [
            {
                "phase": "PHASE 1: PROBLEM FORMULATION",
                "duration": "1-2 weeks",
                "description": "Define the research question and scope",
                "tasks": [
                    "1. Identify the problem:",
                    "   • What specific problem are you solving?",
                    "   • Why is it important?",
                    "   • What's the impact if solved?",
                    "",
                    "2. Literature review:",
                    "   • Read related papers (use paper reading guide)",
                    "   • Identify gaps in existing work",
                    "   • Find datasets and benchmarks",
                    "   • Understand state-of-the-art methods",
                    "",
                    "3. Define research question:",
                    "   • Formulate specific, testable hypothesis",
                    "   • Define success criteria",
                    "   • Identify constraints (compute, data, time)",
                    "",
                    "4. Create research proposal:",
                    "   • Problem statement",
                    "   • Proposed approach",
                    "   • Expected contributions",
                    "   • Experimental plan"
                ]
            },
            {
                "phase": "PHASE 2: SETUP & BASELINES",
                "duration": "1-2 weeks",
                "description": "Set up infrastructure and establish baselines",
                "tasks": [
                    "1. Environment setup:",
                    "   • Set up development environment",
                    "   • Install required libraries",
                    "   • Configure experiment tracking",
                    "   • Set up version control (git)",
                    "",
                    "2. Data preparation:",
                    "   • Collect/download datasets",
                    "   • Exploratory data analysis",
                    "   • Create train/val/test splits",
                    "   • Set up data loading pipelines",
                    "   • Document data characteristics",
                    "",
                    "3. Implement baselines:",
                    "   • Simple baseline (e.g., random, mean)",
                    "   • Standard baseline (e.g., logistic regression)",
                    "   • State-of-the-art baseline (reproduce paper)",
                    "   • Establish evaluation metrics",
                    "",
                    "4. Validation strategy:",
                    "   • Define cross-validation approach",
                    "   • Set up evaluation pipeline",
                    "   • Verify baselines match reported results"
                ]
            },
            {
                "phase": "PHASE 3: EXPERIMENTATION",
                "duration": "4-8 weeks",
                "description": "Run experiments and test hypotheses",
                "tasks": [
                    "1. Hypothesis-driven experiments:",
                    "   • Test one hypothesis at a time",
                    "   • Design controlled experiments",
                    "   • Track all hyperparameters",
                    "   • Use consistent evaluation",
                    "",
                    "2. Systematic exploration:",
                    "   • Ablation studies (remove components)",
                    "   • Hyperparameter tuning",
                    "   • Architecture variations",
                    "   • Different training strategies",
                    "",
                    "3. Document everything:",
                    "   • Log all experiments (use experiment tracking)",
                    "   • Record failures and successes",
                    "   • Note unexpected behaviors",
                    "   • Keep research journal",
                    "",
                    "4. Analyze results:",
                    "   • Compare against baselines",
                    "   • Statistical significance testing",
                    "   • Visualize learning curves",
                    "   • Error analysis"
                ]
            },
            {
                "phase": "PHASE 4: REFINEMENT",
                "duration": "2-4 weeks",
                "description": "Refine approach and validate thoroughly",
                "tasks": [
                    "1. Refine best approach:",
                    "   • Optimize hyperparameters",
                    "   • Fix bugs and issues",
                    "   • Improve training stability",
                    "   • Reduce computational cost",
                    "",
                    "2. Comprehensive evaluation:",
                    "   • Multiple random seeds",
                    "   • Different data splits",
                    "   • Various metrics",
                    "   • Comparison with multiple baselines",
                    "",
                    "3. Ablation studies:",
                    "   • What components are essential?",
                    "   • Sensitivity to hyperparameters",
                    "   • Failure case analysis",
                    "",
                    "4. Reproducibility check:",
                    "   • Clean up code",
                    "   • Document dependencies",
                    "   • Verify results can be reproduced",
                    "   • Create reproducibility script"
                ]
            },
            {
                "phase": "PHASE 5: DOCUMENTATION & WRITING",
                "duration": "2-4 weeks",
                "description": "Document findings and write paper/report",
                "tasks": [
                    "1. Organize results:",
                    "   • Select best results to present",
                    "   • Create figures and tables",
                    "   • Write clear captions",
                    "   • Prepare visualizations",
                    "",
                    "2. Write paper/report:",
                    "   • Abstract (last)",
                    "   • Introduction (motivation, contributions)",
                    "   • Related work",
                    "   • Method description",
                    "   • Experimental setup",
                    "   • Results and analysis",
                    "   • Conclusion and future work",
                    "",
                    "3. Code release:",
                    "   • Clean up code",
                    "   • Write README with instructions",
                    "   • Add examples and demos",
                    "   • Create requirements.txt",
                    "   • Publish on GitHub",
                    "",
                    "4. Review and iterate:",
                    "   • Self-review critically",
                    "   • Get feedback from colleagues",
                    "   • Revise based on feedback",
                    "   • Proofread carefully"
                ]
            },
            {
                "phase": "PHASE 6: SUBMISSION & SHARING",
                "duration": "Ongoing",
                "description": "Submit and share your work",
                "tasks": [
                    "1. Choose venue:",
                    "   • Conference (NeurIPS, ICML, ICLR, CVPR, etc.)",
                    "   • Workshop",
                    "   • Journal",
                    "   • arXiv preprint",
                    "",
                    "2. Submit:",
                    "   • Follow formatting guidelines",
                    "   • Prepare supplementary materials",
                    "   • Submit on time",
                    "",
                    "3. Share:",
                    "   • Post on arXiv",
                    "   • Share on Twitter/LinkedIn",
                    "   • Write blog post",
                    "   • Present at lab meetings",
                    "",
                    "4. Respond to reviews:",
                    "   • Take feedback constructively",
                    "   • Run additional experiments if needed",
                    "   • Revise paper",
                    "   • Resubmit"
                ]
            }
        ]

        for phase_info in phases:
            print(f"\n{phase_info['phase']}")
            print(f"Duration: {phase_info['duration']}")
            print(f"Goal: {phase_info['description']}")
            print("-" * 80)
            for task in phase_info['tasks']:
                print(task)

        print("\n" + "=" * 80)

    def paper_reproduction_workflow(self):
        """Workflow for reproducing research papers."""
        print("=" * 80)
        print("PAPER REPRODUCTION WORKFLOW")
        print("=" * 80)
        print("\nReproducing papers is crucial for:")
        print("• Understanding the method deeply")
        print("• Verifying claims")
        print("• Building on existing work")
        print("• Learning implementation details")
        print()

        steps = [
            {
                "step": "1. UNDERSTAND THE PAPER",
                "details": [
                    "• Read paper thoroughly (use 3-pass method)",
                    "• Understand the problem and motivation",
                    "• Identify key contributions",
                    "• Note all architectural details",
                    "• Understand training procedure",
                    "• List all hyperparameters",
                    "• Check supplementary materials"
                ]
            },
            {
                "step": "2. GATHER RESOURCES",
                "details": [
                    "• Check if official code is available",
                    "• Look for unofficial implementations",
                    "• Find the datasets used",
                    "• Identify required compute resources",
                    "• Check library versions used",
                    "• Look for related discussions/issues"
                ]
            },
            {
                "step": "3. START WITH OFFICIAL CODE (if available)",
                "details": [
                    "• Clone official repository",
                    "• Read README and documentation",
                    "• Install dependencies",
                    "• Download data/pretrained models",
                    "• Run provided scripts",
                    "• Verify you can reproduce reported results",
                    "• Study code to understand implementation"
                ]
            },
            {
                "step": "4. IMPLEMENT FROM SCRATCH (if no code)",
                "details": [
                    "• Set up project structure",
                    "• Implement data loading first",
                    "• Implement model architecture",
                    "• Implement loss function",
                    "• Implement training loop",
                    "• Implement evaluation",
                    "• Add logging and checkpointing"
                ]
            },
            {
                "step": "5. DEBUG AND VALIDATE",
                "details": [
                    "• Test each component individually",
                    "• Verify model forward pass",
                    "• Check loss computation",
                    "• Validate gradients",
                    "• Test on small data first",
                    "• Compare intermediate outputs (if possible)",
                    "• Check for common bugs (learning rate, initialization, etc.)"
                ]
            },
            {
                "step": "6. REPRODUCE RESULTS",
                "details": [
                    "• Use exact hyperparameters from paper",
                    "• Match training procedure exactly",
                    "• Use same evaluation protocol",
                    "• Run multiple seeds if possible",
                    "• Compare results with paper",
                    "• Analyze discrepancies if any"
                ]
            },
            {
                "step": "7. DOCUMENT REPRODUCTION",
                "details": [
                    "• Record all implementation details",
                    "• Note any ambiguities in paper",
                    "• Document differences from paper",
                    "• Track compute time and resources",
                    "• Create comparison table",
                    "• Write reproduction report"
                ]
            },
            {
                "step": "8. EXTEND (optional)",
                "details": [
                    "• Try on different datasets",
                    "• Test different hyperparameters",
                    "• Implement suggested improvements",
                    "• Compare with other methods",
                    "• Analyze failure cases",
                    "• Propose improvements"
                ]
            }
        ]

        for step_info in steps:
            print(f"\n{step_info['step']}")
            print("-" * 80)
            for detail in step_info['details']:
                print(detail)

        print("\n" + "=" * 80)
        print("\nCOMMON CHALLENGES IN REPRODUCTION:")
        print("-" * 80)
        challenges = [
            "• Missing hyperparameters in paper",
            "• Ambiguous description of method",
            "• Different library versions",
            "• Insufficient compute resources",
            "• Data not publicly available",
            "• Random seed not specified",
            "• Implementation tricks not mentioned",
            "• Bugs in official code"
        ]
        for challenge in challenges:
            print(challenge)

        print("\nTIPS FOR SUCCESSFUL REPRODUCTION:")
        print("-" * 80)
        tips = [
            "• Start with official code when available",
            "• Contact authors if stuck (politely!)",
            "• Check GitHub issues/discussions",
            "• Look for unofficial implementations",
            "• Start with smaller experiments first",
            "• Document everything you try",
            "• Be patient - reproduction takes time",
            "• Share your reproduction attempt (helps community)"
        ]
        for tip in tips:
            print(tip)

        print("\n" + "=" * 80)

    def experiment_design_guide(self):
        """Guide for designing good experiments."""
        print("=" * 80)
        print("EXPERIMENT DESIGN GUIDE")
        print("=" * 80)

        print("\n1. CONTROLLED EXPERIMENTS:")
        print("-" * 80)
        print("Change one variable at a time to understand its effect.")
        print()
        print("Example: Testing learning rate")
        print("  • Keep everything else constant")
        print("  • Try: [0.0001, 0.0005, 0.001, 0.005, 0.01]")
        print("  • Use same random seed")
        print("  • Plot results")
        print()

        print("2. ABLATION STUDIES:")
        print("-" * 80)
        print("Remove components to understand their contribution.")
        print()
        ablation_example = '''
Example: Analyzing a model with multiple components

Full model: Attention + Residual + LayerNorm + Dropout
Ablations:
  1. Remove Attention      → See if attention is necessary
  2. Remove Residual       → See if residual connections help
  3. Remove LayerNorm      → See if normalization is crucial
  4. Remove Dropout        → See if regularization helps
  5. Remove multiple       → Test interactions
'''
        print(ablation_example)

        print("3. HYPERPARAMETER TUNING:")
        print("-" * 80)
        tuning_strategies = '''
Strategy 1: Grid Search
  • Define range for each hyperparameter
  • Try all combinations
  • Expensive but thorough

Strategy 2: Random Search
  • Sample random combinations
  • Often better than grid search
  • More efficient exploration

Strategy 3: Bayesian Optimization
  • Use previous results to guide search
  • More sample-efficient
  • Tools: Optuna, Ray Tune, Weights & Biases Sweeps

Strategy 4: Manual Tuning
  • Start with reasonable defaults
  • Tune most important parameters first
  • Learning rate → batch size → architecture → regularization
'''
        print(tuning_strategies)

        print("4. STATISTICAL VALIDITY:")
        print("-" * 80)
        statistical_tips = [
            "• Run multiple random seeds (at least 3-5)",
            "• Report mean and standard deviation",
            "• Use statistical significance tests",
            "• Consider confidence intervals",
            "• Be wary of cherry-picking results",
            "• Account for multiple comparisons"
        ]
        for tip in statistical_tips:
            print(tip)

        print("\n5. BASELINE COMPARISONS:")
        print("-" * 80)
        print("Always compare against appropriate baselines:")
        baseline_types = [
            "• Random baseline: Random predictions",
            "• Simple baseline: Simple model (logistic regression, k-NN)",
            "• Standard baseline: Well-known method in the field",
            "• SOTA baseline: Current state-of-the-art",
            "• Oracle baseline: Upper bound (human performance, etc.)"
        ]
        for baseline in baseline_types:
            print(baseline)

        print("\n6. EVALUATION BEST PRACTICES:")
        print("-" * 80)
        eval_tips = [
            "• Use multiple metrics (don't rely on single metric)",
            "• Test on held-out test set (don't use for development)",
            "• Check for overfitting (compare train vs validation)",
            "• Analyze failure cases",
            "• Visualize predictions",
            "• Check robustness (different data, perturbations)"
        ]
        for tip in eval_tips:
            print(tip)

        print("\n" + "=" * 80)

    def research_tools_and_practices(self):
        """Essential tools and practices for research."""
        print("=" * 80)
        print("RESEARCH TOOLS & PRACTICES")
        print("=" * 80)

        print("\n1. VERSION CONTROL (Git):")
        print("-" * 80)
        git_workflow = '''
# Initialize repository
git init
git remote add origin <url>

# Create branch for experiment
git checkout -b experiment/attention-mechanism

# Make changes and commit
git add .
git commit -m "Add attention mechanism"

# Push to remote
git push origin experiment/attention-mechanism

# Best practices:
• Commit frequently with clear messages
• Use branches for experiments
• Tag important commits (paper submissions, releases)
• Never commit large files (use Git LFS or .gitignore)
• Include git commit hash in experiment logs
'''
        print(git_workflow)

        print("\n2. EXPERIMENT TRACKING:")
        print("-" * 80)
        print("Tools:")
        print("  • Weights & Biases (wandb): Cloud-based, great visualizations")
        print("  • MLflow: Open-source, self-hosted")
        print("  • TensorBoard: Built into PyTorch/TensorFlow")
        print("  • Custom logging: JSON files (see experiment_tracking.py)")
        print()
        print("What to track:")
        print("  • Hyperparameters")
        print("  • Metrics (every epoch)")
        print("  • Model checkpoints")
        print("  • System info (GPU, libraries)")
        print("  • Code version (git commit)")
        print("  • Dataset version")
        print("  • Training time")

        print("\n3. ENVIRONMENT MANAGEMENT:")
        print("-" * 80)
        env_example = '''
# Option 1: conda
conda create -n research python=3.9
conda activate research
pip install -r requirements.txt

# Option 2: venv
python -m venv research_env
source research_env/bin/activate  # Linux/Mac
research_env\\Scripts\\activate  # Windows
pip install -r requirements.txt

# Option 3: Docker
docker build -t my-research .
docker run --gpus all -v $(pwd):/workspace my-research

# Export environment
pip freeze > requirements.txt
conda env export > environment.yml
'''
        print(env_example)

        print("\n4. CODE ORGANIZATION:")
        print("-" * 80)
        structure = '''
research-project/
│
├── README.md                 # Project overview
├── requirements.txt          # Dependencies
├── setup.py                  # Installation script
│
├── data/                     # Data (not committed)
│   ├── raw/
│   ├── processed/
│   └── README.md            # Data description
│
├── notebooks/               # Jupyter notebooks
│   ├── 01_eda.ipynb
│   ├── 02_experiments.ipynb
│   └── figures/            # Generated figures
│
├── src/                    # Source code
│   ├── __init__.py
│   ├── data.py            # Data loading
│   ├── models.py          # Model definitions
│   ├── train.py           # Training code
│   ├── evaluate.py        # Evaluation code
│   └── utils.py           # Utilities
│
├── scripts/               # Executable scripts
│   ├── train.sh
│   ├── evaluate.sh
│   └── reproduce.sh      # Reproduction script
│
├── experiments/          # Experiment logs
│   └── README.md
│
├── models/              # Saved models
│   └── .gitkeep
│
├── paper/              # Paper writing
│   ├── paper.tex
│   ├── references.bib
│   └── figures/
│
└── tests/             # Unit tests
    ├── test_data.py
    ├── test_models.py
    └── test_utils.py
'''
        print(structure)

        print("\n5. DOCUMENTATION:")
        print("-" * 80)
        doc_tips = [
            "• README: Clear instructions to reproduce results",
            "• Docstrings: Document functions and classes",
            "• Comments: Explain complex logic",
            "• Research log: Daily notes on experiments",
            "• Paper notes: Summaries of papers read",
            "• Meeting notes: Discussions with advisors/collaborators"
        ]
        for tip in doc_tips:
            print(tip)

        print("\n6. COMPUTE RESOURCES:")
        print("-" * 80)
        compute_options = [
            "• Local: Your own GPU",
            "• University: Lab cluster",
            "• Kaggle: Free GPU/TPU (30-40 hrs/week)",
            "• Google Colab: Free GPU (limited hours)",
            "• Cloud: AWS, GCP, Azure (paid)",
            "• Academic: Apply for research credits",
            "• Paperspace Gradient: Paid GPU access"
        ]
        for option in compute_options:
            print(option)

        print("\n7. COLLABORATION:")
        print("-" * 80)
        collab_tips = [
            "• Use shared GitHub repository",
            "• Document decisions in issues/discussions",
            "• Regular meetings to sync",
            "• Share experiment results (W&B teams)",
            "• Code review before merging",
            "• Consistent coding style",
            "• Clear division of tasks"
        ]
        for tip in collab_tips:
            print(tip)

        print("\n" + "=" * 80)

    def research_best_practices(self):
        """Best practices for ML research."""
        print("=" * 80)
        print("RESEARCH BEST PRACTICES")
        print("=" * 80)

        print("\n1. REPRODUCIBILITY:")
        print("-" * 80)
        repro_checklist = [
            " Set random seeds (Python, NumPy, PyTorch, etc.)",
            " Document library versions",
            " Save all hyperparameters",
            " Version your data",
            " Save model checkpoints",
            " Document hardware used",
            " Provide reproduction script",
            " Share code publicly"
        ]
        for item in repro_checklist:
            print(item)

        print("\n2. EXPERIMENT HYGIENE:")
        print("-" * 80)
        hygiene_tips = [
            "• One experiment = one hypothesis",
            "• Document before running (what you expect)",
            "• Don't change multiple things at once",
            "• Keep experiment log updated",
            "• Archive failed experiments (learn from failures)",
            "• Regular code reviews",
            "• Clean up code periodically"
        ]
        for tip in hygiene_tips:
            print(tip)

        print("\n3. TIME MANAGEMENT:")
        print("-" * 80)
        time_tips = [
            "• Set milestones and deadlines",
            "• Don't get stuck on one approach",
            "• Time-box experiments (1 week per major idea)",
            "• Balance exploration vs exploitation",
            "• Start writing early (helps clarify thinking)",
            "• Regular progress updates",
            "• Know when to move on"
        ]
        for tip in time_tips:
            print(tip)

        print("\n4. SCIENTIFIC RIGOR:")
        print("-" * 80)
        rigor_tips = [
            "• Be skeptical of surprising results",
            "• Verify claims with multiple experiments",
            "• Report negative results honestly",
            "• Don't cherry-pick results",
            "• Use appropriate statistical tests",
            "• Be transparent about limitations",
            "• Replicate important findings"
        ]
        for tip in rigor_tips:
            print(tip)

        print("\n5. LEARNING AND GROWTH:")
        print("-" * 80)
        learning_tips = [
            "• Read papers regularly (1-2 per week)",
            "• Attend seminars and conferences",
            "• Reproduce important papers",
            "• Implement algorithms from scratch",
            "• Participate in study groups",
            "• Write blog posts (best way to learn)",
            "• Seek feedback on your work"
        ]
        for tip in learning_tips:
            print(tip)

        print("\n6. COMMON PITFALLS TO AVOID:")
        print("-" * 80)
        pitfalls = [
            "• Not reading related work thoroughly",
            "• Overfitting to validation set",
            "• Bugs in evaluation code",
            "• Not using proper baselines",
            "• Claiming novelty without evidence",
            "• Poor experimental design",
            "• Not documenting experiments",
            "• Waiting too long to start writing"
        ]
        for pitfall in pitfalls:
            print(pitfall)

        print("\n" + "=" * 80)


def main():
    """Main function."""
    workflow = ResearchWorkflow()

    print("=" * 80)
    print("RESEARCH WORKFLOW GUIDE")
    print("=" * 80)
    print("\nWhat would you like to learn?")
    print("1. Research project workflow")
    print("2. Paper reproduction workflow")
    print("3. Experiment design guide")
    print("4. Research tools and practices")
    print("5. Research best practices")
    print("6. View complete guide")
    print("7. Exit")

    choice = input("\nEnter your choice (1-7): ")

    if choice == "1":
        workflow.introduction()
        workflow.research_project_workflow()
    elif choice == "2":
        workflow.paper_reproduction_workflow()
    elif choice == "3":
        workflow.experiment_design_guide()
    elif choice == "4":
        workflow.research_tools_and_practices()
    elif choice == "5":
        workflow.research_best_practices()
    elif choice == "6":
        workflow.introduction()
        input("\nPress Enter to continue...")
        workflow.research_project_workflow()
        input("\nPress Enter to continue...")
        workflow.paper_reproduction_workflow()
        input("\nPress Enter to continue...")
        workflow.experiment_design_guide()
        input("\nPress Enter to continue...")
        workflow.research_tools_and_practices()
        input("\nPress Enter to continue...")
        workflow.research_best_practices()
    else:
        print("Exiting...")


if __name__ == "__main__":
    main()
