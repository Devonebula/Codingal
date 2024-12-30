import array as arr
arrayno=arr.array('i',[1,2,3,4,5,6 ])
print(arrayno) 
arrayno.reverse()   
print(arrayno)
print(f"The total number of 1 in array is {arrayno.count(1)}")