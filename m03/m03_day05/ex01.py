import streamlit as st

# 제목 관련 - title,header,subheader
st.title('This is title')
st.title('_이탤릭체 제목_ :blue[파란색] 그리고 선글라스 이모지 :sunglasses:')

st.header('This is header')
st.header('_이탤릭체 헤더_ :red[빨강색] 그리고 선글라스 이모지 :sunglasses:')

st.subheader('This is subheader')
st.subheader('_이탤릭체 서브헤더_ :green[초록색] 그리고 선글라스 이모지 :sunglasses:')
# text
st.text('이것을 택스트입니다!')

# divider - 구분선
st.divider()

st.write('---') # 구분선
