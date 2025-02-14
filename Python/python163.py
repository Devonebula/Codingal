from tkinter import *
t=Tk()
t.geometry("400x400")
t.title('Interest Calculator')

t.columnconfigure(0, weight=1)
t.columnconfigure(1, weight=1)

l=Label(text='Interest Calculator App' , font=('Arial', 30), fg='green')
l.grid(row=0)

principal_frame=Frame(t)
principal=Label(principal_frame, text='Enter the Prinicipal Amount')
principal_entry=Entry(principal_frame)

time_frame=Frame(t)
time=Label(time_frame, text='Enter time (In Years)')
time_entry=Entry(time_frame)

rate_frame=Frame(t)
rate=Label(rate_frame, text='Enter Rate (In Percentage)')
rate_entry=Entry(rate_frame)

textbox=Text(bg='#BEBEBE', fg='black')

btn=Button(text='Calculate', command=calculate)

def calculate():
    textbox.delete(1.0, END)
    principal=principal_entry.get()
    time=time_entry.get()
    rate=rate_entry.get()

    simple_intrest=principal*(1+(rate*time))
    compund_intrest=
    
t.mainloop()