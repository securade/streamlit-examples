import streamlit as st
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
import pandas as pd
import numpy as np

# Load dataset
iris = load_iris()
X, y = iris.data, iris.target
clf = RandomForestClassifier()
clf.fit(X, y)

st.title('ML Model Explorer')

# User input features
def user_input_features():
    sepal_length = st.sidebar.slider('Sepal length', 4.3, 7.9, 5.4)
    sepal_width = st.sidebar.slider('Sepal width', 2.0, 4.4, 3.4)
    petal_length = st.sidebar.slider('Petal length', 1.0, 6.9, 1.3)
    petal_width = st.sidebar.slider('Petal width', 0.1, 2.5, 0.2)
    data = {'sepal_length': sepal_length,
               'sepal_width': sepal_width,
               'petal_length': petal_length,
               'petal_width': petal_width}
    features = pd.DataFrame(data, index=[0])
    return features

input_df = user_input_features()

# Display model predictions
prediction = clf.predict(input_df)
prediction_proba = clf.predict_proba(input_df)

st.subheader('Prediction')
st.write(iris.target_names[prediction])
st.subheader('Prediction Probability')
st.write(prediction_proba)