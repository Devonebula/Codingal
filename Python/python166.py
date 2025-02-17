import tkinter as tk
from tkinter import ttk , messagebox

class Restaurant:
    def __init__(self, root):
        self.root = root
        self.root.title('Restaurant Management App')

        self.menu_items={
            'french fries' : 2,
            "breakFast meal" :2,
            "lunch meal" :2,
            "dinner meal" :2,
            "pizza meal" : 4
        }
        self.exchange_rate=85.85
        
        self.setup_background(root)

        frame=ttk.Frame(root)
        frame.place(relx=0.5, rely=0.5, anchor='center')

        ttk.Label(frame, text='Restaurant Order Management' , font=('Arial', 20, "Bold")). grid(row=0, columnspan=3,padx=10, pady=10)
        
        self.menu_label={}
        self.menu_quantity={}
        
        for i ,(item, price) in enumerate(self.menu_items.items(), start=1):
            label=ttk.Label(frame, text=f"{item} (${price}):", font=('Arial', 12))
            label.grid(row=1, column=0, padx=10, pady=5)
            self.menu_label[item]= label
            
            quantity_entry=ttk.Entry(frame, width=5).grid(row=i, column=1, padx=10, pady=5)
            self.menu_quantity[item]=quantity_entry

        self.currency_var=tk.StringVar()
        ttk.Label(frame, text='Currency', font=('Arial', 12)).grid(row=len(self.menu_items)+1,column=0, padx=10, pady=5)

        currency_dropdown=ttk.Combobox(frame, textvariable=self.currency_var,
                                       state="readonly", 
                                       width=18,
                                       values=("USD", "INR")
                                       )
        currency_dropdown.grid(row=len(self.menu_items)+1, column=1, padx=10, pady=5)
        

            