import numpy as np
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

st.title('課題')
st.markdown('''
カフェラテの内容量

- エスプレッソ
  - 10g
- ミルク
  - 40g
''')

@st.cache
def rand_df(r=10, c=5):
    df = pd.DataFrame(
        np.random.randn(r, c),
        columns=('col %d' % i for i in range(c)))
    return df
dataframe = rand_df(c=3, r=10)

st.dataframe(dataframe.head(n=3))
st.line_chart(dataframe)
st.sidebar.header('サイドバー')
p = st.sidebar.slider('確率の設定', min_value=0.0, max_value=1.0, value=0.8)
st.sidebar.write(f'設定値は {p} です')