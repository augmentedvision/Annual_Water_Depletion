import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os
from datetime import datetime

df = pd.concat(
    pd.read_excel(
        r"/Users/brandonwu/Downloads/ANNUAL_WATER_DEPLETION.xls", sheet_name=None
    ),
    ignore_index=True,
)

print(df.shape)

new_header = df.iloc[2].tolist()  # grab the third row for the header
df = df[1:]  # take the data less the header row
df.columns = new_header  # set the header row as the df header
print(df.columns.tolist())
print(df.shape)
# df["Country Name"].value_counts().plot(kind="bar")
# print(df["2020"].value_counts())
# df["2020"].plot().show()
