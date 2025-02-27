import os
import zipfile
from src.dataset_factory import DatasetFactory

DATA_FOLDER = "data_insights/data"
EXTRACTED_FOLDER = "extracted_data"  # Define extraction folder dynamically

def extract_zip(zip_path):
    """Extract ZIP file into 'extracted_data/' and return extracted file paths."""
    if not os.path.exists(EXTRACTED_FOLDER):  
        os.makedirs(EXTRACTED_FOLDER)  # Create folder if it doesn't exist

    with zipfile.ZipFile(zip_path, "r") as zip_ref:
        zip_ref.extractall(EXTRACTED_FOLDER)
        return [os.path.join(EXTRACTED_FOLDER, f) for f in zip_ref.namelist()]


def detect_and_load_files(folder = DATA_FOLDER):
    """Detect and load different file types from a given folder."""
    for file_name in os.listdir(folder):
        file_path = os.path.join(folder, file_name)
        
        if file_name.endswith(".csv"):
            print(f"Loading CSV: {file_name}")
            loader = DatasetFactory.get_dataset_loader("csv", file_path=file_path)
            data = loader.load_data()
            print(data.head())

        elif file_name.endswith(".json"):
            print(f"Loading JSON: {file_name}")
            loader = DatasetFactory.get_dataset_loader("json", file_path=file_path)
            data = loader.load_data()
            print(data)

        elif file_name.endswith(".db"):  
            print(f"Loading SQL Database: {file_name}")
            loader = DatasetFactory.get_dataset_loader("sql", db_path=file_path, query="SELECT * FROM users")
            data = loader.load_data()
            print(data)

        elif file_name.endswith(".zip"):
            print(f"Extracting ZIP: {file_name}")
            extracted_files = extract_zip(file_path)
            print(f"Extracted to: {EXTRACTED_FOLDER}")
            
            # Process extracted files
            detect_and_load_files(EXTRACTED_FOLDER)  
        else:
            print(f"Unsupported file format: {file_name}")

def main():
    detect_and_load_files()

if __name__ == "__main__":
    main()
