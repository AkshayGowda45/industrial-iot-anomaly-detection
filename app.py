import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import time

# ---------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------

st.set_page_config(
    page_title="Industrial IoT Anomaly Detection",
    layout="wide"
)

# ---------------------------------------------------
# TITLE
# ---------------------------------------------------

st.title("Industrial IoT Sensor Anomaly Detection Dashboard")

st.markdown("""
Real-time monitoring and anomaly detection system for industrial IoT equipment.
""")

# ---------------------------------------------------
# LOAD DATA
# ---------------------------------------------------

df = pd.read_csv(
    'data/final_iot_anomaly_dataset.csv'
)

# ---------------------------------------------------
# SIDEBAR
# ---------------------------------------------------

st.sidebar.header("Filter Options")

machine_ids = df['Machine_ID'].unique()

selected_machine = st.sidebar.selectbox(
    "Select Machine ID",
    machine_ids
)

sensor = st.sidebar.selectbox(
    "Select Sensor",
    [
        'Temperature',
        'Pressure',
        'Vibration',
        'Humidity',
        'Voltage'
    ]
)

# ---------------------------------------------------
# FILTER DATA
# ---------------------------------------------------

filtered_df = df[
    df['Machine_ID'] == selected_machine
]

# ---------------------------------------------------
# KPI SECTION
# ---------------------------------------------------

total_records = len(filtered_df)

total_anomalies = (
    filtered_df['Anomaly_Flag']
    .sum()
)

anomaly_percentage = (
    total_anomalies / total_records
) * 100

avg_temperature = (
    filtered_df['Temperature']
    .mean()
)

avg_vibration = (
    filtered_df['Vibration']
    .mean()
)

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Total Records",
    total_records
)

col2.metric(
    "Detected Anomalies",
    total_anomalies
)

col3.metric(
    "Anomaly %",
    f"{anomaly_percentage:.2f}%"
)

col4.metric(
    "Avg Temperature",
    f"{avg_temperature:.2f}"
)

# ---------------------------------------------------
# MACHINE HEALTH STATUS
# ---------------------------------------------------

st.subheader("Machine Health Status")

if anomaly_percentage < 10:
    st.success("Machine Operating Normally")

elif anomaly_percentage < 25:
    st.warning("Machine Requires Inspection")

else:
    st.error("Critical Machine Condition")

# ---------------------------------------------------
# SENSOR GRAPH
# ---------------------------------------------------

st.subheader(f"{sensor} Monitoring")

fig, ax = plt.subplots(figsize=(15,5))

ax.plot(
    filtered_df[sensor],
    label=sensor
)

anomalies = filtered_df[
    filtered_df['Anomaly_Flag'] == 1
]

ax.scatter(
    anomalies.index,
    anomalies[sensor],
    color='red',
    label='Anomaly'
)

ax.set_title(f"{sensor} Sensor Readings")

ax.set_xlabel("Data Index")

ax.set_ylabel(sensor)

ax.legend()

st.pyplot(fig)

# ---------------------------------------------------
# REAL-TIME STYLE CHART
# ---------------------------------------------------

st.subheader("Live Sensor Trend (Last 50 Readings)")

latest_data = filtered_df.tail(50)

st.line_chart(
    latest_data[sensor]
)

time.sleep(1)

# ---------------------------------------------------
# ANOMALY TABLE
# ---------------------------------------------------

st.subheader("Detected Anomaly Records")

anomaly_table = filtered_df[
    filtered_df['Anomaly_Flag'] == 1
]

st.dataframe(
    anomaly_table.head(20)
)

# ---------------------------------------------------
# DATASET PREVIEW
# ---------------------------------------------------

st.subheader("Dataset Preview")

st.dataframe(
    filtered_df.head(50)
)

# ---------------------------------------------------
# FOOTER
# ---------------------------------------------------

st.markdown("---")

st.markdown("""
### Project Information

- Industrial IoT Sensor Monitoring
- Predictive Maintenance Analytics
- Anomaly Detection using Machine Learning
- Isolation Forest + Autoencoder Models
""")