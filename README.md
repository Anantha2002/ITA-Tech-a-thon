# ITA-Tech-a-thon

## Team name: TrojanArmy

# Stock Value Prediction

## Project Description

This project provides a platform where users can create personalized portfolios of stocks and receive predictions on their future values. After creating an account, users can add stocks to their portfolio, which are then displayed on a dashboard in the form of interactive graphs. Users can select any stock from their portfolio to view detailed predictions.

By default, the platform provides a one-week prediction, but users have the flexibility to adjust the timeline according to their preferences. The model leverages real-time stock data sourced from Yahoo Finance (yfinance) and utilizes a Long Short-Term Memory (LSTM) network to make predictions. The LSTM model is trained on historical stock data to forecast future values with high accuracy.

## Requirements

Before setting up the project, make sure you have the following:

- **Python**: Version 3.8 or higher
- **Dependencies**: Listed in `requirements.txt`

## How to Set Up

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/yourusername/stock-value-prediction.git
   cd stock-value-prediction
2. **Install dependencies**
     ```bash
     pip install -r requirements.txt
3. ```bash
   python main.py

