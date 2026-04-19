import os
from pybaseball import statcast_outfielder_jump
import pandas as pd

os.makedirs("data", exist_ok=True)

# Pull 2021 and 2022 for training/validation
df_2021 = statcast_outfielder_jump(2021)
df_2022 = statcast_outfielder_jump(2022)

# Stack them together
train_val = pd.concat([df_2021, df_2022], ignore_index=True)
train_val.to_csv("data/train_val.csv", index=False)
print(f"Train/val saved: {len(train_val)} rows")

# 2023 is the locked test set
df_2023 = statcast_outfielder_jump(2023)
df_2023.to_csv("data/test.csv", index=False)
print(f"Test saved: {len(df_2023)} rows")