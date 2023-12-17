
# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)

# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

# import pandas
# data = pandas.read_csv("weather_data.csv")


# data_dict = data.to_dict()
# print(data_dict)


# get data in column and compute
# temp_list = data["temp"].to_list()
# mean_temp = sum(temp_list)/len(temp_list)
# print(mean_temp)
# print(data["temp"].mean())
# print(data["temp"].max())
# print(data.temp.max())

# get Data in row
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])


# create a dataframe from scratch
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
#
# data = pandas.DataFrame(data_dict)
# # print(data)
# data.to_csv =("new_data.csv")

import pandas
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
grey = data[data["Primary Fur Color"] == "Gray"]
grey_counts = len(grey)
# print(grey_counts)
black = data[data["Primary Fur Color"] == "Black"]
black_counts = len(grey)
cinnamon = data[data["Primary Fur Color"] == "cinnamon"]
cinnamon_counts = len(grey)
counts =[grey_counts,black_counts,cinnamon_counts]
colors =[grey, black, cinnamon]

data_dict = {
    "Fur color": ["Grey", "Cinnamon", "Black"],
    "Count" : [grey_counts,cinnamon_counts, black_counts]
}
data = pandas.DataFrame(data_dict)
data.to_csv("Squirrel count.csv")