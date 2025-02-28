import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def missing_values_analysis(df):
    """Identifies and visualizes missing data patterns."""
    print("\nMissing Values Count:")
    print(df.isnull().sum())
    
    plt.figure(figsize=(8, 5))
    sns.heatmap(df.isnull(), cbar=False, cmap="viridis")  
    plt.title("Missing Values Bar Chart")
    plt.show()

if __name__ == "__main__":
    FILE_PATH = r"E:\Python Repo\EDA\data_insights\data\transformed\transformed_data.csv"
    df = pd.read_csv(FILE_PATH)
    missing_values_analysis(df)
