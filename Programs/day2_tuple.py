locations=('Dallas', 'Austin', 'Dallas','Houston', 'San fransisco','Dallas','Austin')
# print(locations)
# # print(locations[0])
# # print(locations[2:])
# print(locations.count('Dallas')) # returns count of the item in the tuple
# print(locations.index('Austin')) # returns index of the first occurrence of the item

# locations[0]='New York' # TypeError: 'tuple' object does not support item assignment]
# print(locations)

# def getEmployee ():
#     return ('Meghana', 'Devops Engineer',34000)

# name,designation,salary=getEmployee() # unpacking
# print(f'Name: {name}, Designation: {designation}, Salary: {salary}')    

# city1,city2,*city3=locations # unpacking
# print(f'City1: {city1}, City2: {city2}, City3: {city3}') # City1: Dallas, City2: Austin, City3: ['Houston', 'San fransisco']

# # iterating through tuple
# for city in locations:
#     print(city)

team=(('Meghana', 'Devops Engineer',34000),
      ('Sreenithya', 'Data Engineer', 35000),
      ('Sreeja', 'Data Analyst', 32000))

for name, designation, salary in team:
    print(f'Name: {name}, Designation: {designation}, Salary: {salary}')      
