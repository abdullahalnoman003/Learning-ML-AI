"""
RESEARCH PAPER READING GUIDE
=============================

This guide teaches you how to effectively read research papers using the 3-pass method.
It includes practical examples and templates for summarizing papers.

Author: ML Research Learning Path
"""

import json
from datetime import datetime
from pathlib import Path


class PaperReadingGuide:
    """
    Interactive guide for reading research papers using the proven 3-pass method.

    The 3-Pass Method:
    - Pass 1: Bird's eye view (5-10 minutes)
    - Pass 2: Grasp the content (1 hour)
    - Pass 3: Deep understanding (4-5 hours for beginners)
    """

    def __init__(self):
        self.paper_title = ""
        self.authors = []
        self.venue = ""
        self.year = ""
        self.notes = {
            "pass_1": {},
            "pass_2": {},
            "pass_3": {}
        }

    def display_introduction(self):
        """Display introduction to the 3-pass method."""
        print("=" * 80)
        print("RESEARCH PAPER READING GUIDE - THE 3-PASS METHOD")
        print("=" * 80)
        print("\nReading research papers is a skill that improves with practice.")
        print("The 3-pass method helps you read papers efficiently and effectively.\n")

        print("WHY USE THE 3-PASS METHOD?")
        print("-" * 80)
        print("✓ Prevents wasting time on papers that aren't relevant")
        print("✓ Builds understanding progressively")
        print("✓ Helps you decide when to stop reading")
        print("✓ Improves retention and comprehension")
        print()

    def pass_1_guide(self):
        """Guide for the first pass - quick scan."""
        print("=" * 80)
        print("PASS 1: BIRD'S EYE VIEW (5-10 minutes)")
        print("=" * 80)
        print("\nGOAL: Get a general idea about the paper")
        print("\nSTEPS:")
        print("1. Read the title, abstract, and introduction carefully")
        print("2. Read section and sub-section headings (skip everything else)")
        print("3. Read the conclusions")
        print("4. Glance over references (check which ones you've read)")
        print()

        print("QUESTIONS TO ANSWER:")
        print("-" * 80)
        questions = [
            "1. Category: What type of paper is this?",
            "   - Measurement paper",
            "   - Analysis of existing system",
            "   - Description of research prototype",
            "   - New algorithm/method",
            "   - Survey paper",
            "",
            "2. Context: Which papers is it related to?",
            "   - What related work does it build upon?",
            "",
            "3. Correctness: Do the assumptions appear valid?",
            "   - Are the claims reasonable?",
            "",
            "4. Contributions: What are the paper's main contributions?",
            "   - What problem does it solve?",
            "   - What's novel about the approach?",
            "",
            "5. Clarity: Is the paper well written?",
            "   - Can you understand the main points?",
        ]

        for q in questions:
            print(q)

        print("\nDECISION POINT:")
        print("-" * 80)
        print("After Pass 1, decide:")
        print("• STOP: Paper isn't relevant to your work")
        print("• CONTINUE: Paper is interesting, proceed to Pass 2")
        print("• SAVE: Might be useful later, add to reading list")
        print()

        return {
            "category": "",
            "context": "",
            "correctness": "",
            "contributions": "",
            "clarity": "",
            "decision": ""
        }

    def pass_2_guide(self):
        """Guide for the second pass - deeper reading."""
        print("=" * 80)
        print("PASS 2: GRASP THE CONTENT (Up to 1 hour)")
        print("=" * 80)
        print("\nGOAL: Understand the paper's content (but not all details)")
        print("\nSTEPS:")
        print("1. Read the paper with greater care, but ignore details like proofs")
        print("2. Look carefully at figures, diagrams, and illustrations")
        print("   - Are axes properly labeled?")
        print("   - Are results shown with error bars?")
        print("   - Are conclusions statistically significant?")
        print("3. Mark relevant unread references for further reading")
        print("4. Take notes in margins or separate document")
        print("5. Summarize main thrust with supporting evidence")
        print()

        print("KEY ACTIVITIES:")
        print("-" * 80)
        activities = [
            "• Identify the problem being solved",
            "• Understand the proposed solution/method",
            "• Note the experimental setup",
            "• Examine the results and their interpretation",
            "• Look for strengths and weaknesses",
            "• Note any questions or unclear points",
            "• Mark important figures and tables",
        ]

        for activity in activities:
            print(activity)

        print("\nQUESTIONS TO ANSWER:")
        print("-" * 80)
        questions = [
            "1. Problem: What problem does the paper address?",
            "2. Solution: What is the proposed solution/method?",
            "3. Architecture: What is the model/system architecture?",
            "4. Dataset: What datasets were used?",
            "5. Metrics: How was performance evaluated?",
            "6. Results: What were the main results?",
            "7. Comparison: How does it compare to baselines?",
            "8. Limitations: What are the limitations?",
            "9. Future Work: What future directions are suggested?",
        ]

        for q in questions:
            print(q)

        print("\nDECISION POINT:")
        print("-" * 80)
        print("After Pass 2, you should be able to:")
        print("• Summarize the main contributions")
        print("• Sketch the key ideas and results")
        print("• Decide if you need Pass 3 (deep dive)")
        print()

        return {
            "problem": "",
            "solution": "",
            "architecture": "",
            "dataset": "",
            "metrics": "",
            "results": "",
            "comparison": "",
            "limitations": "",
            "future_work": "",
            "key_figures": []
        }

    def pass_3_guide(self):
        """Guide for the third pass - virtual re-implementation."""
        print("=" * 80)
        print("PASS 3: DEEP UNDERSTANDING (4-5 hours for beginners)")
        print("=" * 80)
        print("\nGOAL: Deeply understand the paper and virtually re-implement it")
        print("\nWHEN TO DO PASS 3:")
        print("• You need to implement the method")
        print("• You're reviewing the paper")
        print("• It's highly relevant to your research")
        print("• You want to deeply understand the technique")
        print()

        print("STEPS:")
        print("-" * 80)
        print("1. Read the paper in detail, understanding every statement")
        print("2. Identify and challenge every assumption")
        print("3. Think about how YOU would present each idea")
        print("4. Compare your mental reconstruction with the actual paper")
        print("5. Note strong and weak points")
        print("6. Identify implicit assumptions and missing citations")
        print("7. Think about potential issues with experimental/analytical techniques")
        print()

        print("VIRTUAL RE-IMPLEMENTATION:")
        print("-" * 80)
        print("Try to mentally (or actually) re-implement the work:")
        print("• Understand each equation and why it's necessary")
        print("• Trace through algorithms step-by-step")
        print("• Understand design decisions and their implications")
        print("• Identify what makes this work novel")
        print("• Think about how to extend or improve it")
        print()

        print("CRITICAL ANALYSIS:")
        print("-" * 80)
        questions = [
            "1. Assumptions: What assumptions are made? Are they valid?",
            "2. Methodology: Is the methodology sound?",
            "3. Evidence: Is there sufficient evidence for the claims?",
            "4. Comparison: Are comparisons fair and comprehensive?",
            "5. Reproducibility: Could you reproduce this work?",
            "6. Innovation: What makes this work novel?",
            "7. Impact: What is the potential impact?",
            "8. Extensions: How could this be extended?",
            "9. Applications: Where else could this be applied?",
            "10. Weaknesses: What are the main weaknesses?",
        ]

        for q in questions:
            print(q)

        print("\nOUTPUT:")
        print("-" * 80)
        print("After Pass 3, you should be able to:")
        print("• Reconstruct the entire structure from memory")
        print("• Identify strong and weak points")
        print("• Pinpoint implicit assumptions and missing citations")
        print("• Suggest improvements or extensions")
        print("• Implement the method if needed")
        print()

        return {
            "assumptions": "",
            "methodology_critique": "",
            "evidence_assessment": "",
            "reproducibility": "",
            "innovation": "",
            "impact": "",
            "extensions": "",
            "weaknesses": "",
            "implementation_notes": ""
        }

    def display_reading_tips(self):
        """Display additional reading tips."""
        print("=" * 80)
        print("ADDITIONAL READING TIPS")
        print("=" * 80)

        print("\nGENERAL TIPS:")
        print("-" * 80)
        tips = [
            "• Don't start reading from beginning to end linearly",
            "• Multiple passes are more efficient than one deep pass",
            "• Take notes and highlight as you read",
            "• Look up unfamiliar terms and concepts",
            "• Draw diagrams to visualize concepts",
            "• Discuss papers with colleagues or study groups",
            "• Read related work to get broader context",
            "• Focus on understanding, not just reading",
        ]

        for tip in tips:
            print(tip)

        print("\nFOR BEGINNERS:")
        print("-" * 80)
        beginner_tips = [
            "• Start with survey papers or tutorials in your field",
            "• Read highly-cited papers (they're usually well-written)",
            "• Don't be discouraged if you don't understand everything",
            "• Build up background knowledge gradually",
            "• Keep a vocabulary list of technical terms",
            "• Read papers from the same authors/groups to see evolution",
        ]

        for tip in beginner_tips:
            print(tip)

        print("\nWHERE TO FIND PAPERS:")
        print("-" * 80)
        sources = [
            "• arXiv.org - Preprints across many fields",
            "• Google Scholar - Search and find citations",
            "• Papers with Code - Papers with code implementations",
            "• Conference websites - NeurIPS, ICML, ICLR, CVPR, etc.",
            "• Semantic Scholar - AI-powered paper search",
            "• Connected Papers - Visual graph of related papers",
        ]

        for source in sources:
            print(source)

        print("\nORGANIZATION:")
        print("-" * 80)
        org_tips = [
            "• Use a reference manager (Zotero, Mendeley, Papers)",
            "• Create a reading list with priorities",
            "• Take structured notes using templates",
            "• Tag papers by topic, method, or relevance",
            "• Keep track of implementation code and datasets",
            "• Write summaries for future reference",
        ]

        for tip in org_tips:
            print(tip)
        print()

    def generate_summary_template(self, paper_info=None):
        """Generate a paper summary template."""
        template = {
            "metadata": {
                "title": paper_info.get("title", "") if paper_info else "",
                "authors": paper_info.get("authors", []) if paper_info else [],
                "venue": paper_info.get("venue", "") if paper_info else "",
                "year": paper_info.get("year", "") if paper_info else "",
                "arxiv_id": paper_info.get("arxiv_id", "") if paper_info else "",
                "pdf_link": paper_info.get("pdf_link", "") if paper_info else "",
                "code_link": paper_info.get("code_link", "") if paper_info else "",
                "date_read": datetime.now().strftime("%Y-%m-%d"),
                "reading_priority": "high/medium/low",
                "tags": ["tag1", "tag2"]
            },

            "pass_1_quick_scan": {
                "category": "What type of paper? (e.g., new method, analysis, survey)",
                "main_contributions": "What are the key contributions?",
                "relevance": "Why is this relevant to your work?",
                "decision": "Continue reading? (yes/no/later)"
            },

            "pass_2_detailed_reading": {
                "problem": "What problem does the paper address?",
                "motivation": "Why is this problem important?",
                "proposed_solution": "What is the proposed solution/method?",
                "key_insights": "What are the key insights or ideas?",
                "architecture": "Describe the model/system architecture",
                "methodology": {
                    "datasets": "What datasets were used?",
                    "baselines": "What methods were compared against?",
                    "metrics": "How was performance evaluated?",
                    "experimental_setup": "Describe the experimental setup"
                },
                "results": {
                    "main_findings": "What were the main results?",
                    "key_figures": ["Figure 1: Description", "Table 2: Description"],
                    "performance": "How does it compare to baselines?"
                },
                "strengths": [
                    "Strength 1",
                    "Strength 2"
                ],
                "weaknesses": [
                    "Weakness 1",
                    "Weakness 2"
                ],
                "limitations": "What limitations are acknowledged?",
                "future_work": "What future directions are suggested?"
            },

            "pass_3_deep_dive": {
                "technical_details": {
                    "key_equations": "Important equations and their meaning",
                    "algorithm_details": "Detailed algorithm description",
                    "design_decisions": "Why were certain design choices made?"
                },
                "critical_analysis": {
                    "assumptions": "What assumptions are made? Are they valid?",
                    "methodology_critique": "Is the methodology sound?",
                    "reproducibility": "Can this be reproduced? What's needed?",
                    "missing_comparisons": "What comparisons are missing?",
                    "questions": [
                        "Question 1",
                        "Question 2"
                    ]
                },
                "innovation": "What makes this work novel?",
                "potential_impact": "What could be the impact of this work?",
                "extensions": [
                    "How could this be extended?",
                    "What are potential applications?"
                ],
                "implementation_notes": "Notes for implementing this method"
            },

            "related_work": {
                "builds_on": ["Paper 1", "Paper 2"],
                "related_papers": ["Paper 3", "Paper 4"],
                "papers_to_read": ["Paper 5", "Paper 6"]
            },

            "personal_notes": {
                "key_takeaways": [
                    "Takeaway 1",
                    "Takeaway 2"
                ],
                "relevance_to_my_work": "How does this relate to my research?",
                "actionable_items": [
                    "Try technique X",
                    "Read paper Y"
                ],
                "questions_for_discussion": [
                    "Question 1",
                    "Question 2"
                ]
            }
        }

        return template

    def save_summary(self, summary, filename=None):
        """Save paper summary to JSON file."""
        if filename is None:
            title = summary["metadata"].get("title", "untitled")
            # Clean filename
            filename = "".join(c if c.isalnum() or c in (' ', '-', '_') else '_' for c in title)
            filename = filename.replace(' ', '_')[:50]  # Limit length
            filename = f"paper_notes/{filename}.json"

        # Create directory if it doesn't exist
        Path(filename).parent.mkdir(parents=True, exist_ok=True)

        with open(filename, 'w') as f:
            json.dump(summary, f, indent=2)

        print(f"Summary saved to: {filename}")
        return filename

    def interactive_guide(self):
        """Run interactive paper reading guide."""
        self.display_introduction()
        input("Press Enter to continue to Pass 1...")

        print("\n")
        self.pass_1_guide()
        input("Press Enter to continue to Pass 2...")

        print("\n")
        self.pass_2_guide()
        input("Press Enter to continue to Pass 3...")

        print("\n")
        self.pass_3_guide()

        print("\n")
        self.display_reading_tips()

        # Ask if user wants to generate a template
        print("\n" + "=" * 80)
        response = input("Would you like to generate a paper summary template? (yes/no): ")

        if response.lower() in ['yes', 'y']:
            print("\nEnter paper information (press Enter to skip):")
            paper_info = {
                "title": input("Title: "),
                "authors": input("Authors (comma-separated): ").split(','),
                "venue": input("Venue (e.g., NeurIPS 2024): "),
                "year": input("Year: "),
                "arxiv_id": input("arXiv ID (if applicable): "),
            }

            template = self.generate_summary_template(paper_info)

            save = input("\nSave template to file? (yes/no): ")
            if save.lower() in ['yes', 'y']:
                self.save_summary(template)
            else:
                print("\nTemplate structure:")
                print(json.dumps(template, indent=2))


def example_paper_summary():
    """
    Example of a completed paper summary.
    This is based on a famous paper: "Attention Is All You Need" (Transformer paper)
    """
    summary = {
        "metadata": {
            "title": "Attention Is All You Need",
            "authors": ["Vaswani et al."],
            "venue": "NeurIPS 2017",
            "year": "2017",
            "arxiv_id": "1706.03762",
            "pdf_link": "https://arxiv.org/pdf/1706.03762.pdf",
            "code_link": "https://github.com/tensorflow/tensor2tensor",
            "date_read": "2024-01-15",
            "reading_priority": "high",
            "tags": ["transformers", "attention", "NLP", "architecture"]
        },

        "pass_1_quick_scan": {
            "category": "New architecture/method",
            "main_contributions": "Introduces Transformer architecture based entirely on attention mechanisms, eliminating recurrence and convolutions",
            "relevance": "Foundational architecture for modern NLP and beyond",
            "decision": "yes - highly influential paper"
        },

        "pass_2_detailed_reading": {
            "problem": "Sequential models (RNNs) are slow to train due to sequential nature; have difficulty with long-range dependencies",
            "motivation": "Need parallelizable architecture that can capture long-range dependencies efficiently",
            "proposed_solution": "Transformer architecture using self-attention mechanisms and positional encodings, fully parallelizable",
            "key_insights": "Self-attention allows modeling dependencies regardless of distance; multi-head attention captures different representation subspaces",
            "architecture": "Encoder-decoder with 6 layers each; each layer has multi-head self-attention and feed-forward networks; residual connections and layer normalization",
            "methodology": {
                "datasets": "WMT 2014 English-German (4.5M pairs) and English-French (36M pairs)",
                "baselines": "RNN/CNN-based models, ByteNet, ConvS2S",
                "metrics": "BLEU score for translation quality",
                "experimental_setup": "Adam optimizer, learning rate schedule, dropout, label smoothing"
            },
            "results": {
                "main_findings": "Achieves 28.4 BLEU on EN-DE (new SOTA), 41.8 on EN-FR; trains much faster than recurrent models",
                "key_figures": [
                    "Table 2: Translation results",
                    "Figure 1: Transformer architecture",
                    "Figure 3: Attention visualizations"
                ],
                "performance": "Outperforms all previous models while being more parallelizable"
            },
            "strengths": [
                "Highly parallelizable - faster training",
                "Better at capturing long-range dependencies",
                "Interpretable attention weights",
                "Strong empirical results"
            ],
            "weaknesses": [
                "Quadratic complexity with sequence length",
                "Requires more data than RNNs",
                "Positional encoding is fixed (not learned)"
            ],
            "limitations": "Computational cost grows quadratically with sequence length",
            "future_work": "Apply to other domains, investigate attention patterns, reduce computational cost"
        },

        "pass_3_deep_dive": {
            "technical_details": {
                "key_equations": "Scaled dot-product attention: Attention(Q,K,V) = softmax(QK^T/sqrt(d_k))V",
                "algorithm_details": "Multi-head attention splits into h heads, processes in parallel, concatenates; positional encoding uses sin/cos functions",
                "design_decisions": "Scaling by sqrt(d_k) prevents softmax saturation; residual connections help training; layer norm stabilizes"
            },
            "critical_analysis": {
                "assumptions": "Assumes positional encoding is sufficient for sequence order; assumes attention is better than recurrence",
                "methodology_critique": "Strong experimental setup; good ablations; could have more analysis on why it works",
                "reproducibility": "Well-described; code available; hyperparameters provided",
                "missing_comparisons": "Could compare memory usage more explicitly",
                "questions": [
                    "Why does scaled dot-product work better than additive attention?",
                    "How sensitive is model to positional encoding choice?"
                ]
            },
            "innovation": "First model to rely entirely on attention; demonstrates attention is sufficient without recurrence",
            "potential_impact": "Huge - has become foundation of modern NLP (BERT, GPT, etc.) and vision (ViT)",
            "extensions": [
                "Apply to other modalities (vision, speech, multimodal)",
                "Reduce quadratic complexity (sparse attention, linear attention)",
                "Learn better positional encodings"
            ],
            "implementation_notes": "Need to implement multi-head attention carefully; masking for decoder; learning rate schedule is important"
        },

        "related_work": {
            "builds_on": [
                "Bahdanau attention mechanism",
                "Residual connections (ResNet)",
                "Layer normalization"
            ],
            "related_papers": [
                "BERT (applies Transformer encoder)",
                "GPT (applies Transformer decoder)",
                "Transformer-XL (extends to longer sequences)"
            ],
            "papers_to_read": [
                "BERT: Pre-training of Deep Bidirectional Transformers",
                "GPT-3: Language Models are Few-Shot Learners",
                "Reformer: The Efficient Transformer"
            ]
        },

        "personal_notes": {
            "key_takeaways": [
                "Attention mechanisms are powerful and sufficient for sequence modeling",
                "Parallelization is key to scaling deep learning",
                "Simple ideas (attention, residual connections) can be combined powerfully"
            ],
            "relevance_to_my_work": "Fundamental architecture to understand for any modern NLP work",
            "actionable_items": [
                "Implement Transformer from scratch",
                "Experiment with attention visualizations",
                "Read follow-up papers (BERT, GPT)"
            ],
            "questions_for_discussion": [
                "How can we reduce the quadratic complexity?",
                "What makes attention so effective compared to recurrence?"
            ]
        }
    }

    return summary


def quick_start_guide():
    """Quick start guide for reading papers."""
    print("=" * 80)
    print("QUICK START GUIDE FOR READING RESEARCH PAPERS")
    print("=" * 80)
    print("\n1. FOR YOUR FIRST PAPER:")
    print("   - Start with a survey paper or tutorial in your field")
    print("   - Choose a highly-cited, well-written paper")
    print("   - Don't aim for 100% understanding on first read")
    print()
    print("2. USE THE 3-PASS METHOD:")
    print("   - Pass 1: Quick scan (5-10 min) - Decide if relevant")
    print("   - Pass 2: Detailed read (1 hour) - Understand main ideas")
    print("   - Pass 3: Deep dive (4-5 hours) - Virtual re-implementation")
    print()
    print("3. TAKE NOTES:")
    print("   - Use the provided template structure")
    print("   - Focus on: problem, solution, results, strengths/weaknesses")
    print("   - Note questions and unclear points")
    print()
    print("4. PRACTICE REGULARLY:")
    print("   - Start with 1-2 papers per week")
    print("   - Gradually increase as you get faster")
    print("   - Discuss papers with others")
    print()
    print("5. BUILD A READING LIST:")
    print("   - Track papers to read (use priority levels)")
    print("   - Follow citations backward and forward")
    print("   - Use tools like Connected Papers for discovery")
    print("=" * 80)


if __name__ == "__main__":
    print("RESEARCH PAPER READING GUIDE")
    print("=" * 80)
    print("\nWhat would you like to do?")
    print("1. Interactive 3-pass method guide")
    print("2. Generate paper summary template")
    print("3. View example paper summary")
    print("4. View quick start guide")
    print("5. Exit")

    choice = input("\nEnter your choice (1-5): ")

    guide = PaperReadingGuide()

    if choice == "1":
        guide.interactive_guide()
    elif choice == "2":
        print("\nEnter paper information (press Enter to skip):")
        paper_info = {
            "title": input("Title: "),
            "authors": input("Authors (comma-separated): ").split(',') if input else [],
            "venue": input("Venue: "),
            "year": input("Year: "),
        }
        template = guide.generate_summary_template(paper_info)
        print("\n" + json.dumps(template, indent=2))

        save = input("\nSave to file? (yes/no): ")
        if save.lower() in ['yes', 'y']:
            guide.save_summary(template)
    elif choice == "3":
        example = example_paper_summary()
        print("\n" + json.dumps(example, indent=2))
    elif choice == "4":
        quick_start_guide()
    else:
        print("Exiting...")
