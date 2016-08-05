import pandas as pd

unames = ['user_id', 'gender', 'age', 'occupation', 'zip']
users = pd.read_table('../data/ml-1m/users.dat', sep='::', header=None, names=unames)

rnames = ['user_id', 'movie_id', 'rating', 'timestamp']
ratings = pd.read_table('../data/ml-1m/ratings.dat', sep='::', header=None, names=rnames)

mnames = ['movie_id', 'title', 'genres']
movies = pd.read_table('../data/ml-1m/movies.dat', sep='::', header=None, names=mnames)

# Show data
print users[:5]

print ratings[:5]

print movies[:5]

# merge data
data = pd.merge(pd.merge(ratings, users), movies)


# See what in data
print data[:5]


'''
DataFrame.ix
A primarily label-location based indexer, with integer position fallback.

.ix[] supports mixed integer and label based access. It is primarily label based, but will fall back to integer positional access unless the corresponding axis is of integer type.

.ix is the most general indexer and will support any of the inputs in .loc and .iloc. .ix also supports floating point label schemes. .ix is exceptionally useful when dealing with mixed positional and label based hierachical indexes.

However, when an axis is integer based, ONLY label based access and not positional access is supported. Thus, in such cases, it’s usually better to be explicit and use .iloc or .loc.
'''
print  data.ix[0]

# see what is for data.ix[:5]
print data.ix[:5]

'''
pivot 

Explort table with one or more group

NOTE: in book, it use 'rows' instead of 'index', but in new pandas version, 'rows' is not supported

'''
mean_ratings = data.pivot_table('rating', index = 'title', columns='gender', aggfunc='mean')


'''
Group dataframe, and get size for each group
'''
# Example : group by title
ratings_by_title = data.groupby('title').size()

print ratings_by_title[:10]

# Filter with rating size > 250
active_titles = ratings_by_title.index[ratings_by_title >= 250]

print active_titles

# use index of receiving at least 250 rating , to select rows from mean_rating
mean_ratings = mean_ratings.ix[active_titles]
print mean_ratings

# sort by rating 
top_female_ratings = mean_ratings.sort_index(by='F', ascending=False)

# Measuring rating disaggrement between male fand female
mean_ratings['diff'] = mean_ratings['M'] - mean_ratings['F']

sorted_ty_diff = mean_ratings.sort_index(by='diff')
print sorted_ty_diff[:5]

# Reverse order of rows, take first 15 rows
print sorted_ty_diff[::-1][:15]

# Get the movies with the most disaggrement among viewer, independent of gender.
# use variance or stand deviation of ratings

rating_std_by_title = data.groupby('title')['rating'].std()

# Filter down to active title
rating_std_by_title = rating_std_by_title.ix[active_titles]

rating_std_by_title.order(ascending=False)[:10]

















