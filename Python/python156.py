from tkinter import *
t=Tk()
t.title("Login Screen")
t.geometry("500x500")

frame=Frame(master = t, height=200, width=360,  bg="#d0efff")
l=Label(frame, text="Name", bg="#3895D3", fg="white" ,width=12)
l2=Label(frame, text="Email", bg="#3895D3", fg="white",width=12)
l3=Label(frame, text="Password", bg="#3895D3", fg="white",width=12)

name_entry=Entry(frame,)
email_entry=Entry(frame,)
pass_entry=Entry(frame,)

textbox=Text(bg="#BEBEBE", fg="black")

def display():
    name=name_entry.get()
    greet="Hello "+name
    message="\nConratulations for your now account"
    textbox.insert(END, greet)
    textbox.insert(END, message)
    
btn=Button(text="Create Account", command=display, bg="red")

frame.pack()
l.pack()
name_entry.pack()
l2.pack()
email_entry.pack()
l3.pack()
pass_entry.pack()
btn.pack()
textbox.pack()
t.mainloop()
    