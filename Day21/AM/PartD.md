# Week 04 · Day 21 AM — Part D: AI-Augmented Task (Evaluation)

Code is in `AM_PartD_Code.py`.

## Prompt
"Explain NumPy broadcasting and vectorisation with practical Python examples."
Model: Claude (claude-sonnet-4-6)

## Critical Evaluation

**Are examples correct?**
Examples 1–4 are correct and runnable. Example 5 had a comment typo claiming 58
would pass `>= 60`, but the code itself correctly excludes it — logic is fine,
comment was wrong.

**Is code efficient and runnable?**
Yes — fully vectorised throughout. Example 4 also applies the `(x+1)²`
algebraic simplification rather than blindly translating the loop expression.

**What I improved:**
Added a broadcasting failure example (shapes `(3,4)` and `(3,)`) to show the
boundary of what broadcasting handles — a common interview follow-up question.
