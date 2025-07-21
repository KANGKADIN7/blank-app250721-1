import streamlit as st

st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
import streamlit as st
import pandas as pd
import numpy as np


st.title("Streamlit 요소 예시 페이지")  # 페이지 제목

st.header("텍스트 요소")  # 헤더
st.subheader("서브헤더")  # 서브헤더
st.text("일반 텍스트입니다.")  # 일반 텍스트
st.markdown("**마크다운** _스타일_도 지원합니다!")  # 마크다운 텍스트

st.header("입력 요소")
name = st.text_input("이름을 입력하세요")  # 텍스트 입력
age = st.number_input("나이를 입력하세요", min_value=0, max_value=120)  # 숫자 입력
agree = st.checkbox("동의합니다")  # 체크박스
color = st.radio("좋아하는 색은?", ["빨강", "파랑", "초록"])  # 라디오 버튼
hobby = st.multiselect("취미를 선택하세요", ["독서", "운동", "게임", "요리"])  # 다중 선택
date = st.date_input("날짜를 선택하세요")  # 날짜 입력
time = st.time_input("시간을 선택하세요")  # 시간 입력
file = st.file_uploader("파일을 업로드하세요")  # 파일 업로더
st.button("버튼 예시")  # 버튼

st.header("데이터 및 차트")
df = pd.DataFrame({
    "a": np.random.randn(10),
    "b": np.random.randn(10)
})
st.dataframe(df)  # 데이터프레임 표시
st.table(df.head())  # 테이블 표시

st.line_chart(df)  # 라인 차트
st.bar_chart(df)  # 바 차트
st.area_chart(df)  # 에어리어 차트


st.header("이미지 표시")
st.image("https://static.streamlit.io/examples/dog.jpg", caption="강아지 이미지")  # 이미지 표시

st.header("알림 및 진행바")
st.success("성공 메시지입니다!")  # 성공 메시지
st.info("정보 메시지입니다!")  # 정보 메시지
st.warning("경고 메시지입니다!")  # 경고 메시지
st.error("에러 메시지입니다!")  # 에러 메시지

st.progress(70)  # 진행바 (0~100)

st.header("코드 및 예외")
st.code("print('Hello, Streamlit!')")  # 코드 블록
try:
    1 / 0
except Exception as e:
    st.exception(e)  # 예외 표시

