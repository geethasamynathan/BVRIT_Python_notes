
# 🧰 Frequently Used Python Modules and Their Methods

This guide lists **frequently used built-in Python modules**, their **popular methods**, and **real-world use cases** with examples.

---

## 📁 1. os (Operating System Interface)

**Use**: File and directory operations, environment management.

### Common Methods:
| Method             | Description                         | Example |
|--------------------|-------------------------------------|---------|
| `os.getcwd()`      | Get current working directory       | `os.getcwd()` |
| `os.listdir()`     | List files in a directory           | `os.listdir('.')` |
| `os.mkdir()`       | Create a directory                  | `os.mkdir('new_folder')` |
| `os.remove()`      | Delete a file                       | `os.remove('file.txt')` |

### Example:
```python
import os
print("Current Directory:", os.getcwd())
print("Files:", os.listdir('.'))
```

---

## 🧮 2. math (Mathematical Functions)

**Use**: Perform standard math operations.

### Common Methods:
| Method         | Description             | Example             |
|----------------|-------------------------|---------------------|
| `math.sqrt()`  | Square root             | `math.sqrt(16)`     |
| `math.ceil()`  | Ceiling value           | `math.ceil(2.3)`    |
| `math.floor()` | Floor value             | `math.floor(2.9)`   |
| `math.pow()`   | Exponentiation          | `math.pow(2, 3)`    |

### Example:
```python
import math
print("Square Root:", math.sqrt(25))
print("Power:", math.pow(2, 3))
```

---

## ⌚ 3. datetime (Date and Time Handling)

**Use**: Working with dates, times, and timestamps.

### Common Methods:
| Method                        | Description                         | Example                       |
|-------------------------------|-------------------------------------|-------------------------------|
| `datetime.now()`              | Current date and time               | `datetime.now()`              |
| `datetime.strptime()`         | Parse string to datetime            | `datetime.strptime('2024-01-01', '%Y-%m-%d')` |
| `datetime.strftime()`         | Format datetime to string           | `now.strftime('%Y-%m-%d')`    |

### Example:
```python
from datetime import datetime
now = datetime.now()
print("Current Time:", now.strftime('%H:%M:%S'))
```

---

## 🔐 4. random (Random Number Generation)

**Use**: Generate random numbers and selections.

### Common Methods:
| Method             | Description                  | Example                    |
|--------------------|------------------------------|----------------------------|
| `random.randint()` | Random integer               | `random.randint(1, 10)`    |
| `random.choice()`  | Random item from list        | `random.choice(['a','b'])` |
| `random.shuffle()` | Shuffle list                 | `random.shuffle(mylist)`   |

### Example:
```python
import random
print("Random Number:", random.randint(1, 100))
```

---

## 📚 5. json (JSON Handling)

**Use**: Convert between JSON and Python dicts.

### Common Methods:
| Method           | Description                        | Example                      |
|------------------|------------------------------------|------------------------------|
| `json.load()`    | Load JSON from file                | `json.load(f)`               |
| `json.loads()`   | Parse JSON string                  | `json.loads('{"a":1}')`      |
| `json.dump()`    | Write Python dict to JSON file     | `json.dump(data, f)`         |
| `json.dumps()`   | Convert Python object to JSON str  | `json.dumps(data)`           |

### Example:
```python
import json
data = {"name": "Alice", "age": 25}
json_str = json.dumps(data)
print("JSON:", json_str)
```

---

## 🧮 6. statistics (Statistical Operations)

**Use**: Simple statistical computations.

### Common Methods:
| Method            | Description                   | Example                   |
|-------------------|-------------------------------|---------------------------|
| `mean()`          | Arithmetic mean               | `mean([1,2,3])`           |
| `median()`        | Median value                  | `median([1,2,3,4])`       |
| `mode()`          | Most frequent value           | `mode([1,2,2,3])`         |

### Example:
```python
import statistics
print("Mean:", statistics.mean([10, 20, 30]))
```

---

## 🧪 7. re (Regular Expressions)

**Use**: Pattern matching and searching in strings.

### Common Methods:
| Method           | Description                      | Example                      |
|------------------|----------------------------------|------------------------------|
| `re.search()`    | Search for a pattern             | `re.search('ab', 'abc')`     |
| `re.match()`     | Match pattern from start         | `re.match('ab', 'abc')`      |
| `re.findall()`   | Find all occurrences             | `re.findall('a', 'banana')`  |
| `re.sub()`       | Replace pattern                  | `re.sub('a', 'o', 'banana')` |

### Example:
```python
import re
text = "My number is 123-456-7890"
match = re.search(r'\d{3}-\d{3}-\d{4}', text)
print("Phone:", match.group())
```

---

## 🧾 Summary Table

| Module     | Use Case             | Key Methods                              |
|------------|----------------------|------------------------------------------|
| `os`       | File/Dir operations  | `getcwd`, `listdir`, `mkdir`, `remove`  |
| `math`     | Math functions       | `sqrt`, `ceil`, `floor`, `pow`          |
| `datetime` | Date and time        | `now`, `strptime`, `strftime`           |
| `random`   | Random generation    | `randint`, `choice`, `shuffle`          |
| `json`     | JSON handling        | `load`, `loads`, `dump`, `dumps`        |
| `statistics`| Statistical ops     | `mean`, `median`, `mode`                |
| `re`       | Regular expressions  | `search`, `match`, `findall`, `sub`     |
