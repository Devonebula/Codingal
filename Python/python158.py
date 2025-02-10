from tkinter import *
t=Tk()
t.title('Event handler')
t.geometry('500x500')

def key_press(event):
    print(event.char)

t.bind('<Key>', key_press)

def button_press(event):
    print("The is clicked")

button=Button(text='Click Me')
button.pack()

button.bind('<Button-1>', button_press)

t.mainloop()