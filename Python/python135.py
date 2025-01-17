class student:
    def __init__(self, a):
        self.a = a
    def __lt__(self, other):
        if self.a < other.a:
            return f"{self.a} is less than {other.a}"
        else:
            return f"{self.a} is not less than {other.a}"
    def __eq__(self, other):
        if self.a == other.a:
            return f"{self.a} is equal to {other.a}"
        else:
            return f"{self.a} is not equal to {other.a}"
ob1=student(10)
ob2=student(20)
print(ob1<ob2)
print(ob1==ob2)
        
        