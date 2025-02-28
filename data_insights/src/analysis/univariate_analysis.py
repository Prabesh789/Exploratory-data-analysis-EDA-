import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def univariate_analysis(df):
    """Performs univariate analysis by plotting trends for Canada and all provinces."""
    
    # Ensure correct formatting
    df["Geography"] = df["Geography"].str.strip()
    df["Characteristics"] = df["Characteristics"].str.strip()
    
    # 1️. Trend Analysis for Canada
    plot_trend(df, geography="Canada", title="Trend of New Cancer Cases in Canada (1992-2022)")

    # 2️. Trend Analysis for All Provinces
    plot_province_trends(df)


def plot_trend(df, geography, title):
    """Plots the trend of cancer cases over time for a given region."""
    
    # Filter for the selected region and only "Number of new cancer cases"
    region_cases = df[
        (df["Geography"] == geography) & 
        (df["Characteristics"] == "Number of new cancer cases")
    ]
    
    # Ensure data is sorted by year
    region_cases = region_cases.sort_values(by="Year")

    # Plot trend
    plt.figure(figsize=(12, 6))
    plt.plot(region_cases["Year"], region_cases["Value"], marker='o', linestyle='-', color='b')
    plt.xlabel("Year")
    plt.ylabel("Number of New Cancer Cases")
    plt.title(title)
    plt.grid(True)
    plt.show()

def plot_province_trends(df):
    """Plots trends for all provinces."""
    
    # Filter only "Number of new cancer cases" and exclude Canada
    df_provinces = df[(df["Characteristics"] == "Number of new cancer cases") & (df["Region Type"] == "Province/Territory")]
    
    # Create a FacetGrid for different provinces
    g = sns.FacetGrid(df_provinces, col="Geography", col_wrap=4, height=3, sharey=False)
    g.map_dataframe(sns.lineplot, x="Year", y="Value", color="b")

    # Set titles and labels
    g.set_axis_labels("Year", "Number of Cancer Cases")
    g.set_titles("{col_name}")  # Keep province names
    plt.subplots_adjust(top=0.9, hspace=0.4)  # Adjust spacing
    g.fig.suptitle("Trend of New Cancer Cases Across Provinces (1992-2022)", fontsize=14)
    
    plt.show()

if __name__ == "__main__":
    FILE_PATH = r"E:\Python Repo\EDA\data_insights\data\transformed\transformed_data.csv"
    df = pd.read_csv(FILE_PATH)
    univariate_analysis(df)
