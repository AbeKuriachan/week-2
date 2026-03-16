Q1 — Base rate fallacy

Suppose a disease affects 1 in 10,000 people. A test is 99% accurate.

If 1,000,000 people are tested:
- True cases ≈ 100
- True positives ≈ 99
- False positives ≈ 9,999

So most positive results are actually false positives. This happens because the base rate of the disease is extremely small.

---

Q2 — simulate_clt()

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

def simulate_clt(distribution, params, n_samples, n_simulations):

    means = []

    for _ in range(n_simulations):
        sample = distribution.rvs(*params, size=n_samples)
        means.append(sample.mean())

    means = np.array(means)

    plt.hist(means, bins=30, density=True)

    mu = means.mean()
    sigma = means.std()

    x = np.linspace(mu-4*sigma, mu+4*sigma,200)
    plt.plot(x, norm.pdf(x, mu, sigma))

    plt.title("CLT Simulation")
    plt.show()

Q3 — Exponential purchase amounts

Exponential distributions are highly skewed with a long right tail.

A few very large purchases increase the mean significantly, making the average misleading.

Instead I would show:

median purchase amount

distribution histogram

percentiles (P50, P90, P99)