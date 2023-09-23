import pandas as pd
import sqlite3

connection = sqlite3.connect("gta.db")

gta_data = pd.read_sql_query("select * from gta", connection)

first_5_rows = gta_data.head(5)
last_2_rows = gta_data.tail(2)
print(first_5_rows)
print(last_2_rows)

# filter and replace
filtered_row = gta_data[ gta_data["city"] == "Liberty City" ]
replaced_city = gta_data.replace("Liberty City", "New York")
print(filtered_row)

# remove data
remove_column = gta_data.drop("city", axis=1)
remove_row = gta_data.iloc[1:4].drop("city", axis=1)
print(remove_column)

# add new rows
row = {
    "release_year": "2021",
    "release_name": "Natural Vision Evolved",
    "city": "Los Angeles"   
       }

# Note: .append() is now ._append()
new_row_data = gta_data._append(row, ignore_index=True)
print(new_row_data)

# Dedup dataframe rows
dedup_data = gta_data.drop_duplicates(subset=["city"])
print(dedup_data)

connection.close()