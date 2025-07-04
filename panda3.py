import pandas as pd
import os


root_dir = "/mnt/f/python_programming"                     # Directory from where we access the files
data_dir = os.path.join(root_dir,"data")                
dataset_path = os.path.join(data_dir,"health_monitor_data.csv")
print(dataset_path)

# Load Data

Health_monitor_Data = pd.read_csv(dataset_path)
print(Health_monitor_Data.head())

### Data cleaning

print(Health_monitor_Data.info())              # Output the data details

# Handle missing values

mask = Health_monitor_Data.isnull()            # checking if any value is missing
print(mask)

mask2 = Health_monitor_Data.isnull().any(axis=1)     # checking the row where the value is missing
print(mask2)

print(Health_monitor_Data[mask2])                 # accessing  missing values 

# Approach 2 (Imputation)

avg_val = Health_monitor_Data['Calories'].mean()

Health_monitor_Data['Calories'] = Health_monitor_Data['Calories'].fillna(           # fill null values with
    value = avg_val                                                           #   average value 
)

print(Health_monitor_Data.head(30))

# Approach 1 (drop)

Health_monitor_Data = Health_monitor_Data.dropna()          # drop null values
print(Health_monitor_Data.isnull().sum())          # Returns total null values sum in a row 

# Remove duplicates

mask3 = Health_monitor_Data.duplicated()       # Returns duplicates True  

print(mask3)                                     

print(Health_monitor_Data[mask3])               # return the duplicated row

Health_monitor_Data = Health_monitor_Data.drop_duplicates()

print(Health_monitor_Data.duplicated().sum())   # Return the total duplicate sum 


print(Health_monitor_Data.info())

# convert data types

Health_monitor_Data['Date'] = Health_monitor_Data['Date'].astype('datetime64[ns]')           # convert data type
print(Health_monitor_Data.info())


