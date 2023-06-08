import streamlit as st # Aliasing the streamlit import as st

st.title('Clean Or Not: Beach Edition')
st.text('Is That A Clean Beach?')

st.header('Here are the different pages of my application:')

st.subheader('Your Beach Is')
st.text('Returns an image to let you know if your Beach is Clean or Not.')
st.image('https://www.rd.com/wp-content/uploads/2020/04/tropic-of-cancer-beach-in-exuma-bahamas.jpg?fit=700,467')
st.image('https://i.natgeofe.com/n/8c1dcd07-ebc0-4c31-8522-0f80df632983/01_beachplastic_photo-one_4x3.jpg')
st.subheader('Summary')
st.text('Summary: Is a summarization page of my application.')

st.subheader('Find Out')
st.text('''Allows a user to enter the name of a New York Beach 
                and return if its considered clean or not.
        ''')
