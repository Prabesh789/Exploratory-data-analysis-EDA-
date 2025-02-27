import pandas as pd
from .base_loader import DatasetLoader

class JSONDataLoader(DatasetLoader):
    def __init__(self, file_path):
        self.file_path = file_path

    def load_data(self):
        return pd.read_json(self.file_path)