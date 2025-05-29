
# 🌀 Generators in Python

## ✅ What is a Generator in Python?

A **generator** is a special type of iterable in Python that **generates values on the fly** using the `yield` keyword instead of returning all values at once. Generators **do not store the entire sequence in memory**, making them **memory-efficient and faster** for large datasets.

---

## 🧠 Why Do We Need Generators?

1. **Memory Efficiency**: Generators yield items one at a time, saving memory.
2. **Performance**: They are faster when working with large data sequences.
3. **Lazy Evaluation**: Values are computed only when needed (on-demand).
4. **Stream Handling**: Ideal for processing large files, data streams, or infinite sequences.

---

## 🧪 Example: Generator Function

```python
def count_up_to(n):
    count = 1
    while count <= n:
        yield count
        count += 1

for num in count_up_to(5):
    print(num)
```

**Output:**
```
1
2
3
4
5
```

---

## 🔁 Alternative to Generators

### 1. **List Comprehensions** (Eager Evaluation)

```python
# This creates the entire list in memory
squares = [x * x for x in range(1000000)]
```

✅ Good for small data  
❌ Consumes a lot of memory for large data

---

### 2. **Iterators with `__iter__()` and `__next__()`**

You can manually implement an iterator class.

```python
class Counter:
    def __init__(self, max):
        self.max = max
        self.current = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= self.max:
            val = self.current
            self.current += 1
            return val
        else:
            raise StopIteration

for i in Counter(5):
    print(i)
```

✅ More control  
❌ More boilerplate code

---

## 🆚 Generator vs List

| Feature         | Generator                 | List                          |
|-----------------|---------------------------|-------------------------------|
| Memory Usage    | Low (on-demand)           | High (entire data in memory)  |
| Speed           | Fast for large sequences  | Slower for large sequences    |
| Syntax          | Uses `yield`              | Uses `return` or `[]`         |
| Use Case        | Infinite/Large datasets   | Small to medium datasets      |
