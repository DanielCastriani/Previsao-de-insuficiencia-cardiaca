from sqlalchemy import create_engine

DB_PATH = 'data/db.sqlite'
CONNECTION_STRING = f"sqlite:///{DB_PATH}"

DB_ENGINE = create_engine(CONNECTION_STRING)
