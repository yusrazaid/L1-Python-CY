from tkinter import *                                                                                    


root = Tk()

root.title("Calculator")
operator=""
text_Input = StringVar()

txtDisplay = Entry(root,font=('arial',20,'bold'), textvariable=text_Input, bd=30, insertwidth=4,
                    bg="powder blue", justify="right").grid(columnspan=4)

def btnClick(numbers):
    global operator
    operator = operator + str(numbers)
    text_Input.set(operator)

def btnClearDisplay():
    global operator
    operator=""
    text_Input.set("")

def btnEqualsInput():
    global operator
    sumup=str(eval(operator))
    text_Input.set(sumup)
    operator=""
#--------------------------------------------------------------------------------------

btn1=Button(root,padx=16,pady=16,bd=8, fg="black",font=('arial',20,'bold'),bg="powder blue",
            text="a",command=lambda:btnClick("a")).grid(row=1,column=0)

btn2=Button(root,padx=16,pady=16,bd=8, fg="Black", font=('arial',20,'bold'),bg="powder blue",
            text="b",command=lambda:btnClick("b")).grid(row=1,column=1)

btn3=Button(root,padx=16,pady=16,bd=8,fg="Black",font=('arial',20,'bold'),bg="powder blue",
            text="c",command=lambda:btnClick("c")).grid(row=1,column=2)
#--------------------------------------------------------------------------------------
btn4=Button(root,padx=16,pady=16,bd=8, fg="black",font=('arial',20,'bold'),bg="powder blue",
            text="d",command=lambda:btnClick("d")).grid(row=1,column=3)

btn5=Button(root,padx=16,pady=16,bd=8, fg="Black", font=('arial',20,'bold'),bg="powder blue",
            text="e",command=lambda:btnClick("e")).grid(row=2,column=0)

btn6=Button(root,padx=16,pady=16,bd=8,fg="Black",font=('arial',20,'bold'),bg="powder blue",
            text="f",command=lambda:btnClick("f")).grid(row=2,column=1)

btn7=Button(root,padx=16,pady=16,bd=8, fg="black",font=('arial',20,'bold'),bg="powder blue",
            text="g",command=lambda:btnClick("g")).grid(row=2,column=2)
#--------------------------------------------------------------------------------------
btn8=Button(root,padx=16,pady=16,bd=8, fg="Black", font=('arial',20,'bold'),bg="powder blue",
            text="h",command=lambda:btnClick("h")).grid(row=2,column=3)

btn9=Button(root,padx=16,pady=16,bd=8,fg="Black",font=('arial',20,'bold'),bg="powder blue",
            text="i",command=lambda:btnClick("i")).grid(row=1,column=2)
#--------------------------------------------------------------------------------------



#--------------------------------------------------------------------------------------
btn0=Button(root,padx=16,pady=16,bd=8, fg="black",font=('arial',20,'bold'),
            text="0", bg="powder blue",command=lambda:btnClick(0)).grid(row=4,column=0)

btnClear=Button(root,padx=16,pady=16,bd=8, fg="black",font=('arial',20,'bold'),
            text="Clear Screen", bg="powder blue",command=btnClearDisplay).grid(row=4,column=1)





