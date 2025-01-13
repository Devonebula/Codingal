class parent:
    __private=10
    public=20
    def __privatemethod(self):
        print("Private method")
    def hello(self):
        print(self.__private)
        self.__privatemethod()
class child(parent):
    pass
a=child()
# print(a.__private)
print(a.public)
a.hello()
    