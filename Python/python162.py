from tkinter import *
t=Tk()
t.title('Length Calculator App')
t.geometry('400x400')

l=Label(t, text='Enter the value in inches')
e=Entry()

btn=Button(t,text='Submit',command=lambda:print(int(e.get())*2.54))

l.pack()
e.pack()
btn.pack()
t.mainloop()
