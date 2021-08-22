import os

import pandas as pd
from configs import DB_ENGINE, DB_PATH


def import_data():
    if not os.path.exists(DB_PATH):
        df = pd.read_csv('data/heart_failure_clinical_records_dataset.csv')
        df.to_sql('heart_failure', DB_ENGINE)
        
        