"""show case the student data using pandas and python"""

import csv
import pandas as pd

df = pd.read_csv("D:\Progmamming\PYTHON\PANDAS\Student.csv")
print(df.head())  # by default first 5 rows we can use number as parameter
print(df.tail())  # value from buttom to top we can use number as parameter
print(df.info())  # full summary of the csv
print(df.describe())  # describe the numerical value statics
print(df.dtypes)  # information about
print(df.shape)  # rows*colums
print(df.columns)  # print all the columns name


# Adding new row in csv file using python build in methods
new_row = ["Rohit", 111, 22, "BSc CS", 90, "Delhi"]


with open("D:\Progmamming\PYTHON\PANDAS\Student.csv", "a", newline="\n") as file:
    writer = csv.writer(file)
    writer.writerow(new_row)

print("Row added successfully!")
