import streamlit as st

st.title("병의원 검색기")

name = st.text_input("병의원 이름 입력")

if name:
    st.write(f"{name} 검색 결과입니다.")
