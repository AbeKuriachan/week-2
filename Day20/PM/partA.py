import random
import math
import matplotlib.pyplot as plt

# -------------------------------
# 1. Generate Dataset & Statistics
# -------------------------------

data = []
for _ in range(1000):
    data.append(random.gauss(0, 1))

# Mean
total = 0
for x in data:
    total += x
mean = total / len(data)

# Variance
var_sum = 0
for x in data:
    var_sum += (x - mean) ** 2
variance = var_sum / len(data)

# Standard Deviation
std_dev = math.sqrt(variance)

print("\n--- Dataset Stats ---")
print("Mean:", mean)
print("Variance:", variance)
print("Std Dev:", std_dev)

# Histogram
plt.hist(data, bins=30)
plt.title("Histogram of Normal Distribution")
plt.show()

# -------------------------------
# 2. Z-score Transformation
# -------------------------------

z_data = []
for x in data:
    z = (x - mean) / std_dev
    z_data.append(z)

# Z Mean
z_sum = 0
for z in z_data:
    z_sum += z
z_mean = z_sum / len(z_data)

# Z Std Dev
z_var_sum = 0
for z in z_data:
    z_var_sum += (z - z_mean) ** 2
z_variance = z_var_sum / len(z_data)
z_std = math.sqrt(z_variance)

print("\n--- Z-score Stats ---")
print("Z Mean:", z_mean)
print("Z Std Dev:", z_std)

# -------------------------------
# 3. Student Marks Analysis
# -------------------------------

marks = [45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 30, 20]

# Mean
total = 0
for m in marks:
    total += m
mean_marks = total / len(marks)

# Median
sorted_marks = sorted(marks)
n = len(sorted_marks)
if n % 2 == 0:
    median = (sorted_marks[n//2 - 1] + sorted_marks[n//2]) / 2
else:
    median = sorted_marks[n//2]

# Variance
var_sum = 0
for m in marks:
    var_sum += (m - mean_marks) ** 2
variance_marks = var_sum / len(marks)

std_marks = math.sqrt(variance_marks)

# Outliers
outliers = []
for m in marks:
    z = (m - mean_marks) / std_marks
    if abs(z) > 2:
        outliers.append(m)

print("\n--- Student Stats ---")
print("Mean:", mean_marks)
print("Median:", median)
print("Variance:", variance_marks)
print("Std Dev:", std_marks)
print("Outliers:", outliers)

# -------------------------------
# 4. One-Sample Hypothesis Test
# -------------------------------

mu_0 = 0
n = len(data)

z_stat = (mean - mu_0) / (std_dev / math.sqrt(n))

z_critical = 1.96

print("\n--- Hypothesis Test ---")
print("Z-statistic:", z_stat)

if abs(z_stat) > z_critical:
    print("Reject H0")
else:
    print("Fail to Reject H0")

# -------------------------------
# 5. Simulation (False Positive Rate)
# -------------------------------

alpha = 0.05
trials = 1000
rejections = 0

for _ in range(trials):
    sample = []

    for _ in range(50):
        sample.append(random.gauss(0, 1))

    # Mean
    total = 0
    for x in sample:
        total += x
    sample_mean = total / len(sample)

    # Std Dev
    var_sum = 0
    for x in sample:
        var_sum += (x - sample_mean) ** 2
    variance = var_sum / len(sample)
    std_dev_sample = math.sqrt(variance)

    # Z-stat
    z = (sample_mean - mu_0) / (std_dev_sample / math.sqrt(len(sample)))

    if abs(z) > z_critical:
        rejections += 1

false_positive_rate = rejections / trials

print("\n--- Simulation ---")
print("False Positive Rate:", false_positive_rate)
print("Expected Alpha:", alpha)