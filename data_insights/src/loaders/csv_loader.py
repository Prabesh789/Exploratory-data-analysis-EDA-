import pandas as pd
from .base_loader import DatasetLoader

class CSVLoader(DatasetLoader):
    def __init__(self, file_path):
        self.file_path = file_path

    def load_data(self):
        # return super().load_data()
        return pd.read_csv(self.file_path)
