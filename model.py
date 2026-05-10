from sklearn.linear_model import LinearRegression
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

def build_model():
    """
    Baseline: linear regression using all physical features.
    The agent will modify this function each iteration.
    """
    return Pipeline([
        ("scaler", StandardScaler()),
        ("model", LinearRegression())
    ])

FEATURES = [
    "rel_league_burst_distance",
    "rel_league_reaction_distance",
    "rel_league_routing_distance",
    "rel_league_bootup_distance",
    "f_bootup_distance",
    "sprint_speed",
    "age"
]