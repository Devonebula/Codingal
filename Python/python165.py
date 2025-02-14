from tkinter import *

t=Tk()
t.title("Password checker")
t.geometry("400x400")

l=Label(t,text='Enter your password')
l.pack()

e=Entry(t)
e.pack()

l1=Label(t, text='')
def check():
    password=e.get()
    if len(password)<=5:
        l1.configure(text='Your password is weak', font=('Arial', 12), fg = 'red')
    elif len(password)>5 and len(password)<=8:
        l1.configure(text='Your password is medium', font=('Arial', 12), fg = 'yellow')
    elif len(password)>8:
        l1.configure(text='Your password is strong', font=('Arial', 12), fg = 'light green')
    elif len(password)>12:
        l1.configure(text='Your password is Very Strong', font=('Arial', 12), fg = 'dark green')
b=Button(t, text='Check', command=check)

l1.pack()
b.pack()
    
t.mainloop()