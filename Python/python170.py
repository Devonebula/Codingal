from tkinter import *
import random
t=Tk()

t.geometry("600x400")
t.title('Rock Paper Scissors')

option=['Rock', 'Paper', 'Scissor']
# these are options that are selected by the computer

l=Label(t, text='Enter your name')
l.grid(row=0, column=0)

e=Entry(t)
e.grid(row=0, column=1)

def rocks():
    text_box.delete(1.0, END)
    computer_choice=random.choice(option)
    nameofuser=e.get()
    if computer_choice=="Rock":
        text_box.insert(END, f"Rock vs {computer_choice}\n {nameofuser} IT'S A DRAW!")
    if computer_choice=="Paper":
        text_box.insert(END, f"Rock vs {computer_choice}\n {nameofuser} LOSE!")
    if computer_choice=="Scissor":
        text_box.insert(END, f"Rock vs {computer_choice}\n {nameofuser} WIN!")
        
    
def papers():
    text_box.delete(1.0, END)
    computer_choice=random.choice(option)
    nameofuser=e.get()
    if computer_choice=="Rock":
        text_box.insert(END, f"Paper vs {computer_choice}\n {nameofuser} WIN!")
    if computer_choice=="Paper":
        text_box.insert(END, f"Paper vs {computer_choice}\n {nameofuser} IT'S A DRAW!")
    if computer_choice=="Scissor":
        text_box.insert(END, f"Paper vs {computer_choice}\n {nameofuser} LOSE!")
        
    
def scissors():
    text_box.delete(1.0, END)
    computer_choice=random.choice(option)
    nameofuser=e.get()
    if computer_choice=="Rock":
        text_box.insert(END, f"Scissor vs {computer_choice}\n {nameofuser} LOSE!")
    if computer_choice=="Paper":
        text_box.insert(END, f"Scissor vs {computer_choice}\n {nameofuser} WIN!")
    if computer_choice=="Scissor":
        text_box.insert(END, f"Scissor vs {computer_choice}\n {nameofuser} IT'S A DRAW!")
    
    
# buttons for user selection
rock=Button(t, text='Rock', command=rocks)
rock.grid(row=2, column=0) 

paper=Button(t, text='Paper', command=papers)
paper.grid(row=2, column=1)

scissor=Button(t, text='Scissor', command=scissors)
scissor.grid(row=2, column=2)


text_box=Text(t, bg='#BEBEBE', fg='black')
text_box.grid(row=3, columnspan=4)

t.mainloop()