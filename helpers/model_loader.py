import pickle
import pandas as pd
import os

def load_model_and_data(base_path):
    with open(os.path.join(base_path, 'rf_model (1).pkl'), 'rb') as f:
        rf = pickle.load(f)

    if not hasattr(rf, "classes_"):
        raise ValueError("Model missing 'classes_' attribute.")

    diseases_list = {i: disease for i, disease in enumerate(rf.classes_)}
    sym_des = pd.read_csv(os.path.join(base_path, 'Symptom-severity (1).csv'))
    precautions = pd.read_csv(os.path.join(base_path, 'precautions_df (1).csv'))
    workout = pd.read_csv(os.path.join(base_path, 'workout_df (1).csv'))
    description = pd.read_csv(os.path.join(base_path, 'description (1).csv'))
    medications = pd.read_csv(os.path.join(base_path, 'medications (1).csv'))
    diets = pd.read_csv(os.path.join(base_path, 'diets (2).csv'))

    for df in [sym_des, precautions, workout, description, medications, diets]:
        df.columns = df.columns.str.strip()

    symptoms_dict = {symptom: idx for idx, symptom in enumerate(sym_des['Symptom'])}

    return rf, diseases_list, symptoms_dict, precautions, workout, description, medications, diets
