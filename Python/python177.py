import pandas as pd
import numpy as np

data={"name":['Keshav', "Alice", "Charlie"],
      "age":[13,12,14],
      "Sallary":[10000,20000,30000]
      }

df=pd.DataFrame(data)
print(df)


print(df.shape)
print(df.size)
print(df.info())
print(df.describe())
