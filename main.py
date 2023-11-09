import streamlit as st

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png")

with col2:
    st.title("Hi, I'm Aleksandr")
    content = """
Hello, my name is Aleksandr. I am an aspiring developer with immense enthusiasm and
a passion for creating innovative software solutions. My journey into the realm of 
programming began with a fascination for technology and a keen desire 
to grow in this field.
My primary areas of interest encompass [list the areas of development that interest you,
for example, web development, mobile development, artificial intelligence, databases, etc.].
I am actively studying [mention specific technologies, programming languages, 
 or frameworks] to expand my skills and reach new heights in development.
Within my portfolio, you'll find several projects I've worked on. Even at the initial
stage of my career, I'm confident that my projects reflect professionalism,
a commitment to quality, and an ongoing drive to enhance my skills.
I also aim to engage in teaching and sharing knowledge within the developer community.
I believe that interacting with other professionals in the field not only deepens my 
knowledge but also helps me grow as a professional.
I take pride in being part of this exciting industry and strive to become a more competent 
and experienced developer in the future.
Thank you for your interest in my portfolio, and I hope for the opportunity to 
contribute to projects that benefit society and create new avenues for innovation.
"""
st.write(content)