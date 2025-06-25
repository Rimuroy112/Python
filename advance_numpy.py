#multidimensional numpy arrays

import numpy as np
scalar = np.array(4)
vector = np.array([1,2,3,4.5])
matrix = np.array([[1,2,3],
                   [4,5,6]])

print('Scalar',scalar)
print('vector',vector)
print('matrix',matrix)

# indexing

my_array = np.array([2,3,4,5,6])
print(my_array[2])
print(my_array[-3])


my_array2 = np.array([[2,3,6,9],
                      [3,5,7,8],
                      [7,8,9,6]])
print(my_array2[1,1])
print(my_array2[-2,-2])

# slicing
print(my_array[0:len(my_array):2]) 
print(my_array[1:4]) 

# 2d slicing
print(my_array2[0:2,1:3])
print(my_array2[0:3:2, 0:3:2])

# Reshape
print(my_array2.reshape(4,3))
print(my_array2.reshape(1,4,3))
my_array3 = np.zeros(
       shape = (1,3,5)
)
my_array3_reshaped = my_array3.reshape(1,-1,3)      # default
print(my_array3)
print(my_array3_reshaped)
print(my_array3.shape)
print(my_array3_reshaped.shape)