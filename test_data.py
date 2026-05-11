import os
import pandas as pd
from pybaseball import statcast_outfielder_jump, statcast_sprint_speed

os.makedirs("data", exist_ok=True)

FEATURES = [
    'rel_league_burst_distance',
    'rel_league_reaction_distance', 
    'rel_league_routing_distance',
    'rel_league_bootup_distance',
    'f_bootup_distance',
    'sprint_speed',
    'age'
]

# Pull all data
print("Pulling outfielder jump data...")
jump_dfs = {}
for year in range(2016, 2025):
    df = statcast_outfielder_jump(year)
    df['year'] = year
    jump_dfs[year] = df
    print(f"{year}: {len(df)} rows")

print("\nPulling sprint speed data...")
speed_dfs = {}
for year in range(2016, 2025):
    df = statcast_sprint_speed(year)
    df['year'] = year
    speed_dfs[year] = df
    print(f"{year}: {len(df)} rows")

# Merge sprint speed into jump data for each year
print("\nMerging sprint speed...")
merged = {}
for year in range(2016, 2025):
    df = jump_dfs[year].copy()
    speed = speed_dfs[year][['player_id', 'sprint_speed', 'age']].copy()
    df = df.merge(speed, left_on='resp_fielder_id', right_on='player_id', how='left')
    merged[year] = df

# Build pairs: avg(year N-1, year N) → year N+1 OAA if both years available, else just year N
print("\nBuilding pairs...")
rows = []

for year in range(2017, 2024):
    curr = merged[year][['resp_fielder_id', 'last_name, first_name'] + FEATURES].copy()
    prev = merged[year - 1][['resp_fielder_id'] + FEATURES].copy()
    next_yr = jump_dfs[year + 1][['resp_fielder_id', 'outs_above_average']].copy()
    next_yr.columns = ['resp_fielder_id', 'next_year_oaa']

    # Merge next year OAA
    curr = curr.merge(next_yr, on='resp_fielder_id', how='inner')
    
    # Merge previous year (optional)
    prev = prev.rename(columns={f: f + '_prev' for f in FEATURES})
    curr = curr.merge(prev, on='resp_fielder_id', how='left')
    
    # Average where previous year exists, else use current year only
    for f in FEATURES:
        curr[f] = curr.apply(
            lambda row: (row[f] + row[f + '_prev']) / 2 
            if pd.notna(row[f + '_prev']) else row[f], axis=1
        )
    
    # Drop prev columns
    curr = curr.drop(columns=[f + '_prev' for f in FEATURES])
    curr['year'] = year
    rows.append(curr)
    print(f"{year}: {len(curr)} pairs")

all_data = pd.concat(rows, ignore_index=True)
all_data = all_data.dropna(subset=FEATURES + ['next_year_oaa'])

# Split
train_val = all_data[all_data['year'] <= 2021].copy()
test = all_data[all_data['year'] >= 2022].copy()

train_val.to_csv("data/train_val.csv", index=False)
test.to_csv("data/test.csv", index=False)

print(f"\nTrain/val: {len(train_val)} rows")
print(f"Test: {len(test)} rows")
print(f"Columns: {all_data.columns.tolist()}")