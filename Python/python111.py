class parrot:
    species = "bird"
    def __init__(self, name, age,):
        self.name = name
        self.age = age
    
blu=parrot("blu",10)
kiki=parrot("kiki",12)

print(f"blu is a {blu.species} and is {blu.age} years old")
print(f"kiki is a {kiki.species} and is {kiki.age} years old")