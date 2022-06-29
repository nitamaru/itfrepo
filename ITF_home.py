import streamlit as st
import pandas as pd

st.set_page_config(
    page_title='ITF_Streamlit_page',
    page_icon='💻'
)


st.title('ようこそ！Streamlitの世界へ！')


# 野球データの入ったデータフレーム
baseball_df = pd.DataFrame({'打率': [0.315, 0.255, 0.260, 0.313, 0.322],
                            '本塁打': [27, 20, 18, 16, 8],
                            '打点': [74, 59, 56, 36, 32]},
                            index=['村上', '岡本', '大山', 'ウォーカー', '佐野'])

st.write('#### st.dataframeでデータフレームの中身を表示')

# データフレームを表示し、最大値に色を付ける
st.dataframe(baseball_df.style.highlight_max(axis=0), 800, 200)


st.write('#### ボタンの表示')

answer = st.button('ボタンだよ')

if answer == True:
     st.write('なにも起こりません。')
else:
     st.write('押してみてね')


st.write('#### チェックボックス')

st.write('2の7乗の結果はどれでしょう。')

answer_1 = st.checkbox('128')
if answer_1 == True :
     st.write('正解！おめでとう。')

answer_2 = st.checkbox('256')
if answer_2 == True :
     st.write('残念！はずれだよ。')

answer_3 = st.checkbox('512')
if answer_3 == True :
     st.write('残念！はずれだよ。')


st.write('#### ラジオボタン')
radio_botton = st.radio('ITF後の懇親会には参加しますか？', ('参加します。', '参加しません。'))


st.write('#### セレクトボックス')

option = st.selectbox(
    '好きな国を選択してください。',
     ('日本', 'アメリカ', '韓国', 'イギリス', 'その他'))
st.write('選ばれたのは、「', option, '」でした。')



st.write('ソースコードを表示')
st.code('''
import streamlit as st
import pandas as pd

st.set_page_config(
    page_title='ITF_Streamlit_page',
    page_icon='💻'
)


st.title('ようこそ！Streamlitの世界へ！')


# 野球データの入ったデータフレーム
baseball_df = pd.DataFrame({'打率': [0.315, 0.255, 0.260],
                            '本塁打': [27, 20, 18],
                            '打点': [74, 59, 56]},
                            index=['村上', '岡本', '大山'])

st.write('#### st.dataframeでデータフレームの中身を表示')

# データフレームを表示し、最大値に色を付ける
st.dataframe(baseball_df.style.highlight_max(axis=0), 800, 200)


st.write('#### ボタンの表示')

answer = st.button('ボタンだよ')

if answer == True:
     st.write('なにも起こりません。')
else:
     st.write('押してみてね')


st.write('#### チェックボックス')

st.write('2の7乗の結果はどれでしょう。')

answer_1 = st.checkbox('128')
if answer_1 == True :
     st.write('正解！おめでとう。')

answer_2 = st.checkbox('256')
if answer_2 == True :
     st.write('残念！はずれだよ。')

answer_3 = st.checkbox('512')
if answer_3 == True :
     st.write('残念！はずれだよ。')


st.write('#### ラジオボタン')
radio_botton = st.radio('ITFの懇親会には参加しますか？', ('参加します。', '参加しません。'))


st.write('#### セレクトボックス')

option = st.selectbox(
    '好きな国をを選択してください。',
     ('日本', 'アメリカ', '韓国', 'イギリス', 'その他'))
st.write('選ばれたのは、「', option, '」でした。')



''')
