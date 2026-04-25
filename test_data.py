import os
import pandas as pd
from pybaseball import statcast_outfielder_jump, statcast_sprint_speed

os.makedirs("data", exist_ok=True)

# Pull outfielder jump data for training years
dfs = []
for year in [2019, 2020, 2021, 2022, 2023]:
    df = statcast_outfielder_jump(year)
    dfs.append(df)
    print(f"{year}: {len(df)} rows")

train_val = pd.concat(dfs, ignore_index=True)

# Pull sprint speed for same years and merge
speed_dfs = []
for year in [2019, 2020, 2021, 2022, 2023]:
    df = statcast_sprint_speed(year)
    df['year'] = year
    speed_dfs.append(df)

speed = pd.concat(speed_dfs, ignore_index=True)
speed = speed[['player_id', 'year', 'sprint_speed']]
train_val = train_val.merge(speed,
    left_on=['resp_fielder_id', 'year'],
    right_on=['player_id', 'year'],
    how='left')

train_val.to_csv("data/train_val.csv", index=False)
print(f"\nTrain/val saved: {len(train_val)} rows")
print(f"Columns: {train_val.columns.tolist()}")

# Test set is 2024 — most recent season, fully locked
df_2024 = statcast_outfielder_jump(2024)
speed_2024 = statcast_sprint_speed(2024)
speed_2024['year'] = 2024
speed_2024 = speed_2024[['player_id', 'year', 'sprint_speed']]
df_2024 = df_2024.merge(speed_2024,
    left_on=['resp_fielder_id', 'year'],
    right_on=['player_id', 'year'],
    how='left')

df_2024.to_csv("data/test.csv", index=False)
print(f"Test saved: {len(df_2024)} rows")