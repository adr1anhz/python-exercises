import streamlit as st
from send_email import send_email
import pandas

df = pandas.read_csv("topics.csv")


st.header("Contact Us")


with st.form(key="email_forms"):
    user_email = st.text_input("Email Address")
    topic = st.selectbox(
        'What topic do you want to discuss?',
        df["topic"])
    raw_message = st.text_area("Your Message")
    message = f"""
    Subject: New email from {user_email}
    From: {user_email}
    {raw_message}
    Topic : {topic}
    """
    button = st.form_submit_button("Submit")
    if button:
        send_email(message)
        st.info("Email sent successfully")
