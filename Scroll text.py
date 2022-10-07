#ScrollText
import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
window=tk.Tk()
window.title("SCROLLED TEXT")
window.geometry("300x200")
ttk.Label(window,text="SCROLLED TEXT",background="gold",foreground="red",font=("Times New Roman",10)).grid(row=0,column=1)
text_area=scrolledtext.ScrolledText(window,wrap=tk.WORD,width=10,height=5,font=("Times New Roman",15))
text_area.grid(column=0,pady=10,padx=10)
text_area.insert(tk.INSERT,"""\Hi CODEYOUNG!!!
Hi CODEYOUNG!!!
Hi CODEYOUNG!!!
Hi CODEYOUNG!!!
Hi CODEYOUNG!!!
Hi CODEYOUNG!!!
Hi CODEYOUNG!!!
Hi CODEYOUNG!!!""")
text_area.focus()
#text_area.configure(state="disabled")#not be able to write 
window.mainloop()
