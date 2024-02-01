# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 11:32:56 2024

@author: duter
"""

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data_03/time_series_data.csv", index_col=0)

print(df.info())

df['Date']=pd.to_datetime(df['Date'], format="%Y-%m-%d")

print(df.info())

"""
# Line plot

plt.plot(df['Date'], df['Temperature'])
plt.xlabel("Date")
plt.ylabel("Temperature")
plt.show()

"""

df['Temperature'].plot(kind='hist', bins=20, title='Temperature')
plt.show()
