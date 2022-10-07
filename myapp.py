import yfinance as yf
import streamlit as st
import pandas as pd

st.write("""
# Simple Stock Price App

shown are the stock **closing price** and ***volume*** of Microsoft!
""")

#define the ticker symbol
tickerSymbol = 'MSFT'

#get data on this ticker
tickerData = yf.Ticker(tickerSymbol)

#get the historical prices for this ticker
tickerDf = tickerData.history(period='1d', start='2010-1-1', end='2020-1-25')

#see your data
st.write("""
### Closing Price of MSFT
""")
st.line_chart(tickerDf.Close)
st.write("""
### Volume Price of MSFT
""")
st.line_chart(tickerDf.Volume)