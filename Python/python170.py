from tkinter import *
import random
t=Tk()

t.geometry("400x400")
t.title('Rock Paper Scissors')

option=['Rock', 'Paper', 'Scissor']

l=Label(t, text='Enter your name')
l.grid(row=0, column=0)
e=Entry(t)
e.grid(row=0, column=1)

l2=Label(t, text='Enter your choice').grid(row=1, column=0, columnspan=3)

def rocks():
    computer_choice=random.choice(option)
    a=e.get()
    
rock=Button(t, text='Rock')
rock.grid(row=2, column=0, COMMAND=rocks) 



paper=Button(t, text='Paper').grid(row=2, column=1)
scissor=Button(t, text='Scissor').grid(row=2, column=2)

result=Entry(t)
result.grid(row=3)

t.mainloop()