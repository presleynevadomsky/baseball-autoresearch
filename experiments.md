# Experiment Log: AutoResearch for Predicting Next-Year Defensive Value in MLB

**Project:** AutoResearch for Predicting Next-Year Defensive Value in MLB  
**Author:** Presley Nevadomsky  
**Research Question:** Can an AI agent discover the best model for predicting an outfielder's OAA next season from their physical tracking data this season?  
**Target Variable:** next_year_oaa (Outs Above Average in year N+1)  
**Input Features:** Average of year N-1 and year N physical tracking stats (burst, reaction, routing, bootup, sprint speed, age)
**Train/val:** 2017-2021 seasons (302 matched pairs)
**Test:** 2022-2023 seasons (131 rows, locked)
**Baseline:** 4.027314 (all features, linear regression, 2-year avg inputs)
**Current Best:** 3.908619

---

## Experiment-Result Matrix

| # | Date | Description | What Changed | Features | Val RMSE | vs Baseline | Result | Error Type |
|---|------|-------------|--------------|----------|----------|-------------|--------|------------|
| 1 | 2026-05-10 | Baseline: all features linear regression | Starting point | all 7 | 4.759972 | — | baseline | — |
| 2 | 2026-05-10 | Dry run: age only | all features → age only | age only | 6.252314 | +1.492 | ❌ discard | Signal Failure |
| 3 | 2026-05-10 | Dry run: all features except age | -age | 6 features | 4.661245 | -0.099 | ✅ keep | — |
| 4 | 2026-05-10 | Dry run: Ridge alpha=1.0 all features | LinearReg → Ridge | all 7 | 4.755890 | -0.004 | ❌ discard | Signal Failure |
| 5 | 2026-05-10 | Dry run: Ridge alpha=1.0 no age | LinearReg → Ridge, -age | 6 features | 4.659598 | -0.100 | ✅ keep | — |
| 6 | 2026-05-10 | Ridge alpha=0.5, no age | alpha: 1.0 → 0.5 | 6 features | 4.660278 | -0.100 | ❌ discard | Signal Failure |
| 7 | 2026-05-10 | Ridge alpha=2.0, no age | alpha: 1.0 → 2.0 | 6 features | 4.658728 | -0.101 | ✅ keep | — |
| 8 | 2026-05-10 | Ridge alpha=5.0, no age | alpha: 2.0 → 5.0 | 6 features | 4.657792 | -0.102 | ✅ keep | — |
| 9 | 2026-05-10 | Ridge alpha=10.0, no age | alpha: 5.0 → 10.0 | 6 features | 4.658094 | -0.102 | ❌ discard | Signal Failure |
| 10 | 2026-05-10 | Ridge alpha=3.0, no age | alpha: 5.0 → 3.0 | 6 features | 4.658229 | -0.102 | ❌ discard | Signal Failure |
| 11 | 2026-05-10 | Lasso alpha=1.0, no age | Ridge → Lasso alpha=1.0 | 6 features | 5.098837 | +0.339 | ❌ discard | Signal Failure |
| 12 | 2026-05-10 | Lasso alpha=0.1, no age | Ridge → Lasso alpha=0.1 | 6 features | 4.681694 | -0.078 | ❌ discard | Signal Failure |
| 13 | 2026-05-10 | ElasticNet alpha=0.5 l1_ratio=0.3, no age | Ridge → ElasticNet | 6 features | 4.766790 | +0.007 | ❌ discard | Signal Failure |
| 14 | 2026-05-10 | RandomForest n=200, no age | Ridge → RandomForest | 6 features | 4.807683 | +0.048 | ❌ discard | Signal Failure |
| 15 | 2026-05-10 | GBR n=100 depth=2 lr=0.1, no age | Ridge → GBR | 6 features | 4.769414 | +0.009 | ❌ discard | Signal Failure |
| 16 | 2026-05-10 | GBR n=300 depth=1 lr=0.05 subsample=0.8, no age | Ridge → shallow GBR | 6 features | 4.746944 | -0.013 | ❌ discard | Signal Failure |
| 17 | 2026-05-10 | SVR RBF C=1.0 epsilon=0.5, no age | Ridge → SVR RBF | 6 features | 4.884822 | +0.125 | ❌ discard | Signal Failure |
| 18 | 2026-05-10 | SVR linear C=5.0 epsilon=0.3, no age | Ridge → SVR linear | 6 features | 4.813741 | +0.054 | ❌ discard | Signal Failure |
| 19 | 2026-05-10 | Ridge alpha=5, burst+routing+sprint only | -reaction -bootup -f_bootup | 3 features | 4.695887 | -0.064 | ❌ discard | Signal Failure |
| 20 | 2026-05-10 | Ridge alpha=5, no age, no f_bootup | -f_bootup_distance | 5 features | 4.608974 | -0.151 | ✅ keep | — |
| 21 | 2026-05-10 | Ridge alpha=10, rel features + sprint, no age no f_bootup | alpha: 5 → 10 | 5 features | 4.611861 | -0.148 | ❌ discard | Signal Failure |
| 22 | 2026-05-10 | Ridge alpha=3, rel features + sprint, no age no f_bootup | alpha: 5 → 3 | 5 features | 4.608180 | -0.152 | ✅ keep | — |
| 23 | 2026-05-10 | Ridge alpha=2, rel features + sprint, no age no f_bootup | alpha: 3 → 2 | 5 features | 4.607978 | -0.152 | ✅ keep | — |
| 24 | 2026-05-10 | Ridge alpha=1.5, rel features + sprint, no age no f_bootup | alpha: 2 → 1.5 | 5 features | 4.607964 | -0.152 | ✅ keep | — |
| 25 | 2026-05-10 | Ridge alpha=1.0, rel features + sprint, no age no f_bootup | alpha: 1.5 → 1.0 | 5 features | 4.608041 | -0.152 | ❌ discard | Signal Failure |
| 26 | 2026-05-10 | Ridge alpha=1.5, no reaction, no age, no f_bootup | -reaction | 4 features | 4.612494 | -0.147 | ❌ discard | Signal Failure |
| 27 | 2026-05-10 | Ridge alpha=1.5, no rel_bootup, no age, no f_bootup | -rel_bootup | 4 features | 4.603920 | -0.156 | ✅ keep | — |
| 28 | 2026-05-10 | Ridge alpha=2.0, burst+reaction+routing+sprint only | alpha: 1.5 → 2.0 | 4 features | 4.604583 | -0.155 | ❌ discard | Signal Failure |
| 29 | 2026-05-10 | Ridge alpha=1.0, burst+reaction+routing+sprint only | alpha: 1.5 → 1.0 | 4 features | 4.603258 | -0.157 | ✅ keep | — |
| 30 | 2026-05-10 | Ridge alpha=0.5, burst+reaction+routing+sprint only | alpha: 1.0 → 0.5 | 4 features | 4.602599 | -0.157 | ✅ keep | — |
| 31 | 2026-05-10 | Ridge alpha=0.1, burst+reaction+routing+sprint only | alpha: 0.5 → 0.1 | 4 features | 4.602074 | -0.158 | ✅ keep | — |
| 32 | 2026-05-10 | Ridge alpha=0.01, burst+reaction+routing+sprint only | alpha: 0.1 → 0.01 | 4 features | 4.601956 | -0.158 | ✅ keep | — |
| 33 | 2026-05-10 | LinearRegression, burst+reaction+routing+sprint only | Ridge → OLS | 4 features | 4.601943 | -0.158 | ✅ keep | — |
| 34 | 2026-05-10 | PolyFeatures(degree=2) + Ridge alpha=1.0, 4 features | +polynomial interactions | 14 poly features | 4.693135 | -0.067 | ❌ discard | Signal Failure |

---

## ⚠️ Approach Change — Week 5

**Date:** 2026-05-10  
**Change:** Switched to 2-year averaged physical tracking inputs to reduce noise. Improved baseline from 4.759972 to 4.027314.

---
| # | Date | Description | What Changed | Features | Val RMSE | vs Baseline | Result | Error Type |
|---|------|-------------|--------------|----------|----------|-------------|--------|------------|
| 35 | 2026-05-10 | 2-year avg baseline: all features linear regression | 2-year avg inputs | all 7 | 4.027314 | — | baseline | — |
| 36 | 2026-05-10 | LinearRegression, no age, 6 features | -age | 6 features | 3.952057 | -0.075 | ✅ keep | — |
| 37 | 2026-05-10 | LinearRegression, 4 core features: burst+reaction+routing+sprint | -bootup features | 4 features | 3.985381 | -0.042 | ❌ discard | Signal Failure |
| 38 | 2026-05-10 | LinearRegression, no age, no f_bootup, 5 rel features + sprint | -f_bootup | 5 features | 3.989897 | -0.037 | ❌ discard | Signal Failure |
| 39 | 2026-05-10 | Ridge alpha=0.1, no age, 6 features | LinearReg → Ridge α=0.1 | 6 features | 3.951926 | -0.075 | ✅ keep | — |
| 40 | 2026-05-10 | Ridge alpha=0.5, no age, 6 features | alpha: 0.1 → 0.5 | 6 features | 3.951607 | -0.076 | ✅ keep | — |
| 41 | 2026-05-10 | Ridge alpha=1.0, no age, 6 features | alpha: 0.5 → 1.0 | 6 features | 3.951500 | -0.076 | ✅ keep | — |
| 42 | 2026-05-10 | Ridge alpha=2.0, no age, 6 features | alpha: 1.0 → 2.0 | 6 features | 3.951757 | -0.076 | ❌ discard | Signal Failure |
| 43 | 2026-05-10 | Ridge alpha=1.0, no age, no f_bootup, 5 rel features + sprint | -f_bootup | 5 features | 3.989362 | -0.038 | ❌ discard | Signal Failure |
| 44 | 2026-05-10 | HuberRegressor ε=1.35 α=0.001, no age, 6 features | Ridge → Huber | 6 features | 3.994817 | -0.033 | ❌ discard | Signal Failure |
| 45 | 2026-05-10 | Ridge alpha=1.0, all 7 features including age | +age | all 7 | 4.024707 | -0.003 | ❌ discard | Signal Failure |
| 46 | 2026-05-10 | Ridge alpha=1.0, no age, no reaction, 5 features | -reaction | 5 features | 3.953546 | -0.074 | ❌ discard | Signal Failure |
| 47 | 2026-05-10 | Ridge alpha=1.0, no age, no burst, 5 features | -burst | 5 features | 3.953726 | -0.074 | ❌ discard | Signal Failure |
| 48 | 2026-05-10 | RidgeCV auto-tuned alpha (logspace -2 to 2, 100 alphas), no age, 6 features | Ridge α=1.0 → RidgeCV | 6 features | 3.998662 | -0.029 | ❌ discard | Signal Failure |
| 49 | 2026-05-10 | PowerTransformer(Yeo-Johnson) + Ridge alpha=1.0, no age, 6 features | StandardScaler → PowerTransformer | 6 features | 3.946055 | -0.081 | ✅ keep | — |
| 50 | 2026-05-10 | PowerTransformer(Yeo-Johnson) + LinearRegression, no age, 6 features | Ridge α=1.0 → OLS | 6 features | 3.943865 | -0.083 | ✅ keep | — |
| 51 | 2026-05-10 | QuantileTransformer(normal) + LinearRegression, no age, 6 features | PowerTransformer → QuantileTransformer | 6 features | 3.976313 | -0.051 | ❌ discard | Signal Failure |
| 52 | 2026-05-10 | RobustScaler + LinearRegression, no age, 6 features | PowerTransformer → RobustScaler | 6 features | 3.952057 | -0.075 | ❌ discard | Signal Failure |
| 53 | 2026-05-17 | XGBoost n=100 depth=3 lr=0.1 PowerTransformer no age | OLS → XGBoost depth=3 | 6 features | 4.036305 | +0.009 | ❌ discard | Signal Failure |
| 54 | 2026-05-17 | XGBoost depth=1 n=500 lr=0.05 lambda=5 PowerTransformer no age | depth=3 → depth=1 stumps, lambda=5 | 6 features | 3.929331 | -0.098 | ✅ keep | — |
| 55 | 2026-05-17 | XGBoost depth=1 n=1000 lr=0.02 lambda=5 PowerTransformer no age | n=500 → n=1000, lr=0.05 → 0.02 | 6 features | 3.931917 | -0.095 | ❌ discard | Signal Failure |
| 56 | 2026-05-17 | XGBoost depth=1 n=500 lr=0.05 lambda=10 PowerTransformer no age | lambda=5 → 10 | 6 features | 3.927346 | -0.100 | ✅ keep | — |
| 57 | 2026-05-17 | XGBoost depth=1 n=500 lr=0.05 lambda=20 PowerTransformer no age | lambda=10 → 20 | 6 features | 3.918694 | -0.109 | ✅ keep | — |
| 58 | 2026-05-17 | XGBoost depth=1 n=500 lr=0.05 lambda=50 PowerTransformer no age | lambda=20 → 50 | 6 features | 3.911379 | -0.116 | ✅ keep | — |
| 59 | 2026-05-17 | XGBoost depth=1 n=500 lr=0.05 lambda=100 PowerTransformer no age | lambda=50 → 100 | 6 features | 3.931181 | -0.096 | ❌ discard | Signal Failure |
| 60 | 2026-05-17 | XGBoost depth=1 n=500 lr=0.05 lambda=50 alpha=1.0 PowerTransformer no age | +reg_alpha=1.0 | 6 features | 3.908619 | -0.119 | ✅ keep | — |
| 61 | 2026-05-17 | XGBoost depth=1 n=500 lr=0.05 lambda=50 alpha=5.0 PowerTransformer no age | alpha=1.0 → 5.0 | 6 features | 3.921280 | -0.106 | ❌ discard | Signal Failure |
| 62 | 2026-05-17 | XGBoost depth=1 n=500 lr=0.05 lambda=50 alpha=1.0 min_child_weight=5 | +min_child_weight=5 | 6 features | 3.908619 | -0.119 | ❌ discard | Signal Failure |
| 63 | 2026-05-17 | XGBoost depth=1 n=800 lr=0.03 lambda=50 alpha=1.0 PowerTransformer no age | n=500 → 800, lr=0.05 → 0.03 | 6 features | 3.918283 | -0.109 | ❌ discard | Signal Failure |
| 64 | 2026-05-17 | XGBoost no scaler depth=1 n=500 lr=0.05 lambda=50 alpha=1.0 no age | removed PowerTransformer | 6 features | 3.908619 | -0.119 | ❌ discard | Signal Failure |
| 65 | 2026-05-17 | XGBoost depth=1 n=500 lr=0.05 lambda=50 alpha=1 subsample=0.8 colsample=0.8 | +subsample +colsample_bytree | 6 features | 3.913961 | -0.113 | ❌ discard | Signal Failure |
| 66 | 2026-05-17 | XGBoost depth=1 n=500 lr=0.05 lambda=50 alpha=1 gamma=0.5 PowerTransformer | +gamma=0.5 | 6 features | 3.908619 | -0.119 | ❌ discard | Signal Failure |
| 67 | 2026-05-17 | XGBoost depth=1 n=500 lr=0.05 lambda=50 alpha=1 PowerTransformer with age | +age | 7 features | 3.987816 | -0.040 | ❌ discard | Signal Failure |
| 68 | 2026-05-17 | HistGradientBoosting max_iter=500 depth=1 lr=0.05 l2=50 no age | XGBoost → HistGBM | 6 features | 3.913448 | -0.114 | ❌ discard | Signal Failure |
| 69 | 2026-05-17 | PowerTransformer + PolyFeatures(degree=2) + Ridge alpha=10, 6 features no age | +polynomial interactions | 21 poly | 3.992703 | -0.035 | ❌ discard | Signal Failure |
| 70 | 2026-05-17 | PowerTransformer + PolyFeatures(degree=2) + Ridge alpha=100, 6 features no age | alpha=10 → 100 | 21 poly | 4.046314 | +0.019 | ❌ discard | Signal Failure |
| 71 | 2026-05-17 | XGBoost depth=1 n=500 lr=0.05 lambda=50 alpha=1 PowerTransformer 4 core features | -bootup features | 4 features | 4.098170 | +0.071 | ❌ discard | Signal Failure |
| 72 | 2026-05-17 | XGBoost depth=1 n=500 lr=0.05 lambda=50 alpha=1 huber objective PowerTransformer | objective=pseudohuber | 6 features | 4.166946 | +0.140 | ❌ discard | Signal Failure |
| 73 | 2026-05-17 | XGBoost depth=2 n=500 lr=0.05 lambda=200 alpha=5 PowerTransformer no age | depth=1→2, extreme reg | 6 features | 3.972294 | -0.055 | ❌ discard | Signal Failure |

---

## Error Taxonomy

### Signal Failure — *Loop ran but no meaningful improvement*
Experiments 2, 4, 6, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 21, 25, 26, 28, 34, 37, 38, 42, 43, 44, 45, 46, 47, 48, 51, 52, 53, 55, 59, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, and 73: model ran correctly but did not beat the current best.

### Code Instability — *Crashes or broken pipeline*
No instances.

### Agent Misbehavior — *Agent broke the rules or made uncontrolled changes*
No instances.

### Evaluation Leakage — *Metric improved but comparability was compromised*
No instances.

---

## Key Findings

- **Baseline RMSE:** 4.759972 — predicting next-year OAA is harder than same-year OAA
- **Age hurts the model:** Removing age improves RMSE from 4.759972 to 4.661245 (1-yr) and 4.027314 to 3.952057 (2-yr avg)
- **Ridge helps slightly without age:** Ridge alpha=1.0 without age achieves 4.659598 (1-yr) and 3.951500 (2-yr avg)
- **2-year averaging changes feature importance:** With 1-yr data, dropping both bootup features helped; with 2-yr avg data, all 6 non-age features contribute — dropping any one hurts performance
- **f_bootup_distance matters with 2-yr avg:** Unlike 1-yr data, removing f_bootup_distance on 2-yr averaged inputs raises RMSE from 3.952 to 3.989 — the absolute bootup feature adds unique signal
- **Optimal Ridge alpha is ~1.0 for 6 features (2-yr data):** Alpha=1.0 is the sweet spot; going lower (RidgeCV) or higher (2.0) both degrade performance
- **PowerTransformer beats StandardScaler:** Yeo-Johnson normalization (which handles skewed physical distributions) improves on StandardScaler — RMSE 3.946055 vs 3.951500
- **OLS beats Ridge with PowerTransformer:** Removing regularization entirely (PowerTransformer + OLS) improves on Ridge α=1.0 — 3.943865 vs 3.946055; PowerTransformer's normalization reduces the need for regularization
- **QuantileTransformer and RobustScaler don't help:** Both perform worse than PowerTransformer on these 6 physical tracking features (3.976313 and 3.952057 respectively)
- **Age still hurts on 2-yr avg:** Ridge alpha=1.0 with age = 4.024707, without age = 3.951500 — 2-yr averaging doesn't fix the age noise problem
- **Non-linear models don't help:** HuberRegressor, along with all tree-based and kernel models tested on 1-yr data, performs worse than regularized linear regression
- **XGBoost requires depth=1 stumps + heavy regularization to compete:** Deeper XGBoost (depth=3) loses badly (4.036). Only depth=1 stumps with lambda≥5 beat the linear model; optimal is lambda=50, reg_alpha=1.0 (L1+L2 combo)
- **XGBoost reg_lambda sweet spot is ~50:** RMSE improves monotonically from lambda=5 (3.929) to lambda=50 (3.911) but degrades at lambda=100 (3.931) — over-regularization collapses the model
- **Adding L1 (reg_alpha=1.0) on top of lambda=50 gives a small further gain:** 3.911 → 3.909; higher alpha=5.0 hurts
- **XGBoost is truly scale-invariant:** Removing PowerTransformer from XGBoost gives identical RMSE (3.908619) — tree splits don't care about monotonic feature transforms
- **Stochasticity hurts with 6 features:** subsample=0.8 + colsample_bytree=0.8 degrades performance (3.914) — too few features per tree with colsample applied
- **Gamma and min_child_weight are redundant with high lambda:** gamma=0.5 and min_child_weight=5 tie but don't improve — lambda=50 already prevents weak splits
- **Age hurts XGBoost too:** Adding age → 3.988 (vs 3.909 without) — confirms age adds noise regardless of model type
- **Polynomial features don't help on 2-yr data:** PolyFeatures(degree=2) + Ridge alpha∈[10,100] both fail — smoothed 2-yr features have no useful nonlinear interactions
- **Both bootup features are necessary:** Dropping to 4 core features → 4.098 (worst in this batch) — f_bootup and rel_league_bootup each contribute unique signal
- **Huber objective is wrong loss for RMSE:** Optimizing pseudo-Huber → 4.167 (worst overall in session) — RMSE metric rewards squared-error optimization
- **depth=2 with extreme regularization doesn't help:** lambda=200, alpha=5, depth=2 → 3.972 — feature interactions provide no lift over additive stumps
- **Best model (2-yr avg):** XGBoost depth=1, n=500, lr=0.05, lambda=50, alpha=1.0 + PowerTransformer, no age, 6 features — RMSE 3.908619 (-0.119 vs 2-yr baseline). Model appears converged.
