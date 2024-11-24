import os
import streamlit as st
from openai import OpenAI

# OpenAI API Key 설정
os.environ["OPENAI_API_KEY"] = "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"

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
)

# Streamlit UI 구성
st.title("AI 브랜드 이름 생성 서비스")
st.write("당신의 브랜드를 위한 완벽한 이름을 AI가 추천해드립니다!")

# 사용자 입력 받기
brand_description = st.text_input(
    "브랜드의 컨셉, 가치, 또는 키워드를 입력하세요:", 
    placeholder="예: 자연 친화적인 스킨케어, 지속 가능성, 젊고 신선한 이미지"
)

if st.button("이름 추천받기"):
    if brand_description.strip() != "":
        with st.spinner("AI가 브랜드 이름을 생성 중입니다..."):
            try:
                chat_completion = client.chat.completions.create(
                    messages=[
                        {
                            "role": "user",
                            "content": f"다음 브랜드 컨셉에 맞는 멋진 브랜드 이름을 추천해줘: {brand_description}",
                        }
                    ],
                    model="gpt-4o",
                )
                # GPT-4의 응답 출력
                st.success("추천된 브랜드 이름들:")
                st.write(chat_completion.choices[0].message.content)
            except Exception as e:
                st.error(f"오류가 발생했습니다: {e}")
    else:
        st.warning("브랜드의 컨셉이나 키워드를 입력해 주세요!")
      
    # 1. 이름 분석 함수 정의하기
def analyze_name(name, concept):
    """
    이름(name)과 브랜드 컨셉(concept)을 받아서 분석한 결과를 반환합니다.
    """
    analysis = f"'{name}'은(는) '{concept}' 브랜드 컨셉에 잘 어울립니다!"
    return analysis

# 2. 예제 데이터
unique_names = ["PureGlow", "FreshBliss", "CleanAura"]
brand_concept = "깨끗하고 순수한 화장품"

# 3. 이름 분석 결과 출력
for idx, name in enumerate(unique_names, 1):
    analysis = analyze_name(name, brand_concept)  # 함수 호출
    print(f"{idx}. {analysis}")
    
        
    def analyze_name(name, concept):
    # 샘플 점수 생성
         return {
        "발음 용이성": 85,
        "차별성": 90,
        "브랜드 연관성": 95,
        "국제 사용성": 80,
        "총점": 87.5,
    }

# 이름 분석 결과 표시
# 1. 처음에 빈 이름표를 만들어 둠
unique_names = []

# 2. 이름표에 이름 넣기
if True:  # 조건에 따라 이름을 추가
    unique_names = ["PureGlow", "FreshBliss", "CleanAura"]

# 3. 이름표를 써서 출력하기
for idx, name in enumerate(unique_names, 1):
    st.write(f"**{idx}. {name}**")
    analysis = analyze_name(name, brand_concept)
    st.write(f"점수: {analysis}")
response = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": f"브랜드 이름 '{name}'에 맞는 슬로건과 로고 아이디어를 제안해줘."
        }
    ],
    model="gpt-4o",
)
st.write(response.choices[0].message.content)

