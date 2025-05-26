import re
text = "That was so funny hahaha!"
match = re.search(r'(?:ha)+', text)
if match:
    print(match.group(0))  # ✅ prints: hahaha
else:
    print("No match found")
