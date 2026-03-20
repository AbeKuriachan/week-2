## 3. Explanation

### When should you standardize data?

Standardization (using Z-score) should be applied in the following cases:

1. **Different Feature Scales**
   - When features have different units or magnitudes  
   - Example: Height (cm) vs Income (₹)  
   - Prevents large-scale features from dominating

2. **Distance-Based Algorithms**
   - KNN, K-Means, SVM  
   - These rely on distance calculations, so scaling is essential

3. **Gradient-Based Models**
   - Linear Regression, Logistic Regression, Neural Networks  
   - Helps models converge faster and more efficiently

4. **Before PCA or Dimensionality Reduction**
   - Ensures all features contribute equally

---

### Why is Z-score important in Machine Learning?

Z-score standardizes data using:

Z = (X - μ) / σ

#### Key Reasons:

1. **Removes Scale Bias**
   - Ensures all features contribute equally to the model

2. **Centers Data Around Zero**
   - Mean becomes 0, improving numerical stability

3. **Normalizes Variance**
   - Standard deviation becomes 1

4. **Improves Model Performance**
   - Faster convergence
   - Better optimization

5. **Helps Detect Outliers**
   - |Z| > 2 → unusual  
   - |Z| > 3 → strong outlier

---

### Final Insight

- Standardization is a crucial preprocessing step  
- Especially important when using distance-based or gradient-based algorithms  
- Z-score makes data comparable, stable, and easier for models to learn