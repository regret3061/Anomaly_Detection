# Real-Time Anomaly Detection Using Moving Average with Thresholding

This project demonstrates a real-time anomaly detection system using a **Moving Average with Thresholding** algorithm. The system continuously processes data from a simulated data stream and detects anomalies in real time. The results are visualized using Matplotlib.

## Table of Contents

- [Introduction](#introduction)
- [Algorithm Overview](#algorithm-overview)
- [Installation](#installation)

## Introduction

This project implements anomaly detection on a simulated data stream using **Moving Average with Thresholding**. The method identifies unusual data points by analyzing the rolling mean and standard deviation over a sliding window.

The project also provides real-time visualization of the data stream and anomalies.

## Algorithm Overview

### Moving Average with Thresholding:

1. **Data Stream Simulation**:
   - The data stream follows a sinusoidal pattern with added noise and occasional anomalies (spikes).
   
2. **Moving Average-Based Anomaly Detection**:
   - A rolling window of data points is maintained.
   - The algorithm computes the mean and standard deviation over the window.
   - Data points that fall outside the range defined by `mean ± (threshold * std)` are flagged as anomalies.
   
3. **Real-Time Visualization**:
   - The data stream and detected anomalies are displayed in real-time using Matplotlib.

## Installation

### Prerequisites

Before running the script, ensure you have Python installed with the necessary libraries:

- `numpy`
- `matplotlib`

You can install them using `pip`:

```bash
pip install numpy matplotlib
