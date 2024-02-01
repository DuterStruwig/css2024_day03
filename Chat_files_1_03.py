# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 11:49:00 2024

@author: duter
"""

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Chat_files/poker_2016_09_27.csv", names=["Time","NUN","x","y","z"])

df['Time']=pd.to_datetime(df['Time'], format='%H:%M:%S').dt.time

# Line plot

df.plot(x='Time', y=['x', 'y', 'z'])

plt.show()