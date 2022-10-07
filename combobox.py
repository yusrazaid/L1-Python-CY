import tkinter as tk 
from tkinter import ttk 
window=tk.Tk()
window.title("COMBO-BOX")
window.geometry("300x200")

ttk.Label(window,text="This is Combo-Box!",background="gold",foreground="red",font=("Times New Roman",10)).grid(row=0,column=1)

ttk.Label(window,text="Select a month: ",background="gold",foreground="red",font=("Times New Roman",10)).grid(row=5,column=0,padx=10,pady=25)

n=tk.StringVar()
monthchoosen=ttk.Combobox(window,width=27,textvariable=n)
monthchoosen["values"]=("JAN","FEB","MARCH","APRIL","MAY","JUNE","JULY","AUG","SEPT","OCT","NOV","DEC")
monthchoosen.grid(column=1,row=5)
monthchoosen.current()
window.mainloop()
'''from tkinter import *  
  
top = Tk()  
top.geometry("140x100")  
frame = Frame(top)  
frame.pack()  
  
leftframe = Frame(top)  
leftframe.pack(side = LEFT)  
  
rightframe = Frame(top)  
rightframe.pack(side = RIGHT)  
  
btn1 = Button(frame, text="Submit",bg="white", fg="red",activebackground = "red")  
btn1.pack(side = LEFT)  
  
btn2 = Button(frame, text="Remove", fg="brown", activebackground = "brown")  
btn2.pack(side = RIGHT)  
  
btn3 = Button(rightframe, text="Add", fg="blue", activebackground = "blue")  
btn3.pack(side = LEFT)  
  
btn4 = Button(leftframe, text="Modify", fg="black", activebackground = "white")  
btn4.pack(side = RIGHT)  
  
top.mainloop()'''
