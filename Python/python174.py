import numpy as np
import time

size=10**6
py_l=list(range(size))
py_l2=list(range(size))

numpy_a=np.arange(size)
numpy_a2=np.arange(size)

start=time.time()
py_result=[py_l[i]+py_l2[i] for i in range(size)]
end=time.time()
total_a=end-start
print(f'Total time take by the list is {total_a}')



start=time.time()
numpy_result=[numpy_a[i]+numpy_a2[i] for i in range(size)]
end=time.time()
total_b=end-start
print(f'Total time take by the numpy array is {total_b}')

print(total_a/total_b)