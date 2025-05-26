
# 🐍 Frequently Used Python Packages with Examples

---

## 📊 1. NumPy
**Purpose**: Numerical computing  
**Used for**: Handling large, multi-dimensional arrays and matrices.

```python
import numpy as np
arr = np.array([1, 2, 3, 4])
print("Mean:", np.mean(arr))
```
**Real-world use**: Sensor data processing, statistical analysis.

---

## 📈 2. Pandas
**Purpose**: Data analysis and manipulation  
**Used for**: Reading, filtering, transforming structured data.

```python
import pandas as pd
df = pd.read_csv("sales.csv")
print(df.groupby("Region")["Profit"].sum())
```
**Real-world use**: Sales analysis, reporting dashboards.

---

## 📉 3. Matplotlib
**Purpose**: Data visualization  
**Used for**: Creating charts like line, bar, scatter, etc.

```python
import matplotlib.pyplot as plt
x = [1, 2, 3]
y = [10, 20, 15]
plt.plot(x, y)
plt.title("Sales Growth")
plt.show()
```
**Real-world use**: Visual reports, trend graphs.

---

## 📊 4. Seaborn
**Purpose**: Statistical data visualization  
**Used for**: Visualizing complex datasets.

```python
import seaborn as sns
import pandas as pd
df = sns.load_dataset("tips")
sns.boxplot(x="day", y="total_bill", data=df)
```
**Real-world use**: Customer spending pattern analysis.

---

## 📡 5. Requests
**Purpose**: HTTP requests  
**Used for**: Sending GET, POST requests to APIs.

```python
import requests
response = requests.get("https://api.github.com/users/octocat")
print(response.json()["name"])
```
**Real-world use**: API integrations like weather, GitHub.

---

## 📦 6. Flask
**Purpose**: Web framework  
**Used for**: Building web APIs or simple websites.

```python
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, World!"
```
**Real-world use**: Creating REST APIs or microservices.

---

## 🤖 7. Scikit-learn
**Purpose**: Machine Learning  
**Used for**: Regression, classification, clustering.

```python
from sklearn.linear_model import LinearRegression
import numpy as np

X = np.array([[1], [2], [3]])
y = np.array([1, 2, 3])

model = LinearRegression().fit(X, y)
print(model.predict([[4]]))
```
**Real-world use**: Predicting sales, customer churn.

---

## 🌐 8. BeautifulSoup
**Purpose**: Web scraping  
**Used for**: Parsing HTML and extracting data.

```python
from bs4 import BeautifulSoup
import requests

html = requests.get("https://example.com").text
soup = BeautifulSoup(html, "html.parser")
print(soup.title.text)
```
**Real-world use**: Price comparison, data scraping.

---

## 🔐 9. OpenCV
**Purpose**: Image processing  
**Used for**: Face detection, object tracking.

```python
import cv2
image = cv2.imread("photo.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray Image", gray)
cv2.waitKey(0)
cv2.destroyAllWindows()
```
**Real-world use**: Surveillance systems, OCR.

---

## 📚 10. TensorFlow / PyTorch
**Purpose**: Deep Learning  
**Used for**: Neural networks, computer vision, NLP

```python
import tensorflow as tf

model = tf.keras.Sequential([
    tf.keras.layers.Dense(10, activation='relu'),
    tf.keras.layers.Dense(1)
])
```
**Real-world use**: AI chatbots, image classification.

---

## 📦 Summary Table

| Package       | Use Case               | Real-world Application         |
|---------------|------------------------|--------------------------------|
| NumPy         | Math operations        | Sensor, ML preprocessing       |
| Pandas        | Data manipulation      | Finance, CSV parsing           |
| Matplotlib    | Graphs & charts        | Reports, trends                |
| Seaborn       | Advanced plotting      | Data exploration               |
| Requests      | API interaction        | REST API integration           |
| Flask         | Web development        | Backend service                |
| Scikit-learn  | Machine learning       | Predictive modeling            |
| BeautifulSoup | Web scraping           | E-commerce, research           |
| OpenCV        | Image/video processing | Face recognition               |
| TensorFlow    | Deep learning          | NLP, computer vision           |
