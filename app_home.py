import streamlit as st


def run_home_app() :
    st.text(' 이 앱은 고객데이터와 자동차 구매 데이터에 대한 내용입니다.\n데이터 분석 및 고객 정보를 넣으면, 얼마 정도의 차를 구매할지를 예측해줍니다.')
    img_url = 'https://www.motorgraph.com/news/photo/201905/22564_72789_5839.jpg'
    st.image(img_url)
