# Pharmalink – B2B Medicine Distribution Platform
---

## Question 1 — Problem Identification

### Is this Supervised or Unsupervised Learning?

This is **Supervised Learning**. The dataset includes a labelled target variable
`will_churn_next_30d` (1 = Churn, 0 = Active), meaning historical examples with
known outcomes are available to train the model. There is no need to discover
hidden structure — the business has already defined what "churn" means and
labelled past instances accordingly.

### Is this Classification or Regression?

This is **Binary Classification**. The target variable takes exactly two discrete
values: 1 (will churn) or 0 (will stay active). There is no continuous quantity
being predicted — only a yes/no decision about each pharmacy's behaviour in the
next 30 days.

### Which Specific ML Category Does This Belong To?

This is a **Churn Prediction** problem, a classic sub-category of supervised
binary classification. Specifically, it belongs to **customer retention modelling**
where the goal is to identify at-risk users before they lapse so the business can
intervene proactively — in Pharmalink's case, by calling or offering credit
incentives to pharmacies showing early warning signals.

---

## Question 2 — The 5-Stage ML Pipeline (Pharmalink-Specific)

### Stage 1 — Data Collection

Pull 15 months of transactional and behavioural data from Pharmalink's app backend.
Critical columns to collect and join: `last_order_date`, `order_frequency_60d`,
`credit_utilization_ratio`, `payment_delay_days`, `app_sessions_30d`,
`city_tier`, and `will_churn_next_30d`.

Ensure the label `will_churn_next_30d` is constructed correctly by looking 30 days
forward from each observation date — a common leakage risk in churn datasets.

### Stage 2 — Data Preprocessing

**Handle missing values:** `payment_delay_days` may be null for pharmacies with no
credit usage — impute with 0. `product_diversity_score` may be missing for new
pharmacies — flag with a `is_new_pharmacy` indicator instead of imputing.

**Engineer features:**
- `days_since_last_order` = today − `last_order_date` (captures recency directly)
- `credit_stress_flag` = 1 if `credit_utilization_ratio > 0.8` AND
  `outstanding_amount > 0`
- `tier_x_frequency_interaction` = `city_tier` × `order_frequency_60d`
  (encodes the nuance that Tier-3 low frequency is not necessarily churn)

**Encode categoricals:** one-hot encode `store_type` (independent / chain);
ordinal-encode `city_tier` (1 > 2 > 3).

### Stage 3 — Model Training

Train a **Gradient Boosting classifier** (XGBoost or LightGBM) as the primary
model — it handles the class imbalance (15% churn = minority class), mixed feature
types, and non-linear interactions between `city_tier` and `order_frequency_60d`
well.

Apply **SMOTE or class-weight balancing** since churners are ~15% of the dataset.
Use time-based train/test split (train on months 1–12, test on months 13–15) to
avoid temporal leakage — random splits would allow future data to bleed into training.

### Stage 4 — Model Evaluation

Evaluate on the held-out 3-month test set. Primary metric: **Recall on the churn
class** (see Q3 for full justification). Secondary metrics: **F1-score** and
**AUC-ROC**.

Segment evaluation by `city_tier` — if Tier-3 recall is significantly lower than
Tier-1, the global model is underserving the urban/rural behaviour split and
separate models should be considered (see Q4).

Use a **confusion matrix** to count false negatives (missed churners) separately
from false positives (wasted calls) — this maps directly to the CRO's cost framing.

### Stage 5 — Deployment

Deploy as a **daily scoring pipeline**: every morning, score all 1.5M pharmacies
and flag the top-N churn-risk accounts. Output a ranked list to the sales team's
CRM with the top features driving each pharmacy's risk score (SHAP values).

Set a **tiered alert threshold**: high-revenue accounts (avg_order_value ×
order_frequency_60d > ₹5L/month) get flagged at a lower probability threshold
(e.g., 0.35) to maximise recall for key accounts — directly addressing the CRO's
₹8L/month hospital concern.

---

## Question 3 — Evaluation Strategy

### Prioritise Precision or Recall?

Pharmalink must prioritise **Recall** (also called Sensitivity).

### Why?

Recall = TP / (TP + FN). A False Negative here means a pharmacy that **will**
churn is **not flagged** — the sales team never calls them, they churn silently,
and Pharmalink loses the revenue permanently. A False Positive means calling a
pharmacy that was never going to churn — a wasted call but not a lost account.

The CRO's quote makes the asymmetry explicit:

> *"We can afford to call 500 pharmacies who were never going to churn.
> But if we lose a high-revenue hospital account placing ₹8 lakh monthly
> orders without warning, that's unacceptable."*

Calling 500 loyal customers wastes call-centre hours. Missing one ₹8L/month
hospital account costs ₹8L+ per month indefinitely. The cost of a False Negative
vastly exceeds the cost of a False Positive.

### Business Trade-off

By maximising Recall, Pharmalink accepts **lower Precision** — i.e., more false
alarms. The sales team will spend time on pharmacies that were not at risk. This
is the explicit trade-off: **operational cost of over-intervention vs. revenue
cost of under-detection**. For the high-revenue segment (hospitals, large chains),
the balance tips heavily toward catching every churner even at the expense of
extra calls.

A practical middle ground: use a **high-recall threshold for high-value accounts**
(avg_order_value > ₹2L) and a balanced threshold for the long tail of small
independent pharmacies.

---

## Question 4 — Advanced Thinking: Handling Tier-3 Behaviour

### The Problem

Tier-3 (small-town) pharmacies place large, infrequent bulk orders — a 28-day gap
since last order might be entirely normal for them. The same gap for a Tier-1
(metro) pharmacy almost certainly signals churn. A single global model will learn
the average behaviour and systematically misclassify Tier-3 stores.

### Recommended Approach: One Global Model + Tier Interaction Features

Rather than three separate models, train **one model with explicit tier-aware
features**:

**Interaction features to add:**

```
days_since_last_order_normed = days_since_last_order / typical_reorder_gap_by_tier
```
Where `typical_reorder_gap_by_tier` is computed from historical medians:
Tier-1 ≈ 7 days, Tier-2 ≈ 14 days, Tier-3 ≈ 25 days.

This transforms absolute recency into **tier-relative recency** — a 25-day gap
reads as 1.0× normal for Tier-3 and 3.6× normal for Tier-1.

Additional interaction features:
- `city_tier × order_frequency_60d`
- `city_tier × avg_order_value`
- `city_tier × credit_utilization_ratio`

### Why Not Separate Models?

| Approach | Pros | Cons |
|----------|------|------|
| Separate models per tier | Captures tier-specific patterns perfectly | 3× maintenance burden; Tier-3 data may be sparser; can't share signal across tiers |
| Global model only | Simple, one pipeline | Ignores the behaviour gap; Tier-3 recall will be poor |
| **Global model + interaction features** | Best of both — learns tier patterns without model explosion | Requires careful feature engineering; slight complexity increase |

The interaction-feature approach is preferable because:
1. The model still sees all 1.5M pharmacies and can share learned patterns
2. Tier-specific behaviour is captured through engineered features, not model
   architecture duplication
3. A single deployment pipeline is far easier to monitor and retrain

**Exception:** if post-deployment evaluation shows Tier-3 recall < 60% while
Tier-1 recall > 85%, then a dedicated Tier-3 sub-model is justified as a
targeted fix — not as the starting architecture.

---

## Part D — AI-Augmented Task

### Prompt Sent to Claude

> "I am working on a churn prediction problem for a B2B pharmaceutical distribution
> platform. The dataset has 1.5M pharmacy records, 42 features including
> last_order_date, order_frequency_60d, credit_utilization_ratio,
> payment_delay_days, city_tier (1/2/3), and a binary target will_churn_next_30d.
> Tier-3 pharmacies place infrequent bulk orders — a 28-day gap is normal for them.
> Which ML model would you recommend, how would you handle class imbalance, what
> evaluation metric should I prioritise, and how would you handle the tier
> behaviour difference?"

**Model:** Claude (claude-sonnet-4-6)

---

### AI Output Summary

The AI recommended:

1. **Model:** XGBoost or LightGBM with `scale_pos_weight` set to
   `(# negatives / # positives)` to handle the ~85:15 class imbalance natively.
   Cited tree-based models as best for mixed feature types and non-linear
   interactions.

2. **Class imbalance:** `scale_pos_weight` in XGBoost or `class_weight` in
   sklearn. Mentioned SMOTE as an alternative but cautioned it can create
   unrealistic synthetic samples for tabular data with correlated features.

3. **Evaluation metric:** Recommended Recall as primary metric given the
   asymmetric cost of missing high-value churners, with F1 as a secondary
   guardrail to prevent the model from predicting everything as churn.

4. **Tier handling:** Suggested creating normalised recency features
   (`days_since_order / median_reorder_gap_by_tier`) and interaction terms
   (`city_tier × order_frequency_60d`). Did not recommend separate models,
   citing data efficiency and maintenance overhead.

---

### Critical Evaluation

**Are concepts correctly explained?**
Yes — the recommendation of LightGBM / XGBoost is well-justified for this scale
(1.5M rows, 42 features). The Recall-first evaluation reasoning matches the
business context precisely.

**Is the SMOTE caution valid?**
Yes and it is a good nuance. SMOTE works on feature space distance, but
`credit_utilization_ratio` and `payment_delay_days` are correlated — synthetic
samples interpolated between them may violate real-world constraints (e.g.,
a pharmacy with 0 credit usage cannot have non-zero payment delay). Using
`scale_pos_weight` is safer here.

**What the AI missed:**
- Did not mention **temporal train/test split** — using a random split on
  time-series churn data causes leakage because future observations bleed
  into training. This is a critical implementation error the AI glossed over.
- Did not address **deployment threshold tuning** by segment — the CRO
  specifically needs a lower threshold for high-revenue accounts.
- No mention of **SHAP explainability**, which is essential for a sales team
  to act on model outputs (they need to know *why* a pharmacy is flagged).

**Verdict:** The AI output is a solid starting framework but incomplete for
production deployment. The temporal leakage blind spot is the most dangerous gap —
it would produce inflated validation metrics that fail in live scoring.
