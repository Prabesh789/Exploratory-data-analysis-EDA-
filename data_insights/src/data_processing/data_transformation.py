import os
import pandas as pd

def transform_data(file_path):
    """Transforms the dataset from wide format to long format and cleans numeric values."""
    
    # Load the dataset
    df = pd.read_csv(file_path)
    
    # Strip spaces from column names and categorical values
    df.columns = df.columns.str.strip()
    df["Geography"] = df["Geography"].str.strip()
    df["Characteristics"] = df["Characteristics"].str.strip()
    
    # Convert from wide to long format
    df_long = df.melt(id_vars=["Geography", "Characteristics"], 
                      var_name="Year", 
                      value_name="Value")

    # Convert "Year" column to integer
    df_long["Year"] = pd.to_numeric(df_long["Year"], errors="coerce")

    # Ensure "Value" column is handled correctly (convert to string before applying string functions)
    df_long["Value"] = df_long["Value"].astype(str).replace("..", pd.NA)
    df_long["Value"] = df_long["Value"].str.replace(",", "", regex=True).astype("float")

    # Define "Region Type" (Country vs. Province/Territory)
    provinces = {
        "Newfoundland and Labrador", "Prince Edward Island", "Nova Scotia", 
        "New Brunswick", "Quebec", "Ontario", "Manitoba", "Saskatchewan", 
        "Alberta", "British Columbia", "Yukon", "Northwest Territories", "Nunavut"
    }
    
    df_long["Region Type"] = df_long["Geography"].apply(lambda x: "Country" if x == "Canada" else (
        "Province/Territory" if x in provinces else "Other"))

    return df_long


FILE_PATH = r"E:\Python Repo\EDA\data_insights\data\extracted\Number and rates of new cases of primary cancer.csv"
df_transformed = transform_data(FILE_PATH)

# Define extraction folder dynamically
transformed_data_path = r"E:\Python Repo\EDA\data_insights\data\transformed\transformed_data.csv"

# Ensure directory exists before saving
os.makedirs(os.path.dirname(transformed_data_path), exist_ok=True)
df_transformed.to_csv(transformed_data_path, index=False)

print(f"Data transformation complete! Saved at: {transformed_data_path}")
