#!/usr/bin/python

import pickle
import sys
import matplotlib.pyplot as plt
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit


### read in data dictionary, convert to numpy array
data_dict = pickle.load( open("../final_project/final_project_dataset.pkl", "r") )
# Remove the "TOTAL" outlier point
data_dict.pop("TOTAL", 0)
features = ["salary", "bonus"]
data = featureFormat(data_dict, features)

import pandas as pd
import numpy as np
df = pd.DataFrame(data_dict).transpose()
# Replace text nan with actual nan
df = df.replace("NaN", np.nan)
# Find row which matches the criterion (see from the plot that both are
# satisfied at once)
# Notice the use of bitwise comparison
hits = df[(df["salary"] > 1e6) & (df["bonus"] > 5e6)]
names = [hit for hit in hits.index]

for name in names:
    print("Outliner name: {}".format(name))

### your code below
plt.scatter( data[:,0], data[:,1] )

plt.xlabel("salary")
plt.ylabel("bonus")
plt.show()
