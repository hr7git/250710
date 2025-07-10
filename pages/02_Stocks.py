import streamlit as st
import pandas as pd
import numpy as np
import datetime

# MBTI 유형별 주식 추천 및 설명 데이터
mbti_stock_data = {
    "ISTJ": {
        "stocks": [
            {"ticker": "JPM", "name": "JP모건 체이스", "desc": "안정적이고 보수적인 투자 성향의 ISTJ에게는 금융권의 대표 주자이자 꾸준한 실적을 보여주는 JP모건 체이스가 적합합니다. 견고한 비즈니스 모델과 배당 성향이 매력적입니다."},
            {"ticker": "PG", "name": "프록터 앤드 갬블", "desc": "일상생활에 필수적인 소비재를 다루는 PG는 경기 변동에 강하고 안정적인 현금 흐름을 자랑합니다. 예측 가능한 투자를 선호하는 ISTJ에게 좋은 선택입니다."},
            {"ticker": "KO", "name": "코카콜라", "desc": "오랜 역사와 강력한 브랜드 파워를 가진 코카콜라는 경기 방어주로서 안정적인 수익을 기대할 수 있습니다. 장기적이고 신뢰할 수 있는 투자를 선호하는 ISTJ에게 안성맞춤입니다."}
        ]
    },
    "ISFJ": {
        "stocks": [
            {"ticker": "JNJ", "name": "존슨앤드존슨", "desc": "헬스케어 분야의 글로벌 리더인 존슨앤드존슨은 필수 소비재 성격이 강해 안정적인 실적을 보여줍니다. 사회적 가치를 중시하고 안정적인 투자를 선호하는 ISFJ에게 적합합니다."},
            {"ticker": "PFE", "name": "화이자", "desc": "의약품 개발 및 생산을 통해 인류 건강에 기여하는 화이자는 꾸준한 연구 개발로 미래 성장 가능성도 높습니다. 안정적이면서도 사회적 기여를 생각하는 ISFJ에게 좋습니다."},
            {"ticker": "MSFT", "name": "마이크로소프트", "desc": "클라우드 서비스와 소프트웨어 분야에서 강력한 입지를 가진 마이크로소프트는 안정적인 성장을 지속하고 있습니다. 기술의 긍정적인 영향력을 고려하는 ISFJ에게 매력적입니다."}
        ]
    },
    "INFJ": {
        "stocks": [
            {"ticker": "GOOGL", "name": "알파벳 (구글)", "desc": "혁신적이고 미래 지향적인 구글은 정보 접근성 향상과 AI 등 인류 발전에 기여합니다. 비전을 중시하는 INFJ에게 성장 가능성과 함께 의미 있는 투자가 될 수 있습니다."},
            {"ticker": "TSLA", "name": "테슬라", "desc": "지속 가능한 에너지와 미래 모빌리티를 선도하는 테슬라는 비전과 변화를 추구하는 INFJ에게 매력적인 선택입니다. 혁신을 통해 세상을 바꾸는 기업에 투자하고 싶다면 좋습니다."},
            {"ticker": "ADBE", "name": "어도비", "desc": "창의적인 도구와 디지털 솔루션을 제공하는 어도비는 예술과 디자인 분야에 기여합니다. 영감과 창의성을 중요시하는 INFJ에게 의미 있는 투자가 될 수 있습니다."}
        ]
    },
    "INTJ": {
        "stocks": [
            {"ticker": "NVDA", "name": "엔비디아", "desc": "인공지능, 데이터 센터 등 미래 기술의 핵심인 반도체를 선도하는 엔비디아는 높은 성장 잠재력을 가지고 있습니다. 통찰력 있고 전략적인 INTJ에게 이상적인 투자처입니다."},
            {"ticker": "AMZN", "name": "아마존", "desc": "전자상거래, 클라우드 컴퓨팅 등 다양한 분야에서 혁신을 이끄는 아마존은 장기적인 성장 잠재력이 높습니다. 분석적이고 미래 지향적인 INTJ에게 적합합니다."},
            {"ticker": "META", "name": "메타 플랫폼스", "desc": "메타버스와 소셜 미디어의 미래를 이끄는 메타는 새로운 기술과 플랫폼에 대한 탐구를 선호하는 INTJ에게 흥미로운 투자처입니다. 잠재적인 파괴적 혁신을 기대할 수 있습니다."}
        ]
    },
    "ISTP": {
        "stocks": [
            {"ticker": "CAT", "name": "캐터필러", "desc": "실용적이고 도구적인 것을 좋아하는 ISTP에게 건설 및 광산 장비 분야의 선두 주자인 캐터필러는 매력적입니다. 실제 사용되는 기계와 산업에 대한 관심과 잘 맞습니다."},
            {"ticker": "DE", "name": "디어앤코", "desc": "농업 및 건설 장비 분야의 글로벌 기업인 디어앤코는 실제적인 생산 활동과 관련이 깊습니다. 손으로 직접 만지고 만드는 것을 선호하는 ISTP의 성향에 부합합니다."},
            {"ticker": "GM", "name": "제너럴 모터스", "desc": "자동차 산업은 기술과 실용성이 결합된 분야로, GM은 오랜 역사와 함께 전기차 등 새로운 기술에 투자하고 있습니다. 기계와 기술에 관심이 많은 ISTP에게 흥미로운 선택입니다."}
        ]
    },
    "ISFP": {
        "stocks": [
            {"ticker": "NKE", "name": "나이키", "desc": "스포츠웨어와 라이프스타일 브랜드인 나이키는 개성 표현과 활동적인 삶을 지향하는 ISFP에게 어필합니다. 감각적이고 자유로운 영혼의 ISFP에게 좋은 선택입니다."},
            {"ticker": "LULU", "name": "룰루레몬", "desc": "애슬레저 의류의 선두 주자인 룰루레몬은 건강하고 아름다운 삶을 추구하는 ISFP에게 매력적입니다. 편안함과 스타일을 동시에 추구하는 성향과 잘 맞습니다."},
            {"ticker": "SBUX", "name": "스타벅스", "desc": "편안하고 아늑한 공간에서 커피와 문화를 즐기는 스타벅스는 감성적이고 여유를 중시하는 ISFP에게 잘 맞습니다. 일상 속 작은 행복을 중요시하는 성향과 연결됩니다."}
        ]
    },
    "INFP": {
        "stocks": [
            {"ticker": "ETSY", "name": "엣시", "desc": "수공예품과 빈티지 상품을 거래하는 엣시는 독창성과 개성을 중시하는 INFP에게 이상적인 투자처입니다. 예술과 공예를 통해 가치를 창출하는 기업에 관심이 많다면 좋습니다."},
            {"ticker": "SPOT", "name": "스포티파이", "desc": "음악과 팟캐스트를 통해 영감을 제공하는 스포티파이는 창의적이고 감성적인 INFP에게 매력적입니다. 예술과 소통의 가치를 중요시하는 성향과 잘 맞습니다."},
            {"ticker": "CHWY", "name": "츄이", "desc": "반려동물 용품 및 서비스를 제공하는 츄이는 동물과 생명에 대한 사랑이 깊은 INFP에게 어필합니다. 따뜻한 마음과 가치 있는 소비를 추구하는 성향에 부합합니다."}
        ]
    },
    "INTP": {
        "stocks": [
            {"ticker": "GOOGL", "name": "알파벳 (구글)", "desc": "복잡한 문제 해결과 정보 탐구를 즐기는 INTP에게 구글은 검색, AI 등 무한한 지적 자극을 제공합니다. 끊임없이 탐구하고 분석하는 성향과 잘 맞습니다."},
            {"ticker": "INTC", "name": "인텔", "desc": "컴퓨터 프로세서의 핵심인 인텔은 기술의 근본 원리를 이해하려는 INTP에게 흥미로운 투자처입니다. 기술의 기반을 다지는 기업에 대한 관심이 높습니다."},
            {"ticker": "IBM", "name": "IBM", "desc": "오랜 역사와 함께 인공지능(왓슨) 및 클라우드 기술을 연구하는 IBM은 복잡한 시스템과 이론에 관심이 많은 INTP에게 매력적입니다. 깊이 있는 기술과 연구에 대한 투자를 선호합니다."}
        ]
    },
    "ESTP": {
        "stocks": [
            {"ticker": "UBER", "name": "우버", "desc": "즉흥적이고 활동적인 ESTP에게 우버는 빠르고 편리한 이동 수단을 제공하며 도시의 역동성을 경험하게 합니다. 새로운 경험과 빠른 변화를 즐기는 성향에 부합합니다."},
            {"ticker": "MGM", "name": "MGM 리조트 인터내셔널", "desc": "호텔, 카지노, 엔터테인먼트 산업의 선두 주자인 MGM은 ESTP의 스릴과 즐거움을 추구하는 성향과 잘 맞습니다. 활기찬 분위기와 즉각적인 만족을 선호합니다."},
            {"ticker": "NFLX", "name": "넷플릭스", "desc": "다양한 콘텐츠를 통해 새로운 경험을 제공하는 넷플릭스는 ESTP의 즉흥적이고 즐거움을 추구하는 성향과 잘 맞습니다. 엔터테인먼트를 통해 활력을 얻는 투자처입니다."}
        ]
    },
    "ESFP": {
        "stocks": [
            {"ticker": "DIS", "name": "월트 디즈니", "desc": "꿈과 즐거움을 선사하는 디즈니는 사교적이고 낙천적인 ESFP에게 완벽한 투자처입니다. 사람들에게 행복을 주고 함께 즐길 수 있는 테마파크와 엔터테인먼트 산업에 관심이 많습니다."},
            {"ticker": "MCD", "name": "맥도날드", "desc": "전 세계적으로 사랑받는 맥도날드는 친근하고 보편적인 즐거움을 제공합니다. 사람들과 함께 식사하고 교류하는 것을 좋아하는 ESFP에게 매력적입니다."},
            {"ticker": "NCLH", "name": "노르웨이 크루즈 라인 홀딩스", "desc": "여행과 새로운 경험을 좋아하는 ESFP에게 크루즈 산업은 매력적인 선택입니다. 다양한 사람들과 만나고 즐거운 시간을 보낼 수 있는 분야에 관심이 높습니다."}
        ]
    },
    "ENFP": {
        "stocks": [
            {"ticker": "TSLA", "name": "테슬라", "desc": "혁신과 미래를 선도하는 테슬라는 ENFP의 열정과 비전을 자극합니다. 세상을 더 좋게 변화시키려는 기업에 투자하고 싶다면 좋습니다."},
            {"ticker": "NIO", "name": "니오 (중국 전기차)", "desc": "혁신적인 전기차 기술과 사용자 경험을 중시하는 니오는 ENFP의 새로운 아이디어와 가능성을 탐구하는 성향과 잘 맞습니다. 미래 지향적인 기술에 대한 관심이 높습니다."},
            {"ticker": "SQ", "name": "블록 (스퀘어)", "desc": "핀테크 혁신을 통해 금융 서비스를 대중화하는 블록은 ENFP의 창의적이고 사회적 영향을 미치는 기술에 대한 관심을 충족시킵니다. 새로운 비즈니스 모델에 대한 흥미가 높습니다."}
        ]
    },
    "ENTP": {
        "stocks": [
            {"ticker": "NFLX", "name": "넷플릭스", "desc": "다양한 장르와 끊임없는 콘텐츠 실험을 하는 넷플릭스는 ENTP의 새로운 아이디어와 도전을 즐기는 성향과 잘 맞습니다. 끊임없이 진화하는 미디어 산업에 흥미를 느낍니다."},
            {"ticker": "BABA", "name": "알리바바 그룹 홀딩", "desc": "전자상거래, 클라우드, 핀테크 등 다양한 분야에서 혁신을 추구하는 알리바바는 ENTP의 복합적인 문제 해결과 다양한 가능성을 탐색하는 성향과 잘 맞습니다."},
            {"ticker": "ROKU", "name": "로쿠", "desc": "스트리밍 플랫폼과 광고 기술을 통해 미디어 산업의 변화를 이끄는 로쿠는 ENTP의 미래 지향적인 사고와 새로운 기술에 대한 관심을 충족시킵니다."}
        ]
    },
    "ESTJ": {
        "stocks": [
            {"ticker": "BRK-B", "name": "버크셔 해서웨이 (B주)", "desc": "워렌 버핏이 이끄는 버크셔 해서웨이는 장기적이고 가치 중심의 투자를 지향합니다. 체계적이고 현실적인 ESTJ에게 안정적인 포트폴리오를 제공합니다."},
            {"ticker": "XOM", "name": "엑슨모빌", "desc": "에너지 산업의 거인인 엑슨모빌은 안정적인 현금 흐름과 필수적인 자원을 다룹니다. 현실적이고 실용적인 ESTJ에게 신뢰할 수 있는 투자처입니다."},
            {"ticker": "UNH", "name": "유나이티드헬스 그룹", "desc": "미국 최대의 건강 보험 회사인 유나이티드헬스 그룹은 안정적인 수요와 성장 잠재력을 가지고 있습니다. 체계적인 산업에서 효율적인 경영을 추구하는 ESTJ에게 매력적입니다."}
        ]
    },
    "ESFJ": {
        "stocks": [
            {"ticker": "CRM", "name": "세일즈포스", "desc": "고객 관계 관리(CRM) 소프트웨어 분야의 선두 주자인 세일즈포스는 사람들과의 소통과 관계를 중요시하는 ESFJ에게 매력적입니다. 사람들을 돕는 기술에 관심이 높습니다."},
            {"ticker": "MGM", "name": "MGM 리조트 인터내셔널", "desc": "엔터테인먼트와 환대를 제공하는 MGM은 ESFJ의 사교적이고 즐거움을 공유하려는 성향과 잘 맞습니다. 사람들과 함께 행복한 경험을 만들어가는 기업에 관심이 많습니다."},
            {"ticker": "AAL", "name": "아메리칸 항공 그룹", "desc": "여행을 통해 사람들을 연결하는 항공 산업은 ESFJ의 사회적 상호작용과 연결을 중요시하는 성향과 잘 맞습니다. 사람들에게 즐거움을 주는 경험을 제공하는 기업에 투자하고 싶다면 좋습니다."}
        ]
    },
    "ENFJ": {
        "stocks": [
            {"ticker": "MSFT", "name": "마이크로소프트", "desc": "기술을 통해 전 세계 사람들의 삶을 향상시키는 마이크로소프트는 ENFJ의 리더십과 긍정적인 영향력을 추구하는 성향과 잘 맞습니다. 사회적 책임을 다하는 기업에 투자하고 싶다면 좋습니다."},
            {"ticker": "V", "name": "비자", "desc": "전 세계적인 결제 시스템을 통해 경제 활동을 원활하게 하는 비자는 ENFJ의 사람들을 돕고 연결하는 가치를 실현하는 기업입니다. 글로벌 영향력을 가진 기업에 관심이 많습니다."},
            {"ticker": "SBUX", "name": "스타벅스", "desc": "커피를 통해 사람들에게 영감을 주고 공동체를 형성하는 스타벅스는 ENFJ의 따뜻하고 포용적인 성향과 잘 맞습니다. 사람들과의 유대감을 형성하는 기업에 매력을 느낍니다."}
        ]
    },
    "ENTJ": {
        "stocks": [
            {"ticker": "AAPL", "name": "애플", "desc": "혁신적인 제품과 강력한 브랜드 리더십을 가진 애플은 ENTJ의 비전과 목표 달성을 위한 추진력과 잘 맞습니다. 시장을 선도하는 기업에 대한 관심이 높습니다."},
            {"ticker": "TSM", "name": "TSMC", "desc": "세계 최대의 파운드리 기업인 TSMC는 반도체 산업의 핵심이자 기술 혁신을 주도합니다. 전략적이고 효율성을 중시하는 ENTJ에게 글로벌 시장 지배력을 가진 기업이 매력적입니다."},
            {"ticker": "BAC", "name": "뱅크 오브 아메리카", "desc": "글로벌 금융 시장의 주요 플레이어인 뱅크 오브 아메리카는 ENTJ의 리더십과 대규모 조직 운영에 대한 관심과 잘 맞습니다. 체계적이고 효율적인 금융 시스템에 대한 이해가 높습니다."}
        ]
    }
}

def generate_dummy_stock_data(ticker, days=5*252): # 5년치 영업일 기준 (대략)
    """가상의 주가 데이터를 생성합니다."""
    end_date = datetime.date.today()
    start_date = end_date - datetime.timedelta(days=days * 1.5) # 넉넉하게 기간 잡기
    
    dates = pd.date_range(start=start_date, end=end_date, freq='B') # Business day frequency
    
    # Simulate a general upward trend with some volatility
    prices = np.cumsum(np.random.normal(0.1, 0.5, len(dates))) + 100
    prices = np.maximum(prices, 50) # Ensure prices don't go too low
    
    df = pd.DataFrame({
        'Date': dates,
        'Close': prices
    })
    
    # Filter to last 5 years of data
    five_years_ago = end_date - datetime.timedelta(days=5 * 365)
    df = df[df['Date'] >= five_years_ago].reset_index(drop=True)

    return df

st.set_page_config(layout="wide")
st.title("💖 당신의 MBTI에 딱 맞는 미국 주식은? 📈")
st.write("아래에서 당신의 MBTI 유형을 선택하면, 그에 맞는 미국 주식을 추천해 드립니다! 🎈")

# MBTI 유형 드롭다운 메뉴
mbti_options = list(mbti_stock_data.keys())
selected_mbti = st.selectbox("당신의 MBTI 유형을 선택하세요:", mbti_options)

if st.button("✨ 주식 추천받기 ✨"):
    if selected_mbti:
        st.balloons()  # 풍선 효과 추가
        st.success(f"🎉 **{selected_mbti}** 유형에게 추천하는 미국 주식입니다! 🎉")
        st.markdown("---")

        recommendations = mbti_stock_data[selected_mbti]["stocks"]

        for stock in recommendations:
            st.subheader(f"💰 {stock['ticker']}: {stock['name']}")
            st.write(f"👉 {stock['desc']}")

            st.write(f"📊 **{stock['ticker']}** 최근 5년 가상 주가 추이:")
            
            # 가상의 주가 데이터 생성 및 출력
            dummy_data = generate_dummy_stock_data(stock['ticker'])
            st.line_chart(dummy_data.set_index('Date')['Close'])
            
            st.markdown("---")
    else:
        st.info("MBTI 유형을 선택해주세요.")

st.markdown("""
<style>
.stButton>button {
    background-color: #6C5CE7;
    color: white;
    font-size: 18px;
    padding: 10px 20px;
    border-radius: 10px;
    border: none;
    cursor: pointer;
    box-shadow: 2px 2px 5px rgba(0,0,0,0.2);
}
.stButton>button:hover {
    background-color: #8A2BE2;
    transform: translateY(-2px);
    transition: all 0.2s ease-in-out;
}
.stSubheader {
    color: #FF69B4;
}
</style>
""", unsafe_allow_html=True)
