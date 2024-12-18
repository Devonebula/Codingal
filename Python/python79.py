l=[1,2,3,4,5,6,7,8,9,10]
print("Original list is : ", l)
count=0
for i in l:
    count+=1
print("Number of elements in list is : ", count)

sum=0
for i in l:
    sum+=i
print("Sum of elements in list is : ", sum)
avg= sum/count
print("Average of elements in list is : ", avg)

average=(sum/len(l))
print(average)
l.sort()
print(l)

l.sort(reverse=True)
print(l)

    