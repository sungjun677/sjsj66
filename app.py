import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
from time import sleep



st.set_page_config(
    page_icon="😁",
    page_title="인공지능~~~스트림릿 배포하기",
    layout="wide",
)

with st.spinner(text="페이지 로딩중"):
    sleep(3)

st.header("~~~페이지에 오신것을 환영합니다~~~")
st.subheader("스트림릿 기능 맛보기")

cols = st.columns((1, 1, 2))
cols[0].metric("10/11", "15 °C", "2")
cols[0].metric("10/12", "17 °C", "2 °F")
cols[0].metric("10/13", "15 °C", "2")
cols[1].metric("10/14", "17 °C", "2 °F")
cols[1].metric("10/15", "14 °C", "-3 °F")
cols[1].metric("10/16", "13 °C", "-1 °F")

chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c']
)
cols[2].line_chart(chart_data)