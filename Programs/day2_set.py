x=set()
print(type(x))
print(x)
x.add('Test')
x.add(234)
x.add(23.45)
print(x)

list1 = [1,1,12,12,3,4,5,6,1,1,'test','demo']
unique_numbers=set(list1) # set will remove duplicates
print(unique_numbers)
#unique_numbers.pop()
# print(unique_numbers)
# unique_numbers.remove('demo')    
print(unique_numbers)
unique_numbers.discard('demo1') # discard will not raise error if item is not present
copied_set=unique_numbers.copy() # copy the set
print(f'Copied Set {copied_set}')   
#unique_numbers.clear() # clear the set
#print(f' Afetr clear {unique_numbers}')

set1={1,2,3,4}
set2={3,6,1,8}

set_difference=set1.difference(set2) # difference will return the difference between two sets
print(f'Sets difference {set_difference}') # {8, 6}