import numpy as np

my_list = [1,2,3,4,5]                   # list
print(type(my_list))

my_np_array = np.array(my_list)         # convert the  list into np array
print(type(my_np_array))

print(my_np_array.dtype)                # type 
print(my_np_array.shape)                # The number of elements along each dimension
print(my_np_array.ndim)                # type 

np_zeros = np.zeros(                  # create array with zeros
    shape = (10,3)
)
print(np_zeros)

np_ones = np.ones(                  # create array with ones
    shape = (10,3)
)
print(np_ones)

np_specific_value = np.full(                  # create array with specific value
    shape = (5,5),
    fill_value = 5
)
print(np_specific_value)

id_matrix = np.eye(4)
print(id_matrix)

empty_array = np.empty(                  # create empty array
    shape = (3,3)
)
print(empty_array)

print(empty_array.dtype)
array = empty_array.astype('int')         # conversion from one data to another data
print(array)
print(array.dtype)