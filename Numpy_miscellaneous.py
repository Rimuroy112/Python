import numpy as np

a = np.array([1,2,3,4,5])
b = np.array([6,7,8,9,10])
print(np.concatenate((a,b)))               #concatenation

print(a[a<5])
print(a[(a>1) & (a<5)])

c = np.array([[1,1],
             [2,2]])
d = np.array([[3,3],
             [4,4]])
print(np.vstack((c,d)))       # stack index vertically


print(np.hstack((c,d)))       # stack index horizontally

print(c.max())
print(d.min())

e = np.array([1,1,2,2,3,3,4,4,5,5])
u = np.unique(e,return_index = True,return_counts = True)       # Unique elements,indices and counts
print(u)

f = np.array([[1,1],
              [2,2],
              [3,3],
              [4,4],
              [5,5]])
v = np.unique(f,axis=0,return_index = True,return_counts = True)
print(v)

arr = np.array([[1,2,3],
               [4,5,6]])
print(arr.transpose())                    # Transpose matrix

print(arr.T)                         # Transpose

g = np.array([1,2,3,4,5])
print(np.flip(g))                   # reverse

h = np.array([[1,2,3],              # Full reverse
              [4,5,6],
              [7,8,9]])
print(np.flip(h))

print(np.flip(h,axis=0))      # reverse in rows

print(np.flip(h,axis=1))      # reverse in columns

x = np.flip(h[1])
print(x)                # reverse a specific row

print(np.flip(h[:,1]))          # reverse a specific row


print(h.flatten())    # Flatten a matrix