import streamlit as st
from send_email import send_email

st.title("Contact me")

st.write(
    "Please fill out the form below to send me a message.\
    I will get back to you as soon as possible."
)

# Email input field
with st.form(key="email_form"):
    email = st.text_input("Your email address")
    theme = st.text_input("Theme")

    message = f"Subject: {theme}\n\n{st.text_area("Your message")}\n{email}"

    submit_button = st.form_submit_button("Send Email")
    if submit_button:
        send_email(message)
        st.success("Email sent successfully!")
