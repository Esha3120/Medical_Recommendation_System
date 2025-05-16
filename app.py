
import streamlit as st
from helpers.model_loader import load_model_and_data
from helpers.predictor import predict_disease
from helpers.disease_info import get_disease_info

# Load custom CSS
with open("assets/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Load model and data
try:
    rf, diseases_list, symptoms_dict, precautions, workout, description, medications, diets = load_model_and_data("data")
except Exception as e:
    st.error(f"Error loading model or data: {e}")
    st.stop()

st.markdown('<div class="title">🏥 Medical Disease Prediction System</div>', unsafe_allow_html=True)

with st.sidebar:
    st.header("📝 Instructions")
    st.write(
        '''
        - Select all symptoms you are currently experiencing.
        - Click the **Predict Disease** button.
        - View detailed info about your predicted condition.
        '''
    )
    st.info("Powered by a Random Forest model trained on medical data.")

st.subheader("Select Your Symptoms")
selected_symptoms = st.multiselect(
    "Choose symptoms (start typing to search):",
    options=list(symptoms_dict.keys()),
    help="Select all symptoms that apply to you"
)

if st.button("Predict Disease", type="primary"):
    if not selected_symptoms:
        st.warning("Please select at least one symptom.")
    else:
        with st.spinner("Analyzing symptoms and predicting disease..."):
            predicted_disease = predict_disease(symptoms_dict, rf, selected_symptoms)

        if predicted_disease is None:
            st.error("Could not predict the disease. Try again.")
        else:
            desc, pre, med, die, wrkout = get_disease_info(predicted_disease, description, precautions, medications, diets, workout)

            st.markdown(f'''
                <div class="result-card">
                <h2 style="color:#1B4F72;">🔎 Predicted Condition: <strong>{predicted_disease}</strong></h2>
                </div>
            ''', unsafe_allow_html=True)

            st.markdown('<h3 class="section-header">📝 Description</h3>', unsafe_allow_html=True)
            st.markdown(f'<div class="description-box">{desc}</div>', unsafe_allow_html=True)
            st.markdown("<hr>", unsafe_allow_html=True)

            if pre:
                st.markdown('<h3 class="section-header">🛡️ Recommended Precautions</h3>', unsafe_allow_html=True)
                cols = st.columns(2)
                for i, p in enumerate(pre):
                    col = cols[i % 2]
                    col.write(f"🛡️ **{i+1}.** {p}")
                st.markdown("<hr>", unsafe_allow_html=True)

            if med:
                st.markdown('<h3 class="section-header">💊 Suggested Medications</h3>', unsafe_allow_html=True)
                for i, m in enumerate(med, 1):
                    st.write(f"💊 **{i}.** {m}")
                st.markdown("<hr>", unsafe_allow_html=True)

            if wrkout:
                st.markdown('<h3 class="section-header">🏋️ Recommended Exercises</h3>', unsafe_allow_html=True)
                for i, w in enumerate(wrkout, 1):
                    st.write(f"🏋️ **{i}.** {w}")
                st.markdown("<hr>", unsafe_allow_html=True)

            if die:
                st.markdown('<h3 class="section-header">🍎 Dietary Recommendations</h3>', unsafe_allow_html=True)
                for i, d in enumerate(die, 1):
                    st.write(f"🍎 **{i}.** {d}")

st.markdown('<div class="footer-text">Made by Esha Bodhani - Medical AI Assistant</div>', unsafe_allow_html=True)
