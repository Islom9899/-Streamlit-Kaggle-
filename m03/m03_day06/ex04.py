import streamlit as st
import pandas as pd

# 1.텍스트 입력 창 : 좋아하는 포켓몬 이름 받기
string1 = st.text_input('좋아하는 포켓몬은??',placeholder = '당신이 가장 좋아하는 포켓몬 이름을 적어주세요!',max_chars =32 # 최대 글자 수 제한(32자까지)
                        )

# 입력값이 있다면 화면에 출력
if string1:
    st.text(f'Your answer is {string1}')

#2.비밀번호 입력 창 : 싫어하는 음식 받기(입력 내용을 숨긴다)
string2 = st.text_input(
    '싫어하는 음식은??',
    placeholder = '당신이 가장 싫어하는 음식을 하나 적어주세요!',
    type='password' # 입력값은 *로 가린다
)
# 입력값이 있으면 화면에 출력
if string2:
    st.text(f'Your answer is {string2}')

st.divider()

# 3.파일 업로더 : csv 파일만 업로드 가능
file = st.file_uploader(
    'Choose a file',
    type='csv',  # 확장자를 제한(csv 파일만)
    accept_multiple_files=False # 한번에 하나의 파일만 업로드 가능
)

# 파일이 업로드되면 판다스로 읽어 데이터프레임 생성 후
# 화면에 표형태로 출력

if file is not None:
    df = pd.read_csv(file)
    st.write(df)
