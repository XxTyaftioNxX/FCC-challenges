import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
df = pd.read_csv('medical_examination.csv')

# Add 'overweight' column
df['overweight'] = (df['weight'] / (df['height'] * df['height'] / 10000 ) > 25).astype(int)

# Normalize data by making 0 always good and 1 always bad. 
# If the value of 'cholesterol' or 'gluc' is 1, make the value 0. 
# If the value is more than 1, make the value 1.

df['cholesterol'], df['gluc']   = (df['cholesterol'] >= 2).astype(int), (df['gluc'] >= 2).astype(int)


#Convert the data into long format and create a chart that shows the value counts of the 
# categorical features using seaborn's catplot(). 
# The dataset should be split by 'Cardio' so there is one chart for each cardio value. 
# The chart should look like examples/Figure_1.png.
# Create DataFrame for cat plot using `pd.melt` using just the values from 
# 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.

columns = [
      'active',
      'alco',
      'cholesterol',
      'gluc',
      'overweight',
      'smoke'
    ]

df_cat = pd.melt(df, id_vars=["cardio"], value_vars=columns)

# Group and reformat the data to split it by 'cardio'. Show the counts of each feature. 
# You will have to rename one of the collumns for the catplot to work correctly.

df_cat = df_cat.reset_index().groupby(['variable', 'cardio', 'value']).agg('count') \
            .rename(columns={'index': 'total'}).reset_index()

# Draw the catplot with 'sns.catplot()'
fig = sns.catplot(
        x="variable",
        y="total",
        col="cardio",
        hue="value",
        data=df_cat,
        kind="bar").fig

#plt.show() 

# Draw Heat Map
def draw_heat_map():
    # Clean the data
    #Filter out the following patient segments that represent incorrect data:
    #diastolic pressure is higher than systolic (Keep the correct data with (df['ap_lo'] <= df['ap_hi']))
    #height is less than the 2.5th percentile (Keep the correct data with (df['height'] >= df['height'].quantile(0.025)))
    #height is more than the 97.5th percentile
    #weight is less than the 2.5th percentile
    #weight is more than the 97.5th percentile

    df_heat = df[(df['ap_lo'] <= df['ap_hi']) & (df['height'] >= df['height'].quantile(0.025)) 
                & (df['height'] <= df['height'].quantile(0.975)) & (df['weight'] >= df['weight'].quantile(0.025))
                &  df['weight'] <= df['weight'].quantile(0.975)]

    # Calculate the correlation matrix
    corr = df_heat.corr()

    # Generate a mask for the upper triangle
    mask = np.zeros_like(corr)
    mask[np.triu_indices_from(mask)] = True

    # Set up the matplotlib figure
    fig, ax = plt.subplots(figsize=(10, 12))

    # Draw the heatmap with 'sns.heatmap()'
    sns.heatmap(corr, annot=True, fmt='.1f', mask=mask, vmin=.16, vmax=.32, center=0)
    #plt.show()


#draw_heat_map()