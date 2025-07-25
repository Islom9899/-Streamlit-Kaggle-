import streamlit as st
from datetime import time,datetime,timedelta

#슬라이더 -> 0부터 100까지의 점수, 기본값은 1
score = st.slider('Your score is ...',0, 100, 1)
# 입력받은 점수를 텍스트로 화면에 출력
st.text(f'Score : {score}')

# 합격/불합격 조건문 -> 60점 이상이면 합격
if score >=60:
    st.success('합격입니다!')
else:
    st.error('불합격입니다! ㅠㅠ')

st.divider()


# 시작 시간과 종료 시간을 슬라이더로 입력받는다
start_time,end_time = st.slider(
    'Working time is...',
    min_value = time(0), # 최소 시간 0 시 -> 00:00
    max_value = time(23), # 최대 시간 23 시 -> 23:00(24시간 기준)
    value= (time(9), time(18)), # 기본값 09:00  ~ 18:00 
    format = 'HH:MM' # 시간 포맷을 시:분 으로 표시
)

# 선택한 근무 시작 시간과 종료 시간을 텍스트로 출력
st.text(f'Working time : {start_time}, {end_time}')

# 근무 시간 계산 (분 단위 차이) ,같은 날짜 기준
datetime_start = datetime.combine(datetime.today(), start_time)
datetime_end = datetime.combine(datetime.today(), end_time)

# 근무 시간 차이 계산
working_duration = datetime_end - datetime_start

# 9시간 이상인지 확인
if working_duration >= timedelta(hours=9):
    st.success('근무시간이 9시간 이상입니다.(점심시간 1시간 포함)')
else:
    st.warning('근무시간이 9시간 미만입니다.(점심시간 1시간 포함)')