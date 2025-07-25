import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from PIL import Image

# 메인 페이지
st.title('This is main page')
# 사이드 바(왼쪽)
with st.sidebar:
    st.title('This is sidebar')
    side_option = st.multiselect(
        label='Your selection is',
        options = ['Car','Airplane','Train','Ship','Bicycle'],
        placeholder='select transportation'
    )
img2 = Image.open(r'input\image2.jpg')
img3 = Image.open(r'input\image3.jpg')

st.header('Lemona+de')
st.image(img2,width=300, caption='Image from Unsplash')
st.header('Cocktail')
st.image(img3, width=300,caption='Image from Unsplash')

# columns
col1,col2 = st.columns(2)

with col1:
    st.header('Lemonade')
    st.image(img2,width=300,caption='Image from Unsplash')

with col2:
    st.header('Cocktail')
    st.image(img3,width=300,caption='Image from Unsplash')

st.divider()

# tabs
tab1, tab2 = st.tabs(['Table','Graph'])

df = pd.read_csv(r'input\medical_cost.csv')
# region이 "northwest"인 것만 다시 데이터프레임(df)에 저장
df = df.query('region =="northwest"')

with tab1:
    st.table(df.head())

with tab2: # 차트
    # 차트공간 ,축
    fig,ax = plt.subplots()
    #seaborn에 있는 산점도 그래프 사용
    #df의 'bmi'컬럼,'changes'컬럼,axis=축값(ax)
    sns.scatterplot(data=df,x='bmi',y='charges',ax=ax)
    st.pyplot(fig)
    

