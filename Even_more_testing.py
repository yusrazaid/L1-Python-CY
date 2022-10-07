'''import tkinter as tk

app = tk.Tk()

entryExample1 = tk.Entry(app)
entryExample2 = tk.Entry(app)

entryExample1.grid(row=0,
               column=0,
               padx=10,
               pady=10,
               ipady=30)

entryExample2.grid(row=1,
               column=0,
               padx=10,
               pady=10,
               ipadx=20,
               ipady=30)

app.geometry("200x200")

app.mainloop()'''

import tkinter as tk

app = tk.Tk()

entryExample1 = tk.Entry(app)
entryExample2 = tk.Entry(app)

entryExample1.grid(row=0,
               column=0,
               padx=10,
               pady=10,
               ipady=50)

entryExample2.grid(row=0,
               column=1,
               padx=10,
               pady=10,
               ipady=60)

app.geometry("300x200")

app.mainloop()
