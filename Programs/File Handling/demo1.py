# with open('The-zen-of-python.txt') as f:
#     content = f.read()
#     print(content)

# #Example of reading a file using readlines()
# with open('the-zen-of-python.txt') as f:
#     [print(line.strip()) for line in f.readlines()]


# # Example of reading a file using readline()
# with open('the-zen-of-python.txt') as f:
#     while True:
#         line = f.readline()
#         if not line:
#             break
#         print(line.strip())


# # concise way of reading a file
# with open('the-zen-of-python.txt') as f:
#     for line in f:
#         print(line.strip())
        
        
# lines = ['Readme', 'How to write text files in Python']
# # lines=["added line 1", "added line 2", "added line 3"]
# with open('readme.txt','a+') as f:
#     for line in lines:
#         f.write(line)
#         f.write('\n')
#     f.seek(0)  # Move the cursor to the beginning of the file
#     content=f.read()
#     print(f'Content from readme.txt\n {content}')
  
# with open('readme.txt') as f:      
#     content=f.readlines();
#     print(f'Content from readme.txt\n {content}')
    
# more_lines = ["added line 4", "added line 5", "added line 6"]
# with open('readme.txt','w') as f:
#     f.write('\n'.join(more_lines))
    
# #example of writing string to a file
# list1 = ['This is a test file.\n', 'This is the second line.\n', 'This is the third line.\n']
# content= ''.join(list1)
# # # with open('testfile1.txt','w') as f:
# # #     f.write(content)
# # #     f.write("\n")

# # with open('testfile1.txt', 'a') as f:
# #     for line in list1:
# #         f.write(line)


# # writing a list to a file
# with open('testfile2.txt', 'w') as f:
#     f.writelines(list1)
    
# with open('testfile2.txt', 'r') as f:
#     content = f.readlines()
#     print(content)