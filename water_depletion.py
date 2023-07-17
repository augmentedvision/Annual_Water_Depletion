import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os
from datetime import datetime

df1 =pd.read_excel(
        r"/Users/brandonwu/Downloads/ANNUAL_WATER_DEPLETION.xls")

print(df1.shape)

new_header = df1.iloc[2].tolist()  # grab the third row for the header
df1 = df1[1:]  # take the data less the header row
df1.columns = new_header  # set the header row as the df header
print(df1.columns.tolist())

df2 = pd.read_excel
#print(df.shape)
# df["Country Name"].value_counts().plot(kind="bar")
# print(df["2020"].value_counts())
# df["2020"].plot().show()
