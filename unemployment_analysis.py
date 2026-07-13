import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

try:
    # Make sure your downloaded dataset is named 'unemployment_data.csv' in the same folder
    df = pd.read_csv('unemployment_data.csv')
    
    # Data Cleaning
    df.columns = df.columns.str.strip()
    df['Date'] = pd.to_datetime(df['Date'])
    
    print("Dataset Overview:")
    print(df.info())

    # Visualization: Unemployment Trend Over Time
    plt.figure(figsize=(12, 6))
    sns.lineplot(data=df, x='Date', y='Unemployment_Rate', errorbar=None, color='blue', linewidth=2)
    plt.title('Unemployment Rate Trends')
    plt.xlabel('Date')
    plt.ylabel('Unemployment Rate (%)')
    plt.grid(True)
    plt.show()

    # Yearly Distribution
    df['Year'] = df['Date'].dt.year
    plt.figure(figsize=(12, 6))
    sns.boxplot(data=df, x='Year', y='Unemployment_Rate')
    plt.title('Unemployment Rate Distribution by Year')
    plt.xticks(rotation=45)
    plt.show()

except FileNotFoundError:
    print("Error: Place 'unemployment_data.csv' in this folder before running the script.")