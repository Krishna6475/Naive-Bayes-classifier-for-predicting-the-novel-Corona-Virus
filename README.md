# Naive-Bayes-classifier-for-predicting-the-novel-Corona-Virus
# 🦠 COVID-19 Predictor

## 📌 Overview
COVID-19 Predictor is a **machine learning-based web application** that predicts the likelihood of COVID-19 infection based on user-inputted symptoms. The prediction is made using a **Naïve Bayes Classifier**, and the web app is built with **Streamlit** for easy interactivity.

## 🚀 Features
- **Interactive Web Interface** using Streamlit 🎛️
- **Probabilistic Prediction** using a trained Naïve Bayes model 🤖
- **Lightweight & Fast** (Runs entirely on your local machine or cloud)
- **Deployable on Streamlit Cloud** 🌍

## 🛠️ Technologies Used
- **Python** 🐍 – Core programming language
- **Streamlit** 🌐 – Web framework for interactive UI
- **JSON** 📂 – Stores trained data (`trained_data.txt`)
- **Naïve Bayes Algorithm** 📊 – Machine Learning model for prediction
- **time** ⏳ – Simulates loading effects for better user experience

## 📥 Installation & Setup

### 🔹 Prerequisites
Ensure you have **Python 3.7+** installed on your system. Install dependencies using:

```bash
pip install -r requirements.txt
```

### 🔹 Run the Application
Execute the following command in your terminal:

```bash
streamlit run app.py
```

### 🔹 Directory Structure
```bash
📂 covid19-predictor
├── 📄 app.py  # Main Streamlit app
├── 📄 trained_data.txt  # JSON-based trained dataset
├── 📄 requirements.txt  # List of dependencies
├── 📄 README.md  # Project Documentation
```

## 🎮 Usage
1. **Run the application** using the above command.
2. **Enter your symptoms** in the interactive UI.
3. **Get an instant prediction** on whether COVID-19 is likely present or not.

## 🚀 Deployment on Streamlit Cloud
1. Push your project to **GitHub**.
2. Go to [Streamlit Cloud](https://share.streamlit.io/).
3. Click **New App** → Connect your GitHub repository.
4. Set `app.py` as the entry point.
5. Deploy & Share the link! 🎉

## 🛡️ Disclaimer
This tool is **not a medical diagnosis tool**. It only provides a probabilistic prediction and should not be used as a replacement for professional medical advice.

## 🤝 Contributing
Feel free to fork this repository, submit issues, and contribute to improvements!

## 📜 License
MIT License © 2025 COVID-19 Predictor

---
### 🔗 Connect
💡 Have suggestions? Reach out on **GitHub Issues** or [Streamlit Community](https://discuss.streamlit.io/)!
