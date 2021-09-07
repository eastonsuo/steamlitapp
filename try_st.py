import streamlit as st
import pandas as pd
import numpy as np

st.title("hello1")
st.write("hello2")


st.table(pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
}))

st.dataframe(pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
}))

st.write({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
})

"123"  # 自动打印

st.markdown('Streamlit is **_really_ cool**.')
st.latex(r'''
a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
 \sum_{k=0}^{n-1} ar^k =
 a \left(\frac{1-r^{n}}{1-r}\right)
 ''')
# 每次修改了代码，都会重新执行（刷新界面时执行）
chart_data = pd.DataFrame(
    np.random.randn(20, 2),
    columns=['a', 'b'])
# 支持 matplotlib Altair deck.gl等画图的库
st.sidebar.line_chart(chart_data)
"123"
# 画map，比如北京的坐标[39.9, 116.3]
map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [39.9, 116.3],
    columns=['lat', 'lon'])

st.map(map_data)
# widgets
# checkbox
if st.checkbox('Show dataframe'):
    chart_data = pd.DataFrame(
       np.random.randn(20, 3),
       columns=['a', 'b', 'c'])

    chart_data

# 下拉框
df = pd.DataFrame({
  'first column': [1, 2, 3, 4],
  'second column': [10, 20, 30, 40]
})
option = st.selectbox(
    'Which number do you like best?',
     df['first column'])

'You selected: ', option
# 在左边出现下拉框可以选择数字
option = st.sidebar.selectbox(
    'Which number do you like best?',
     [0,1])

'You selected:', option

# 使用column进行界面编排
left_column, right_column = st.columns(2)
pressed = left_column.button('Press me?')
if pressed:
  right_column.write("Woohoo!")
# expander隐藏
expander = st.expander("FAQ")
expander.write("Here you could put in some really, really long explanations...")


'Starting a long computation...'
import time
# Add a placeholder
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(50):
  # Update the progress bar with each iteration.
  latest_iteration.text(f'Iteration {i+1}')
  # 到100的时候填满bar
  bar.progress(i + 1)
  time.sleep(0.1)

'...and now we\'re done!'
