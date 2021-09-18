import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv("fcc-forum-pageviews.csv", parse_dates=['date'], index_col='date')

#Clean the data by filtering out days when the page views were in 
#the top 2.5% of the dataset or bottom 2.5% of the dataset.

df = df[(df['value'] >= df['value'].quantile(0.025)) & (df['value'] <= df['value'].quantile(0.975))]

#Create a draw_line_plot function that uses Matplotlib to draw a line chart similar to "examples/Figure_1.png". 
# The title should be "Daily freeCodeCamp Forum Page Views 5/2016-12/2019". 
# The label on the x axis should be "Date" and the label on the y axis should be "Page Views".


def draw_line_plot():

    fig, ax = plt.subplots(figsize=(12, 6))

    ax.plot(df.index, df['value'], color='red')

    ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    ax.set_xlabel('Date')
    ax.set_ylabel('Page Views')

    fig.savefig('line_plot.png')
    return fig

#Create a draw_bar_plot function that draws a bar chart similar to "examples/Figure_2.png". 
# It should show average daily page views for each month grouped by year. 
# The legend should show month labels and have a title of "Months". 
# On the chart, the label on the x axis should be "Years" and the label on the y axis should be "Average Page Views".

def draw_bar_plot():

    df_bar = df.copy()

    df_bar['month'], df_bar['year'] = df_bar.index.month, df_bar.index.year

    df_bar = df_bar.groupby(by=['year', 'month'])['value'].mean()
    df_bar = df_bar.unstack()

    fig = df_bar.plot.bar(legend=True, figsize=(12, 6), ylabel='Average Page Views', xlabel='Years').figure

    plt.legend(['January', 'February', 'March', 'April','May', 'June', 
                    'July', 'August', 'September', 'October', 'November', 'December'])

    plt.xticks(fontsize=10)
    plt.yticks(fontsize=10)
    
    fig.savefig('bar_plot.png')
    return fig

#Create a draw_box_plot function that uses Searborn to draw two adjacent box plots # similar to "examples/Figure_3.png". 
# These box plots should show how the values are distributed within a given year or month and how it compares over time. 
# The title of the first chart should be "Year-wise Box Plot (Trend)" and the title of 
# the second chart should be "Month-wise Box Plot (Seasonality)". 
# Make sure the month labels on bottom start at "Jan" and the x and x axis are labeled correctly.

def draw_box_plot():
    df_box = df.copy()

    df_box['year'], df_box['month'] = df_box.index.year, df_box.index.strftime('%b')
    df_box.reset_index(inplace=True)
    df_box['month_num'] = df_box['date'].dt.month
    df_box = df_box.sort_values('month_num')

    #Draw box plots using seaborn
    fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(12, 6))
    axes[0] = sns.boxplot(x=df_box['year'], y=df_box['value'], ax = axes[0])
    axes[1] = sns.boxplot(x=df_box['month'], y=df_box['value'], ax = axes[1])

    axes[0].set_title("Year-wise Box Plot (Trend)")
    axes[0].set_xlabel('Year')
    axes[0].set_ylabel('Page Views')

    axes[1].set_title("Month-wise Box Plot (Trend)")
    axes[1].set_xlabel('Month')
    axes[1].set_ylabel('Page Views')

    fig.savefig('box_plot.png')
    return fig




draw_box_plot()