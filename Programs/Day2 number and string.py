# print(2+3)
# print(2*3)
# print(4.2/3.1)
# print(2**3)
# print(2 + 10 * 10 + 3)

# income=45000
# tax_rate=0.2
# tax=income*tax_rate
# print("Your tax is", tax)

company_name="capgemini"
# print(company_name)
# print(company_name[0])
# print(company_name[1])

#print(company_name[0:3])
# print(company_name[:3])
# print(company_name[3:])
# print(company_name[:5]) # capge
# print(company_name[5:]) # mini
# print(company_name[::-1]) #inimegpac
#Skipping Elements 
#print(company_name[::2])  #cpeii

# Sting concatenation
company_name+=" india"

# print(company_name)
# print(f'upper {company_name.upper()}')
# print(f'lower {company_name.lower()}')
# print(f'title {company_name.title()}') #Capgemini India
# print(f'capitalize {company_name.capitalize()}') # Capgemini india

# str1='Hello', 'World', 'concatenate', 'me!'
# #str1='Hello' 'World' 'concatenate' 'me!'
# print(' '.join(str1)) # Hello World concatenate me!
# print(' '.join(str1).split()) # ['Hello', 'World', 'concatenate', 'me!']

# print("H"*3) # HHHHHHHHHH
# print("H"*10 + "W"*10) # HHHHHHHHHHWWWWWWWWWW

# String Formatting
# print("I am going to inject %s here." %"something")
# print("I'm going to inject %s text here, and %s text here." %('some','more'))
# x, y = 'some', 'more'
# print("I'm going to inject %s text here, and %s text here."%(x,y))
# print('Floating point numbers: %1.0f' %(13.144))
# print('Floating point numbers: %10.2f' %(13.144))

# print(len('Floating point numbers:')) 
# print(len('Floating point numbers: %10.2f' %(13.144)))

# print('{0:8} | {1:9}'.format('Fruit', 'Quantity'))
# print('{0:8} | {1:9}'.format('Apples', 3.))
# print('{0:8} | {1:9}'.format('Oranges', 10))

print('{0:<8} | {1:^8} | {2:>8}'.format('Left','Center','Right'))
print('{0:<8} | {1:^8} | {2:>8}'.format(11,22,33))

first_name = 'Geetha'
print(f'Hello {first_name}, would you like to teach some Python today?')
