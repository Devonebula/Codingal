from tkinter import *
k=Tk()
k.title("My vooory")
k.geometry("400x400")

nums=[[9, 8 ,7],
      [6,5,4],
      [3,2,1],
      ["/", 0 ,"*"]]
      
for i in range(4):
      k.columnconfigure(i,weight=1, minsize=75)
      k.rowconfigure(i, weight=1, minsize=50)         

      for j in range(3):
            frame=Frame(
                  master=k,
                  relief=SUNKEN,
                  borderwidth=1
            )
            frame.grid(row=i, column=j)
            label=Label(master=frame, text=nums[i][j])
            label.pack(padx=3, pady=3)
k.mainloop()

            
            
    