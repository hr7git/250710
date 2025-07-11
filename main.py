import streamlit as st

def get_travel_recommendations(mbti_type):
    recommendations = {
        "ISTJ": {
            "여행지": [
                "1. 스위스 알프스 (Switzerland Alps) 🏔️",
                "2. 교토, 일본 (Kyoto, Japan) 🌸",
                "3. 뉴질랜드 남섬 (South Island, New Zealand) 🏞️"
            ],
            "관광지_설명": [
                "**스위스 알프스**: 질서 정연하고 체계적인 ISTJ에게는 웅장하면서도 잘 정돈된 스위스 알프스가 완벽한 선택입니다. 융프라우요흐 같은 곳에서 정확한 기차 시간에 맞춰 자연의 경이로움을 경험하며 계획적인 여행을 즐길 수 있습니다.",
                "**교토, 일본**: 전통과 역사를 중요시하는 ISTJ에게 교토는 고즈넉한 사찰과 정원, 그리고 잘 보존된 옛 거리를 탐험하기에 이상적인 곳입니다. 후시미 이나리 신사의 질서 있는 도리이 길을 걷거나 금각사에서 아름다운 건축물을 감상하며 차분한 시간을 보낼 수 있습니다.",
                "**뉴질랜드 남섬**: 그림 같은 자연 풍경과 다양한 액티비티를 정돈된 환경에서 즐길 수 있어 ISTJ에게 매력적입니다. 퀸스타운에서 계획된 하이킹 코스를 따르거나 밀포드 사운드에서 유람선을 타며 웅장한 자연을 체계적으로 경험할 수 있습니다."
            ]
        },
        "ISFJ": {
            "여행지": [
                "1. 제주도, 대한민국 (Jeju Island, South Korea) 🍊",
                "2. 발리, 인도네시아 (Bali, Indonesia) 🌴",
                "3. 코타키나발루, 말레이시아 (Kota Kinabalu, Malaysia) 🌅"
            ],
            "관광지_설명": [
                "**제주도, 대한민국**: 따뜻하고 배려심 깊은 ISFJ에게 제주는 자연의 아름다움과 편안함을 동시에 선사합니다. 한라산 둘레길을 거닐거나 오름에서 평화로운 풍경을 감상하며 소중한 사람들과 조용한 시간을 보내기 좋습니다.",
                "**발리, 인도네시아**: 휴식과 치유를 중요하게 생각하는 ISFJ에게 발리는 완벽한 휴양지입니다. 우붓의 고요한 논밭에서 요가 수업을 듣거나 울루와투 사원에서 일몰을 보며 평온함을 느낄 수 있습니다.",
                "**코타키나발루, 말레이시아**: 아름다운 해변과 친근한 분위기가 ISFJ에게 안정감을 줍니다. 석양이 아름다운 탄중아루 비치에서 휴식을 취하거나 만따나니 섬에서 스노클링을 즐기며 편안하고 따뜻한 추억을 만들 수 있습니다."
            ]
        },
        "INFJ": {
            "여행지": [
                "1. 산토리니, 그리스 (Santorini, Greece) 💙",
                "2. 아이슬란드 (Iceland) 🌌",
                "3. 아유타야, 태국 (Ayutthaya, Thailand) 🕌"
            ],
            "관광지_설명": [
                "**산토리니, 그리스**: 이상주의적이고 통찰력 있는 INFJ에게 산토리니의 아름다운 풍경은 영감을 줍니다. 이아 마을에서 환상적인 일몰을 감상하며 깊은 사색에 잠기거나 푸른 돔 교회를 보며 평화를 느낄 수 있습니다.",
                "**아이슬란드**: 신비롭고 웅장한 자연은 INFJ의 상상력을 자극합니다. 오로라를 감상하며 우주의 경이로움을 느끼거나 빙하 동굴을 탐험하며 내면의 깊이를 탐구할 수 있습니다.",
                "**아유타야, 태국**: 역사와 영적인 의미가 깊은 아유타야는 INFJ에게 사색의 기회를 제공합니다. 고대 사원의 유적을 거닐며 과거의 이야기를 상상하거나 왓 마하탓에서 부처의 머리를 보며 깨달음을 얻을 수 있습니다."
            ]
        },
        "INTJ": {
            "여행지": [
                "1. 베를린, 독일 (Berlin, Germany) 🏛️",
                "2. 보스턴, 미국 (Boston, USA) 📚",
                "3. 이스라엘 (Israel) 📜"
            ],
            "관광지_설명": [
                "**베를린, 독일**: 독립적이고 전략적인 INTJ에게 베를린은 역사, 예술, 혁신이 어우러진 도시입니다. 박물관 섬에서 지식을 탐구하거나 베를린 장벽 기념지에서 역사적 의미를 되새기며 깊이 있는 경험을 할 수 있습니다.",
                "**보스턴, 미국**: 지적인 자극을 추구하는 INTJ에게 보스턴은 유서 깊은 교육 기관과 풍부한 역사를 가진 도시입니다. 하버드 대학교 캠퍼스를 거닐거나 프리덤 트레일을 따라 미국의 역사를 탐구하며 지적 호기심을 충족시킬 수 있습니다.",
                "**이스라엘**: 고대 문명과 종교의 발상지로서 INTJ의 분석적인 사고를 자극합니다. 예루살렘의 구시가지를 탐험하며 복잡한 역사와 문화를 이해하거나 사해에서 독특한 자연 현상을 경험하며 깊이 있는 고찰을 할 수 있습니다."
            ]
        },
        "ISTP": {
            "여행지": [
                "1. 스위스 인터라켄 (Interlaken, Switzerland) 🏞️",
                "2. 퀸스타운, 뉴질랜드 (Queenstown, New Zealand) ⛰️",
                "3. 파타고니아, 아르헨티나/칠레 (Patagonia, Argentina/Chile) 🌲"
            ],
            "관광지_설명": [
                "**스위스 인터라켄**: 모험을 즐기고 실용적인 ISTP에게 인터라켄은 패러글라이딩, 래프팅 등 다양한 액티비티를 체험하기에 최적의 장소입니다. 직접 몸으로 부딪히며 스릴을 만끽할 수 있습니다.",
                "**퀸스타운, 뉴질랜드**: 다이나믹한 활동을 선호하는 ISTP에게 퀸스타운은 번지점프, 스카이다이빙 등 극한 스포츠의 천국입니다. 아름다운 자연 속에서 짜릿한 경험을 만끽하며 스트레스를 해소할 수 있습니다.",
                "**파타고니아, 아르헨티나/칠레**: 독립적이고 새로운 경험을 좋아하는 ISTP에게 파타고니아는 대자연 속에서 트레킹과 캠핑을 즐기기에 완벽합니다. 피츠로이 또는 토레스 델 파이네에서 웅장한 자연을 탐험하며 스스로의 한계를 시험해 볼 수 있습니다."
            ]
        },
        "ISFP": {
            "여행지": [
                "1. 몰디브 (Maldives) 🏝️",
                "2. 베니스, 이탈리아 (Venice, Italy) 🚣",
                "3. 교토, 일본 (Kyoto, Japan) 🎋"
            ],
            "관광지_설명": [
                "**몰디브**: 온화하고 예술적인 ISFP에게 몰디브는 아름다운 자연 속에서 영감을 얻고 휴식하기 좋은 곳입니다. 에메랄드빛 바다에서 스노클링을 즐기거나 해변에서 그림 같은 일몰을 감상하며 내면의 평화를 찾을 수 있습니다.",
                "**베니스, 이탈리아**: 감성적이고 아름다움을 추구하는 ISFP에게 베니스는 예술적인 영감을 주는 도시입니다. 곤돌라를 타고 운하를 따라 낭만적인 분위기를 느끼거나 부라노 섬의 다채로운 건물들을 보며 예술적인 감각을 일깨울 수 있습니다.",
                "**교토, 일본**: 고요하고 아름다운 정취를 좋아하는 ISFP에게 교토는 평화로운 사색의 시간을 제공합니다. 아라시야마 대나무 숲길을 거닐거나 전통 찻집에서 차분한 시간을 보내며 자신을 돌아보는 시간을 가질 수 있습니다."
            ]
        },
        "INFP": {
            "여행지": [
                "1. 아이슬란드 (Iceland) 🌌",
                "2. 포틀랜드, 미국 (Portland, USA) 🌲",
                "3. 아유타야, 태국 (Ayutthaya, Thailand) 🧘"
            ],
            "관광지_설명": [
                "**아이슬란드**: 이상주의적이고 창의적인 INFP에게 아이슬란드의 신비로운 자연은 무한한 영감을 줍니다. 오로라 아래에서 명상하거나 폭포와 빙하를 보며 내면의 세계를 탐험할 수 있습니다.",
                "**포틀랜드, 미국**: 자유로운 영혼의 INFP에게 포틀랜드는 독특한 예술과 문화, 그리고 자연이 어우러진 도시입니다. 독립 서점에서 영감을 얻거나 장미 정원에서 평화로운 시간을 보내며 자신만의 시간을 즐길 수 있습니다.",
                "**아유타야, 태국**: 역사와 영적인 분위기를 좋아하는 INFP에게 아유타야는 사색과 성찰의 기회를 제공합니다. 고대 사원 유적을 거닐며 과거의 지혜를 배우거나 불교 명상을 통해 내면의 평화를 찾을 수 있습니다."
            ]
        },
        "INTP": {
            "여행지": [
                "1. 베를린, 독일 (Berlin, Germany) 💻",
                "2. 실리콘밸리, 미국 (Silicon Valley, USA) 💡",
                "3. 교토, 일본 (Kyoto, Japan) 🧠"
            ],
            "관광지_설명": [
                "**베를린, 독일**: 분석적이고 논리적인 INTP에게 베를린은 지적인 탐구를 위한 도시입니다. 박물관 섬에서 깊이 있는 지식을 습득하거나 첨단 기술 관련 전시회를 방문하며 새로운 아이디어를 얻을 수 있습니다.",
                "**실리콘밸리, 미국**: 새로운 기술과 아이디어에 관심이 많은 INTP에게 실리콘밸리는 혁신의 중심지입니다. 스탠포드 대학교나 컴퓨터 역사 박물관을 방문하며 미래 기술의 흐름을 파악하고 지적인 자극을 받을 수 있습니다.",
                "**교토, 일본**: 고도로 정교한 문화와 역사적 건축물은 INTP의 분석적인 사고를 자극합니다. 일본 정원의 철학이나 사찰 건축의 미학을 탐구하며 복잡한 시스템을 이해하는 즐거움을 느낄 수 있습니다."
            ]
        },
        "ESTP": {
            "여행지": [
                "1. 라스베이거스, 미국 (Las Vegas, USA) ✨",
                "2. 이비자, 스페인 (Ibiza, Spain) 🎶",
                "3. 방콕, 태국 (Bangkok, Thailand) 🛍️"
            ],
            "관광지_설명": [
                "**라스베이거스, 미국**: 활동적이고 즉흥적인 ESTP에게 라스베이거스는 화려하고 역동적인 에너지를 경험하기에 완벽한 곳입니다. 카지노, 쇼, 나이트라이프를 즐기며 짜릿한 순간을 만끽할 수 있습니다.",
                "**이비자, 스페인**: 파티와 새로운 경험을 좋아하는 ESTP에게 이비자는 세계적인 클럽과 아름다운 해변이 어우러진 곳입니다. 밤새도록 춤을 추거나 해양 스포츠를 즐기며 에너지를 발산할 수 있습니다.",
                "**방콕, 태국**: 활기찬 도시 분위기와 다양한 경험을 선호하는 ESTP에게 방콕은 흥미로운 선택입니다. 길거리 음식을 탐험하고, 루프탑 바에서 야경을 감상하거나, 활기찬 시장에서 쇼핑을 즐기며 도시의 에너지를 느낄 수 있습니다."
            ]
        },
        "ESFP": {
            "여행지": [
                "1. 리우데자네이루, 브라질 (Rio de Janeiro, Brazil) 💃",
                "2. 칸쿤, 멕시코 (Cancun, Mexico) 🏖️",
                "3. 하와이, 미국 (Hawaii, USA) 🌺"
            ],
            "관광지_설명": [
                "**리우데자네이루, 브라질**: 사교적이고 즉흥적인 ESFP에게 리우데자네이루는 열정적인 문화와 아름다운 해변이 있는 도시입니다. 삼바 축제를 즐기거나 코파카바나 해변에서 활기찬 분위기를 만끽하며 사람들과 어울릴 수 있습니다.",
                "**칸쿤, 멕시코**: 즐거움과 경험을 추구하는 ESFP에게 칸쿤은 휴식과 모험을 동시에 즐길 수 있는 곳입니다. 에메랄드빛 카리브해에서 스노클링을 하거나 마야 유적지를 탐험하며 새로운 경험을 쌓을 수 있습니다.",
                "**하와이, 미국**: 자연 속에서 활기찬 활동을 즐기고 싶은 ESFP에게 하와이는 완벽한 선택입니다. 서핑을 배우거나 루아우 파티에서 현지 문화를 체험하며 신나는 시간을 보낼 수 있습니다."
            ]
        },
        "ENFP": {
            "여행지": [
                "1. 바르셀로나, 스페인 (Barcelona, Spain) 🎨",
                "2. 멜버른, 호주 (Melbourne, Australia) ☕",
                "3. 뉴욕, 미국 (New York, USA) 🗽"
            ],
            "관광지_설명": [
                "**바르셀로나, 스페인**: 열정적이고 창의적인 ENFP에게 바르셀로나는 예술, 건축, 그리고 활기찬 분위기가 넘치는 도시입니다. 가우디의 건축물을 보며 영감을 얻거나 람블라스 거리에서 사람들과 교류하며 새로운 아이디어를 얻을 수 있습니다.",
                "**멜버른, 호주**: 자유분방하고 새로운 경험을 좋아하는 ENFP에게 멜버른은 다채로운 카페 문화, 예술, 그리고 활기찬 도시 분위기를 선사합니다. 골목길을 탐험하며 숨겨진 예술 작품을 발견하거나 페더레이션 스퀘어에서 사람들과 교류하며 영감을 얻을 수 있습니다.",
                "**뉴욕, 미국**: 끊임없이 변화하고 다양한 문화가 공존하는 뉴욕은 ENFP의 호기심을 자극합니다. 브로드웨이에서 공연을 보거나 센트럴 파크에서 다양한 사람들과 교류하며 에너지와 영감을 얻을 수 있습니다."
            ]
        },
        "ENTP": {
            "여행지": [
                "1. 런던, 영국 (London, UK) 💡",
                "2. 베를린, 독일 (Berlin, Germany) 🎨",
                "3. 샌프란시스코, 미국 (San Francisco, USA) 🌉"
            ],
            "관광지_설명": [
                "**런던, 영국**: 똑똑하고 도전적인 ENTP에게 런던은 지적인 자극과 끊임없는 논쟁 거리를 제공합니다. 대영 박물관에서 다양한 지식을 탐구하거나 코벤트 가든에서 다양한 문화를 경험하며 토론할 수 있는 기회를 찾을 수 있습니다.",
                "**베를린, 독일**: 혁신적이고 자유로운 분위기의 베를린은 ENTP의 아이디어를 자극합니다. 예술적인 벽화가 가득한 이스트 사이드 갤러리를 거닐거나 다양한 스타트업 문화를 경험하며 새로운 아이디어를 얻을 수 있습니다.",
                "**샌프란시스코, 미국**: 기술과 혁신의 중심지인 샌프란시스코는 ENTP의 지적인 호기심을 충족시켜 줍니다. 실리콘밸리 주변을 탐험하거나 다양한 기술 컨퍼런스에 참여하여 새로운 아이디어와 트렌드를 접할 수 있습니다."
            ]
        },
        "ESTJ": {
            "여행지": [
                "1. 싱가포르 (Singapore) 🏙️",
                "2. 프랑크푸르트, 독일 (Frankfurt, Germany) 🏦",
                "3. 서울, 대한민국 (Seoul, South Korea) 🏢"
            ],
            "관광지_설명": [
                "**싱가포르**: 체계적이고 효율적인 ESTJ에게 싱가포르는 잘 정돈된 도시 계획과 효율적인 시스템을 경험하기에 좋은 곳입니다. 가든스 바이 더 베이에서 깔끔하게 관리되는 정원을 보거나 마리나 베이 샌즈에서 도시의 효율성을 느낄 수 있습니다.",
                "**프랑크푸르트, 독일**: 질서와 효율성을 중시하는 ESTJ에게 프랑크푸르트는 금융과 비즈니스의 중심지로서 체계적인 도시 구조를 보여줍니다. 유럽중앙은행을 방문하거나 금융 지구를 거닐며 조직적인 시스템의 중요성을 느낄 수 있습니다.",
                "**서울, 대한민국**: 빠르고 효율적인 시스템과 잘 정비된 인프라를 갖춘 서울은 ESTJ에게 만족스러운 여행지입니다. 첨단 기술과 전통이 조화된 모습을 보거나 대기업 빌딩 숲을 거닐며 역동적인 도시의 에너지를 느낄 수 있습니다."
            ]
        },
        "ESFJ": {
            "여행지": [
                "1. 파리, 프랑스 (Paris, France) 🗼",
                "2. 로마, 이탈리아 (Rome, Italy) 🍕",
                "3. 오사카, 일본 (Osaka, Japan) 🐙"
            ],
            "관광지_설명": [
                "**파리, 프랑스**: 사교적이고 따뜻한 ESFJ에게 파리는 낭만적인 분위기와 아름다운 문화가 어우러진 곳입니다. 에펠탑 아래에서 피크닉을 즐기거나 루브르 박물관에서 예술을 감상하며 소중한 사람들과 행복한 시간을 보낼 수 있습니다.",
                "**로마, 이탈리아**: 사람들과의 교류를 중요하게 생각하는 ESFJ에게 로마는 풍부한 역사와 활기찬 분위기를 선사합니다. 콜로세움에서 고대 로마의 역사를 느끼거나 트레비 분수에서 소원을 빌며 행복한 추억을 만들 수 있습니다.",
                "**오사카, 일본**: 친근하고 활기찬 분위기를 선호하는 ESFJ에게 오사카는 다양한 먹거리와 쇼핑, 그리고 유니버설 스튜디오 재팬 같은 즐길 거리가 가득한 도시입니다. 도톤보리에서 맛있는 음식을 즐기거나 오사카 성을 방문하며 사람들과 즐거운 시간을 보낼 수 있습니다."
            ]
        },
        "ENFJ": {
            "여행지": [
                "1. 피렌체, 이탈리아 (Florence, Italy) 🇮🇹",
                "2. 런던, 영국 (London, UK) 💂",
                "3. 시드니, 호주 (Sydney, Australia) 🐨"
            ],
            "관광지_설명": [
                "**피렌체, 이탈리아**: 통솔력 있고 따뜻한 ENFJ에게 피렌체는 아름다운 예술과 문화가 살아 숨 쉬는 도시입니다. 우피치 미술관에서 르네상스 예술을 감상하며 영감을 얻거나 두오모에서 도시의 아름다움을 조망하며 사람들과 소통할 수 있습니다.",
                "**런던, 영국**: 다양한 문화와 활기찬 에너지가 넘치는 런던은 ENFJ에게 리더십을 발휘하고 사람들과 교류하기 좋은 곳입니다. 웨스트엔드에서 공연을 보거나 버킹엄 궁전에서 왕실 문화를 체험하며 다양한 사람들과 소통의 기회를 가질 수 있습니다.",
                "**시드니, 호주**: 따뜻하고 외향적인 ENFJ에게 시드니는 활기찬 도시 분위기와 아름다운 자연이 어우러진 곳입니다. 오페라 하우스에서 공연을 보거나 시드니 하버 브릿지 위를 걸으며 사람들과 함께 즐거운 시간을 보낼 수 있습니다."
            ]
        },
        "ENTJ": {
            "여행지": [
                "1. 뉴욕, 미국 (New York, USA) 🏙️",
                "2. 도쿄, 일본 (Tokyo, Japan) 🗼",
                "3. 상하이, 중국 (Shanghai, China) 东方明珠"
            ],
            "관광지_설명": [
                "**뉴욕, 미국**: 리더십이 강하고 비전 있는 ENTJ에게 뉴욕은 역동적인 에너지와 무한한 기회를 제공합니다. 월스트리트에서 금융의 중심을 경험하거나 타임스퀘어에서 도시의 활기찬 에너지를 느끼며 새로운 목표를 설정할 수 있습니다.",
                "**도쿄, 일본**: 효율적이고 미래지향적인 도쿄는 ENTJ의 전략적 사고를 자극합니다. 신주쿠의 고층 빌딩에서 도시를 조망하며 미래를 구상하거나 첨단 기술 전시회를 방문하여 새로운 비즈니스 아이디어를 얻을 수 있습니다.",
                "**상하이, 중국**: 빠르게 성장하는 상하이는 ENTJ에게 도전적인 기회를 제공합니다. 푸동의 스카이라인을 감상하며 도시의 성장을 느끼거나 상하이 타워에서 도시 전체를 조망하며 전략적인 계획을 세울 수 있습니다."
            ]
        }
    }
    return recommendations.get(mbti_type, None)

st.title("💖 당신의 MBTI에 딱 맞는 여행지는 어디일까요? 🌍")
st.write("아래에서 당신의 MBTI 유형을 선택해 보세요!")

# MBTI 유형 드롭다운 메뉴
mbti_options = [
    "ISTJ", "ISFJ", "INFJ", "INTJ",
    "ISTP", "ISFP", "INFP", "INTP",
    "ESTP", "ESFP", "ENFP", "ENTP",
    "ESTJ", "ESFJ", "ENFJ", "ENTJ"
]
selected_mbti = st.selectbox("당신의 MBTI 유형을 선택하세요:", mbti_options)

if st.button("✨ 여행지 추천받기 ✨"):
    if selected_mbti:
        st.balloons()  # 풍선 효과 추가
        recommendations = get_travel_recommendations(selected_mbti)
        if recommendations:
            st.success(f"🎉 **{selected_mbti}** 유형에게 추천하는 여행지입니다! 🎉")
            st.markdown("---")

            for i, place in enumerate(recommendations["여행지"]):
                st.subheader(f"{place}")
                st.write(recommendations["관광지_설명"][i])
                st.markdown("---")
        else:
            st.warning("선택한 MBTI 유형에 대한 정보가 없습니다. 다시 시도해주세요.")
    else:
        st.info("MBTI 유형을 선택해주세요.")

st.markdown("""
<style>
.stButton>button {
    background-color: #4CAF50;
    color: white;
    font-size: 18px;
    padding: 10px 20px;
    border-radius: 10px;
    border: none;
    cursor: pointer;
}
.stButton>button:hover {
    background-color: #45a049;
}
</style>
""", unsafe_allow_html=True)
