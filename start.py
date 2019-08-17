import pandas as pd
import matplotlib.pyplot as plt


data = pd.ExcelFile('data/obes-phys-acti-diet-eng-2014-tab.xls')
# print(data.sheet_names)

# Define the columns to be read
columns1 = ['year', 'total', 'males', 'females']
data_gender = data.parse(u'7.1', skiprows=4, skipfooter=14, names=columns1)
data_gender.dropna(inplace=True)
data_gender.set_index('year', inplace=True)
# print(data_gender)
#data_gender.plot()
# plt.show()

data_age = data.parse('7.2', skiprows=4, skipfooter=14)
data_age.rename(columns={'Unnamed: 0': 'Year'}, inplace=True)
data_age.dropna(inplace=True)
data_age.set_index('Year', inplace=True)
data_age_minus_total = data_age.drop('Total', axis=1)
print(data_age)
#data_age_minus_total.plot()
#plt.show()

print(data_age['Under 16'])

# Plot children vs adults
data_age['Under 16'].plot(label = 'Under 16')
data_age['25-34'].plot(label = '25-34')
plt.legend(loc='upper left')
plt.show()

user_columns = ['user_id', 'age', 'sex']
users = pd.read_csv('data/ml-100k/u.user', sep='|', names=user_columns, 
                    usecols=range(3))
rating_columns = ['user_id', 'movie_id', 'rating']
ratings = pd.read_csv('data/ml-100k/u.data', sep='\t', 
                      names=rating_columns, usecols=range(3))
movie_columns = ['movie_id', 'title']
movies = pd.read_csv('data/ml-100k/u.item', sep='|', names=movie_columns,
                     usecols=range(2), encoding='iso-8859-1')
# Create one merged DataFrame
movie_ratings = pd.merge(movies, ratings)
movie_data = pd.merge(movie_ratings, users)

# Top rated movies
print('Top rated movies (overall):\n'), movie_data.groupby('title').size(
        ).sort_values(ascending=False)[:20]

oldies = movie_data[(movie_data.age > 60)]
oldies = oldies.groupby('title').size().sort_values(ascending=False)
# Extract movies for teens
teens = movie_data[(movie_data.age > 12) & (movie_data.age<20)]
teens = teens.groupby('title').size().sort_values(ascending=False)
print('Top ten movies for oldies: \n', oldies[:10])
print('Top ten movies for teens: \n', teens[:10])

ratings_by_title = movie_data.groupby('title').size()
popular_movies = ratings_by_title.index[ratings_by_title >= 250]
ratings_by_gender = movie_data.pivot_table('rating', index='title', columns='sex')
ratings_by_gender = ratings_by_gender.loc[popular_movies]
print('Top rated movies by gender \n', ratings_by_gender.head(10))

top_movies_women = ratings_by_gender.sort_values(by='F', ascending=False)
print('Top rated movies by women \n', top_movies_women.head(6))

ratings_by_gender['diff'] = ratings_by_gender['M'] - ratings_by_gender['F']
print('Difference by gender \n', ratings_by_gender.head(4))

gender_diff = ratings_by_gender['diff']
gender_diff = abs(gender_diff)
# Sort by size
gender_diff.sort_values(inplace=True, ascending=True)
gender_diff[:10].plot(kind='barh')
plt.show()































