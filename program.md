# AutoResearch Program: Defensive Metric Discovery in MLB

## Objective

You are an autonomous research agent. Your goal is to discover a combination of Statcast defensive tracking variables that predicts Outs Above Average (OAA) better than the current best model.

You will do this by modifying `model.py` one change at a time, evaluating the result, and keeping or discarding the change based on whether it improves val_rmse.

## What You May Modify

You may ONLY modify `model.py`. Nothing else.

Specifically, you may change:
- The `FEATURES` list — which Statcast variables to include
- The `build_model()` function — which sklearn model and parameters to use

## What You Must Never Touch

- `prepare.py` — frozen, do not modify
- `run.py` — frozen, do not modify
- `data/` — do not modify any data files
- `results.tsv` — do not modify manually, it is written by run.py

## Available Features

You may use any combination of these variables in FEATURES:

- `rel_league_routing_distance` — route efficiency relative to league average
- `rel_league_burst_distance` — burst speed relative to league average
- `rel_league_reaction_distance` — reaction time relative to league average
- `rel_league_bootup_distance` — first step relative to league average
- `f_bootup_distance` — absolute first step distance
- `outs_per_play` — how often the player converts opportunities into outs
- `sprint_speed` — player sprint speed in ft/sec

## Available Models

You may use any sklearn-compatible estimator inside build_model(). Some options to explore:

- `LinearRegression()` — baseline, simple linear model
- `Ridge(alpha=...)` — linear model with regularization, try alpha values like 0.1, 1.0, 10.0
- `Lasso(alpha=...)` — linear model that can zero out weak features
- `RandomForestRegressor(n_estimators=...)` — ensemble of decision trees
- `GradientBoostingRegressor(n_estimators=..., max_depth=...)` — powerful ensemble
- `SVR(kernel=..., C=...)` — support vector regression

You can also combine feature engineering with any model using sklearn Pipelines:
- `PolynomialFeatures(degree=2)` — adds interaction terms between features
- `StandardScaler()` — normalizes features (already in baseline)

## How to Run an Experiment

Always use this exact command:
```bash
/Users/presleynevadomsky/Desktop/baseball-autoresearch/stat390/bin/python3 run.py "<short description of what you changed>"
```

This will:
1. Load your updated model.py
2. Train on 80% of train_val.csv
3. Score on the remaining 20%
4. Print and log val_rmse to results.tsv

## Keep / Discard Rule

- If new val_rmse < current best val_rmse → KEEP the change
- If new val_rmse >= current best val_rmse → REVERT model.py to previous version

## Current Baseline

- Features: `rel_league_routing_distance` only
- val_rmse: 4.524665
- Your job: beat this number

## Experiment Log

All results are automatically logged to `results.tsv` with timestamp, description, features, val_rmse, and runtime.

## Loop Instructions

1. Read results.tsv to review what has been tried
2. Propose one change to model.py
3. Run: `python3 run.py "<description>"`
4. Compare new val_rmse to current best
5. Keep or revert
6. Repeat for at least 20 iterations
7. After all iterations run: `python3 prepare.py` to generate performance.png