'''from tkinter import * 
master=Tk()
w=Canvas(master,width=100,height=120)
w.pack()

canvas_height=200
canvas_width=200

y=int(canvas_height/2)
w.create_line(0,y,canvas_width,y)

master.mainloop()
#---------------------------------------
from tkinter import * 
master=Tk()
master.title("Canvas Lines")
master.geometry("555x555")

w=Canvas(master,width=300,height=200,bg="red",)
w.pack()
#creating rectangle
w.create_rectangle(50,150,250,50,fill="purple")

master.mainloop()
#----------------------------------------


from tkinter import * 
master=Tk()
master.title("Canvas Lines")
master.geometry("555x555")

w=Canvas(master,width=300,height=200,bg="gold",)
w.pack()
#creating shapes
w.create_polygon(150,150,34,23,250,50,30,34,fill="purple")

master.mainloop()
#-----------------------------------
from tkinter import * 
master=Tk()
master.geometry("400x350")

var1=IntVar()
Checkbutton(master,text="Yes",variable=var1).grid(sticky=E)

var2=IntVar()
Checkbutton(master,text="No",variable=var2).grid(sticky=E)
master.mainloop()
#--------------------------------
from tkinter import *
top=Tk()
Lb=Listbox(top)
Lb.insert(1,"School")
Lb.insert(2,"College")
Lb.insert(3,"Office") 
Lb.insert(4,"Home")
Lb.pack()
top.mainloop()

from tkinter import *
main=Tk()
m=Message(main,text="Hi,It's Sakshi Sinha over here!!")
m.config(bg="light blue")
m.pack()
main.mainloop()'''
from tkinter import *   
  
top = Tk()  
  
top.geometry("200x200")  
  
#creating a simple canvas  
c = Canvas(top,bg = "pink",height = "200",width = 200)  
  
arc = c.create_arc((10,20,30,40),start = 0,extent = 180, fill= "white")  
  
c.pack()  
  
top.mainloop()
