import streamlit as st
import plotly.express as px
import sqlite3
import pandas as pd

connection = sqlite3.connect("data")


def read():
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM events")
    rows = cursor.fetchall()
    df = pd.DataFrame(rows, columns=["date", "temperature"])
    return df

df = read()

figure = px.line(x=df["date"], y=df["temperature"], labels={"x": "Date", "y": "Temperature (C)"})

st.plotly_chart(figure)
