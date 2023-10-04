import pandas as pd

data = pd.read_csv("bmi.csv", sep='\t')

print(data)
print(data.head(1))
print(data.tail(1))

# Filter and replace
filtered_row = data[data["height"] < 1]
replaced_height = data.replace("height", data["height"] + 0.01)

# remove data
remove_column = data.drop(["height"], axis=1)
remove_row = data.iloc[1:4].drop("weight", axis=1)

# add new row
row = {"name": "Donna",
       "bmi": 15}

data.drop_duplicates(subset=["name"])
