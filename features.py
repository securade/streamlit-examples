import streamlit as st
import pandas as pd

user_input = st.text_input("Enter your name")
st.write(f'Hello, {user_input}!')

if st.button('Click me'):
    st.write('Button clicked!')
    
age = st.slider('Select your age', 0, 100, 25)
st.write(f'Your age: {age}')

show_info = st.checkbox('Show Info')
if show_info:
    st.write('Showing information...')
    
col1, col2 = st.columns(2)
with col1:
    st.write("Column 1 content here")
with col2:
    st.write("Column 2 content here")
    
with st.expander("See details"):
   st.write("Hidden content here")
   
option = st.sidebar.selectbox('Choose your option', ['A', 'B', 'C'])
st.write(f'You selected: {option}')

st.markdown("# This is a header\nSome *italicized text* and **bold text**")

st.markdown("""
    <style>
    .big-font {
        font-size:50px !important;
    }
    </style>
    """, unsafe_allow_html=True)

st.markdown('<p class="big-font">Large Text</p>', unsafe_allow_html=True)

# Initialize state
if 'count' not in st.session_state:
    st.session_state['count'] = 0

# Increment count on button click
if st.button('Click me!'):
    st.session_state['count'] += 1

st.write('Count:', st.session_state['count'])

user_input = st.text_input("Enter your name", key="name")

# Store the name in session state
if user_input:
      st.session_state.user_name = user_input

# Display stored name
if 'user_name' in st.session_state:
      st.write(f"Hello, {st.session_state.user_name}!")