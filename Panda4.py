# Exploratory Data Analysis

import pandas as pd

H_M_D = pd.read_csv("/mnt/f/python_programming/data/health_monitor_data.csv")

print(H_M_D.describe())

# plot = H_M_D.plot(
#     kind = 'line',
#     x = 'Pulse'
# )
# print(plot)

# Remove outliers

Q1 = H_M_D['Pulse'].quantile(0.25)
print(Q1)

Q3 = H_M_D['Pulse'].quantile(0.75)
print(Q3)

IQR = Q3-Q1                     # InterQuartile range
L = Q1-1.5*IQR                  
R = Q3+1.5*IQR
print(L,R)

non_outlier_mask = H_M_D['Pulse'].between(L,R)       # Output True of values in the range
outlier_mask = ~non_outlier_mask

print(non_outlier_mask)          # non outlier mask

print(outlier_mask)     # outlier mask 
print(H_M_D[outlier_mask])           # output the rows of outlier

H_M_D = H_M_D[non_outlier_mask]       # remove the outliers

### Data transformation

# Data normalization

def normalize(col):
    mean = col.mean()
    std = col.std()
    normal_col2 = (col-mean)/std
    return normal_col2

H_M_D['Pulse'] = H_M_D['Pulse'].agg(normalize)
H_M_D['Maxpulse'] = H_M_D['Maxpulse'].agg(normalize)
H_M_D['Duration'] = H_M_D['Duration'].agg(normalize)
H_M_D['Calories'] = H_M_D['Calories'].agg(normalize)

print(H_M_D.head())

# Encoding categorical data

print(H_M_D['Type'].value_counts())

# one hot encoding

H_M_D_O_H_E = pd.get_dummies(              # Apply one hot encoding
    H_M_D,
    columns=["Type"],
    sparse= True
)

print(H_M_D_O_H_E.head())

# Label encoding

H_M_D['Label_encoded_type'] = pd.Categorical(
      H_M_D['Type'],
      categories = ['Easy','Moderate','Heavy'],
      ordered = True
).codes

print(H_M_D.head())



