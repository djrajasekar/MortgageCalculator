import streamlit as st
st.title("Hello, Streamlit!")

st.write("Welcome to your first Streamlit app.")

mov = st.text_input("What is your favorite movie?")
st.write(f"your favourite movies is {mov}")