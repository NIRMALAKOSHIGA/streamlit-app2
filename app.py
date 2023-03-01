import streamlit as st
import pandas as pd
st.title("Machine Learning Model:Hert Disease Prediction")
dataframe = pd.read_csv("heart.csv")
st.write(dataframe)
from PIL import Image
st.subheader("Disease of heart")
image = Image.open('pic.png')
st.image(image, caption='Heart disease ')
