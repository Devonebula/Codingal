from tkinter import *
tk=Tk()
tk.geometry("400x400")
tk.title("My First Game Screen")

l=Label(tk, text="Enter first number" ,fg="red")
i=Entry(tk)
l2=Label(tk, text="Enter second number", fg="red")
i2=Entry(tk)
l3=Entry(tk, state="readonly")

def calculate():
    a=int(i.get())
    b=int(i2.get())
    l3.config(state="normal")
    l3.delete(0, END)
    l3.insert(END, f"Result is {a*b}")
    l3.config(state='readonly')

btn=Button(tk,text='Calculate', command=calculate)

l.pack()
i.pack()
l2.pack()
i2.pack()
btn.pack()
l3.pack()
tk.mainloop()