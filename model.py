from sklearn.linear_model import LinearRegression
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

def build_model():
    """
    Baseline: linear regression using routing distance only.
    The agent will modify this function each iteration.
    """
    return Pipeline([
        ("scaler", StandardScaler()),
        ("model", LinearRegression())
    ])

FEATURES = [
    "rel_league_routing_distance"
]