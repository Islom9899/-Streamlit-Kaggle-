import streamlit as st
from PIL import Image

image = Image.open(r'm03_day05\images.jpg')
st.image(image)# 원본 크기로 나온다

st.divider()

# 비율에 맞게 가로 100로 줄어든다
st.image(image, caption='가로100', width=100)

st.divider()

st.image(image, caption='가로200', width=200)
