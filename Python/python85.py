tup1=(1,2,3,4,5,6)
tup2=(6,5,4,3,2,1)
for i in tup1:
    print(i*tup2[tup1.index(i)])