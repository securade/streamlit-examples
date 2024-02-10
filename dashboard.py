import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.title("Data Dashboard")

# Sidebar for filters
sidebar = st.sidebar
sidebar.header("Filters")

# Sample data
df = sns.load_dataset('iris')

# Sidebar Filters
species = sidebar.multiselect("Select Species", options=df['species'].unique(), default=df['species'].unique())

# Filtering Data
filtered_df = df[df['species'].isin(species)]

# Displaying Charts
st.subheader("Sepal Length Distribution")
fig, ax = plt.subplots()
ax.hist(filtered_df['sepal_length'], bins=20)
st.pyplot(fig)