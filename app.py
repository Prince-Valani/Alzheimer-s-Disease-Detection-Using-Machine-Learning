import streamlit as st
import pickle
import numpy as np

# Load your models
model = pickle.load(open('selected_cols.pkl', 'rb'))
pipe = pickle.load(open('pipe.pkl', 'rb'))

# Load CSS file
with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Title and Input Fields
st.title("Alzheimer's Disease Detection")
BMI = st.number_input('Enter your BMI')
SleepQuality = st.number_input('Enter your Sleep Quality')
SystolicBP = st.number_input('Enter your Systolic BP')
CholestrolLDL = st.number_input('Enter your Cholesterol LDL')
CholestrolHDL = st.number_input('Enter your Cholesterol HDL')
CholestrolTriglycerides = st.number_input('Enter your Cholesterol Triglycerides')
MMSE = st.number_input('Enter your MMSE')
FunctionalAssessment = st.number_input('Enter your Functional Assessment')
ADL = st.number_input('Enter your  Activities of Daily Living score')
BehavioralProblems = st.selectbox('Enter Behavioral Problems', model['BehavioralProblems'].unique())
MemoryComplaints = st.selectbox('Enter Memory Complaints', model['MemoryComplaints'].unique())

# Detection button and prediction
if st.button('Detect'):
    query = np.array([BMI, SleepQuality, SystolicBP, CholestrolLDL, CholestrolHDL, CholestrolTriglycerides,
                      MMSE, FunctionalAssessment, ADL, BehavioralProblems, MemoryComplaints])
    query_reshaped = query.reshape(1, -1)
    prediction = pipe.predict(query_reshaped)

    # Display prediction result
    if prediction == 0:
        st.markdown('<div class="prediction-result">Congratulations, you do not have Alzheimer\'s Disease</div>', unsafe_allow_html=True)
    else:
        st.markdown('<div class="prediction-result">You have been diagnosed with Alzheimer\'s Disease</div>', unsafe_allow_html=True)