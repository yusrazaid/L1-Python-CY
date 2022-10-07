import tkinter as tk

app = tk.Tk()
app.geometry("400x200")

entryExample = tk.Entry(app,
                        width=10)

entryExample.pack(side=tk.LEFT,
                  padx=10)

app.mainloop()
