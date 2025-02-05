from tkinter import *
tk=Tk()
tk.geometry("400x400")
tk.title("My First Game Screen")

l=Label(tk, text="Enter first number")
i=int(Entry(tk))
l2=Label(tk, text="Enter second number")
i2=int(Entry(tk))

l3=Text(tk, text=("Result =" , i*i2))




tk.mainloop()