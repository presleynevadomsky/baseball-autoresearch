# Experiment Log: AutoResearch for Predicting Next-Year Defensive Value in MLB

**Project:** AutoResearch for Predicting Next-Year Defensive Value in MLB  
**Author:** Presley Nevadomsky  
**Research Question:** Can an AI agent discover the best model for predicting an outfielder's OAA next season from their physical tracking data this season?  
**Target Variable:** next_year_oaa (Outs Above Average in year N+1)  
**Input Features:** Average of year N-1 and year N physical tracking stats (burst, reaction, routing, bootup, sprint speed, age)
**Train/val:** 2017-2021 seasons (302 matched pairs)
**Test:** 2022-2023 seasons (131 rows, locked)
**Baseline:** 4.027314 (all features, linear regression, 2-year avg inputs)
**Current Best:** 4.027314

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

| 35 | 2026-05-10 | 2-year avg baseline: all features linear regression | 2-year avg inputs | all 7 | 4.027314 | — | baseline | — |

---

## Error Taxonomy

### Signal Failure — *Loop ran but no meaningful improvement*
Experiments 2, 4, 6, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 21, 25, 26, 28, and 34: model ran correctly but did not beat the current best.

### Code Instability — *Crashes or broken pipeline*
No instances.

### Agent Misbehavior — *Agent broke the rules or made uncontrolled changes*
No instances.

### Evaluation Leakage — *Metric improved but comparability was compromised*
No instances.

---

## Key Findings

- **Baseline RMSE:** 4.759972 — predicting next-year OAA is harder than same-year OAA
- **Age hurts the model:** Removing age improves RMSE from 4.759972 to 4.661245
- **Ridge helps slightly without age:** Ridge alpha=1.0 without age achieves 4.659598
- **Optimal Ridge alpha is ~5 for 6 features:** Increasing regularization helps up to alpha=5, then degrades
- **Dropping f_bootup_distance is beneficial:** Removing the absolute bootup distance (keeping only the relative version) improves 5-feature RMSE from 4.657792 → 4.608974 (with best alpha tuning reaching 4.607964)
- **Dropping BOTH bootup features is even better:** Removing rel_league_bootup_distance too (leaving burst, reaction, routing, sprint) drops RMSE to ~4.602
- **OLS beats Ridge with 4 clean features:** As features are pruned to only the most predictive ones, regularization becomes unnecessary — plain LinearRegression achieves the best RMSE of 4.601943
- **Non-linear models don't help:** RandomForest, GBR, SVR, ElasticNet, Lasso, and PolynomialFeatures all perform worse than simple linear regression on this dataset
- **Best model:** LinearRegression with 4 features (burst, reaction, routing, sprint_speed) — RMSE 4.601943 (-0.158 vs baseline)
