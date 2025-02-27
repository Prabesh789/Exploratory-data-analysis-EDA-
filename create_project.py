import os

# Project name
project_name = input("Enter your project name: ")

# Project structure
folders = [
    f"{project_name}/data",
    f"{project_name}/src/loaders",
    f"{project_name}/src/analysis_src",
    f"{project_name}/notebooks",
    f"{project_name}/tests",
    f"{project_name}/utils"
]

files = [
    f"{project_name}/README.md",
    f"{project_name}/requirements.txt",
    f"{project_name}/main.py",
    f"{project_name}/src/dataset_factory.py",
    # f"{project_name}/src/eda.py",
    f"{project_name}/notebooks/EDA.ipynb",
    f"{project_name}/src/loaders/__init__.py",
    f"{project_name}/src/loaders/base_loader.py",
    f"{project_name}/src/loaders/csv_loader.py",
    f"{project_name}/src/loaders/json_loader.py",
    f"{project_name}/src/loaders/sql_loader.py",
     f"{project_name}/src/analysis_src/basic_data_inspection.py",
    f"{project_name}/src/analysis_src/missing_values_analysis.py",
    f"{project_name}/src/analysis_src/univariate_analysis.py",
    f"{project_name}/src/analysis_src/bivariate_analysis.py",
    f"{project_name}/src/analysis_src/multivariate_analysis.py",
    f"{project_name}/tests/test_csv_loader.py",
    f"{project_name}/tests/test_json_loader.py",
    f"{project_name}/tests/test_sql_loader.py",
    f"{project_name}/utils/preprocessing.py",
    f"{project_name}/utils/logger.py"
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
