from tkinter import *
from tkinter import messagebox
i=int(input("Enter a number"))
if i%2==0:
    root=Tk()
    root.geometry("200x200")
    w=Label(root,text="MESSAGE BOX!",font="50")
    w.pack()
    
    messagebox.showinfo("showinfo","Your number is even!")


elif i%2!=0:
    root=Tk()
    root.geometry("200x200")
    w=Label(root,text="MESSAGE BOX!",font="50")
    w.pack()

    messagebox.showinfo("showinfo","Your number is odd!")  


  
else:
    print("Error")
        
root.mainloop()
