from xgboost import XGBRegressor
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import PowerTransformer

def build_model():
    return Pipeline([
        ("scaler", PowerTransformer()),
        ("model", XGBRegressor(n_estimators=500, max_depth=1, learning_rate=0.05,
                               reg_lambda=50, reg_alpha=1.0, random_state=42, verbosity=0))
    ])

FEATURES = [
    "rel_league_burst_distance",
    "rel_league_reaction_distance",
    "rel_league_routing_distance",
    "rel_league_bootup_distance",
    "f_bootup_distance",
    "sprint_speed"
]