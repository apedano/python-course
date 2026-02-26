# with open("weather_data.csv") as file:
#     lines = file.readlines()
#
# print(lines)

# import csv
#
# with open("weather_data.csv") as data_file:
#     reader = csv.reader(data_file)
#     temperatures = []
#     for row in reader:
#         try:
#             temperatures.append(int(row[1]))
#         except (ValueError):
#             print(f"row[1] is {row[1]}, not a valid integer. It is skipped.")
#
#         print(row) #Each row is ['day', 'temp', 'condition']
# print(temperatures)


import pandas as pd

data_dict = {"students":["Amy", "Wine", "House"], "scores":[90, 80, 70] }
df = pd.DataFrame(data_dict)
df.to_csv("data.csv")

print(df)


# data = pd.read_csv("weather_data.csv")
#
# #Extract column data (excluding the head)
# day_series= data["day"]
# temp_series = data["temp"]
# condition_series = data.condition
#
# print(condition_series)
# print(type(condition_series))
# # Get data in row
# monday_data=data[data.day== "Monday"]
#
# print(monday_data)
# print(type(monday_data))






# print(type(data))
# print(type(data["temp"]))
