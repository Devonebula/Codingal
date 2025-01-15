class parent:
    __bankbalance=100000
    phoneno="000000000"
    __psw="xxx"
    
    def __str__(self):
        return "My name is Ram"
class child(parent):
    print(parent.phoneno)
    def __str__(self):
        return "My name is Sham"
a=child()
print(a)
b=parent()
print(b)