class India:
    def capital(self):
        print("New Delhi is the capital of India.")
    def language(self):
        print("Hindi is primary language of India.")
    def type(self):
        print("India is a developing country.")
class USA:
    def capital(self):
        print("Washington, D.C. is the capital of USA.")
    def language(self):
        print("English is the primary language of USA.")
    def type(self):
        print("USA is a developed country.")
india=India()
usa=USA()
tuple=(india,usa)
for i in tuple:
    i.capital()
    i.language()
    i.type()