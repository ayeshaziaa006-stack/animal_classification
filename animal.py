import streamlit as st

st.title("🐶 Animal Classification App")
st.write("My first AI web app is running!")

uploaded_file = st.file_uploader("Upload an image")

if uploaded_file:
    st.image(uploaded_file)
    st.write("Prediction: (model will go here)")