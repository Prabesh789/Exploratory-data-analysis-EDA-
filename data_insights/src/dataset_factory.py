from .loaders.csv_loader import CSVLoader
from .loaders.json_loader import JSONDataLoader
from .loaders.sql_loader import SQLLoader

class DatasetFactory:
    @staticmethod
    def get_dataset_loader(source_type, **kwargs):
        if source_type == "csv":
            return CSVLoader(kwargs.get("file_path"))
        elif source_type == "json":
            return JSONDataLoader(kwargs.get("file_path"))
        elif source_type == "sql":
            return SQLLoader(kwargs.get("db_path"), kwargs.get("query"))
        else:
            raise ValueError(f"Unknown source type: {source_type}")
