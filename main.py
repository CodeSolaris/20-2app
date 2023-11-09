import streamlit as st

# Set page configuration
st.set_page_config(
    page_title="Aleksandr's Portfolio",
    layout="wide",
)

# Create two columns
left_column, right_column = st.columns(2)

# Left column
with left_column:
    st.write("")
    st.write("")
    st.image("images/photo.png", use_column_width=True)

# Right column
with right_column:
    st.title("Hi, I'm Aleksandr")
    content = """
<p>I'm a passionate developer enthusiastic about crafting web and desktop applications,
 website scraping, and Telegram bots.
My journey into programming began with a fascination for technology and a desire to 
create innovative solutions in these domains.</p>
<p>I'm particularly drawn to the development of web and desktop applications
 finding joy in building intuitive and user-friendly interfaces.
Additionally, I've found interest in the art of web scraping, extracting valuable 
information from websites, and leveraging it for various purposes.
Moreover, exploring the realm of Telegram bots has been an exciting avenue, 
allowing me to delve into chatbot development and automation within 
this popular platform.</p>
<p>My portfolio showcases projects where I've applied my skills,
even at this early stage of my career. 
These projects reflect my commitment to precision,
a pursuit of excellence, and an unwavering dedication to continuous 
learning and improvement.</p>
<p>I'm also keen on engaging with the developer community, fostering collaboration, 
and sharing knowledge. I strongly believe that interacting with other
experts in the field enhances not only my knowledge 
but also my growth as a professional.</p>
<p>Being a part of the dynamic world of technology fills me with immense pride. 
My goal is to continue evolving as a skilled and experienced developer
while contributing meaningfully to innovative projects that make a difference.</p>
<p>Thank you for your interest in exploring my portfolio. 
I'm excited about the prospect of contributing to projects that push the boundaries
 of innovation and have a positive impact.</p>
"""
    st.write(content, unsafe_allow_html=True)

st.write(
    "Below you can find some of the apps I have built in Python.Feel free to contact me!"
)
