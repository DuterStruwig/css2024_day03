# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 12:21:05 2024

@author: duter
"""

import pandas as pd
from ydata_profiling import ProfileReport

df = pd.read_csv("data_03/iris.csv")

profile = ProfileReport(df, title="Profiling Report")

profile.to_file("your_report.html")