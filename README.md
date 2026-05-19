# Industrial IoT Sensor Anomaly Detection

## Overview

This project focuses on detecting anomalies in industrial IoT sensor data using Machine Learning and Deep Learning techniques. The system helps identify abnormal equipment behavior for predictive maintenance and operational efficiency.

The solution includes:

* Data preprocessing and cleaning
* Exploratory Data Analysis (EDA)
* Feature engineering
* Isolation Forest anomaly detection
* Autoencoder neural network
* Interactive Streamlit dashboard
* Industrial monitoring analytics

---

# Business Problem

Industrial machines continuously generate sensor readings such as:

* Temperature
* Pressure
* Vibration
* Humidity
* Voltage
* Current
* RPM
* Noise levels

Undetected anomalies can lead to:

* Equipment failure
* Increased downtime
* Higher maintenance costs
* Reduced operational efficiency

This project provides an intelligent anomaly detection system capable of identifying irregular sensor behavior early for predictive maintenance.

---

# Project Objectives

* Detect anomalies in industrial sensor readings
* Monitor equipment health in real-time
* Improve predictive maintenance strategies
* Reduce unplanned equipment downtime
* Visualize sensor behavior using dashboards
* Build an industry-style ML monitoring application

---

# Dataset Information

The dataset contains industrial IoT sensor readings including:

| Feature           | Description                  |
| ----------------- | ---------------------------- |
| Temperature       | Machine temperature readings |
| Pressure          | Operational pressure values  |
| Vibration         | Machine vibration levels     |
| Humidity          | Environmental humidity       |
| Voltage           | Voltage readings             |
| Current           | Current consumption          |
| RPM               | Rotations per minute         |
| Power_Consumption | Energy usage                 |
| Load_Percent      | Machine load percentage      |
| Noise_Level       | Noise intensity              |
| Machine_ID        | Unique machine identifier    |
| Anomaly_Flag      | Ground truth anomaly label   |

---

# Technologies Used

## Programming & Analytics

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn

## Machine Learning

* Scikit-learn
* TensorFlow / Keras

## Dashboard

* Streamlit

## Version Control

* Git
* GitHub

---

# Machine Learning Workflow

## 1. Data Cleaning

* Handled missing values
* Removed duplicates
* Standardized anomaly labels
* Processed industrial sensor data

---

## 2. Exploratory Data Analysis (EDA)

Performed:

* Correlation analysis
* Sensor trend analysis
* Outlier visualization
* Anomaly distribution analysis

---

## 3. Feature Engineering

Created advanced features including:

* Rolling averages
* Rolling standard deviation
* Sensor trend indicators
* Time-series statistical features

---

# Models Implemented

## Isolation Forest

Isolation Forest is an unsupervised anomaly detection algorithm that isolates anomalies instead of profiling normal data points.

### Features

* Handles high-dimensional sensor data
* Efficient anomaly detection
* Suitable for industrial monitoring systems

---

## Autoencoder Neural Network

The Autoencoder learns normal sensor behavior patterns and identifies anomalies based on reconstruction error.

### Features

* Deep learning-based anomaly detection
* Reconstruction error analysis
* Better representation learning

---

# Dashboard Features

The Streamlit dashboard includes:

* Machine-wise monitoring
* Dynamic sensor visualization
* KPI cards
* Anomaly percentage tracking
* Machine health status
* Interactive filtering
* Real-time style monitoring graphs
* Anomaly inspection tables

---

# Project Structure

```bash
industrial-iot-anomaly-detection/
│
├── app.py
├── README.md
├── requirements.txt
│
├── data/
│   └── final_iot_anomaly_dataset.csv
│
├── notebooks/
│   └── IoT_Anomaly_Detection.ipynb
│
├── screenshots/
│   ├── dashboard.png
│   ├── anomaly_graph.png
│   └── kpi_cards.png
│
├── models/
│
└── reports/
```

---

# Installation

## Clone Repository

```bash
git clone https://github.com/yourusername/industrial-iot-anomaly-detection.git
```

---

## Move Into Project Folder

```bash
cd industrial-iot-anomaly-detection
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Run Streamlit Dashboard

```bash
streamlit run app.py
```

If Streamlit command does not work:

```bash
python -m streamlit run app.py
```

---

# Results

* Successfully detected anomalous industrial sensor behavior
* Built predictive maintenance monitoring workflow
* Developed interactive anomaly visualization dashboard
* Implemented feature engineering for time-series analytics
* Compared multiple anomaly detection approaches

---

# Future Improvements

The project can be upgraded further using:

* FastAPI integration
* PostgreSQL database
* Docker containerization
* Real-time IoT streaming
* AWS/Azure deployment
* Kafka event streaming
* LSTM Autoencoder
* Model monitoring pipeline

---

# Industry Applications

This solution can be applied in:

* Manufacturing
* Smart factories
* Automotive industries
* Semiconductor industries
* Industrial automation
* Predictive maintenance systems

---

# Author

Akshay Gowda
Project – Industrial IoT Sensor Anomaly Detection
