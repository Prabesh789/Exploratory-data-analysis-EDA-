import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def multivariate_analysis(df):
    analyze_cancer_growth_heatmap(df)


def analyze_cancer_growth_heatmap(df):
    """Generates a heatmap showing year-over-year cancer case growth per region."""
    
    # Ensure correct formatting
    df["Geography"] = df["Geography"].str.strip()
    df["Characteristics"] = df["Characteristics"].str.strip()
    
    # Convert "Year" to numeric
    df["Year"] = pd.to_numeric(df["Year"], errors="coerce")

    # Filter only "Number of new cancer cases" and exclude Canada
    df_cases = df[(df["Characteristics"] == "Number of new cancer cases") & (df["Geography"] != "Canada")]

    # Pivot data to get Year-Region matrix
    df_pivot = df_cases.pivot(index="Year", columns="Geography", values="Value")

    # Compute year-over-year growth rates (percentage change) without forward-filling
    df_growth = df_pivot.pct_change(fill_method=None).multiply(100)  # Convert to percentage

    # Handle missing values (fill NaN with 0 or forward-fill)
    df_growth.fillna(0, inplace=True)  

    # Plot heatmap
    plt.figure(figsize=(12, 6))
    sns.heatmap(df_growth, cmap="coolwarm", annot=True, fmt=".1f", linewidths=0.5)

    plt.title("Year-over-Year Growth Rate of Cancer Cases by Region")
    plt.xlabel("Region")
    plt.ylabel("Year")
    plt.xticks(rotation=90)
    plt.show()

if __name__ == "__main__":
    FILE_PATH = r"E:\Python Repo\EDA\data_insights\data\transformed\transformed_data.csv"
    
    # Load dataset
    df = pd.read_csv(FILE_PATH)
    
    # Run the function
    multivariate_analysis(df)
