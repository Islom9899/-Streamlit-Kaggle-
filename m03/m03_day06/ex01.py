import streamlit as st

#다중 선택 박스
fruits = st.multiselect(
    '문제) 과일을 모두 선택하세요(복수 정답 가능)',
    ['사과','토마토','당근','바나나']
)
correct = {'사과','토마토','바나나'} # 정답(세트형식)

if set(fruits) == correct:
    st.write('완벽해요! 모두 맞았습니다 ^^')
else:
    st.write('다시 선택해보세요!')
