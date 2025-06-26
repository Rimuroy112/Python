# numpy filtering
import numpy as np

my_array = np.array ([1,2,3,4,5])
filter_mask = [True,False,True,False,True]
print(my_array[filter_mask])

indices = [0,2,4]
print(my_array[filter_mask])

# vectorization

my_array2 = np.array([2,3,4,5,6])

for val in my_array2:              # Loop
    if val % 2 == 1:
        print(val)

print(my_array2[my_array2 % 2 == 1])   # vectorization



# Broadcasting
w = np.array([[2,3],
              [2,3],
              [2,3]])
x = np.array([1,2])

print(w*x)

# Numpy axis
my_array3 = np.array([[1,2,3],
                      [4,5,6]])

print(my_array3.shape)
my_array3_sum = np.sum(my_array3,axis=1)
print(my_array3_sum)
print(my_array3_sum.shape)

my_3d = np.zeros(
    shape=(3,2,4)
)
print(np.sum(my_3d,axis=0).shape)
print(np.sum(my_3d,axis=1).shape)
print(np.sum(my_3d,axis=2).shape)

# Numpy random

print(np.random.rand(5))
print(np.random.rand(5,3))
print(np.random.randint(10))
my_array4 = np.random.randint(10, size=(5,3))
print(my_array4)
np.random.shuffle(my_array4)                   # randomly shuffle
print(my_array4)