import streamlit as st # Aliasing the streamlit import as st

st.title('Clean Or Not: Beach Edition')
st.text('Is That A Clean Beach?')

st.header('Here are the different pages of my application:')
st.subheader('Your Beach Is')
st.text('Your Beach Is: Returns an image to let you know if your beach is clean or not.')

st.subheader('Summary')
st.text('Summary: Is a summarization page of all the inner workings of my application.')

st.subheader('Query')
st.text('Query: Allows a user to enter the name of a New York beach and return if its considered clean or not.')
