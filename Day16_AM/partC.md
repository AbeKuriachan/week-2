Q1

A p-value tells us how likely it is to observe the data if the null hypothesis were true.

A confidence interval gives a range of plausible values for the true parameter.

p-values are useful for decision making in hypothesis testing.
Confidence intervals are better for understanding the magnitude and uncertainty of an effect.


Q2

Implemented in ab_test.py. The function checks normality using the Shapiro test. 
If both samples are normal it runs a t-test, otherwise it uses the Mann–Whitney U test.
It returns statistic, p-value, decision, effect size and 95% confidence interval.


Q3

Before shipping the feature I would ask:

1. Is the effect size practically meaningful for the business?
2. How large was the sample size and is the test sufficiently powered?
3. Could the result be due to seasonality, segmentation effects or data quality issues?