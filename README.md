# ⚡ Energy Consumption Prediction

A Machine Learning project that predicts building energy consumption based on building and environmental factors.

## 📌 Project Overview

Energy consumption in buildings is influenced by several factors such as temperature, humidity, building size, occupancy, renewable energy usage, HVAC systems, and lighting.

This project uses Machine Learning regression techniques to predict energy consumption and provides an interactive web application using Streamlit.

## 🎯 Objectives

- Analyze factors affecting building energy consumption
- Perform data cleaning and preprocessing
- Conduct exploratory data analysis
- Engineer and select relevant features
- Develop and compare regression models
- Evaluate model performance using appropriate regression metrics
- Deploy the best-performing model as an interactive web application

## 📊 Dataset

The dataset contains building-related and environmental information.

### Features

- Temperature
- Humidity
- SquareFootage
- Occupancy
- RenewableEnergy
- HVAC_On
- Lighting_On

### Target Variable

- EnergyConsumption

Additional engineered features were also explored during the analysis, including:

- Energy_per_Person
- Renewable_Ratio

## 🤖 Machine Learning Models

The following regression models were evaluated:

1. Linear Regression
2. Ridge Regression
3. Lasso Regression
4. Decision Tree
5. Random Forest

## 🏆 Model Performance

Ridge Regression achieved the best performance among the evaluated models.

| Metric | Ridge Regression |
|---|---:|
| R² | 0.5875 |
| RMSE | 5.044 |
| MAE | 3.957 |

R² indicates the proportion of variation in energy consumption explained by the model. It is not treated as classification accuracy.

## 🌐 Live Demo

Try the interactive Streamlit application:

https://energyconsumption-jmczafwqhybukkxpfmtwph.streamlit.app/

The application allows users to enter building information and obtain an energy consumption prediction in real time.

## 🖥️ Application

The Streamlit application provides inputs for:

- Temperature
- Humidity
- Square Footage
- Occupancy
- Renewable Energy
- HVAC status
- Lighting status

The trained Ridge Regression model then generates the predicted energy consumption.

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Seaborn
- Joblib
- Streamlit
- Jupyter Notebook

