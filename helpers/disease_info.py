import streamlit as st
import pandas as pd

def get_disease_info(dis, description, precautions, medications, diets, workout):
    try:
        desc = description[description['Disease'] == dis]['Description']
        desc = " ".join(str(x) for x in desc.values) if not desc.empty else "No description available."

        pre = []
        if not precautions.empty:
            pre_df = precautions[precautions['Disease'] == dis]
            if not pre_df.empty:
                pre = pre_df[['Precaution_1', 'Precaution_2', 'Precaution_3', 'Precaution_4']].values.flatten().tolist()
                pre = [p for p in pre if pd.notna(p) and p.strip()]

        med = medications[medications['Disease'] == dis]['Medication'].tolist() if not medications.empty else []
        die = diets[diets['Disease'] == dis]['Diet'].tolist() if not diets.empty else []
        wrkout = workout[workout['disease'] == dis]['workout'].tolist() if not workout.empty else []

        return desc, pre, med, die, wrkout

    except Exception as e:
        st.error(f"Error getting disease info: {e}")
        return "Error loading information.", [], [], [], []
