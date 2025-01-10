class person:
    def __init__(self, name, id):
        self.name = name
        self.id = id
    def display(self):
        print(f"Name:{self.name}\nID:{self.id}")
class employee(person):
    def __init__(self, name, id, salary, post):
        self.salary = salary
        self.post = post
        super().__init__(name, id)
    def displayUpdated(self):
        self.display()
        print(f"Salary:{self.salary}\nPost:{self.post}")
Keshav=employee("Keshav", 13213, 10000, "Computer Engineer")
Keshav.displayUpdated()
        