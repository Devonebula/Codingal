import pandas as pd
import numpy as np

data={"Name":["Pankaj", "Meghna", "David", "Lisa"],
      "Role":["CEO", None, None, None],
      "Sallary":[100, 200, None, None]
      }

df=pd.DataFrame(data)

print(df.loc[0:1],"\n")
# printing first two rows

print(df.loc[2:3],"\n")
# printing last two rows

print(df.isnull().sum(),"\n")
# getting all the null values and giving number that how many null values are there in each column

print(df.info(),"\n")
# printing detailed information of the dataframe

new_df_row= df.dropna()
print(new_df_row,"\n")
# dropping the null values in rows and printing the new dataframe

new_df_col= df.dropna(axis=1)
print(new_df_col,"\n")
# dropping the null values in columns and printing the new dataframe

df["Sallary"].fillna(300, inplace=True)
print(df,"\n")
# replacing the null values in sallary column with 300

