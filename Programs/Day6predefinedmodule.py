# import os
# print("Current Directory:", os.getcwd())
# print("Files:", os.listdir('.'))
# os.makedirs('test_folder', exist_ok=True)
# print("files after creating test_folder:", os.listdir('.'))
# os.remove('test_folder')
# print("files after creating and removing test_folder:", os.listdir('.'))

import json
data = {"name": "Alice", "age": 25}
json_str = json.dumps(data)
print("JSON:", json_str)