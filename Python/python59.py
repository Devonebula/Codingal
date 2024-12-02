a=input("Enter a string:\t")
for i in a:
    if i=="a" or i=="A":
        print("A or a is present in the string")
        break
else:
    print("A or a is not present in the string")