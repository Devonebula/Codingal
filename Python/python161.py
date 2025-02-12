from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfile

t=Tk()
t.title('Text Editor')
t.geometry('600x600')
t.rowconfigure(0, minsize=800, weight=1)
t.columnconfigure(1,minsize=800, weight=1) 

def openfile():
    filepath=askopenfilename(
        filetypes=[('Tect Files', '*.txt'), ('All Files', '*.*')]
    )
    if not filepath:
        return
    
    textedit.delete(1.0, END)
    with open(filepath, 'r') as input_file:
        text=input_file.read()
        textedit.insert(END, text)
        input_file.close()
    t.title(f"Text Editor {filepath}")

def savefile():
    filepath=asksaveasfile(
        defaultextension='.txt',
        filetypes=[('Tect Files', '*.txt'), ('All Files', '*.*')]
    )
    if not filepath:
        return
    with open(filepath, 'w') as output_file:
        text=textedit.get(1.0, END)
        output_file.write(text)
    t.title(f"Text Editor {filepath}")

textedit=Text(t)
fr_buttons=Frame(t, relief=RAISED, bd=2)
btn_open=Button(fr_buttons, text='Open', command=openfile)
btn_save=Button(fr_buttons, text='save', command=savefile)

btn_open.grid(row=0, column=0, sticky='ew', padx=5, pady=5)
btn_save.grid(row=1, column=0, sticky='ew', padx=5)

fr_buttons.grid(row=0,column=0, sticky='ns')
textedit.grid(row=0,column=1, sticky='nsew')

t.mainloop()


