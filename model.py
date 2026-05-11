from sklearn.linear_model import LinearRegression
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import PowerTransformer

def build_model():
    return Pipeline([
        ("scaler", PowerTransformer(method="yeo-johnson")),
        ("model", LinearRegression())
    ])

FEATURES = [
    "rel_league_burst_distance",
    "rel_league_reaction_distance",
    "rel_league_routing_distance",
    "rel_league_bootup_distance",
    "f_bootup_distance",
    "sprint_speed"
]