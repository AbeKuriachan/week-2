
---

# 5. File: `partD_ai_task.md`

```md
Prompt

Explain the Central Limit Theorem to a non-statistician product manager. Why does it matter for A/B testing? Include a Python simulation.

---

AI Explanation (summary)

The Central Limit Theorem states that when we take many samples from any distribution and compute their averages, those averages tend to follow a normal distribution as the sample size grows.

This matters for A/B testing because we compare average metrics such as conversion rate. Thanks to the CLT, these averages approximately follow a normal distribution, allowing us to calculate confidence intervals and p-values.

Example simulation

```python
import numpy as np
import matplotlib.pyplot as plt

data = np.random.exponential(1,10000)

means = []
for _ in range(1000):
    sample = np.random.choice(data,30)
    means.append(sample.mean())

plt.hist(means, bins=30)
plt.title("CLT Simulation")
plt.show()