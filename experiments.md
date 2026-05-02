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
| 17 | 2026-05-02 | Exp6: max_depth=2 only | depth 3 → 2 | all 7 | 2.323412 | -2.201 | ✅ keep | — |
| 18 | 2026-05-02 | Exp7: max_depth=4 only | depth 3 → 4 | all 7 | 2.430151 | -2.095 | ❌ discard | Signal Failure |
| 19 | 2026-05-02 | Combo: lr=0.01 + depth=2 + no sprint_speed | combined top 3 improvements | 6 features | 2.327434 | -2.197 | ❌ discard | Signal Failure |
| 20 | 2026-05-02 | Exp8: learning_rate=0.005 only | lr 0.01 → 0.005 | all 7 | 2.411349 | -2.113 | ❌ discard | Signal Failure |

---

## Error Taxonomy

### Signal Failure — *Loop ran but no meaningful improvement*
Experiments 4, 5, 6, 8, 12, 14, 16, 18, 19 all produced worse RMSE than the current best and were discarded. This was the most common failure type — 9 out of 19 experiments. In most cases the model was a reasonable idea but simply didn't outperform the current best on this dataset.

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
- **Total improvement:** 4.524665 → 2.297824 (49% reduction in RMSE over 19 experiments)
- **Optimal learning rate:** lr=0.01 is the sweet spot — lr=0.005 underfits (RMSE 2.411) and lr=0.05 overfits (RMSE 2.440). Lower is not always better.
