# ⚽ Football Analytics Platform

![Python](https://img.shields.io/badge/Python-3.13-blue?logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-1.47-red?logo=streamlit)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-ML-orange?logo=scikitlearn)
![License](https://img.shields.io/badge/License-MIT-green)

An end-to-end Football Analytics Platform built using **Machine Learning**, **Python**, and **Streamlit** to analyze international football matches, predict match outcomes, and visualize football statistics through an interactive web application.

> Predict. Analyze. Explore.

---

## 📖 Overview

Football Analytics Platform is a machine learning-powered web application that enables users to:

- 🏆 Predict the outcome of international football matches
- 📊 Explore team statistics through interactive dashboards
- 👤 Analyze player performance
- 🎯 Discover player clusters using unsupervised learning
- 📈 Visualize historical football data

The project combines **data preprocessing**, **feature engineering**, **machine learning**, and **interactive visualization** into a single platform.

---

## 🚀 Features

### ⚽ Match Predictor
- Predicts match outcomes using a trained Random Forest model
- Select Home Team and Away Team
- Displays predicted winner
- Shows prediction confidence scores

### 📊 Team Dashboard
- Team performance statistics
- Win, Draw and Loss percentages
- Goal Difference analysis
- Historical trends

### 👤 Player Analytics
- Player statistics
- Performance comparison
- Career insights
- Interactive charts

### 🎯 Player Clustering
- Groups players based on performance metrics
- Machine Learning based clustering
- Visual cluster exploration

---

## 🛠 Tech Stack

### Programming Language
- Python

### Machine Learning
- Scikit-learn
- Random Forest Classifier

### Data Processing
- Pandas
- NumPy

### Visualization
- Plotly
- Matplotlib

### Web Framework
- Streamlit

### Version Control
- Git
- GitHub

---

## 📂 Project Structure

```
Football Analytics Platform
│
├── app/
│   ├── app.py
│   └── pages/
│       ├── Predictor.py
│       ├── Dashboard.py
│       ├── Player_Analytics.py
│       ├── Player_Clusters.py
│       └── About.py
│
├── assets/
│
├── data/
│   ├── results.csv
│   ├── features.csv
│   ├── target.csv
│   └── model_data2.csv
│
├── models/
│   └── random_forest_model.pkl
│
├── notebooks/
│
├── README.md
└── requirements.txt
```

---

## 🧠 Machine Learning Pipeline

### Data Collection
Historical international football match dataset containing:

- Home Team
- Away Team
- Match Result
- Goals Scored
- Tournament
- Venue

---

### Feature Engineering

The prediction model uses engineered team statistics including:

- Home Win Rate
- Home Draw Rate
- Home Loss Rate
- Away Win Rate
- Away Draw Rate
- Away Loss Rate
- Home Goal Difference
- Away Goal Difference

---

### Model Training

Models evaluated:

- K-Nearest Neighbors
- Random Forest Classifier

Final Model:

**Random Forest Classifier**

---

## 📊 Prediction Workflow

```
Select Teams
      │
      ▼
Retrieve Team Statistics
      │
      ▼
Feature Engineering
      │
      ▼
Random Forest Model
      │
      ▼
Prediction + Confidence
```

---

## 📸 Screenshots

### Home Page

![Home](assets/screenshots/home.png)

### Match Predictor

![Predictor](assets/screenshots/predictor.png)

### Dashboard

![Dashboard](assets/screenshots/dashboard.png)

### Player Analytics

![Analytics](assets/screenshots/analytics.png)

### Player Clustering

![Clustering](assets/screenshots/clustering.png)

## ⚙ Installation

Clone the repository

```bash
git clone https://github.com/ShuklaIshan/Football-Analytics-Platform.git
```

Navigate to the project

```bash
cd Football-Analytics-Platform
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
streamlit run app/app.py
```

---

## 📈 Future Improvements

- Live football API integration
- FIFA ranking based features
- Team logo support
- Current squad statistics
- Player injury analysis
- Deep Learning based prediction models
- Match simulation
- Mobile responsive UI

---

## 📂 Dataset

The project uses historical international football match data
covering nearly 50,000 matches played across multiple tournaments,
including FIFA World Cup, continental championships,
qualifiers and international friendlies.

## 📊 Model Performance

| Model | Accuracy |
|--------|---------:|
| K-Nearest Neighbors | 50.8% |
| Random Forest | **53.6%** |

## 🤝 Contributors

### Ishan

- Machine Learning Pipeline
- Feature Engineering
- Model Development
- Match Predictor
- Streamlit Frontend
- UI Design

### Prince

- Dashboard Development
- Player Analytics
- Data Visualization
- Player Clustering
- UI Design

---

## 📄 License

This project is licensed under the MIT License.

---

## 🌐 Live Demo

🚀 **Try the application here**

https://your-streamlit-app-url.streamlit.app

## 🔗 Repository

https://github.com/ShuklaIshan/Football-Analytics-Platform

## ⭐ If you found this project interesting, consider giving it a star!
