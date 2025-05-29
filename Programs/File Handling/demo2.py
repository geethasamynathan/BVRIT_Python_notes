# from os.path import exists

# path_to_file = "testfile14.txt"
# file_exists = exists(path_to_file)
# print(file_exists )

# from pathlib import Path

# # path = Path("Writing\\tutorial.md")
# path=Path("testfile1.txt")
# print(path.is_file())

# Example to Read CSV Content
# import csv

# with open('C:\\Users\\Lenovo\\Downloads\\country.csv', encoding='utf-8') as f:
#     reader = csv.reader(f)
#     for row in reader:
#         print(row)
        
# import csv

# with open('C:\\Users\\Lenovo\\Downloads\\country.csv', 'r') as f:
#     csv_reader = csv.reader(f)
#     for line_no,line in enumerate(csv_reader,1):
#         if line_no == 1:
#             print(f"Header")
#             print(line)
#             print('Records')
#         else:
#             print(line)

## Example to calculate total area from Csv file using CSV reader

# import csv

# total_area=0
# with open('C:\\Users\\Lenovo\\Downloads\\country.csv', 'r') as f:
#     csv_reader = csv.reader(f)
#     next(csv_reader) # Skip header
#     for line in csv_reader:
#         # Skip header
#         total_area += float(line[1])  # Assuming area is in the third column
       

# print(f'Total area of all countries is {total_area} sq.km')

## Example to calculate total area from Csv file using CSV DictReader
# import csv

# total_area=0
# with open('C:\\Users\\Lenovo\\Downloads\\country.csv', 'r') as f:
#     csv_reader = csv.DictReader(f)
#     next(csv_reader) # Skip header
#     for line in csv_reader:
#         # Skip header
#         total_area += float(line['area'])  # Assuming area is in the third column
       

# print(f'Total area of all countries is {total_area} sq.km')

## Example to write to CSV file using CSV
# import csv
# with open('C:\\Users\\Lenovo\\Downloads\\country1.csv', 'w') as f:
#     writer = csv.writer(f)
#     writer.writerow(['Country', 'Area', 'Population'])  # Write header
#     writer.writerow(['India', '3287263', '1393409038'])  # Write data


# import csv
# with open('country1.csv', 'w') as f:
#     writer = csv.writer(f)
#     data=[
#         ["Country", "Area", "Population"],
#         ["India", "3287263", "1393409038"],
#         ["USA", "9833517", "331002651"],
#         ["China", "9596961", "1439323776"]
#     ]
#     writer.writerows(data)  # Write multiple rows at once
#     f.seek(0) 

import csv

field_names= ['Country', 'Area', 'Population']    
data = [
         {'Country': 'India', 'Area': '3287263', 'Population': '1393409038'},
         {'Country': 'USA', 'Area': '9833517', 'Population': '331002651'},
         {'Country': 'China', 'Area': '9596961', 'Population': '1439323776'},
         {'Country': 'Brazil', 'Area': '8515767', 'Population': '212559417'},
         {'Country': 'Russia', 'Area': '17098242', 'Population': '145912025'}
]
with open('country1.csv', 'w+') as f:
    writer = csv.DictWriter(f, fieldnames=field_names)
    writer.writeheader()  # Write header
    writer.writerows(data)  # Write multiple rows at once
    f.seek(0)
    print(f"Content of country1.csv")
    print(f.read())