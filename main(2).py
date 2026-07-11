import streamlit as st

st.set_page_config(
    page_title="YouTube 댓글 분석기",
    page_icon="▶️",
    layout="wide",
)

home = st.Page("pages/1_홈.py", title="홈", icon="🏠", default=True)
video = st.Page("pages/2_영상_조회.py", title="영상·썸네일", icon="🎬")
comments = st.Page("pages/3_댓글_분석.py", title="댓글 분석", icon="📊")
popular = st.Page("pages/4_인기_댓글.py", title="좋아요 많은 댓글", icon="👍")

navigation = st.navigation([home, video, comments, popular])
navigation.run()
