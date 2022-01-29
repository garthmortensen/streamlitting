import streamlit as st

st.write("# Streamlit test")

input_value = st.text_input("Enter a Message")

if st.button("Display Message"):
    st.write(input_value)
