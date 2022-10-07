from tkinter import *
import tkinter.messagebox
root=Tk()
root.title("Simple Interest Calculator")


amount_l=Label(root,text="Principal Amount")
amount_l.grid(row=1,column=5)

amount_e=Entry(root,bg="white",)
amount_e.grid(row=1,column=10)

rate_l=Label(root,text="----Rate----")
rate_l.grid(row=2,column=5)

rate_e=Entry(root,bg="white")
rate_e.grid(row=2,column=10)

time_l=Label(root,text="Time  (in Years)")
time_l.grid(row=3,column=5)

time_e=Entry(root,bg="white")
time_e.grid(row=3,column=10)

def Calculate():
    m=int(amount_e.get())
    n=int(rate_e.get())
    o=int(time_e.get())
    a=m*n*o/100
    Label(text=f"{a}",font="arial 30 bold",bg="cadet blue").grid(row=4,column=10)
 
btn1 = Button(root,font=('arial',20,'bold'),text="$",bg="cadet blue",command=Calculate)
btn1.grid(row=4,column=10)
root.mainloop()
