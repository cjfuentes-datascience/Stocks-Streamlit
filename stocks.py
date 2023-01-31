import yfinance as yf
import streamlit as st
import pandas as pd

st.write("""
# simple stock price app

shown are the stock closing price and volume of google!

""")

tickerSymbol='AAPL'
tickerData=yf.Ticker(tickerSymbol)
tickerDf=tickerData.history(period='1d', start='2010-5-31', end='2020-5-31')

st.write("""
## closing price
""")

st.line_chart(tickerDf.Close)

st.write("""
## volume price
""")
st.line_chart(tickerDf.Volume)
