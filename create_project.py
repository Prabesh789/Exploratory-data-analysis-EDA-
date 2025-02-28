import os

# Project name
project_name = input("Enter your project name: ")

# Project structure
folders = [
    f"{project_name}/src",
    f"{project_name}/src/analysis",
    f"{project_name}/src/data_processing",
    f"{project_name}/src/loaders",
    f"{project_name}/src/utils",
    f"{project_name}/tests",
]

files = [
    f"{project_name}/README.md",
    f"{project_name}/requirements.txt",
    f"{project_name}/main.py",

    # Source EDA
    f"{project_name}/src/EDA.ipynb",

    # Source - Analysis
    f"{project_name}/src/analysis/__init__.py",
    f"{project_name}/src/analysis/basic_data_inspection.py",
    f"{project_name}/src/analysis/missing_values_analysis.py",
    f"{project_name}/src/analysis/univariate_analysis.py",
    f"{project_name}/src/analysis/bivariate_analysis.py",
    f"{project_name}/src/analysis/multivariate_analysis.py",

    # Source - Data Processing
    f"{project_name}/src/data_processing/__init__.py",
    f"{project_name}/src/data_processing/data_transformation.py",
    f"{project_name}/src/data_processing/dataset_factory.py",


    # Source - Loaders
    f"{project_name}/src/loaders/__init__.py",
    f"{project_name}/src/loaders/base_loader.py",
    f"{project_name}/src/loaders/csv_loader.py",
    f"{project_name}/src/loaders/json_loader.py",
    f"{project_name}/src/loaders/sql_loader.py",

    # Source - Utils
    f"{project_name}/src/utils/logger.py",
     f"{project_name}/src/utils/preprocessing.py",

    # Tests
    f"{project_name}/tests/test_csv_loader.py",
    f"{project_name}/tests/test_json_loader.py",
    f"{project_name}/tests/test_sql_loader.py"
]

# Create directories
for folder in folders:
    os.makedirs(folder, exist_ok=True)

# Create empty files
for file in files:
    if not os.path.exists(file):
        with open(file, 'w') as f:
            pass

print(f"Project '{project_name}' structure created successfully!")
