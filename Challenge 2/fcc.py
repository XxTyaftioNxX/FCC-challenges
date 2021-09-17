import pandas as pd 

df = pd.read_csv('adult.data.csv')

# How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
race_count = pd.Series(df['race'].value_counts().tolist(), index=df['race'].value_counts().index)

# What is the average age of men?
average_age_men = round(df['age'].loc[df['sex'] == 'Male'].mean(), 1)

# What is the percentage of people who have a Bachelor's degree?
percentage_bachelors = round(df['education'].value_counts()['Bachelors'] / df.shape[0] * 100, 1)

# What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
higher_education = df[df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]

higher_education_rich = round(higher_education[higher_education['salary'] == '>50K'].shape[0] / higher_education.shape[0] * 100, 1)

# What percentage of people without advanced education make more than 50K?
lower_education = df[~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]

lower_education_rich = round(lower_education[lower_education['salary'] == '>50K'].shape[0] / lower_education.shape[0] * 100, 1)

# What is the minimum number of hours a person works per week (hours-per-week feature)?
min_work_hours = df['hours-per-week'].min()

# What percentage of the people who work the minimum number of hours per week have a salary of >50K?
num_min_workers = df[df['hours-per-week'] == df['hours-per-week'].min()]

rich_percentage = round(num_min_workers[num_min_workers['salary'] == '>50K'].shape[0] / num_min_workers.shape[0] * 100, 1)

# What country has the highest percentage of people that earn >50K?
country_sort = round(((df.loc[df['salary'] == '>50K'].groupby(by='native-country').count() / df.groupby(by = 'native-country').count())
                                                        .sort_values(by=['salary'], ascending=False)) * 100, 1)

highest_earning_country = country_sort.index[0]
highest_earning_country_percentage = country_sort.salary[0]

# Identify the most popular occupation for those who earn >50K in India.
top_IN_occupation = df[(df['native-country'] == 'India') &( df['salary'] == '>50K')].occupation.value_counts().index[0]

if __name__ == '__main__':
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

