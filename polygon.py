from tkinter import*
root=Tk()
root.geometry("300x300")
C=Canvas(root,bg="orchid1",height=150,width=150)
oval = C.create_polygon(150,150,150,150)
C.pack()
root.mainloop()
#I made a square
