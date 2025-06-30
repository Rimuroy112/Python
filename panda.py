import pandas as pd

health_data_table = {                      # Dictionary
    "height" : [5,6,7,5,4,7,8],
    "weight"  : [50,60,70,80,30,60,40],
    "bmi" : [3,4,5,6,7,8,9],
    "x" : [3,4,5,6,6,7,9],
    "y" : [3,4,5,6,4,7,8],
    "z" : [3,4,5,6,8,9,7],
} 

data = pd.DataFrame(                       # Dictionary to panda DataFrame pip3 install pandas
    health_data_table
)

print(type(data))

print(data.head())             # Output first 5 rows

print(data.tail())             # Output last 5 rows

print(data.head(3))             # Output first 3 rows

print(data.tail(3))             # Output last 3 rows

print(data.shape)               # output shape

print(data.info())              # output details

print(data.describe())         # more details

print(data.values)               # output only values

print(type(data.values))          # type of values

print(data.columns)               # output the column names

data.columns = [                  # Edit columns
    "Height(feet)","Weight(KG)","BMI","X","Y","Z"
]

print(data.head())

data.to_csv(                                 # convert data to csv file
    path_or_buf="/mnt/f/python_programming/data.csv",
    index = False
)

df = pd.read_csv("/mnt/f/python_programming/data.csv")
print(df.head())