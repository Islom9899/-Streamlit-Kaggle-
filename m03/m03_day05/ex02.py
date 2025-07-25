# code

import streamlit as st

code = '''
import seaborn as sns

iris = sns.load_dataset('iris')
sns.pairplot(data=iris, hue='species',corner=True)
plt.show()
'''
st.code(code, language='python') # 파이썬 언어다(파이썬 언어로 표현해라.)