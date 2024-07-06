import pandas as pd
import matplotlib.pyplot as plt
import xlrd

file_path_1 = '/Users/shivamkumar/Downloads/2016-Ethical-Hacking-with-Sources-and-Count_data.xlsx'
file_path_2 = '/Users/shivamkumar/Downloads/ethical_hacking 2/data/ethical_hackers.csv'
file_path_3 = '/Users/shivamkumar/Downloads/ethical_hacking 2/data/IIB Data Breaches - LATEST.xlsx'


ethical_hacking_df = pd.read_excel(file_path_1, sheet_name='Worksheet')
ethical_hackers_data = pd.read_csv(file_path_2)
data_breaches_data = pd.read_excel(file_path_3, sheet_name='breaches')

ethical_hacking_df.columns = ['Encoded', 'Longitude', 'Count', 'Location', 'Sources']

for column in ['Longitude', 'Count', 'Location', 'Sources']:
    ethical_hacking_df[column] = ethical_hacking_df[column].str.replace('_x0000_', '', regex=False)

ethical_hacking_df['Count'] = pd.to_numeric(ethical_hacking_df['Count'], errors='coerce')
ethical_hacking_df_cleaned = ethical_hacking_df.dropna(subset=['Count'])


ethical_hackers_data['country'] = ethical_hackers_data['country'].replace({
    'USA': 'United States',
    'U.S.A.': 'United States'
})

ethical_hackers_data['gender'] = ethical_hackers_data['gender'].astype('category')
ethical_hackers_data['country'] = ethical_hackers_data['country'].astype('category')

breach_date_column = 'date' 
data_breaches_data[breach_date_column] = pd.to_datetime(data_breaches_data[breach_date_column], errors='coerce')
data_breaches_data_cleaned = data_breaches_data.dropna(subset=[breach_date_column])


plt.figure(figsize=(12, 6))
ethical_hacking_df_cleaned['Location'].value_counts().head(10).plot(kind='bar')
plt.title('Top 10 Locations with Most Ethical Hacking Incidents')
plt.xlabel('Location')
plt.ylabel('Number of Incidents')
plt.xticks(rotation=45)
plt.show()


plt.figure(figsize=(12, 6))
ethical_hackers_data['company worked/working'].value_counts().head(10).plot(kind='bar')
plt.title('Top 10 Companies with Most Ethical Hackers')
plt.xlabel('Company')
plt.ylabel('Number of Ethical Hackers')
plt.xticks(rotation=45)
plt.show()


plt.figure(figsize=(12, 6))
data_breaches_data_cleaned[breach_date_column].dt.year.value_counts().sort_index().plot(kind='line')
plt.title('Trend of Data Breaches Over Time')
plt.xlabel('Year')
plt.ylabel('Number of Breaches')
plt.xticks(rotation=45)
plt.show()


plt.figure(figsize=(12, 6))
data_breaches_data_cleaned['sector'].value_counts().head(10).plot(kind='bar')
plt.title('Top 10 Sectors with Most Data Breaches')
plt.xlabel('Sector')
plt.ylabel('Number of Data Breaches')
plt.xticks(rotation=45)
plt.show()
