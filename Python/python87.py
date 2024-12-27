dict={"Keshav":1, "Amit":2, "Raj":3, "Rahul":2, "Vishal":41}
k=2
res=0
for key in dict:
    if dict[key]==k:
        res+=1
print(f"The total number of {k} in the dictionary is {res}")
