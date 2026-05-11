from sklearn.linear_model import Ridge
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import PowerTransformer

def build_model():
    return Pipeline([
        ("scaler", PowerTransformer(method="yeo-johnson")),
        ("model", Ridge(alpha=1.0))
    ])

FEATURES = [
    "rel_league_burst_distance",
    "rel_league_reaction_distance",
    "rel_league_routing_distance",
    "rel_league_bootup_distance",
    "f_bootup_distance",
    "sprint_speed"
]