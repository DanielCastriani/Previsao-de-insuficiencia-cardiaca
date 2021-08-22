

from database.import_data import import_data
from utils.db_utils import select_from_sql


def load_dataset():
    import_data()

    heart_failure = select_from_sql('database/sql/dataset.sql')

    return heart_failure