import numpy as np
import random
from collections import deque
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Set parameters for the data stream and anomaly detection
WINDOW_SIZE = 25  # Rolling window for moving average
THRESHOLD = 2 # Threshold factor for detecting anomalies

# Queues to store the rolling data window and detected anomalies
data_window = deque(maxlen=WINDOW_SIZE)
anomalies_window = deque(maxlen=WINDOW_SIZE)

# A function to simulate a real-time data stream
def data_stream():
    time_step = 0
    while True:
        # Sinusoidal pattern to simulate seasonality
        seasonal_value = 10 * np.sin(2 * np.pi * time_step / 30)
        
        # Adding some random noise
        noise_value = random.uniform(-3, 3)
        
        # Simulate normal data points (seasonal + noise)
        data_point = seasonal_value + noise_value
        
        # Occasionally inject an anomaly (a rare large spike)
        if random.random() < 0.10:  # 10% chance of anomaly
            data_point += random.uniform(10, 20)
        
        yield data_point  # Yield one data point at a time to simulate streaming
        time_step += 1

# Function to detect anomalies using Moving Average with Thresholding
def detect_anomaly_moving_average(data_point, threshold=THRESHOLD):
    data_window.append(data_point)
    
    if len(data_window) == WINDOW_SIZE:
        mean = np.mean(data_window)
        std = np.std(data_window)
        
        upper_bound = mean + (threshold * std)
        lower_bound = mean - (threshold * std)
        
        # Detect anomaly if the data point is outside the bounds
        if data_point > upper_bound or data_point < lower_bound:
            anomalies_window.append(data_point)

        else:
            anomalies_window.append(np.nan)  # No anomaly
    else:
        anomalies_window.append(np.nan)  # Until the window is full, append NaN

# Setting up the real-time visualization
fig, ax = plt.subplots()
x_data, y_data, anomaly_data = [], [], []

# The update function for real-time plot animation
def update(frame_count):
    # Get the next data point from the simulated stream
    data_point = next(data_stream_gen)
    
    # Use the moving average method to detect anomalies
    detect_anomaly_moving_average(data_point)
    
    # Append the new data for visualization
    x_data.append(frame_count)
    y_data.append(data_point)
    anomaly_data.append(anomalies_window[-1])  # Either an anomaly or NaN
    
    # Clear and redraw the plot
    ax.clear()
    ax.plot(x_data, y_data, label='Data Stream')
    ax.scatter(x_data, anomaly_data, color='red', label='Anomalies')
    ax.set_title("Real-Time Anomaly Detection with Moving Average")
    ax.set_xlabel("Time")
    ax.set_ylabel("Data Value")
    ax.legend()

# Set up the data stream generator
data_stream_gen = data_stream()  # This will simulate the real-time data stream

# Test the update function for 300 frames
for i in range(300):
    update(i)

# Create the animation object, refreshing every 200 ms
ani = FuncAnimation(fig, update, interval=200)

# Keep the FuncAnimation object alive by assigning it to a global variable
plt.show()
