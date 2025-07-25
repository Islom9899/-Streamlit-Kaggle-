import streamlit as st

# button

# 버튼을 클릭했을 때
def button_write():
    st.write('버튼을 클릭했음!!!')

st.button('Reset', type='primary')
#'클릭했음'버튼을 클릭하면 button_write() 이벤트함수가 실행된다
st.button('글릭했음!',on_click=button_write)

# 버튼을 클릭 -> if문을 실행
if st.button('ㅋㅋㅋ'):
    st.write('메롱~~~')
    
st.divider() # 구분선

# 중요버튼
if st.button('중요!',type='primary',key='btn1'):
    st.write('중요버튼이 클릭되었다!')

if st.button('일반!',type='secondary',key='btn2'):
    st.write('일반버튼이 클릭되었다!')

# 버튼처럼 생기지 않음(디차인만) -> 버튼 기능은 한다.
if st.button('무시!', type='tertiary',key='btn3'):
    st.write('무시 버튼이 클릭되었다!')