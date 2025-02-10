from tkinter import *
from tkinter import messagebox

t=Tk()
t.title("Virus checker")
t.geometry('300x300')

def msg():
    messagebox.showwarning('Alert', "Virus Found")

button= Button(t, text="Dont Click Me", command=msg)
button.pack()
t.mainloop()