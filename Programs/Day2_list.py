# my_list=[1,2,4,5,6]
# print(my_list)
# print(len(my_list))
# print(my_list[0])
# print (my_list[1:])
# print (my_list[:4])
# print(my_list+['test data']) # newly added item will not be available in original list
# my_list=my_list+['test data']

# mylist2=['Meghana','Sreenithya','Sreeja']
# my_list.append(mylist2) # newly added item will be available in original list
# print(my_list)

# # double the list
# my_list=my_list*2
# print(my_list)  

# popped_item=my_list.pop() # remove last element
# print(popped_item)
# print(my_list)

# # can we remove item in a specifix  index using pop
# popped_item=my_list.pop(2) # remove last element
# print(popped_item)
# print(my_list)

# print(my_list.index('test data')) # returns index of the first occurrence of the item
# print(my_list.count('test data')) # returns count of the item in the list


#list1=[1,2,3,4]
#list2=[5,6,7,8]
# # list3=list1+list2
# # print(list3)

# matrix=[list1,list2]
# print(matrix)
# print(matrix[0])
# print(matrix[0][1]) # 2
# print(matrix[1][2]) # 7

names=['Geetha','Meghana','Sreenithya','Sreeja','Abinaya','Pravalika']
# names.sort() # sort the list
# print(names)
print(sorted(names)) # sort the list
print(names) # original list is not changed

# names.sort(reverse=True) # sort the list in reverse order
# print(names)

# names.reverse() # reverse the list
# print(names)

# list1=[10,30,50]
# list2=[20,40,60]
# list3=[30,50,70]
# matrix=[list1,list2,list3]
# print(matrix)

# # List comprehension
# first_column=[row[0] for row in matrix]
# print(first_column) # [10, 20, 30]
# third=[row[2] for row in matrix]
# print(third) # [50, 60, 70]