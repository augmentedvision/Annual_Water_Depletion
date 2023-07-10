import pandas as pd
df = pd.read_excel(r'/Users/brandonwu/Downloads/ANNUAL_WATER_DEPLETION.xls')
print(df.shape)
#print(df)
new_header = df.iloc[2].tolist() #grab the first row for the header
df = df[1:] #take the data less the header row
df.columns = new_header #set the header row as the df header
print(df.columns.tolist())

df["Country Name"].value_counts().plot(kind="bar")
print(df["2020.0"].value_counts())