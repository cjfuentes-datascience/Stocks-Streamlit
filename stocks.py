import yfinance as yf
import streamlit as st
import pandas as pd

st.write("""
# Simple Stock Price App
Enter the stock symbol to see its closing price and volume!
""")

ticker_symbol = st.text_input("Enter a stock symbol (e.g. 'AAPL' for Apple):")
ticker_data = yf.Ticker(ticker_symbol)
ticker_df = ticker_data.history(period='1d', start='2010-5-31', end='2023-1-31')

st.write("""
## Closing Price
""")

st.line_chart(ticker_df.Close)

st.write("""
## Volume Price
""")
st.line_chart(ticker_df.Volume)
