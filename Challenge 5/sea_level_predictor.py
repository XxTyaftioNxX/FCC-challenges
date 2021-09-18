import pandas as pd
from scipy.stats import linregress
import matplotlib.pyplot as plt


def draw_plots():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

    # Create first line of best fit
    result = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    m = result.slope
    b = result.intercept

    x_range = range(1880, 2051)
    ax.plot(x_range, m*x_range+b, color='red')

    # Create second line of best fit
    df_2000 = df[df['Year'] >= 2000]
    result_2000 = linregress(df_2000['Year'], df_2000['CSIRO Adjusted Sea Level'])
    m_2000 = result_2000.slope
    b_2000 = result_2000.intercept

    x_range_2000 = range(2000, 2051)
    ax.plot(x_range_2000, m_2000*x_range_2000+b_2000, color='orange')

    # Add labels and title
    ax.set_title('Rise in Sea Level')
    ax.set_xlabel("Year")
    ax.set_ylabel("Sea Level (inches)")

    plt.savefig('sea_level_plot.png')
    return plt.show()


(draw_plots())






