from tkinter import *
tk=Tk()
tk.geometry("400x400")
tk.title("My First Game Screen")

l=Label(tk, text="Enter first number" ,fg="red")
i=Entry(tk)
l2=Label(tk, text="Enter second number", fg="red")
i2=Entry(tk)
a=i.get()
b=i2.get()
l3=Label(tk, text=("Result =" , a,b))


l.pack()
i.pack()
l2.pack()
i2.pack()
l3.pack()

tk.mainloop()