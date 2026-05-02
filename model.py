from sklearn.ensemble import GradientBoostingRegressor
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

def build_model():
    return Pipeline([
        ("scaler", StandardScaler()),
        ("model", GradientBoostingRegressor(n_estimators=500, max_depth=3, learning_rate=0.01, subsample=0.8, random_state=42))
    ])

FEATURES = [
    "rel_league_routing_distance",
    "rel_league_burst_distance",
    "rel_league_reaction_distance",
    "rel_league_bootup_distance",
    "f_bootup_distance",
    "outs_per_play",
    "sprint_speed"
]