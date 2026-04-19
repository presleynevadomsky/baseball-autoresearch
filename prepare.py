import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import os

# ── Load data ──────────────────────────────────────────────────────────────
df = pd.read_csv("data/train_val.csv")

# ── Define features and target ─────────────────────────────────────────────
FEATURES = [
    "rel_league_burst_distance",
    "rel_league_reaction_distance",
    "rel_league_routing_distance",
    "rel_league_bootup_distance",
    "f_bootup_distance",
    "outs_per_play"
]
TARGET = "outs_above_average"

# Drop rows with missing values
df = df.dropna(subset=FEATURES + [TARGET])

# ── Train / validation split (80/20, fixed seed for reproducibility) ───────
X = df[FEATURES]
y = df[TARGET]
X_train, X_val, y_train, y_val = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print(f"Train: {len(X_train)} rows | Val: {len(X_val)} rows")
print(f"Test set: locked in data/test.csv (not touched until final evaluation)")

# ── Plotting ───────────────────────────────────────────────────────────────
def plot_results():
    if not os.path.exists("results.tsv"):
        print("No results.tsv found yet.")
        return
    results = pd.read_csv("results.tsv", sep="\t")
    if len(results) == 0:
        print("No experiments logged yet.")
        return

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(results["val_rmse"], marker="o", color="steelblue", label="val_rmse")
    ax.axhline(results["val_rmse"].iloc[0], color="gray", linestyle="--", label="baseline")
    ax.set_xlabel("Iteration")
    ax.set_ylabel("Val RMSE")
    ax.set_title("AutoResearch: RMSE Over Iterations")
    ax.legend()
    plt.tight_layout()
    plt.savefig("performance.png")
    print("Saved performance.png")

if __name__ == "__main__":
    plot_results()