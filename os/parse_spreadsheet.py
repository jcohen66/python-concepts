import csv
csv_mapping_list = []
with open("/path/to/data.csv") as my_data:
    csv_reader = csv.reader(my_data, delimiter=",")
    line_count = 0
    for line in csv_reader:
        if line_count == 0:
            header = line
        else:
            row_dict = {key: value for key, value in zip(header, line)}
            csv_mapping_list.append(row_dict)
        line_count += 1
