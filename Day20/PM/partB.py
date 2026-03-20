# part_b_solution.py

import random
import math
import matplotlib.pyplot as plt

# -----------------------------------
# 1. Normal vs Standard Normal
# -----------------------------------

# Generate Normal Distribution (mean=50, std=10)
normal_data = []
for _ in range(1000):
    normal_data.append(random.gauss(50, 10))

# Compute mean manually
total = 0
for x in normal_data:
    total += x
mean = total / len(normal_data)

# Compute std dev manually
var_sum = 0
for x in normal_data:
    var_sum += (x - mean) ** 2
variance = var_sum / len(normal_data)
std_dev = math.sqrt(variance)

# Convert to Standard Normal (Z-score)
z_data = []
for x in normal_data:
    z = (x - mean) / std_dev
    z_data.append(z)

print("\n--- Distribution Comparison ---")
print("Original Mean:", mean)
print("Original Std Dev:", std_dev)

# Compute Z stats
z_sum = 0
for z in z_data:
    z_sum += z
z_mean = z_sum / len(z_data)

z_var_sum = 0
for z in z_data:
    z_var_sum += (z - z_mean) ** 2
z_variance = z_var_sum / len(z_data)
z_std = math.sqrt(z_variance)

print("Z Mean (≈0):", z_mean)
print("Z Std Dev (≈1):", z_std)

# Plot histograms
plt.hist(normal_data, bins=30, alpha=0.5, label="Normal (μ≈50, σ≈10)")
plt.hist(z_data, bins=30, alpha=0.5, label="Standard Normal (μ≈0, σ≈1)")
plt.legend()
plt.title("Normal vs Standard Normal Distribution")
plt.show()

# -----------------------------------
# 2. Two-Group Comparison
# -----------------------------------

group_A = []
group_B = []

for _ in range(100):
    group_A.append(random.gauss(50, 10))
    group_B.append(random.gauss(55, 10))  # slightly higher mean

def mean_func(data):
    total = 0
    for x in data:
        total += x
    return total / len(data)

mean_A = mean_func(group_A)
mean_B = mean_func(group_B)

difference = mean_B - mean_A

print("\n--- Two Group Comparison ---")
print("Mean A:", mean_A)
print("Mean B:", mean_B)
print("Difference (B - A):", difference)

if abs(difference) < 1:
    print("Conclusion: Groups are similar")
else:
    print("Conclusion: Noticeable difference between groups")

