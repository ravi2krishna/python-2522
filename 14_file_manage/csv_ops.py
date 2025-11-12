# Working With CSV files 

import csv

# Read Data 
with open("14_file_manage/students.csv","r") as file_data:
    # print(file_data)
    csv_reader = csv.reader(file_data)
    # print(csv_reader)
    for row in csv_reader:
        print(row)

print("=" * 50)

# Assume we have 10k records like this 
# Customer Requirement : Fetch me details of Hyderabad customers 
filter_by_city = "Hyderabad"
with open("14_file_manage/students.csv","r") as file_data:
    csv_reader = csv.reader(file_data)
    for row in csv_reader:
        if row[3] == filter_by_city:
            print(row)

print("=" * 50)

# Assume we have 10k records like this 
# Customer Requirement : Fetch me details of gmail customers 
filter_by_email = "@gmail.com"
with open("14_file_manage/students.csv","r") as file_data:
    csv_reader = csv.reader(file_data)
    for row in csv_reader:
        if row[1].endswith(filter_by_email):
            print(row)

print("=" * 50)
            
# As per some new business requirements we changed the structure of data set 
# Customer Requirement : Fetch me details of gmail customers 
filter_by_email = "@gmail.com"
with open("14_file_manage/sample.csv","r") as file_data:
    csv_reader = csv.reader(file_data)
    for row in csv_reader:
        if row[2].endswith(filter_by_email):
            print(row)

print("=" * 50)
            
# Now working with dynamic data sets not relying on fixed index 
filter_by_email = "@gmail.com"
with open("14_file_manage/sample.csv","r") as file_data:
    csv_reader = csv.DictReader(file_data)
    for row in csv_reader:
        # print(row)
        if row["email"].endswith(filter_by_email):
            print(row)

print("=" * 50)
            
filter_by_email = "@gmail.com"
with open("14_file_manage/students.csv","r") as file_data:
    csv_reader = csv.DictReader(file_data)
    for row in csv_reader:
        # print(row)
        if row["email"].endswith(filter_by_email):
            print(row)
        