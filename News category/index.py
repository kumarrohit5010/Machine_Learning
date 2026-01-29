import streamlit as st 
import joblib

# Page configuration
st.set_page_config(
    page_title="News Category Predictor",
    page_icon="📰",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS styling
st.markdown("""
    <style>
        /* Main container styling */
        .main {
            padding: 2rem;
        }
        
        /* Title styling */
        h1 {
            color: #1f77b4;
            text-align: center;
            font-size: 2.5em;
            margin-bottom: 1rem;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
        }
        
        /* Subtitle styling */
        .subtitle {
            text-align: center;
            color: #555;
            font-size: 1.1em;
            margin-bottom: 2rem;
        }
        
        /* Text area styling */
        textarea {
            border-radius: 10px;
            border: 2px solid #1f77b4;
        }
        
        /* Button styling */
        .stButton > button {
            background: linear-gradient(90deg, #1f77b4 0%, #0d5a99 100%);
            color: white;
            font-weight: bold;
            font-size: 1.1em;
            border-radius: 8px;
            padding: 12px 40px;
            border: none;
            transition: all 0.3s ease;
            width: 100%;
            height: 50px;
        }
        
        .stButton > button:hover {
            transform: translateY(-2px);
            box-shadow: 0 8px 16px rgba(31, 119, 180, 0.3);
        }
        
        /* Success message styling */
        .stSuccess {
            border-radius: 10px;
            padding: 1.5rem;
        }
    </style>
""", unsafe_allow_html=True)

# Load model
model = joblib.load('model.joblib')

# Header section
st.markdown("<h1>📰 News Category Prediction</h1>", unsafe_allow_html=True)
st.markdown("<p class='subtitle'>Predict the category of your news article using AI</p>", unsafe_allow_html=True)

# Divider
st.divider()

# Input section with columns for better layout
col1, col2 = st.columns([3, 1], gap="medium")

with col1:
    st.markdown("### ✍️ Enter News Article")
    input_text = st.text_area(
        label="Paste your news article text here",
        max_chars=1000,
        height=300,
        placeholder="Enter the news article you want to categorize..."
    )

with col2:
    st.markdown("### 📋 Guidelines")
    st.info("""
    • Keep text under 1000 characters
    • Include the full article
    • Use clear language
    """)

st.divider()

# Prediction button
if st.button("🔍 Predict Category", use_container_width=True):
    if input_text.strip():
        with st.spinner("Analyzing article..."):
            prediction = model.predict([input_text])[0]
        st.success(f"✅ **Predicted Category:** `{prediction}`", icon="✅")
    else:
        st.warning("⚠️ Please enter some text before predicting!", icon="⚠️")
