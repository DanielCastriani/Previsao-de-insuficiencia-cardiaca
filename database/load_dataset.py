

from database.import_data import import_data
from utils.db_utils import select_from_sql


def load_dataset():
    import_data()
    
    df = select_from_sql('database/sql/dataset.sql')