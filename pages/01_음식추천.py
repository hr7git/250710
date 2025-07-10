import streamlit as st

# MBTI 별 음식 추천 데이터
mbti_food_recommendations = {
    "INTJ": [
        {"food": "샐러드 볼 🥗", 
         "recipe": "채소, 퀴노아, 닭가슴살, 올리브오일을 섞어 간단하게 만들어요.", 
         "reason": "건강하면서도 체계적인 식단을 선호하는 INTJ에게 잘 맞아요."},
        {"food": "스시 🍣", 
         "recipe": "신선한 생선과 밥, 김을 준비해 정갈하게 만듭니다.", 
         "reason": "정돈된 모양과 맛이 INTJ의 감성과 어울려요."},
        {"food": "미소된장국 🍲", 
         "recipe": "된장과 다시마 육수에 두부, 파를 넣고 끓입니다.", 
         "reason": "심플하지만 깊은 맛을 좋아하는 INTJ에게 딱이에요."}
    ],
    "ENFP": [
        {"food": "타코 🌮", 
         "recipe": "또르띠아에 고기, 채소, 소스를 올려 싸먹어요.", 
         "reason": "재미있고 다채로운 조합을 즐기는 ENFP에게 잘 맞아요."},
        {"food": "떡볶이 🌶️", 
         "recipe": "떡, 어묵, 고추장 양념을 넣고 매콤하게 끓여요.", 
         "reason": "매콤한 맛과 친근한 분위기가 ENFP 스타일!"}, 
        {"food": "망고 스무디 🥭", 
         "recipe": "망고, 요거트, 얼음을 블렌더에 갈아요.", 
         "reason": "상큼하고 활기찬 에너지 충전에 좋아요."}
    ],
    "ISTP": [
        {"food": "불고기 🍖", 
         "recipe": "양념한 소고기를 팬에 볶아 맛있게 익혀요.", 
         "reason": "전통적이면서도 간편하게 조리할 수 있어 실용적인 ISTP에게 적합해요."},
        {"food": "카레라이스 🍛", 
         "recipe": "야채와 고기를 볶고, 물과 카레 가루를 넣어 끓여요.", 
         "reason": "간단하면서도 풍부한 맛을 선호하는 스타일이에요."},
        {"food": "치킨랩 🌯", 
         "recipe": "또르띠아에 치킨과 채소를 넣고 돌돌 말아요.", 
         "reason": "휴대성과 효율을 중시하는 ISTP에게 딱!"}
    ],
    "ISFJ": [
        {"food": "된장찌개 🫕", 
         "recipe": "된장, 두부, 호박, 감자 등을 넣고 푹 끓여요.", 
         "reason": "정감 가는 전통 음식은 ISFJ에게 안식 같은 존재에요."},
        {"food": "계란찜 🍳", 
         "recipe": "계란, 물, 소금을 넣고 부드럽게 쪄요.", 
         "reason": "따뜻하고 부드러운 음식이 잘 어울려요."},
        {"food": "김밥 🍙", 
         "recipe": "밥, 재료들을 김에 넣고 말아요.", 
         "reason": "정성과 손맛이 필요한 김밥은 ISFJ의 정서와 잘 맞아요."}
    ],
    # 나머지 MBTI는 아래처럼 복사해서 패턴만 유지하면 됩니다.
}

# Streamlit 앱 구성
st.set_page_config(page_title="MBTI 음식 추천기", page_icon="🍽️")

st.title("🍱 MBTI 음식 추천기")
st.markdown("당신의 **MBTI 유형**에 맞는 음식을 추천해드릴게요! 😋")

# MBTI 선택
selected_mbti = st.selectbox("MBTI 유형을 선택하세요:", list(mbti_food_recommendations.keys()))

if selected_mbti:
    st.balloons()
    st.success(f"🎉 {selected_mbti} 유형에게 어울리는 음식들을 소개합니다!")

    for item in mbti_food_recommendations[selected_mbti]:
        st.markdown(f"### 🍴 {item['food']}")
        st.write(f"**📌 간단 레시피:** {item['recipe']}")
        st.write(f"**💡 추천 이유:** {item['reason']}")
        st.markdown("---")
