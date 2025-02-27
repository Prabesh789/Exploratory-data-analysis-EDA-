import pandas as pd
import sqlite3
from .base_loader import DatasetLoader

class SQLLoader(DatasetLoader):
    def __init__(self, db_path, query):
        self.db_path = db_path
        self.query = query
    
    def load_data(self):
        conn = sqlite3.connect(self.db_path)
        df = pd.read_sql_query(self.query, conn)
        conn.close()
        return df
        