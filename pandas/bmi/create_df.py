import pandas as pd

column = ['Mariya', 'Batman', 'Spongebob']
titled_columns = {"name": column,
                  "height": [1.67, 1.9, 0.25],
                  "weight": [54, 100, 1]}
data = pd.DataFrame(titled_columns)

select_column = data['weight'][1]
select_row = data.iloc[1]['weight']

print(select_column)
print(select_row)

bmi = []
# weight/(height**2)
for i in range(len(data)):
    bmi_score = data["weight"][i]/(data["height"][i]**2)
    bmi.append(bmi_score)

data["bmi"] = bmi
data.to_csv("bmi.csv", sep='\t')

print(data)
