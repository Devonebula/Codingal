class flashcard:
    def __init__(self, word, meaning):
        self.word = word
        self.meaning = meaning
    def __str__(self):
        return f"{self.word} ({self.meaning})" 

flash=[]
print("Wolcome to my Flashcard App")

while True:
    word=input("Enter the word:\t")
    meaning=input("Enter the meaning:\t")
    
    ob=flashcard(word, meaning)
    flash.append(ob)
    option=int(input("Enter 1 to continue and 0 to exit:\t"))
    if option==0:
        break

for i in flash:
    print(i)
        