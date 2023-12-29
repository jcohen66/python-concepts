import pandas as pd 

data = pd.read_csv("./insurance.csv")


head = data.head()

print(f"Head: \n{head}\n")

print(f"Shape: \n{data.shape}\n")
print(f"Info: \n{data.info()}\n")
print(f"Nulls \n{data.isnull()}\n")
print(f"Sum: \n{data.isnull().sum()}\n")
print(f"DataTypes: \n {data.dtypes}\n")

# Data preprocessing
data['sex'] = data['sex'].astype('category')
data['region'] = data['region'].astype('category')
data['smoker'] = data['smoker'].astype('category')

print(f"DTYPES \next(iterable, default){data.dtypes}\n")

print(f"Describe: \n{data.describe().T}\n")

smoke_data = data.groupby("smoker").count()

print(smoke_data)

import seaborn as sns

sns.set_style("whitegrid")
sns.pairplot(
    data[["age", "bmi", "charges", "smoker"]],
    hue = "smoker",
    height = 3,
    palette = "Set1"
)
sns.heatmap(data.corr(), annot=True)