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


def calculate():
    textbox.delete(1.0, END)
    principal=int(principal_entry.get())
    time=int(time_entry.get())
    rate=int(rate_entry.get())

    simple_intrest=principal*(1+(rate*time))
    compund_intrest=principal*(1+(rate/100))**time
    
    textbox.insert(END, f'Simple Intrest: {simple_intrest}₨\nCompound Intrest: {compund_intrest}₨')
    principal_entry.delete(0, END)
    time_entry.delete(0, END)
    rate_entry.delete(0, END)
    
    
btn=Button(text='Calculate', command=calculate)

principal_frame.grid(row=1, column=0, pady=5)
principal.pack(side=LEFT, padx=5)
principal_entry.pack(side=LEFT, padx=5)

time_frame.grid(row=2, column=0, pady=5)
time.pack(side=LEFT, padx=5)
time_entry.pack(side=LEFT, padx=5)

rate_frame.grid(row=3, column=0, pady=5)
rate.pack(side=LEFT, padx=5)
rate_entry.pack(side=LEFT, padx=5)

btn.grid(row=4, column=0)

textbox.grid(row=5)


t.mainloop()