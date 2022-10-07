from tkinter import *
root=Tk()
root.geometry("150x150")

a=Canvas(root,bg="orchid1",height=150,width=150)
arc=a.create_arc((50,25,100,100),start=360,extent=100,fill='lavender')
a.pack()
root.mainloop()
