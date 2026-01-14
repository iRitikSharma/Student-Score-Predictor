# 📊 Student Score Predictor

A simple Machine Learning project that predicts a student’s exam score based on the number of hours studied using a Linear Regression model in Python. This project demonstrates the complete ML workflow including data loading, model training, evaluation, and real-time prediction.

## 🧠 Project Overview

Predicting student performance is a common beginner-level machine learning problem. In this project, Linear Regression is used to estimate exam scores using study hours as the input feature. This project helps in understanding data preprocessing, regression modeling, model evaluation, and real-time predictions.

## 🚀 Features

- Linear Regression model implementation
- Model evaluation using MAE, MSE, RMSE
- Real-time prediction using user input
- Implemented completely in Python
- Beginner-friendly machine learning project

## 🗂️ Project Structure

Student-Score-Predictor/
├── README.md
├── machine_learning.csv
├── project.py
└── dataset.csv

## 🛠️ Technologies Used

| Technology | Purpose |
|-----------|---------|
| Python | Core programming |
| Pandas | Data handling |
| NumPy | Numerical operations |
| Matplotlib | Data visualization |
| Scikit-learn | Machine learning |

## ⚙️ Installation & Setup

Clone the repository:
git clone https://github.com/iRitikSharma/Student-Score-Predictor.git
cd Student-Score-Predictor

Create a virtual environment (recommended):
python -m venv env

Activate the virtual environment:

Windows:
env\Scripts\activate

Linux / macOS:
source env/bin/activate

Install dependencies:
pip install -r requirements.txt

## ▶️ Run the Project

python project.py

## 🤖 Sample Prediction

Enter hours studied: 6  
Predicted Score: 58.42

## 📊 Model Evaluation Metrics

| Metric | Description |
|------|-------------|
| MAE | Mean Absolute Error |
| MSE | Mean Squared Error |
| RMSE | Root Mean Squared Error |

These metrics indicate how accurately the model predicts student scores.

## 📈 Dataset

The dataset contains two columns:

| Hours Studied | Score |
|--------------|-------|
| 2.5 | 21 |
| 5.1 | 47 |
| 8.5 | 81 |
| 9.2 | 88 |

## 💡 Future Improvements

- Add more features such as attendance and previous marks
- Try advanced regression models like Random Forest or SVR
- Add data visualization
- Build a web application using Flask or Streamlit

## 👤 Author

Ritik Sharma  
GitHub: https://github.com/iRitikSharma

## ⭐ Support

If you like this project, please give it a ⭐ star on GitHub.

## 📜 License

This project is open-source and free to use.
