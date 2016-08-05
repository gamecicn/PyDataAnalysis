import pandas as pd

names1880 = pd.read_table('../data/yob1880.txt', sep = ',', header=None, names=['name', 'sex', 'births'])

print names1880.head(10)

names1880.groupby('sex').births.sum()

# collect all years data
years = range(1880, 2015)

pieces = []

columns = ['name', 'sex', 'birth']

for year in years:
    path = '../data/yob%d.txt' % year
    frame = pd.read_csv(path, names=columns)
    
    frame['year'] = year
    pieces.append(frame)

# concatenate everything into a sigle DataFrame
names = pd.concat(pieces, ignore_index = True)
    






































































