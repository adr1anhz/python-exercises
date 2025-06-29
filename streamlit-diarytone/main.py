import glob
import streamlit as st
import plotly.express as px

from nltk.sentiment import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()

files = glob.glob("diary/*.txt")
files_sorted = sorted(files)

negativity = []
positivity = []
for file in files_sorted:
    with open(file, 'r') as f:
        content = f.read()
    scores = analyzer.polarity_scores(content)
    positivity.append(scores["pos"])
    negativity.append(scores["neg"])

dates = [name.strip(".txt").strip("diary/") for name in files_sorted]

st.title("Diary Tone")
st.subheader("Positivity")
pos_figure = px.line(x=dates, y=positivity,
                     labels={"x": "Date", "y": "Positivity"})
st.plotly_chart(pos_figure)

st.subheader("Negativity")
neg_figure = px.line(x=dates, y=negativity,
                     labels={"x": "Date", "y": "Negativity"})
st.plotly_chart(neg_figure)
