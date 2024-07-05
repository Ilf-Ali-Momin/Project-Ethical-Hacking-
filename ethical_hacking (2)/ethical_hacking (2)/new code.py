import pandas as pd

import matplotlib.pyplot as plt

# Load data
file_path_2 = r"C:\Users\MSI\Desktop\Babarson\ethical_hackers.csv"
file_path_3 = r"C:\Users\MSI\Desktop\Babarson\IIB Data Breaches - LATEST.xlsx"

ethical_hackers_data = pd.read_csv(file_path_2)
data_breaches_data = pd.read_excel(file_path_3, sheet_name='breaches', engine='openpyxl')
# Clean and preprocess data
def clean_data(df, column):
    df[column] = pd.to_numeric(df[column], errors='coerce')
    return df.dropna(subset=[column])

ethical_hackers_data['country'] = ethical_hackers_data['country'].replace({'USA': 'United States', 'U.S.A.': 'United States'})

breach_date_column = 'date'
data_breaches_data[breach_date_column] = pd.to_datetime(data_breaches_data[breach_date_column], errors='coerce')
data_breaches_data = clean_data(data_breaches_data, breach_date_column)

# Plot data
def plot_data(df, column, title, xlabel, ylabel):
    plt.figure(figsize=(12, 6))
    df[column].value_counts().head(10).plot(kind='bar')
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.xticks(rotation=45)
    plt.show()

plot_data(ethical_hackers_data, 'company worked/working', 'Top 10 Companies with Most Ethical Hackers', 'Company', 'Number of Ethical Hackers')
plot_data(data_breaches_data, 'sector', 'Top 10 Sectors with Most Data Breaches', 'Sector', 'Number of Data Breaches')