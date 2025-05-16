import numpy as np
import streamlit as st

def predict_disease(symptoms_dict, rf, patient_symptoms):
    try:
        input_vector = np.zeros(len(symptoms_dict))
        for item in patient_symptoms:
            if item in symptoms_dict:
                input_vector[symptoms_dict[item]] = 1
            else:
                st.warning(f"Symptom '{item}' not found in database")
        return rf.predict(input_vector.reshape(1, -1))[0]
    except Exception as e:
        st.error(f"Prediction failed: {e}")
        return None
