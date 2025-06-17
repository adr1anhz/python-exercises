import streamlit as st


st.header("Contact Me")


with st.form(key="email_forms"):
    user_email = st.text_input("Your Email Address")
    message = st.text_area("Your message")
    button = st.form_submit_button("Submit")
    if button:
        message = message + user_email
        print(button)