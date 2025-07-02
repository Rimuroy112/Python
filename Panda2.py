import pandas as pd

# data.to_csv(                                 # convert data to csv file
#     path_or_buf="/mnt/f/python_programming/data.csv",
#     index = False
# )

df = pd.read_csv("/mnt/f/python_programming/data.csv")
print(df.head())

# sorting

sorted_df1 = df.sort_values(
    by = ['X']
)
print(sorted_df1.head())
sorted_df2 = df.sort_values(
    by = ['X'],
    ascending=[False]
)
print(sorted_df2.head())

sorted_df3 = df.sort_values(
    by = ['Height(feet)','Weight(KG)'],
)
print(sorted_df3.head())