import streamlit as st
from PIL import Image # imageをインポート
import pandas as pd

# localhostで表示されるサイトはまだネットには公開されない
st.title('ねこえもんWEB') # タイトル表示
st.caption('僕はねこえもんです。') # タイトルの下に表示
st.subheader('ねこえもんの正体とは？？') # タイトルの下のタイトル
st.text('こんにちは、ねこえもんです。某○○えもんとは別の生き物だよ！よろしくお願いします。') # サブヘッダーのテキスト

code = '''
import streamlit as st

st.title('ねこえもんWEB')
'''
st.code(code, language='python') # pythonのコードを画面上に表示

# 画像
image = Image.open('Cat.png') # iamgeファイルオブジェクトの作成
st.image(image, width=200)

# 動画
video_file = open('ねこえもん.mp4', 'rb')
video_bytes = video_file.read()
st.video(video_bytes)

with st.form(key='profile_form'):
    
    # 名前と住所のテキストボックス
    name = st.text_input('名前')
    address = st.text_input('住所')

    # セレクトボックス(selectboxの所をradioに変更するとラジオボタンに)
    age_category = st.selectbox(
        '年齢層',
        ('子ども(18才満)', '大人(18才以上)'))
    
    # 複数選択
    hobby = st.multiselect(
        '趣味',
    ('野球', 'ゲーム', '手芸', 'ダンス'))

    # ボタンの作成
    submit_btn = st.form_submit_button('送信')
    cancel_btn = st.form_submit_button('キャンセル')
    if submit_btn:
        st.text(f'ようこそ！{name}さん！{address}に住所を送りました！')
        st.text(f'年齢層: {age_category}')
        st.text(f'趣味: {", ".join(hobby)}') # この設定で文字列に変換して表示が出来る


# データ分析
df = pd.read_excel('sanada.xlsx', sheet_name = "202303")
# st.bar_chart(df['202301']) 棒グラフの表示
# st.line_chart(df) #チャート表示される
# st.dataframe(df) # データを表示
st.table(df) # データが画面全体で表示される
    

# ウィジェット一覧.
# https://docs.streamlit.io/library/api-reference/widgets#input-widgets

# グラフ一覧.
# https://docs.streamlit.io/library/api-reference/charts#chart-elements
