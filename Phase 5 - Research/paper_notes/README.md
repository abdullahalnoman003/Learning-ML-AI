# Paper Notes

This directory contains summaries and notes from research papers you've read.

## Organization

Papers are organized by topic and can be in either Markdown (`.md`) or JSON (`.json`) format.

### Suggested Folder Structure:
```
paper_notes/
├── computer_vision/
│   ├── transformers/
│   ├── object_detection/
│   └── image_generation/
├── natural_language_processing/
│   ├── language_models/
│   ├── machine_translation/
│   └── question_answering/
├── reinforcement_learning/
├── general_ml/
└── to_read.md          # Reading list
```

## Paper Summary Template

For each paper, create a file using this template:

---

# [Paper Title]

**Authors:** Author names
**Venue:** Conference/Journal, Year
**Links:** [Paper](url) | [Code](url) | [Project Page](url)
**Date Read:** YYYY-MM-DD
**Tags:** #tag1 #tag2 #tag3
**Priority:** High / Medium / Low
**Status:**  Read /  Reading /  To Read

---

## Quick Summary (TL;DR)

One paragraph summary of the paper's main contribution and findings.

---

## Pass 1: Quick Scan (5-10 minutes)

### Category
- [ ] Measurement paper
- [ ] Analysis of existing system
- [ ] Research prototype description
- [ ] New algorithm/method
- [ ] Survey paper
- [ ] Other: ___________

### Main Contributions
1. Contribution 1
2. Contribution 2
3. Contribution 3

### Relevance to My Work
Why is this paper relevant? What can I learn from it?

### Decision
- [ ] Continue reading (Pass 2)
- [ ] Save for later
- [ ] Not relevant

---

## Pass 2: Detailed Reading (1 hour)

### Problem Statement
What problem does the paper address? Why is it important?

### Motivation
What are the limitations of existing approaches?

### Proposed Solution
High-level description of the proposed method/approach.

### Key Insights
What are the key ideas or insights that make this work?

### Architecture/Method Details
Describe the model architecture or methodology.

### Datasets & Experimental Setup
- **Datasets:** Dataset names and sizes
- **Baselines:** Methods compared against
- **Metrics:** Evaluation metrics used
- **Implementation:** Framework, hardware, training details

### Results
#### Main Findings
Key quantitative and qualitative results.

#### Performance Comparison
How does it compare to baselines?

| Method | Metric 1 | Metric 2 | Metric 3 |
|--------|----------|----------|----------|
| Baseline 1 | | | |
| Baseline 2 | | | |
| **This Paper** | | | |

#### Key Figures/Tables
- Figure 1: Description
- Table 2: Description

### Strengths
1. Strength 1
2. Strength 2
3. Strength 3

### Weaknesses
1. Weakness 1
2. Weakness 2
3. Weakness 3

### Limitations
What limitations are acknowledged by the authors?

### Future Work
What future directions do the authors suggest?

---

## Pass 3: Deep Understanding (4-5 hours) [Optional]

### Technical Details
#### Key Equations
Important equations and their explanations.

```
Equation 1: Description
```

#### Algorithm Walkthrough
Step-by-step explanation of the algorithm.

#### Design Decisions
Why were certain design choices made?

### Critical Analysis
#### Assumptions
What assumptions are made? Are they valid?

#### Methodology Critique
Is the methodology sound? Any concerns?

#### Evidence Assessment
Is there sufficient evidence for the claims?

#### Reproducibility
Can this work be reproduced? What's needed?

### Innovation & Impact
#### What Makes This Novel?
What distinguishes this from prior work?

#### Potential Impact
What could be the impact of this work?

#### Possible Extensions
How could this work be extended or improved?

#### Applications
Where else could this method be applied?

### Implementation Notes
Notes for implementing this method:
- Key implementation details
- Potential pitfalls
- Tricks and best practices

---

## Related Work

### Builds Upon
Papers this work directly builds on:
1. [Paper 1](url) - How it relates
2. [Paper 2](url) - How it relates

### Related Papers
Other relevant papers:
1. [Paper 3](url) - Brief description
2. [Paper 4](url) - Brief description

### Papers to Read Next
Papers referenced that I should read:
- [ ] Paper 5 - Why read this
- [ ] Paper 6 - Why read this

---

## Personal Notes

### Key Takeaways
1. Takeaway 1
2. Takeaway 2
3. Takeaway 3

### Relevance to My Research
How does this relate to my current/future research?

### Actionable Items
- [ ] Try technique X in my project
- [ ] Implement the proposed method
- [ ] Compare with my baseline
- [ ] Read related paper Y

### Questions
1. Question about unclear aspect
2. Question for potential discussion
3. Question about extension

### Code/Implementation
- **Official Code:** [Link](url) - Notes on code quality
- **Unofficial Implementations:** [Link](url)
- **My Implementation:** [Link](url) - Status and notes

---

## Discussion & Updates

### Initial Thoughts (Date)
My first impressions after Pass 2.

### After Implementation (Date)
What I learned from implementing/using this method.

### Community Feedback
Interesting discussions from conferences, social media, etc.

---

## Citation

```bibtex
@inproceedings{authorYYYY,
  title={Paper Title},
  author={Author Names},
  booktitle={Conference/Journal},
  year={YYYY}
}
```

---

## Example Paper Notes

See `example_attention_is_all_you_need.md` for a complete example of filled-out paper notes.

---

## Tips for Effective Note-Taking

1. **Be Consistent:** Use the same template for all papers
2. **Be Honest:** Note what you don't understand
3. **Be Critical:** Question assumptions and claims
4. **Be Practical:** Focus on actionable insights
5. **Be Connected:** Link to related papers
6. **Be Updated:** Add notes as you learn more
7. **Use Tags:** Makes searching easier
8. **Add Visuals:** Screenshots of important figures
9. **Track Status:** Mark what you've read vs. to-read
10. **Review Regularly:** Revisit notes periodically

---

## JSON Format Alternative

If you prefer structured data, use JSON format (see `paper_reading_guide.py` for template generation):

```json
{
  "metadata": {
    "title": "Paper Title",
    "authors": ["Author 1", "Author 2"],
    "venue": "Conference YYYY",
    "tags": ["tag1", "tag2"]
  },
  "pass_1": {...},
  "pass_2": {...},
  "pass_3": {...}
}
```

Generate JSON templates using:
```bash
python paper_reading_guide.py
```

---

## Reading List

Maintain a `to_read.md` file with papers you plan to read:

### High Priority
- [ ] Paper 1 - Why important
- [ ] Paper 2 - Why important

### Medium Priority
- [ ] Paper 3
- [ ] Paper 4

### Low Priority / Reference
- [ ] Paper 5
- [ ] Paper 6

---

## Review Schedule

- **Daily:** Spend 30-60 minutes reading papers
- **Weekly:** Summarize 1-2 papers in detail
- **Monthly:** Review all notes, identify patterns
- **Before Project:** Read 5-10 related papers thoroughly

---

## Resources

- **Paper Search:** [arXiv](https://arxiv.org/), [Google Scholar](https://scholar.google.com/), [Semantic Scholar](https://www.semanticscholar.org/)
- **Connected Papers:** [Visual graph of related papers](https://www.connectedpapers.com/)
- **Papers with Code:** [Papers with implementations](https://paperswithcode.com/)
- **Reference Managers:** Zotero, Mendeley, Papers
