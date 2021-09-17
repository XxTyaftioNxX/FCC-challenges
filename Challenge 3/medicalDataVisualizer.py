import pandas as pd

df = pd.read_csv('medical_examination.csv')

# Add 'overweight' column
df['overweight'] = df['weight'] / (df['height'] * df['height'] / 10000 ) > 25
df['overweight'] = df['overweight'].astype(int)

# Normalize data by making 0 always good and 1 always bad. 
# If the value of 'cholesterol' or 'gluc' is 1, make the value 0. 
# If the value is more than 1, make the value 1.
print(df)

df['cholesterol']  = df['cholesterol'] >= 2
df['cholesterol'] = df['cholesterol'].astype(int)

df['gluc']  = df['gluc'] >= 2
df['gluc'] = df['gluc'].astype(int)

print(df)
