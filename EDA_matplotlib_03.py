# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 09:27:57 2024

@author: duter
"""

#EDA -> Exploratory Data Analysis

import matplotlib.pyplot as plt

# ---USING MATPLOTLIB---

# Line plot

"""
react_conv = [0.5, 0.6, 0.7, 0.7, 0.9]
temp = [180, 200, 220, 240, 260]

plt.plot(temp, react_conv)
plt.xlabel("Temperature")
plt.ylabel("Reaction Conversion")
plt.title("Chemical Experiment")
plt.show()
"""

# Bar plot

"""

day1_attendees = [70, 20, 64, 90, 80]
day1_names = ["Blessing", "Mali", "Pangi", "Tafi", "Shini"]

plt.bar(day1_names, day1_attendees)
plt.xlabel("Names")
plt.ylabel("Attendees")
plt.title("CSS2024 Attendees")
plt.show
"""

# Scatter plot

"""
x_scatter = [1, 2, 3, 4, 5]
y_scatter = [2, 4, 6, 8, 10]

plt.scatter(x_scatter, y_scatter)
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Data")
plt.show()
"""

# Histogram

x_histogram = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5]
plt.hist(x_histogram)
plt.title("Data")
plt.show()
