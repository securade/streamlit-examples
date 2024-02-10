import streamlit as st

# Title of the app
st.title('Interactive Streamlit App')

# Taking input from the user
user_input = st.text_input("Enter some text")

# Displaying the input text
if user_input:
    st.write(f'You entered: {user_input}')
    
