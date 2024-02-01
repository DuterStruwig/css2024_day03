# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 10:23:27 2024

@author: duter
"""

import plotly.express as px

#---USING PLOTLY---

# Line plot

"""
react_conv = [0.5, 0.6, 0.7, 0.7, 0.9]
temp = [180, 200, 220, 240, 260]

fig = px.line(x = temp, y = react_conv)

fig.write_html("plot.html")
"""

# Bar plot

day1_attendees = [70, 20, 64, 90, 80]
day1_names = ["Blessing", "Mali", "Pangi", "Tafi", "Shini"]

fig = px.bar(x = day1_names, y = day1_attendees)

fig.write_html("plot2.html")

# To automatically open up a browser of your plot

import webbrowser

#webbrowser.open("plot2.html")

