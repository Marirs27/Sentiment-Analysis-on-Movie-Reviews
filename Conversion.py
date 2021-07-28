import pandas as pd
import matplotlib.pyplot as plt
import pyprind as pyp
import numpy as np
import os

# Labeling positive and negative ...
labels = {"pos":1,"neg":0}

# Initializing dataframe ...
data = pd.DataFrame()

# Connecting the dataframe to the data ...
pper = pyp.ProgPercent(50000)
for s in ('test', 'train'):
    for n in ('pos', 'neg'):
        path ='./aclImdb/%s/%s' % (s, n)
        for file in os.listdir(path):
            with open(os.path.join(path, file), encoding="utf8") as infile:
                text = infile.read()
            data = data.append([[text, labels[n]]], ignore_index=True)
            pper.update()

data.columns = ['review', 'sentiment']

np.random.seed(0)

# Shuffle data
data = data.reindex(np.random.permutation(data.index))

# Convert into a single CSV file.
data.to_csv('./movie_reviews_data.csv', index=False)

print("movie_reviews_data.csv file is created")