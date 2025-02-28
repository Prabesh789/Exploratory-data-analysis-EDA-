import subprocess
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def run_script(script_path):
    """Runs a Python script given its path."""
    abs_path = os.path.join(BASE_DIR, script_path)
    print(f"Running {script_path}...")
    result = subprocess.run(["python", abs_path], capture_output=True, text=True)
    
    if result.returncode == 0:
        print(f"{script_path} completed successfully!\n")
    else:
        print(f"Error in {script_path}:\n{result.stderr}\n")
        exit(1)  # Stop execution if a script fails

if __name__ == "__main__":
    print("Starting the EDA Pipeline...\n")

    # Step 1: Extract Data
    run_script("main.py")

    # Step 2: Transform Data
    run_script("src/data_processing/data_transformation.py")

    # Step 3: Run EDA Notebook
    print("Running EDA Notebook...")
    EDA_NOTEBOOK_PATH = "data_insights\src\EDA.ipynb"
    
    if os.path.exists(EDA_NOTEBOOK_PATH):
        result = subprocess.run(["jupyter", "nbconvert", "--to", "notebook", "--execute", "--inplace", EDA_NOTEBOOK_PATH], capture_output=True, text=True)

        if result.returncode == 0:
            print("✅ EDA Notebook executed successfully!\n")
        else:
            print(f"❌ Error executing EDA Notebook:\n{result.stderr}\n")
            exit(1)
    else:
        print(f"❌ ERROR: Notebook not found at {EDA_NOTEBOOK_PATH}. Check the path!")
        exit(1)

    print("🎉 EDA Pipeline Execution Completed!")
