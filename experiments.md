# Experiment Log: AutoResearch for Defensive Metric Discovery in MLB

**Project:** AutoResearch for Defensive Metric Discovery in MLB  
**Author:** Presley Nevadomsky  
**Target Variable:** Outs Above Average (OAA)  
**Validation Metric:** val_rmse (lower is better)  
**Baseline:** 4.524665 (routing distance only, linear regression)  
**Current Best:** 2.297824 (GradientBoosting, lr=0.01, all features)

---

## Experiment-Result Matrix

| # | Date | Description | What Changed | Features | Val RMSE | vs Baseline | Result | Error Type |
|---|------|-------------|--------------|----------|----------|-------------|--------|------------|
| 1 | 2026-04-24 | Baseline: routing distance only | Starting point | routing only | 4.524665 | — | baseline | — |
| 2 | 2026-04-25 | Added burst distance | +burst_distance | 2 features | 3.147574 | -1.377 | ✅ keep | — |
| 3 | 2026-04-25 | All features linear regression | +5 more features | all 7 | 2.404943 | -2.120 | ✅ keep | — |
| 4 | 2026-04-25 | Random forest all features | LinearRegression → RandomForest | all 7 | 2.433751 | -2.091 | ❌ discard | Signal Failure |
| 5 | 2026-04-25 | Ridge regression alpha=1.0 | LinearRegression → Ridge | all 7 | 2.409692 | -2.115 | ❌ discard | Signal Failure |
| 6 | 2026-04-25 | Polynomial degree=2 + Ridge | +PolynomialFeatures | all 7 | 2.686570 | -1.838 | ❌ discard | Signal Failure |
| 7 | 2026-04-25 | GradientBoosting n=300 depth=3 lr=0.05 | LinearRegression → GradientBoosting | all 7 | 2.379784 | -2.145 | ✅ keep | — |
| 8 | 2026-04-25 | SVR RBF C=10 | GradientBoosting → SVR | all 7 | 2.401305 | -2.123 | ❌ discard | Signal Failure |
| 9 | 2026-04-25 | GradientBoosting n=500 depth=3 lr=0.03 subsample=0.8 | tuned hyperparameters | all 7 | 2.358819 | -2.166 | ✅ keep | — |
| 10 | 2026-04-25 | Reproducibility check | none (same as #9) | all 7 | 2.358819 | -2.166 | ✅ confirmed | — |
| 11 | 2026-05-02 | Restore best model | reset to #9 config | all 7 | 2.358819 | -2.166 | ✅ confirmed | — |
| 12 | 2026-05-02 | Exp1: remove outs_per_play only | -outs_per_play | 6 features | 3.285204 | -1.239 | ❌ discard | Signal Failure |
| 13 | 2026-05-02 | Exp2: remove sprint_speed only | -sprint_speed | 6 features | 2.348206 | -2.177 | ✅ keep | — |
| 14 | 2026-05-02 | Exp3: remove f_bootup_distance only | -f_bootup_distance | 6 features | 2.465137 | -2.060 | ❌ discard | Signal Failure |
| 15 | 2026-05-02 | Exp4: learning_rate=0.01 only | lr 0.03 → 0.01 | all 7 | 2.297824 | -2.227 | ✅ keep — new best | — |
| 16 | 2026-05-02 | Exp5: learning_rate=0.05 only | lr 0.03 → 0.05 | all 7 | 2.440453 | -2.084 | ❌ discard | Signal Failure |
| 17 | 2026-05-02 | Exp6: max_depth=2 only | depth 3 → 2 | all 7 | 2.323412 | -2.201 | ❌ discard | Signal Failure |
| 18 | 2026-05-02 | Exp7: max_depth=4 only | depth 3 → 4 | all 7 | 2.430151 | -2.095 | ❌ discard | Signal Failure |
| 19 | 2026-05-02 | Combo: lr=0.01 + depth=2 + no sprint_speed | combined top 3 improvements | 6 features | 2.327434 | -2.197 | ❌ discard | Signal Failure |
| 20 | 2026-05-02 | Exp8: learning_rate=0.005 only | lr 0.01 → 0.005 | all 7 | 2.411349 | -2.113 | ❌ discard | Signal Failure |
| 21 | 2026-05-02 | n_estimators=1000 lr=0.01 depth=3 | n 500 → 1000 | all 7 | 2.314264 | -2.210 | ❌ discard | Signal Failure |
| 22 | 2026-05-02 | max_features=sqrt n=500 lr=0.01 | +max_features=sqrt | all 7 | 2.305921 | -2.219 | ❌ discard | Signal Failure |
| 23 | 2026-05-02 | max_features=0.8 n=500 lr=0.01 | +max_features=0.8 | all 7 | 2.298670 | -2.226 | ❌ discard | Signal Failure |
| 24 | 2026-05-02 | subsample=0.7 n=500 lr=0.01 | subsample 0.8 → 0.7 | all 7 | 2.313879 | -2.211 | ❌ discard | Signal Failure |
| 25 | 2026-05-02 | subsample=0.9 n=500 lr=0.01 | subsample 0.8 → 0.9 | all 7 | 2.310793 | -2.214 | ❌ discard | Signal Failure |
| 26 | 2026-05-02 | min_samples_leaf=3 n=500 lr=0.01 | +min_samples_leaf=3 | all 7 | 2.342772 | -2.182 | ❌ discard | Signal Failure |
| 27 | 2026-05-02 | HistGradientBoosting max_iter=500 lr=0.01 | GBR → HistGBR | all 7 | 2.453276 | -2.071 | ❌ discard | Signal Failure |
| 28 | 2026-05-02 | ExtraTreesRegressor n=500 | GBR → ExtraTrees | all 7 | 2.377399 | -2.147 | ❌ discard | Signal Failure |
| 29 | 2026-05-02 | n_estimators=350 lr=0.01 depth=3 | n 500 → 350 | all 7 | 2.331515 | -2.193 | ❌ discard | Signal Failure |
| 30 | 2026-05-02 | VotingRegressor GBR+Ridge | GBR → ensemble(GBR+Ridge) | all 7 | 2.324838 | -2.200 | ❌ discard | Signal Failure |

---

## Error Taxonomy

### Signal Failure — *Loop ran but no meaningful improvement*
Experiments 4, 5, 6, 8, 12, 14, 16, 18, 19–30 all produced worse RMSE than the current best and were discarded. This was the most common failure type — 19 out of 29 experiments. In most cases the model was a reasonable idea but simply didn't outperform the current best on this dataset.

### Code Instability — *Crashes or broken pipeline*
Two instances occurred:
- **numpy architecture mismatch**: Mac system Python (x86_64) is incompatible with the project venv (arm64). When the agent used `python3` instead of the full venv path, numpy failed and run.py crashed entirely.
- **Claude Code terminal install**: The `claude` command failed to install correctly on first attempt, requiring a PATH fix before the agent could run autonomously.

### Agent Misbehavior — *Agent broke the rules or made uncontrolled changes*
One instance occurred:
- **Worktree logging conflict**: Claude Code ran experiments in a separate worktree directory (`.claude/worktrees/`) instead of the main repo, causing results to log to the wrong `results.tsv`. This also caused `model.py` changes to not sync back to the main repo correctly, requiring manual intervention.

### Evaluation Leakage — *Metric improved but comparability was compromised*
No instances observed. The evaluation logic in `run.py` remained frozen throughout all experiments. The fixed random seed (`random_state=42`) ensured the same train/val split was used every run, maintaining full comparability across all 19 experiments.

---

## Key Findings

- **Most impactful single feature:** `outs_per_play` — removing it caused the largest RMSE spike (+0.926)
- **Least impactful feature:** `sprint_speed` — removing it slightly improved RMSE (-0.011)
- **Best hyperparameter change:** learning_rate=0.01 — single biggest improvement in controlled experiments
- **Combinations don't always stack:** lr=0.01 + depth=2 + no sprint_speed performed worse than lr=0.01 alone, suggesting these changes partially conflict
- **Total improvement:** 4.524665 → 2.297824 (49% reduction in RMSE over 29 experiments)
- **Optimal learning rate:** lr=0.01 is the sweet spot — lr=0.005 underfits (RMSE 2.411) and lr=0.05 overfits (RMSE 2.440). Lower is not always better.
- **Optimal n_estimators:** n=500 is the sweet spot — n=350 (2.332) and n=1000 (2.314) both perform worse; the model may be at capacity for this dataset size.
- **Feature subsampling:** max_features=0.8 came within 0.0008 of the best (2.2987 vs 2.2978) — the closest any new experiment came to beating the record.
- **subsample sensitivity:** Values of 0.7, 0.8, 0.9 all tried — 0.8 remains optimal.
- **Alternative models:** HistGradientBoosting (2.453), ExtraTrees (2.377), VotingRegressor GBR+Ridge (2.325) all underperform the tuned GBR.
- **Convergence signal:** 10 consecutive failed experiments (21–30) suggest the current GBR configuration may be near the performance ceiling for this feature set.
