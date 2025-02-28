import pandas as pd

def basic_data_inspection(file_path):
    """Loads data and performs basic inspection."""
    df = pd.read_csv(file_path)

    print("\nBasic Information:")
    df.info()

    print("\nSummary Statistics:")
    print(df.describe(include='all'))
    

# While the Script Directly run The code inside __name__ == "__main__" will execute
if __name__ == "__main__":
    FILE_PATH = r"E:\Python Repo\EDA\data_insights\data\transformed\transformed_data.csv"
    basic_data_inspection(FILE_PATH)
