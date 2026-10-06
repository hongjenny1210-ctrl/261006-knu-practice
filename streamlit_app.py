import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="Streamlit 요소 체험",
    page_icon="🚀",
    layout="wide",
)


@st.cache_data
def get_demo_data():
    return pd.DataFrame(
        {
            "월": ["1월", "2월", "3월", "4월", "5월", "6월", "7월", "8월"],
            "매출": [120, 180, 150, 210, 260, 230, 310, 350],
            "목표": [100, 150, 170, 200, 220, 240, 280, 300],
            "방문자": [300, 420, 370, 490, 540, 520, 620, 700],
        }
    )


df = get_demo_data()

st.title("Streamlit 요소를 직접 체험해보세요")
st.caption("이 페이지는 텍스트, 입력창, 버튼, 체크박스, 표, 차트 등 Streamlit에서 자주 쓰는 요소를 한 번에 확인할 수 있게 만든 예시입니다.")

st.markdown(
    """
    Streamlit은 Python 코드를 이용해 웹 앱을 쉽게 만들 수 있는 도구입니다.  
    버튼을 눌러보거나 입력값을 바꾸면 화면이 즉시 반응합니다.  
    초보자도 작은 예제부터 만들면서 기능을 익힐 수 있다는 장점이 있습니다.
    """
)

st.info("💡 핵심 포인트: Streamlit은 '코드 작성 → 화면 반영'이 매우 빠르기 때문에 프로토타입 개발에 적합합니다.")

st.header("1. 텍스트와 메시지 표시", divider="gray")
st.write("아래 요소들은 사용자에게 정보를 전달하는 역할을 합니다.")

st.subheader("기본 텍스트")
st.markdown("- **굵은 글씨**")
st.markdown("- *기울임 글씨*")
st.markdown("- ~~취소선~~")
st.code("st.title(), st.header(), st.markdown(), st.write()", language="python")

st.subheader("알림 메시지")
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.success("성공 메시지")
with col2:
    st.warning("경고 메시지")
with col3:
    st.info("정보 메시지")
with col4:
    st.error("오류 메시지")

st.header("2. 사용자 입력 받기", divider="gray")
st.write("입력창은 사용자와 앱이 상호작용하는 가장 기본적인 방법입니다.")

name = st.text_input("이름을 입력해 주세요", value="홍길동")
comment = st.text_area("한 줄 소개를 적어보세요", value="Streamlit을 배우고 있습니다.")
age = st.number_input("나이 입력", min_value=0, max_value=120, value=25)

selected_day = st.date_input("날짜 선택")
selected_time = st.time_input("시간 선택")
selected_language = st.selectbox("좋아하는 프로그래밍 언어를 고르세요", ["Python", "JavaScript", "Java", "C#", "Go"])
selected_tags = st.multiselect("관심 있는 분야를 고르세요", ["AI", "웹 개발", "데이터 분석", "자동화", "게임"])
selected_level = st.radio("학습 난이도", ["초급", "중급", "고급"])

st.checkbox("이 앱이 이해하기 쉬웠나요?", value=True)

if st.button("입력 결과 확인하기"):
    st.success(
        f"{name}님, {selected_day} {selected_time}에 입력하신 내용은 "
        f"나이 {age}, 언어 {selected_language}, 난이도 {selected_level}입니다."
    )

st.code(
    """
name = st.text_input("이름")
comment = st.text_area("메모")
selected = st.selectbox("선택", ["A", "B", "C"])
checkbox = st.checkbox("체크")
""",
    language="python",
)

st.header("3. 슬라이더와 체크박스", divider="gray")

st.write("슬라이더는 값의 범위를 조절할 때 사용하고, 체크박스는 옵션을 켜거나 끌 때 사용합니다.")

progress_value = st.slider("진행률을 설정해 보세요", 0, 100, 45)
st.progress(progress_value)

show_detail = st.checkbox("추가 설명 보기", value=False)
if show_detail:
    st.caption("체크박스를 켜면 추가 설명이 보입니다. 이처럼 상태에 따라 다른 내용을 보여줄 수 있습니다.")

st.sidebar.title("🧭 사이드바")
st.sidebar.write("이 영역은 보조 메뉴나 설정을 넣는 데 자주 사용됩니다.")
st.sidebar.selectbox("사용 목적", ["학습", "프로토타입", "실무 도구"])
st.sidebar.slider("사이드바 범위", 0, 100, (20, 80))
st.sidebar.checkbox("사이드바 옵션 활성화")

st.header("4. 데이터 표와 차트", divider="gray")
st.write("실제 앱에서는 데이터를 보여줄 때 표나 차트를 자주 사용합니다. 사용자는 그래프를 보면서 정보를 빠르게 이해할 수 있습니다.")

st.subheader("데이터 표")
st.dataframe(df, use_container_width=True)

st.subheader("데이터 테이블")
st.table(df.head(5))

st.subheader("차트 예시")
chart_col1, chart_col2 = st.columns(2)
with chart_col1:
    st.line_chart(df.set_index("월")["매출"])
with chart_col2:
    st.bar_chart(df.set_index("월")["목표"])

st.subheader("복합 차트")
st.area_chart(df.set_index("월")["방문자"])

st.header("5. 탭과 확장 기능", divider="gray")
st.write("탭은 관련 내용을 공간을 나눠서 보여줄 때 사용합니다. 정보를 깔끔하게 정리하는 데 유용합니다.")

tab1, tab2, tab3 = st.tabs(["기본 요소", "입력 요소", "결과 요약"])

with tab1:
    st.markdown("- 제목, 문단, 메시지")
    st.markdown("- 간단한 설명과 안내 문구")

with tab2:
    st.markdown(f"입력한 이름: **{name}**")
    st.markdown(f"선택한 언어: **{selected_language}**")
    st.markdown(f"관심 분야: **{', '.join(selected_tags) if selected_tags else '없음'}**")

with tab3:
    summary = pd.DataFrame(
        {
            "항목": ["이름", "나이", "언어", "선호 난이도"],
            "값": [name, age, selected_language, selected_level],
        }
    )
    st.dataframe(summary, hide_index=True, use_container_width=True)

with st.expander("이 앱에서 각 요소의 역할을 더 자세히 보기"):
    st.markdown(
        """
        - 제목(title): 페이지의 큰 내용을 표현합니다.
        - 입력창(text_input, text_area): 사용자가 값을 입력하게 합니다.
        - 버튼(button): 사용자의 명령을 실행합니다.
        - 체크박스(checkbox): 옵션을 켜거나 끄는 상태를 관리합니다.
        - 슬라이더(slider): 범위 값을 조정할 수 있게 합니다.
        - 데이터프레임(dataframe): 표 형태로 데이터를 보여줍니다.
        - 차트(line_chart, bar_chart): 추세와 비교를 시각적으로 보여줍니다.
        """
    )

st.header("6. 다운로드 버튼", divider="gray")

csv_data = df.to_csv(index=False).encode("utf-8")
st.download_button(
    label="샘플 데이터 다운로드",
    data=csv_data,
    file_name="streamlit_demo_data.csv",
    mime="text/csv",
)

st.subheader("정리")
st.markdown(
    """
    이 예제는 Streamlit에서 자주 쓰는 요소를 하나씩 살펴보는 데 초점을 맞췄습니다.  
    처음에는 간단한 텍스트와 버튼부터 익히고, 점점 입력창, 표, 차트까지 확장해 나가면 됩니다.  
    핵심은 '사용자가 직접 조작하고 결과를 바로 확인하는 경험'입니다.
    """
)

st.balloons()

if st.button("마지막으로 앱을 테스트해 보기"):
    st.toast("좋아요! 이제 Streamlit 앱을 직접 이해하고 사용할 준비가 되었습니다.")
    st.success("앱 테스트 완료! 위 위젯들을 자유롭게 조작해 보세요.")
