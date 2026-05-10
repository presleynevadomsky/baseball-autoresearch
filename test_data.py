import os
import pandas as pd
from pybaseball import statcast_outfielder_jump, statcast_sprint_speed

os.makedirs("data", exist_ok=True)

# Pull outfielder jump data for all available years
print("Pulling outfielder jump data...")
jump_dfs = {}
for year in range(2016, 2025):
    df = statcast_outfielder_jump(year)
    df['year'] = year
    jump_dfs[year] = df
    print(f"{year}: {len(df)} rows")

# Pull sprint speed data for all years
print("\nPulling sprint speed data...")
speed_dfs = {}
for year in range(2016, 2025):
    df = statcast_sprint_speed(year)
    df['year'] = year
    speed_dfs[year] = df
    print(f"{year}: {len(df)} rows")

# Build year-matched pairs: X = year N features, y = year N+1 OAA
print("\nBuilding year-matched pairs...")
rows = []

for year in range(2016, 2024):  # 2016-2023 as input years
    current = jump_dfs[year].copy()
    next_year = jump_dfs[year + 1][['resp_fielder_id', 'outs_above_average']].copy()
    next_year.columns = ['resp_fielder_id', 'next_year_oaa']
    
    # Merge sprint speed and age
    speed = speed_dfs[year][['player_id', 'sprint_speed', 'age']].copy()
    current = current.merge(speed, 
        left_on='resp_fielder_id', 
        right_on='player_id', 
        how='left')
    
    # Merge next year OAA
    current = current.merge(next_year, on='resp_fielder_id', how='inner')
    
    rows.append(current)
    print(f"{year} -> {year+1}: {len(current)} matched pairs")

all_data = pd.concat(rows, ignore_index=True)

# Features to keep
KEEP_COLS = [
    'last_name, first_name', 'resp_fielder_id', 'year',
    'rel_league_burst_distance', 'rel_league_reaction_distance',
    'rel_league_routing_distance', 'rel_league_bootup_distance',
    'f_bootup_distance', 'sprint_speed', 'age',
    'next_year_oaa'
]

all_data = all_data[[c for c in KEEP_COLS if c in all_data.columns]]
all_data = all_data.dropna()

# Split: train/val = 2016-2022 input years, test = 2023 only
train_val = all_data[all_data['year'] <= 2022].copy()
test = all_data[all_data['year'] == 2023].copy()

train_val.to_csv("data/train_val.csv", index=False)
test.to_csv("data/test.csv", index=False)

print(f"\nTrain/val: {len(train_val)} rows")
print(f"Test: {len(test)} rows")
print(f"Columns: {all_data.columns.tolist()}")