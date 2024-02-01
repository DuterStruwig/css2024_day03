# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 12:10:08 2024

@author: duter
"""

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel("Chat_files/chat_data_02.xlsx")

print(df.info())

plt.scatter(df["REFCODE"], df["Activation_Energy(kcal/mol)"])
plt.xlabel("REFCODE")
plt.ylabel("Activation_Energy(kcal/mol)")