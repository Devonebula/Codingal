import numpy as np

# this is main array
arr1=np.array([1,2,3,4,5,6,7,8,9])

# array where -1 will be stored
arr2=np.array([])

# code for -1 in arr2
for i in arr1:
    if i%2==0:
        arr2=np.append(arr2,i)
    else:
        arr2=np.append(arr2,-1)
print(arr1)
print(arr2)
        
        