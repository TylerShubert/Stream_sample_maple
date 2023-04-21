import pandas as pd
import hvplot.pandas
import numpy as np
from pathlib import Path
import streamlit as st

st.write("#DEEP ANALYTICS LLC. STREAMLIT SAMPLE#")



#Reading stock data
df_stock = pd.read_csv(
    Path("aapl-price.csv"), 
    index_col="date", 
    parse_dates=True, 
    infer_datetime_format=True
)


# Review the DataFrame
st.write(df_stock.head())


df_trends = pd.read_csv(
    Path("apple-trends.csv"), 
    index_col="date", 
    parse_dates=True, 
    infer_datetime_format=True
)

st.write(df_trends.head())




df_apple = pd.concat([df_stock, df_trends], axis=1).dropna()

st.write(df_apple.head())

st.line_chart(df_apple)

df_spotlight = df_apple.loc["2019-03-01":"2020-01-31"]


st.line_chart(df_spotlight)


df_apple["lagged_trends"] = df_apple["trend-worldwide"].shift(1)

df_apple["weekly_returns"] = df_apple["close"].pct_change()

df_apple["weekly_volatility"] = df_apple["close"].pct_change().rolling(window=4).std()


st.write(df_apple.head())

st.write(df_apple[["lagged_trends", "weekly_returns", "weekly_volatility"]].corr())