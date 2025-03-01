# 🔍 Cyber Phishing Detector - Detect Malicious URLs Using Machine Learning

Cyber Phishing Detector is a **machine learning-based web application** that identifies phishing websites based on URL features. The model is trained using **Random Forest Classifier** and deployed with **Flask**, offering a reliable and efficient way to detect fraudulent sites.

## 🚀 Features
✅ **Automated Phishing Detection** – Identifies malicious websites with high accuracy.  
✅ **URL-Based Classification** – Enter a URL to get an instant classification result.  
✅ **Machine Learning Model** – Trained using Random Forest for robust performance.  
✅ **Web-Based Interface (Future Scope)** – Plan to integrate a web UI for easy access.  
✅ **Flask Deployment** – Lightweight and scalable backend for real-time predictions.  

## 🛠️ Technologies Used
- **Python** (Machine Learning & Backend)
- **Scikit-Learn** (Machine Learning Model)
- **Pandas & NumPy** (Data Processing)
- **Flask** (Web Framework - Future Integration)
- **Joblib** (Model Saving & Loading)

## 📸 Screenshots
(Add screenshots of your web app interface here to showcase the UI!)
![Screenshot 2025-03-01 091504](https://github.com/user-attachments/assets/c9bfc2e6-79d8-4286-8a11-beb42e336ad8)


## 📂 Installation & Setup
To run this project locally, follow these steps:

### 1️⃣ Clone the repository:
```bash
git clone https://github.com/your-username/cyber-phishing-detector.git
cd cyber-phishing-detector
```

### 2️⃣ Install dependencies:
```bash
pip install -r requirements.txt
```

### 3️⃣ Train the model:
```bash
python phishing_detector.py
```

### 4️⃣ Predict phishing websites:
```python
from phishing_detector import predict_phishing

url = "http://example.com"
print(predict_phishing(url))
```

### 5️⃣ (Future) Run Flask Web App:
```bash
python app.py
```
Then open your browser and go to:
```cpp
http://127.0.0.1:5000
```

## 🤝 Contributing
Feel free to contribute by submitting issues, feature requests, or pull requests!

## 📜 License
This project is open-source under the **MIT License**.

