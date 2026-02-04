import streamlit as st 
import joblib
import os
from langdetect import detect

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "model.joblib")
model = joblib.load(MODEL_PATH)

st.title('Nepali News Category Prediction')
st.markdown('Enter news below:')
input_text=st.text_area(
    label='📰 News Content',
    placeholder='📝 Paste your Nepali news article here...',
    max_chars=1000, height=300)

if st.button("🔍 Predict Category"):
    if not input_text.strip():
        st.warning("⚠️ Please enter text to search")
    else:
        if detect(input_text) == 'en':
            st.warning("⚠️ This is English. Please enter Nepali news.")
        else:
            prediction=model.predict([input_text])[0]
            st.success(f'Predicted Category is **{prediction}**')