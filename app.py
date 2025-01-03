import streamlit as st
import joblib
import bleach

# Title of the app
st.title("Sentimental Analysis for Disaster predictions")

model = joblib.load('model.pkl')
PREDICTIONS=["NOT DISATER","DISASTER"]
# Display an input field with a label
st.markdown("<h3 style='font-size: 30px;'>Sentinental analysis of message (disaster or not disaster)</h3>", unsafe_allow_html=True)
user_input = st.text_input(label="Enter your message",key="user_input",value="")
safe_user_input=bleach.clean(user_input)

if st.button("Submit"):
    result=model.predict([safe_user_input])
    st.markdown(f"<h3 style='font-size: 30px;'>The message {user_input} is predicted as {PREDICTIONS[result[0]]} </h3>", unsafe_allow_html=True)