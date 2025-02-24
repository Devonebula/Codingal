import numpy as np

arr1=np.array([1,2,3,4,5,6])
arr2=np.array([[1,2,3],[4,5,6]])
print(arr1)
print(arr2)

print(f'Shape {arr2.shape}')
print(f"Size {arr2.size}")
print(f'Data type {arr2.dtype}')

zeros=np.zeros((3,3))
ones=np.ones((2,2))
np.identity=np.eye(3)
random_r=np.random.rand(3,3)