import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import random as rand

file_path="USA_Housing.csv"
df = pd.read_csv(file_path)

print(df.head())

print(df.describe())

print(df.info())

sns.set_style("whitegrid")

plt.figure(figsize=(10,8))
sns.pairplot(df.drop("Address", axis=1), diag_kind="kde", plot_kws={"alpha":0.6})
plt.suptitle("Pairplot of USA Housing Features", y=1.02)
plt.show()


plt.figure(figsize=(12,6))
sns.violinplot(data=df, x="Avg. Area Number of Bedrooms", y = "Price", palette="muted")
plt.title("Price distribution by no. of bedrooms")
plt.xlabel("Number of Bedrooms")  
plt.ylabel("Price")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()



plt.figure(figsize=(10,8))
sns.jointplot(data=df, x="Avg. Area Income", y="Price", kind='reg', color="purple",join_kws={"scatter_kws":{"alpha":0.6}}, marginal_kws={"bins":30})  
plt.xlabel("Avg. Area Income")
plt.ylabel("Price")
plt.tight_layout()
plt.show()