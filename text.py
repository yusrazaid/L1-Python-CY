'''from tkinter import *
master=Tk()
master.geometry("350x350")

t=Text(master,height=2,width=30)
t.pack()
t.insert(END,"HI, WELCOME TO CODEYOUNG!")

master.mainloop()

#----------------------------
from tkinter import *
root = Tk()
# specify size of window
root.geometry("250x170")
# Create text widget and specify size.
T = Text(root, height = 5, width = 52)
# Create label
l = Label(root, text = "Fact of the Day")
l.config(font =("Courier", 14))
Fact = """Hi, Welcome to CodeYoung,my name is yusra and I am 12 years old,I love coding. i can solve a rubix cube in about a minute"""
# Create button for next text.
b1 = Button(root, text = "Next", )
# Create an Exit button.
b2 = Button(root, text = "Exit",command =root.destroy) 
l.pack()
T.pack()
b1.pack()
b2.pack()
T.insert(END, Fact)
root.mainloop()''''
#--------------------------------------------------------------------------------


