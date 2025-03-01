import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def bivariate_analysis(df):
    """Performs bivariate analysis using scatter plots and regional cancer growth trends."""
    
    # Ensure correct formatting of categorical columns
    df["Geography"] = df["Geography"].str.strip()
    df["Characteristics"] = df["Characteristics"].str.strip()
    
    # Convert "Year" to numeric (Fix for invalid literal error)
    df["Year"] = pd.to_numeric(df["Year"], errors="coerce")

    # **1️⃣ Cancer Cases vs. Incidence Rate**
    analyze_cancer_cases_vs_incidence(df)
    
    # **2️⃣ Regional Cancer Growth Over Time (Multi-Line Plot)**
    analyze_regional_growth(df)


def analyze_cancer_cases_vs_incidence(df):
    """Plots the relationship between cancer cases and incidence rates in Canada."""
    
    # Filter data for Canada only
    df_canada = df[df["Geography"] == "Canada"]
    
    # Pivot data to get side-by-side comparisons
    df_pivot = df_canada.pivot_table(index="Year", 
                                     columns="Characteristics", 
                                     values="Value").reset_index()

    # Ensure columns exist
    if "Number of new cancer cases" not in df_pivot.columns or "Cancer incidence rate" not in df_pivot.columns:
        print("Error: Required data columns are missing.")
        return
    
    # Scatter Plot
    plt.figure(figsize=(8, 6))
    sns.scatterplot(x=df_pivot["Number of new cancer cases"], y=df_pivot["Cancer incidence rate"])
    plt.xlabel("Number of New Cancer Cases")
    plt.ylabel("Cancer Incidence Rate")
    plt.title("Cancer Cases vs. Incidence Rate (Canada)")
    plt.grid(True)
    plt.show()

    # Correlation Calculation
    correlation = df_pivot["Number of new cancer cases"].corr(df_pivot["Cancer incidence rate"])
    print(f"Correlation between Cancer Cases and Incidence Rate: {correlation}")


def analyze_regional_growth(df):
    """Compares regional cancer case trends over time using a multi-line plot for the top 5 provinces."""
    
    # Filter only "Number of new cancer cases" and exclude Canada
    df_provinces = df[(df["Characteristics"] == "Number of new cancer cases") & (df["Region Type"] == "Province/Territory")]
    
    # Identify the top 5 provinces/territories with the highest total cancer cases
    top_5_provinces = df_provinces.groupby("Geography")["Value"].sum().nlargest(5).index.tolist()

    # Filter data to only include the top 5 provinces
    df_top_5 = df_provinces[df_provinces["Geography"].isin(top_5_provinces)]

    # Pivot data for easier visualization
    df_pivot = df_top_5.pivot(index="Year", columns="Geography", values="Value")

    # Plot regional trends (Multi-Line for Top 5 Provinces)
    plt.figure(figsize=(14, 7))
    for column in df_pivot.columns:
        plt.plot(df_pivot.index, df_pivot[column], label=column, marker='o')

    plt.xlabel("Year")
    plt.ylabel("Number of New Cancer Cases")
    plt.title("Top 5 Provinces with Highest Cancer Cases (1992-2022)")
    plt.legend(title="Province/Territory", bbox_to_anchor=(1.05, 1), loc="upper left", fontsize=8)
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    FILE_PATH = r"E:\Python Repo\EDA\data_insights\data\transformed\transformed_data.csv"
    
    # Ensure "Year" is read as an integer
    df = pd.read_csv(FILE_PATH, dtype={"Year": str})
    
    # # Convert "Year" to numeric, fixing the invalid literal error
    # df["Year"] = pd.to_numeric(df["Year"], errors="coerce")
    bivariate_analysis(df)
