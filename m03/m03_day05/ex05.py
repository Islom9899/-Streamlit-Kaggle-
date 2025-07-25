import streamlit as st
import pandas as pd

df_menu = pd.DataFrame({
    '메뉴명':['아메리카노','카페라때','카푸치노','말차라떼'],
    '가격' : [4500,5000,5500,6000]
})

# 데이터프레임 출력
st.dataframe(df_menu, width=10, height=170, use_container_width=True)

st.divider()

#테이블
st.table(df_menu)