# AutoResearch Program: Predicting Next-Year Defensive Value in MLB

## Objective

You are an autonomous research agent. Your goal is to discover the best model for predicting an outfielder's Outs Above Average (OAA) **next season** using only their physical tracking data from **this season**.

This is a forward-looking prediction problem — the model should help teams identify which players will be elite defenders next year before the season starts, based purely on physical skills.

You will do this by modifying `model.py` one change at a time, evaluating the result, and keeping or discarding the change based on whether it improves val_rmse.

## What You May Modify

You may ONLY modify `model.py`. Nothing else.

Specifically, you may change:
- The `FEATURES` list — which physical tracking variables to include
- The `build_model()` function — which sklearn model and parameters to use

## What You Must Never Touch

- `prepare.py` — frozen, do not modify
- `run.py` — frozen, do not modify
- `data/` — do not modify any data files
- `results.tsv` — do not modify manually, it is written by run.py
- `program.md` — frozen, this is the human's instruction file
- `experiments.md` — do not modify manually, update after each run per step 8

## Dataset

- **Input (X):** Average of year N-1 and year N physical tracking stats (2-year average) for each outfielder
- **Target (y):** Year N+1 OAA for the same outfielder
- **Train/val:** 2017-2021 seasons (302 matched pairs)
- **Test:** 2022-2023 seasons → next-year OAA (131 rows, locked — do not touch)
- **Note:** If a player only appears in year N (not N-1), year N stats are used alone

## Available Features

You may use any combination of these variables in FEATURES:

- `rel_league_burst_distance` — burst speed relative to league average
- `rel_league_reaction_distance` — reaction time relative to league average
- `rel_league_routing_distance` — route efficiency relative to league average
- `rel_league_bootup_distance` — first step relative to league average
- `f_bootup_distance` — absolute first step distance
- `sprint_speed` — player sprint speed in ft/sec
- `age` — player age (important for predicting year-over-year change)

## Available Models

You may use any sklearn-compatible estimator inside build_model(). Some options to explore:

- `LinearRegression()` — baseline, simple linear model
- `Ridge(alpha=...)` — linear model with regularization
- `Lasso(alpha=...)` — linear model that can zero out weak features
- `RandomForestRegressor(n_estimators=...)` — ensemble of decision trees
- `GradientBoostingRegressor(n_estimators=..., max_depth=...)` — powerful ensemble
- `XGBRegressor(...)` — if xgboost is installed
- `SVR(kernel=..., C=...)` — support vector regression

You can also combine feature engineering with any model using sklearn Pipelines:
- `PolynomialFeatures(degree=2)` — adds interaction terms between features
- `StandardScaler()` — normalizes features (already in baseline)

## How to Run an Experiment

Make sure your virtual environment is activated:
```bash
source stat390/bin/activate
```

Then run:
```bash
python3 run.py "<short description of what you changed>"
```

## Current Best

Check results.tsv to find the current best val_rmse before starting. Beat this number to keep a change.

## Keep / Discard Rule

- If new val_rmse < current best val_rmse → KEEP the change
- If new val_rmse >= current best val_rmse → REVERT model.py to previous version

## Experiment Log

All results are automatically logged to `results.tsv` with timestamp, description, features, val_rmse, and runtime.

## Loop Instructions

1. Read results.tsv to find the current best val_rmse
2. Propose one change to model.py
3. Activate venv and run: `python3 run.py "<description>"`
4. Compare new val_rmse to current best
5. Keep or revert
6. Repeat for at least 20 iterations
7. After all iterations run: `python3 prepare.py` to generate performance.png
8. After each experiment, append a new row to `experiments.md` with: experiment number, description of what changed, val_rmse, keep or discard decision, and error type (Signal Failure, Code Instability, Agent Misbehavior, or Evaluation Leakage)