import streamlit as st

st.title('User Feedback System')

with st.form(key='feedback_form'):
    feedback = st.text_area(label='Enter your feedback here')
    submit_button = st.form_submit_button(label='Submit')
    
def store_feedback(feedback):
   with open('feedback.txt', 'a') as f:
       f.write(feedback + '\n')

if submit_button and feedback:
   store_feedback(feedback)
   st.success('Thank you for your feedback!')

st.subheader('User Feedback')
if st.checkbox('Show feedback'):
    with open('feedback.txt', 'r') as f:
        for line in f:
            st.text_area(label='', value=line, height=100, disabled=True)