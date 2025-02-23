import streamlit as st

#Upload pdf files
st.header("My first chatbot")

with st.sidebar:
    st.title("Your documents")
    file = st.file_uploader("Upload the file and start asking questions", type="pdf")