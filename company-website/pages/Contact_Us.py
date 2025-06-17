import streamlit as st
from send_email import send_email


st.header("Contact Us")


with st.form(key="email_forms"):
    user_email = st.text_input("Email Address")
    topic = st.selectbox("Choose a topic", ["Topic 1", "Topic 2", "Topic 3"])
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
