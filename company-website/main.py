import streamlit as st
import pandas


st.header("The Best Company")

st.write("Loreum ipsum... Here we should write description about the company.")

st.title("Our Team")

col1, empty_col, col2, empty_col2, col3 = st.columns([1.5, 0.3, 1.5, 0.3, 1.5])

df = pandas.read_csv("data.csv", sep=",")
with col1:
    for index, row in df[:1].iterrows():
        st.header((row["first name"] + " " + row["last name"]).title())
        st.write(row["role"])
        st.image(f"images/" + row["image"])
    for index, row in df[1:2].iterrows():
        st.header((row["first name"] + " " + row["last name"]).title())
        st.write(row["role"])
        st.image(f"images/" + row["image"])
    for index, row in df[2:3].iterrows():
        st.header((row["first name"] + " " + row["last name"]).title())
        st.write(row["role"])
        st.image(f"images/" + row["image"])
    for index, row in df[3:4].iterrows():
        st.header((row["first name"] + " " + row["last name"]).title())
        st.write(row["role"])
        st.image(f"images/" + row["image"])


with col2:
    for index, row in df[4:5].iterrows():
        st.header((row["first name"] + " " + row["last name"]).title())
        st.write(row["role"])
        st.image(f"images/" + row["image"])
    for index, row in df[5:6].iterrows():
        st.header((row["first name"] + " " + row["last name"]).title())
        st.write(row["role"])
        st.image(f"images/" + row["image"])
    for index, row in df[6:7].iterrows():
        st.header((row["first name"] + " " + row["last name"]).title())
        st.write(row["role"])
        st.image(f"images/" + row["image"])
    for index, row in df[7:8].iterrows():
        st.header((row["first name"] + " " + row["last name"]).title())
        st.write(row["role"])
        st.image(f"images/" + row["image"])


with col3:
    for index, row in df[8:9].iterrows():
        st.header((row["first name"] + " " + row["last name"]).title())
        st.write(row["role"])
        st.image(f"images/" + row["image"])
    for index, row in df[9:10].iterrows():
        st.header((row["first name"] + " " + row["last name"]).title())
        st.write(row["role"])
        st.image(f"images/" + row["image"])
    for index, row in df[10:11].iterrows():
        st.header((row["first name"] + " " + row["last name"]).title())
        st.write(row["role"])
        st.image(f"images/" + row["image"])
    for index, row in df[11:12].iterrows():
        st.header((row["first name"] + " " + row["last name"]).title())
        st.write(row["role"])
        st.image(f"images/" + row["image"])


