# Week 04 · Day 21 PM — Part D: AI-Augmented Task (Evaluation)

Code is in `PM_PartD_Code.py`.

## Prompt
"Explain regression vs classification and bias-variance tradeoff with Python
examples and visualizations."
Model: Claude (claude-sonnet-4-6)

## Critical Evaluation

**Are explanations correct?**
Yes. Regression uses covariance-based weight estimation (correct). Classification
threshold logic is sound. Bias-variance table correctly shows training MSE falling
monotonically with degree.

**Do visualisations correctly show underfitting and overfitting?**
No — the AI produced text output only, not matplotlib plots. The table communicates
the trend but a plot would make the U-shaped test error curve immediately obvious.
This is the main gap.

**What I improved:**
Added a train/test split (35 train, 15 test). Now test MSE rises after degree 5
even as train MSE keeps falling — overfitting becomes numerically visible without
needing a plot. Full visualisation would require matplotlib (not in scope here).
