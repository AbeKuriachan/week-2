# Week 04 · Day 21 PM — Part B: Bias-Variance Tradeoff (Written)

Code is in `PM_PartB_StretchProblem.py`.

## What is Bias?

Bias is error from a model too simple to capture the true pattern. A degree-1
line fitted to a sine curve will always be systematically wrong regardless of
how much data you give it. This is underfitting.

High bias → model assumptions too restrictive → systematic, predictable error.

## What is Variance?

Variance is how much predictions change across different training samples. A
degree-10 polynomial memorises the training noise — tiny changes in data produce
wildly different curves.

High variance → model too sensitive to training data → poor generalisation.

## Where is the Optimal Model?

Total error = Bias² + Variance + Irreducible noise.

- Too simple (left of sweet spot) → bias² dominates → underfitting
- Too complex (right of sweet spot) → variance dominates → overfitting
- Optimal: the degree where test error is minimised (found via cross-validation)

Practical fixes:
- Underfitting → increase complexity, add features, reduce regularisation
- Overfitting → L1/L2 regularisation, more data, early stopping, dropout
