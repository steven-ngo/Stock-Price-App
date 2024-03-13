import streamlit as st
import yfinance as yf
import pandas as pd
import datetime
import plotly.graph_objects as go

# App description
st.markdown('''
# Stock Price App

- Source Code: 
- Language: `Python`
- Libraries: `streamlit`,`yfinance`, `pandas`, `plotly`, and `datetime`
''')
st.write('---')


# Retrieving tickers data
ticker_list = pd.read_csv('https://raw.githubusercontent.com/rreichel3/US-Stock-Symbols/main/all/all_tickers.txt')
tickerSymbol = st.sidebar.selectbox('Stock ticker', ticker_list)
tickerData = yf.Ticker(tickerSymbol)


st.header('**'+ tickerData.info['longName']+ '**')

string_summary = tickerData.info['longBusinessSummary']
st.info(string_summary)



# Ticker data
st.header('**Ticker data**')

period = st.radio(
    'Time Range',
    ['1d','5d','1mo','3mo','6mo','1y','2y','5y','ytd','max'], horizontal=True, index=2)


tickerDf = tickerData.history(period=period)

st.write(tickerDf)


# Candlestick Chart
st.header('**Candlestick Chart**')
figs = go.Figure(data=[go.Candlestick(x=tickerDf.index,
                open=tickerDf['Open'],
                high=tickerDf['High'],
                low=tickerDf['Low'],
                close=tickerDf['Close'])])
figs.update_layout(title= tickerData.info['shortName'] + ' SHARE PRICE')

figs

