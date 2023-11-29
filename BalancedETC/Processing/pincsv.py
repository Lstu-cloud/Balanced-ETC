import pandas as pd
import os

file_dir = r'C:\Processing_classification\Processing_classification\Processing_classification\TTTTST'
files = os.listdir(file_dir)
df1 = pd.read_csv(os.path.join(file_dir, files[0]))

for e in files[1:]:
    df2 = pd.read_csv(os.path.join(file_dir, e))
    df1 = pd.concat((df1, df2), axis=0, join='inner')

    df1.to_csv("TTTTTTST" + ".csv", index=0, sep=',')
print(df1)
