import pandas as pd
from datetime import datetime
import os

# Function to read the file, filter by date range, drop specific columns, and forward fill missing values
def process_data(file_path, start_date, end_date, columns_to_drop, save_path):
    # Read the dataset from the CSV file
    df = pd.read_csv(file_path)

    # Convert the 'Date' column to datetime format (day-month-year)
    df['Date'] = pd.to_datetime(df['Date'], format='%d-%m-%Y')

    # Filter rows based on the start_date and end_date
    start_date = pd.to_datetime(start_date, format='%Y-%m-%d')
    end_date = pd.to_datetime(end_date, format='%Y-%m-%d')

    # Filter the data by the specified date range
    filtered_df = df[(df['Date'] >= start_date) & (df['Date'] <= end_date)]

    # Drop specified columns
    filtered_df.drop(columns=columns_to_drop, inplace=True)


    # Format the 'Date' column to year-month-day format (YYYY-MM-DD)
    filtered_df['Date'] = filtered_df['Date'].dt.strftime('%Y-%m-%d')

    # Ensure directory exists
    os.makedirs(os.path.dirname(save_path), exist_ok=True)

    # Save the processed DataFrame to a CSV file
    filtered_df.to_csv(save_path, index=False)

    # Return the processed DataFrame
    return filtered_df


# Example usage
file_path = 'C:\\Users\\gjujj\\OneDrive\\Documents\\INRUSDX.csv'
start_date = '2014-01-01'
end_date = '2022-08-15'
columns_to_drop = []  # specify the columns to drop

# Set the save path for the processed file with name 'INR_to_USD.csv'
save_path = r'C:\Users\gjujj\OneDrive\Documents\DATASETS\INR_to_USD.csv'

# Call the function to process data and save it
INR_to_USD = process_data(file_path, start_date, end_date, columns_to_drop, save_path)

# Print the processed DataFrame
print(INR_to_USD)








