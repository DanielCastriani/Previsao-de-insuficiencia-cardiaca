from configs import DB_ENGINE
from typing import List
import pandas as pd


def select_df(query: str, params: List = []):
    return pd.read_sql(query, params=params, con=DB_ENGINE)


def select_from_sql(path: str, params: List = []):
    with open(path, 'r') as f:
        query = ''.join(f.readlines())

        return select_df(query, params=params)
