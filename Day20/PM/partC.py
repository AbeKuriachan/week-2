def z_score(x, mean, std):
    if std == 0:
        raise ValueError("Standard deviation cannot be zero")

    return (x - mean) / std


import math

# Sample dataset
data = [10, 20, 30, 40, 50]

# Step 1: Compute mean
total = 0
for x in data:
    total += x
mean = total / len(data)

# Step 2: Compute standard deviation
var_sum = 0
for x in data:
    var_sum += (x - mean) ** 2
variance = var_sum / len(data)
std = math.sqrt(variance)

# Step 3: Apply z_score to dataset
z_data = []
for x in data:
    z_data.append(z_score(x, mean, std))

print("Original Data:", data)
print("Z-score Data:", z_data)