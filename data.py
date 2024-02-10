import streamlit as st
import pandas as pd

uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    # To read file as string:
    # string_data = uploaded_file.read().decode('utf-8')
    # To convert to a DataFrame (for CSV files):
    df = pd.read_csv(uploaded_file)
    st.write(df)
    
# Filtering data based on user input
user_input = st.sidebar.text_input("Search by keyword")
filtered_df = df[df['Name'].str.contains(user_input, na=False)]

st.write("Filtered DataFrame:", filtered_df)

# Sample data
data = pd.DataFrame({
  'numbers': [1, 2, 3, 4],
  'values': [10, 20, 30, 40]
})

# Line chart
st.line_chart(data)

# Bar chart with customization
chart = st.bar_chart(data, width=500, height=300)

import plotly.express as px

# Sample data
df = px.data.iris()

# Creating a Plotly figure
fig = px.scatter(df, x='sepal_width', y='sepal_length', color='species')

# Displaying the figure in Streamlit
st.plotly_chart(fig)

import altair as alt

# Altair example
chart = alt.Chart(df).mark_circle(size=60).encode(
    x='sepal_width',
    y='sepal_length',
    color='species',
    tooltip=['species', 'sepal_length', 'sepal_width']
)

# Displaying the chart
st.altair_chart(chart, use_container_width=True)