import streamlit as st
import joblib
import os
import numpy as np

# load model
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "knn_model.joblib")
model = joblib.load(MODEL_PATH)

# page config
st.set_page_config(page_title="Student Performance Predictor", page_icon="🎓")

st.title("🎓 Student Performance Predictor")
st.write("Enter student details to predict final performance grade.")

st.divider()

# input fields
StudyHours = st.slider(
    "📘 Study Hours (per day)",
    min_value=0.0, max_value=10.0, value=5.0, step=0.5
)

AttendancePercentage = st.slider(
    "📊 Attendance Percentage",
    min_value=0.0, max_value=100.0, value=75.0, step=1.0
)

PreviousGPA = st.slider(
    "🎯 Previous GPA",
    min_value=0.0, max_value=4.0, value=3.0, step=0.1
)

PracticeTestScore = st.slider(
    "📝 Practice Test Score",
    min_value=0.0, max_value=100.0, value=70.0, step=1.0
)

# prepare input
sample = np.array([[StudyHours, AttendancePercentage, PreviousGPA, PracticeTestScore]])

st.divider()

# prediction
if st.button("🔮 Predict Performance"):
    prediction = model.predict(sample)[0]

    if prediction == "A":
        st.success("🏆 Predicted Grade: A (Excellent Performance)")
    elif prediction == "B":
        st.info("👍 Predicted Grade: B (Good Performance)")
    elif prediction == "C":
        st.warning("⚠️ Predicted Grade: C (Average Performance)")
    else:
        st.error("❌ Predicted Grade: D (Needs Improvement)")




#https://stdntperformance.streamlit.app/