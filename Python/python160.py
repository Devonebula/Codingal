from tkinter import *
from datetime import date


t=Tk()
t.title('Age Calculator App')
t.geometry('700x500')
t.columnconfigure(0, weight=1)
t.columnconfigure(1, weight=1)

l=Label(text='Age Calculator App' , font=('Arial', 30), fg='green')
l.grid(row=0)

name_frame=Frame(t)
name=Label(name_frame,text='Enter your Name')
name_entry=Entry(name_frame)

year_frame=Frame(t)
year=Label(year_frame,text='Enter your Year')
year_entry=Entry(year_frame)

month_frame=Frame(t)
month=Label(month_frame,text='Enter your Month')
month_entry=Entry(month_frame)

bdate_frame=Frame(t)
bdate=Label(bdate_frame,text='Enter your Date')
bdate_entry=Entry(bdate_frame)

textbox=Text(bg='#BEBEBE', fg='black')




def calculate_age():
    textbox.delete(1.0, END)
    name=name_entry.get()
    year=int(year_entry.get())
    month=int(month_entry.get())
    bdate=int(bdate_entry.get())
    today=date.today()
    age=today.year - year - ((today.month, today.day) < (month, bdate))
    
    textbox.insert(END, f'Hello {name}. Welcome here.\n You are {age} years old.')
    
    name_entry.delete(0, END)
    year_entry.delete(0, END)
    month_entry.delete(0, END)
    bdate_entry.delete(0, END)

btn=Button(text='Calculate Age', command=calculate_age)


name_frame.grid(row=1, column=0, pady=5)
name.pack(side=LEFT, padx=5)
name_entry.pack(side=LEFT, padx=5)


year_frame.grid(row=2, column=0, pady=5)
year.pack(side=LEFT, padx=5)
year_entry.pack(side=LEFT, padx=5)

month_frame.grid(row=3, column=0, pady=5)
month.pack(side=LEFT, padx=5)
month_entry.pack(side=LEFT, padx=5)

bdate_frame.grid(row=4, column=0, pady=5)
bdate.pack(side=LEFT, padx=5)
bdate_entry.pack(side=LEFT, padx=5)

btn.grid(row=5, column=0)

textbox.grid(row=6)



t.mainloop()
