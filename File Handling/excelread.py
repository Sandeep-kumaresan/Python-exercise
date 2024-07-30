import pandas as pd
filepath='student.xlsx'
df=pd.read_excel(filepath)
print("Excel contents:")
print(df)
print("few elements")
print(df.head())