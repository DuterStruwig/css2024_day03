# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 10:41:27 2024

@author: duter
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

iris_file = pd.read_csv("data_03/iris.csv")

iris_file["class"] = iris_file["class"].str.replace("Iris-", "")

# Plotting
"""
#Scatter

plt.scatter(iris_file["sepal_length"], iris_file["sepal_width"])
plt.xlabel("Sepal Length")
plt.ylabel("Sepal Width")

#Bar

plt.bar(iris_file["class"], iris_file["sepal_length"])

#Seaborn???

sns.pairplot(iris_file, hue="class")

"""

#Pie

class_count = iris_file['class'].value_counts() #To get the number of classes in the data

plt.pie(class_count, labels=class_count.index)

plt.show()