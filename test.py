import streamlit as st
import easyocr
import requests

def translate_text_mymemory(text, src_lang="en", tgt_lang="ko", api_key=None):
    base_url = "https://api.mymemory.translated.net/get"
    params = {
        "q": text,
        "langpair": f"{src_lang}|{tgt_lang}",
    }
    if api_key:
        params["key"] = api_key

    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        data = response.json()
        return data.get("responseData", {}).get("translatedText", "")
    else:
        return "번역 실패"

reader = easyocr.Reader(['en', 'ko'], gpu=False)

st.title("이미지 OCR + 번역 (EasyOCR + MyMemory API)")

# 내 API 키 기본값으로 세팅
api_key = st.text_input("MyMemory API Key (기본 내 키 사용)", value="eaf9dbd6c502db179714", type="password")

col1, col2 = st.columns(2)
with col1:
    src_lang = st.text_input("원본 언어 코드 (ex: en, ko)", value="en")
with col2:
    tgt_lang = st.text_input("번역 언어 코드 (ex: ko, en)", value="ko")

uploaded_file = st.file_uploader("이미지를 업로드하세요", type=["png", "jpg", "jpeg"])

if uploaded_file:
    st.image(uploaded_file, caption="업로드한 이미지", use_column_width=True)
    with st.spinner("이미지에서 텍스트 인식 중..."):
        result = reader.readtext(uploaded_file.read(), detail=0)
    
    if not result:
        st.warning("텍스트를 인식하지 못했습니다.")
    else:
        recognized_text = "\n".join(result)
        st.subheader("인식된 텍스트")
        st.text(recognized_text)

        with st.spinner("번역 중..."):
            translated = translate_text_mymemory(recognized_text, src_lang, tgt_lang, api_key)
        
        st.subheader("번역 결과")
        st.text(translated)
