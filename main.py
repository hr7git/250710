import streamlit as st

# MBTI 별 여행지 추천 데이터
mbti_travel_recommendations = {
    "INTJ": [
        {"place": "교토, 일본 🇯🇵", "reason": "조용하고 깊이 있는 사찰과 정원이 많아 사색하기 좋아요."},
        {"place": "아이슬란드 🇮🇸", "reason": "광활한 자연 속에서 에너지 충전과 창의적인 생각을 할 수 있어요."},
        {"place": "프라하, 체코 🇨🇿", "reason": "역사적인 건축물과 예술적인 분위기가 내면을 자극해요."}
    ],
    "INFP": [
        {"place": "피렌체, 이탈리아 🇮🇹", "reason": "예술과 감성의 도시에서 감수성을 채울 수 있어요."},
        {"place": "우붓, 발리 🇮🇩", "reason": "자연과 명상이 어우러진 힐링 스팟이에요."},
        {"place": "퀘벡시티, 캐나다 🇨🇦", "reason": "동화 같은 분위기의 마을이 마음을 따뜻하게 해줘요."}
    ],
    "ENTP": [
        {"place": "베를린, 독일 🇩🇪", "reason": "창의적인 에너지가 넘치는 도시로 새로운 아이디어를 얻을 수 있어요."},
        {"place": "뉴욕, 미국 🗽", "reason": "다양성과 혁신이 공존하는 곳에서 자극을 받을 수 있어요."},
        {"place": "방콕, 태국 🇹🇭", "reason": "에너지 넘치고 다채로운 경험이 가득해요."}
    ],
    "ISFP": [
        {"place": "산토리니, 그리스 🇬🇷", "reason": "감각적인 풍경과 조용한 감성이 어우러져 있어요."},
        {"place": "퀸스타운, 뉴질랜드 🇳🇿", "reason": "자연 속에서 자유롭고 평화로운 시간을 보낼 수 있어요."},
        {"place": "바르셀로나, 스페인 🇪🇸", "reason": "예술적인 도시 분위기와 자유로움이 매력적이에요."}
    ]
}

# Streamlit 앱 시작
st.set_page_config(page_title="MBTI 여행지 추천기", page_icon="🌍")

st.title("✈️ MBTI 여행지 추천기")
st.markdown("당신의 **MBTI** 유형을 선택하면, 맞춤형 여행지를 추천해드릴게요! 😎")

selected_mbti = st.selectbox("MBTI 유형을 선택하세요:", list(mbti_travel_recommendations.keys()))

if selected_mbti:
    st.balloons()
    st.success(f"🎉 {selected_mbti} 유형에게 딱 맞는 여행지를 추천드릴게요!")

    recommendations = mbti_travel_recommendations[selected_mbti]
    for rec in recommendations:
        st.markdown(f"### 📍 {rec['place']}")
        st.write(f"👉 {rec['reason']}")
        st.markdown("---")
