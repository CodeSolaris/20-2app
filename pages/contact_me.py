import streamlit as st
from send_email import send_email

st.title("Contact me")

st.write(
    "Please fill out the form below to send me a message.\
    I will get back to you as soon as possible."
)

# Email input field
with st.form(key="email_form"):
    user_email = st.text_input("Your email address")
    raw_message = st.text_area("Your message")

    message = f"""\
Subject: new email from {user_email}

From: {user_email}
{raw_message}
"""

    submit_button = st.form_submit_button("Send Email")
    if submit_button:
        send_email(message)
        st.success("Email sent successfully!")
