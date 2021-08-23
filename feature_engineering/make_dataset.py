
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from utils.file_utils import create_path_if_not_exists, save_model


def make_feature_engineering(heart_failure: pd.DataFrame):
    path = create_path_if_not_exists('bin/', file_name='scaler.pickle')

    scaler = MinMaxScaler()

    numerical_col = [
        'age',
        'creatinine_phosphokinase',
        'ejection_fraction',
        'platelets',
        'serum_creatinine',
        'serum_sodium',
        'time',
    ]

    heart_failure[numerical_col] = scaler.fit_transform(heart_failure[numerical_col])

    save_model(scaler, path)

    return heart_failure
