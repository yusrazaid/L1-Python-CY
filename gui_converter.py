from tkinter import *
import tkinter.messagebox
root=Tk()
root.title("Kg Converter")



amount_l=Label(root,text="KG/kilos")
amount_l.grid(row=1,column=2)

amount_e=Entry(root,bg="white",)
amount_e.grid(row=1,column=3)

def calc_pounds():
    k=int(amount_e.get())
    ans=k* 2.205
    Label(text=f"{ans}",font="arial 30 bold",
          bg="cadet blue").grid(row=2,column=5)
btn1 = Button(root,font=('arial',20,'bold'),text="lb",bg="cadet blue",
              command=calc_pounds)
btn1.grid(row=2,column=5)
#-------------------------------------------------------------------------
def calc_grams():
    k=int(amount_e.get())
    ans=k* 1000
    Label(text=f"{ans}",font="arial 30 bold",
          bg="cadet blue").grid(row=2,column=6)
btn1 = Button(root,font=('arial',20,'bold'),text="Grams",bg="cadet blue",
              command=calc_grams)
btn1.grid(row=2,column=6)
#----------------------------------------------------------------
def calc_ounces():
    k=int(amount_e.get())
    ans=k* 35.274 
    Label(text=f"{ans}",font="arial 30 bold",
          bg="cadet blue").grid(row=2,column=7)
btn1 = Button(root,font=('arial',20,'bold'),text="Ounces",bg="cadet blue",
              command=calc_ounces)
btn1.grid(row=2,column=7)

