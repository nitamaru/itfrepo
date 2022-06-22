import pandas as pd
import yfinance as yf
import altair as alt
import streamlit as st

# ページのタイトルを作成
st.title('株価可視化アプリ')

# サイドバーの説明文
st.sidebar.write('''
                 # 米国株価
                 こちらは株価可視化ツールです。
                 以下のオプションから表示日数を指定できます。

                 ''')


# 表示日数を指定するスライダー
st.sidebar.write('''
                 ## 表示日数選択
                 ''')

# 初期値20日、最小値1日、最大値60日
days = st.sidebar.slider('日数', 1, 60, 20)

# 表示日数を表示
st.write(f'''
          ### 過去 **{days}日間** のGAFA株価
          ''')

@st.cache
def get_data(days, tickers):
    '''
    データ取得関数

    Parameters
    -------------
    days: int
        表示する日数
    tickers: dict
        企業名と略称の入った辞書

    Returns
    -------------
    df: DataFrame
        該当期間の各企業のデータが入ったdf
    '''

    df = pd.DataFrame()

    for company in tickers.keys():

        # 企業の略称を格納（ex.Apple→AAPL）
        tkr = yf.Ticker(tickers[company])

        # 過去のdays日のデータを取得
        hist = tkr.history(period=f'{days}d')

        # インデックスを（01 January 2022）に変更
        hist.index = hist.index.strftime('%d %B %Y')

        hist = hist[['Close']]
        hist.columns = [company]
        hist = hist.T
        hist.index.name = 'Name'

        # 各企業のdfをconcat
        df = pd.concat([df, hist])

    return df

try:
    # 株価の範囲設定
    st.sidebar.write('''
    ## 株価の範囲指定
    ''')

    ymin, ymax = st.sidebar.slider(
        '範囲を指定してください。',
        0.0, 3500.0, (0.0, 3500.0)
        )

    # 企業名と略称の入った辞書
    tickers = {
        'apple': 'AAPL',
        'facebook': 'FB',
        'google': 'GOOGL',
        'microsoft': 'MSFT',
        'netflix': 'NFLX',
        'amazon': 'AMZN'
    }

    # 入力された期間のデータ取得する
    df = get_data(days, tickers)

    # 企業を選択する
    companies = st.multiselect(
        '会社名を選択してください。',
        list(df.index),
        ['google', 'amazon', 'facebook', 'apple']
    )

    # 企業をしていない場合、メッセージを返す
    if not companies:
        st.error('1社以上指定してください。')

    else:
        # 指定された企業の株価のリストを表示
        data = df.loc[companies]

        # 株価のチャートを表示
        st.write("### 株価 (USD)", data.sort_index())
        data = data.T.reset_index()
        data = pd.melt(data, id_vars=['Date']).rename(
            columns={'value': 'Stock Prices(USD)'}
        )
        chart = (
            alt.Chart(data)
            .mark_line(opacity=0.8, clip=True)
            .encode(
                x="Date:T",
                y=alt.Y("Stock Prices(USD):Q", stack=None, scale=alt.Scale(domain=[ymin, ymax])),
                color='Name:N'
            )
        )
        st.altair_chart(chart, use_container_width=True)

except:
    st.error('エラーが発生しました。')

