s1={1,2,3}
s2={"a","b","c"}
s3=list(zip(s1,s2))
print(s3)

list1=[10,20,30]
list2=[100, 200, 300]

for x, y in zip(list1, list2):
    print(x, y)
    
    
stocks=["Reliance", "HDFC", "ICICI"]
prices=[1000, 2000, 3000]
dict={stocks:prices for stocks, prices in zip(stocks, prices)}
print(dict)