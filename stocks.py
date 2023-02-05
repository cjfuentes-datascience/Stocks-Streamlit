import yfinance as yf
import streamlit as st
import pandas as pd

st.write("""
# simple stock price app
Enter the stock symbol to see its closing price and volume!
""")

ticker_symbol = st.text_input("Enter a stock symbol (e.g. 'AAPL' for Apple):")
ticker_data = yf.Ticker(ticker_symbol)
ticker_df = ticker_data.history(period='1d', start='2010-5-31', end='2020-5-31')

st.write("""
## closing price
""")

st.line_chart(ticker_df.Close)

st.write("""
## volume price
""")
st.line_chart(ticker_df.Volume)
