import sys
import time
import pandas as pd
import numpy as np
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
from datetime import datetime
from model import build_model, FEATURES

# ── Load data ──────────────────────────────────────────────────────────────
df = pd.read_csv("data/train_val.csv")
TARGET = "next_year_oaa"

# Drop missing
df = df.dropna(subset=FEATURES + [TARGET])

# ── Fixed train/val split (same seed every run) ────────────────────────────
X = df[FEATURES]
y = df[TARGET]
X_train, X_val, y_train, y_val = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# ── Build and train model ──────────────────────────────────────────────────
start = time.time()
model = build_model()
model.fit(X_train, y_train)
preds = model.predict(X_val)
val_rmse = np.sqrt(mean_squared_error(y_val, preds))
runtime = round(time.time() - start, 2)

# ── Description from command line ─────────────────────────────────────────
desc = sys.argv[1] if len(sys.argv) > 1 else "no description"

# ── Log result ────────────────────────────────────────────────────────────
result = {
    "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    "description": desc,
    "features": str(FEATURES),
    "val_rmse": round(val_rmse, 6),
    "runtime_sec": runtime
}

log = pd.DataFrame([result])
header = not pd.io.common.file_exists("results.tsv")
log.to_csv("results.tsv", sep="\t", mode="a", header=header, index=False)

print(f"Description: {desc}")
print(f"Features: {FEATURES}")
print(f"val_rmse: {val_rmse:.6f}")
print(f"Runtime: {runtime}s")