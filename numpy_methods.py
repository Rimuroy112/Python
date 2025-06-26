import numpy as np

# numpy methods
a = np.array([5,3,2,4,1])
print(np.sort(a))                 # sorting 
b = np.sort(a)[::-1]              # reverse sorting 
print(b)        


# argmax , argmin

print(np.argmax(a))        # return the index of max value
print(np.argmin(a))        # return the index of min value


# split

my_np = np.array([1,5,1,1,5,7])
new_np = np.split(my_np,
                  indices_or_sections=3
                  )
print(new_np)



