from tkinter import *
from datetime import date

window=Tk()
window.title("Text box")
window.geometry("600x600")

l=Label(window, text="Hey there", fg="white", bg="black" , height=1, width=300)
name_lbl=Label(window, text="Enter your name", )
e=Entry(window)
text_box=Text(window, height=3, fg="white", bg="black")

def display():
    name=e.get()

    global message
    message=(f'Hello {name}, welcome to the application. Todays date is {date.today()} ')

    text_box.insert(END, message)

btn=Button(window, text="Submit", command=display)

l.pack()
name_lbl.pack()
e.pack()
btn.pack()
text_box.pack()

window.mainloop()   
    
