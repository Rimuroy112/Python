import pandas as pd
import numpy as np

# data.to_csv(                                 # convert data to csv file
#     path_or_buf="/mnt/f/python_programming/data.csv",
#     index = False
# )

df = pd.read_csv("/mnt/f/python_programming/data.csv")
print(df.head())

# sorting

sorted_df1 = df.sort_values(               # Sorted ascending order
    by = ['X']
)
print(sorted_df1.head())

sorted_df2 = df.sort_values(              # Sorted descending order
    by = ['X'],
    ascending=[False]
)
print(sorted_df2.head())


sorted_df3 = df.sort_values(
    by = ['Height(feet)', 'Weight(KG)'],
    ascending = [False, True]
)
print(sorted_df3.head())

bmi = df['BMI']                       # Access column values
print(bmi)

bmi_np = np.array(df['BMI'])           # convert pandas to numpy
print(type(bmi_np))

bmi = df[df['BMI'] > 6]                # BMI values greater than six
print(bmi)

mask = df[(df['BMI']> 5) & (df['Y'] > 6)]            # filtering
print(mask)

df['new'] = df['X']+df['Y']              # Adding a new column

print(df.head())

new_df = df.query(                     # Mask using query method
    "BMI > 6 & Y > 7"
)

print(new_df.head())

print(df.columns)             # Drops  a column

new_df2 = df.drop(
    columns = ['new']
)

print(new_df2.head())

print(new_df2['X'].mean())       # average of a column
print(new_df2['X'].sum())       # average of a column
print(new_df2['X'].min())       # average of a column
print(new_df2['X'].max())       # average of a column

print(new_df2[['X','Y']].mean())       # average of a column

def normal(col):
    mean = col.mean()
    std = col.std()
    normal_col = (col-mean)/std
    return normal_col
def normal2(col):
    min = col.min()
    max = col.max()
    normal_col2 = (col-min)/max-min
    return normal_col2
normal_df = df[['X','Y']].agg(            # Apply custom method
   [normal,normal2]
)
print(normal_df.head())

category = df.value_counts(              # output categorical values
    ['BMI','X']
)
print(category)