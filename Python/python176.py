import pandas as pd
import numpy as np

exam_data={
    'Name': ['Keshav', 'Dima', "Raj", "James", "Macaulay", "Colebrooke", "Cameron", "John", "Ronaldo", "Messi"],
    'Score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
    "attempts":[1,3,4,5,1,3,2,1,1,2],
    "qualify":["yes", "no", "yes", "no", "no", "yes", "yes", "no", "no", "yes"]
    }

labels=[1,2,3,4,5,6,7,8,9,10]

df=pd.DataFrame(exam_data, index=labels)
print(df)
