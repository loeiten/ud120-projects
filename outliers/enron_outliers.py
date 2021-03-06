#!/usr/bin/python

import pickle
import sys
import matplotlib.pyplot as plt
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit


### read in data dictionary, convert to numpy array
data_dict = pickle.load( open("../final_project/final_project_dataset.pkl", "r") )
features = ["salary", "bonus"]
data = featureFormat(data_dict, features)

### your code below
max_salary = data[:,0].max()
max_bonus = data[:,1].max()
import pandas as pd
import numpy as np
df = pd.DataFrame(data_dict).transpose()
# Replace text nan with actual nan
df = df.replace("NaN", np.nan)
# Find row which matches the criterion (see from the plot that both are
# satisfied at once)
# Notice the use of bitwise comparison
hit = df[(np.isclose(df["salary"], max_salary)) & (np.isclose(df["bonus"], max_bonus))]
print("Outliner name: {}".format(hit.index[0]))

plt.scatter( data[:,0], data[:,1] )

plt.xlabel("salary")
plt.ylabel("bonus")
plt.show()
