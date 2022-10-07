from tkinter import *                                                                                    


root = Tk()

root.title("Interactive keyboard")
operator=""
text_Input = StringVar()

txtDisplay = Entry(root,font=('arial',20,'bold'), textvariable=text_Input,width=50, bd=40, insertwidth=7,
                    bg="lavender", justify="left").grid(columnspan=50)

def btnClick(numbers):
    global operator
    operator = operator + str(numbers)
    text_Input.set(operator)

def btnClearDisplay():
    global operator
    operator=""
    text_Input.set("")
    


#--------------------------------------------------------------------------------------


#--------------------------------------------------------------------------------------
btna=Button(root,padx=10,pady=10,bd=5, fg="black",font=('arial',20,'bold'),bg="lavender",
            text="a",command=lambda:btnClick("a")).grid(row=1,column=0)

btnb=Button(root,padx=10,pady=10,bd=5, fg="black",font=('arial',20,'bold'),
            text="b", bg="lavender",command=lambda:btnClick("b")).grid(row=1,column=1)

btnc=Button(root,padx=10,pady=10,bd=5, fg="black",font=('arial',20,'bold'),
            text="c", bg="lavender",command=lambda:btnClick("c")).grid(row=1,column=2)

btnd=Button(root,padx=10,pady=10,bd=5, fg="black",font=('arial',20,'bold'),bg="lavender",
            text="d",command=lambda:btnClick("d")).grid(row=1,column=3)

btne=Button(root,padx=10,pady=10,bd=5, fg="Black", font=('arial',20,'bold'),bg="lavender",
            text="e",command=lambda:btnClick("e")).grid(row=1,column=4)

btnf=Button(root,padx=10,pady=10,bd=5,fg="Black",font=('arial',20,'bold'),bg="lavender",
            text="f",command=lambda:btnClick("f")).grid(row=1,column=5)
#------------------------------------------------------------------------------------------------------------------------
btnA=Button(root,padx=10,pady=10,bd=5, fg="black",font=('arial',20,'bold'),
            text="A", bg="lavender",command=lambda:btnClick("A")).grid(row=1,column=6)

btnB=Button(root,padx=10,pady=10,bd=5, fg="black",font=('arial',20,'bold'),
            text="B", bg="lavender",command=lambda:btnClick("B")).grid(row=1,column=7)

btnC=Button(root,padx=10,pady=10,bd=5, fg="black",font=('arial',20,'bold'),
            text="C", bg="lavender",command=lambda:btnClick("C")).grid(row=1,column=8)

btnD=Button(root,padx=10,pady=10,bd=5, fg="black",font=('arial',20,'bold'),
            text="D", bg="lavender",command=lambda:btnClick("D")).grid(row=1,column=9)

btnE=Button(root,padx=10,pady=10,bd=5, fg="black",font=('arial',20,'bold'),
            text="E", bg="lavender",command=lambda:btnClick("E")).grid(row=1,column=10)

btnF=Button(root,padx=10,pady=10,bd=5, fg="black",font=('arial',20,'bold'),
            text="F", bg="lavender",command=lambda:btnClick("F")).grid(row=1,column=11)
#---------------------------------------------------------------------------------------------------
btng=Button(root,padx=10,pady=10,bd=5, fg="black",font=('arial',20,'bold'),
            text="g", bg="lavender",command=lambda:btnClick("g")).grid(row=2,column=2)

btnh=Button(root,padx=10,pady=10,bd=5, fg="black",font=('arial',20,'bold'),
            text="h", bg="lavender",command=lambda:btnClick("h")).grid(row=2,column=0)

btni=Button(root,padx=10,pady=10,bd=5, fg="black",font=('arial',20,'bold'),
            text="i", bg="lavender",command=lambda:btnClick("i")).grid(row=2,column=1)

btnj=Button(root,padx=10,pady=10,bd=5, fg="black",font=('arial',20,'bold'),
            text="j", bg="lavender",command=lambda:btnClick("j")).grid(row=2,column=3)

btnk=Button(root,padx=10,pady=10,bd=5, fg="black",font=('arial',20,'bold'),
            text="k", bg="lavender",command=lambda:btnClick("k")).grid(row=2,column=4)

btnl=Button(root,padx=10,pady=10,bd=5, fg="black",font=('arial',20,'bold'),
            text="l", bg="lavender",command=lambda:btnClick("l")).grid(row=2,column=5)
#--------------------------------------------------------------------------------------------------------------------------------------------------
btnClear=Button(root,padx=10,pady=10,bd=5, fg="black",font=('arial',20,'bold'),
            text="-", bg="lavender",command=btnClearDisplay).grid(row=5,column=2)
#---------------------------------------------------------------------------------------------------------------------------------------------------

btnG=Button(root,padx=10,pady=10,bd=5, fg="black",font=('arial',20,'bold'),
            text="G", bg="lavender",command=lambda:btnClick("G")).grid(row=2,column=6)

btnH=Button(root,padx=10,pady=10,bd=5, fg="black",font=('arial',20,'bold'),
            text="H", bg="lavender",command=lambda:btnClick("H")).grid(row=2,column=7)

btnI=Button(root,padx=10,pady=10,bd=5, fg="black",font=('arial',20,'bold'),
            text="I", bg="lavender",command=lambda:btnClick("I")).grid(row=2,column=8)

btJ=Button(root,padx=10,pady=10,bd=5, fg="black",font=('arial',20,'bold'),
            text="J", bg="lavender",command=lambda:btnClick("J")).grid(row=2,column=9)

btnK=Button(root,padx=10,pady=10,bd=5, fg="black",font=('arial',20,'bold'),
            text="K", bg="lavender",command=lambda:btnClick("K")).grid(row=2,column=10)

btnL=Button(root,padx=10,pady=10,bd=5, fg="black",font=('arial',20,'bold'),
            text="L", bg="lavender",command=lambda:btnClick("L")).grid(row=2,column=11)
#--------------------------------------------------------------------------------------------------------------------------

btm=Button(root,padx=10,pady=10,bd=5, fg="black",font=('arial',20,'bold'),
            text="m", bg="lavender",command=lambda:btnClick("m")).grid(row=3,column=0)

btnn=Button(root,padx=10,pady=10,bd=5,fg="black",font=('arial',20,'bold'),
            text="n", bg="lavender",command=lambda:btnClick("n")).grid(row=3,column=1)

btno=Button(root,padx=10,pady=10,bd=5, fg="black",font=('arial',20,'bold'),
            text="o", bg="lavender",command=lambda:btnClick("o")).grid(row=3,column=2)
btnp=Button(root,padx=10,pady=10,bd=5, fg="black",font=('arial',20,'bold'),
            text="p", bg="lavender",command=lambda:btnClick("p")).grid(row=3,column=3)

btnq=Button(root,padx=10,pady=10,bd=5, fg="black",font=('arial',20,'bold'),
            text="q", bg="lavender",command=lambda:btnClick("q")).grid(row=3,column=4)

btnr=Button(root,padx=10,pady=10,bd=5, fg="black",font=('arial',20,'bold'),
            text="r", bg="lavender",command=lambda:btnClick("r")).grid(row=3,column=5)

#-------------------------------------------------------------------------------------------------------------------------------
btnM=Button(root,padx=10,pady=10,bd=5, fg="black",font=('arial',20,'bold'),
            text="M", bg="lavender",command=lambda:btnClick("M")).grid(row=3,column=6)

btnN=Button(root,padx=10,pady=10,bd=5, fg="black",font=('arial',20,'bold'),
            text="N", bg="lavender",command=lambda:btnClick("n")).grid(row=3,column=7)

btnO=Button(root,padx=10,pady=10,bd=5, fg="black",font=('arial',20,'bold'),
            text="O", bg="lavender",command=lambda:btnClick("O")).grid(row=3,column=8)

btnP=Button(root,padx=10,pady=10,bd=5, fg="black",font=('arial',20,'bold'),
            text="P", bg="lavender",command=lambda:btnClick("P")).grid(row=3,column=9)

btnQ=Button(root,padx=10,pady=10,bd=5, fg="black",font=('arial',20,'bold'),
            text="Q", bg="lavender",command=lambda:btnClick("Q")).grid(row=3,column=10)

btnR=Button(root,padx=10,pady=10,bd=5, fg="black",font=('arial',20,'bold'),
            text="R", bg="lavender",command=lambda:btnClick("R")).grid(row=3,column=11)
#---------------------------------------------------------------------------------------------------------------
btns=Button(root,padx=10,pady=10,bd=5, fg="black",font=('arial',20,'bold'),
            text="s", bg="lavender",command=lambda:btnClick("s")).grid(row=4,column=0)

btnt=Button(root,padx=10,pady=10,bd=5, fg="black",font=('arial',20,'bold'),
            text="t", bg="lavender",command=lambda:btnClick("t")).grid(row=4,column=1)

btnu=Button(root,padx=10,pady=10,bd=5, fg="black",font=('arial',20,'bold'),
            text="u", bg="lavender",command=lambda:btnClick("u")).grid(row=4,column=2)

btnv=Button(root,padx=10,pady=10,bd=5, fg="black",font=('arial',20,'bold'),
            text="v", bg="lavender",command=lambda:btnClick("v")).grid(row=4,column=3)

btnw=Button(root,padx=10,pady=10,bd=5, fg="black",font=('arial',20,'bold'),
            text="w", bg="lavender",command=lambda:btnClick("w")).grid(row=4,column=4)

btnx=Button(root,padx=10,pady=10,bd=5, fg="black",font=('arial',20,'bold'),
            text="x", bg="lavender",command=lambda:btnClick("x")).grid(row=4,column=5)
#-------------------------------------------------------------------------------------------------------------------------------------------
btnS=Button(root,padx=10,pady=10,bd=5, fg="black",font=('arial',20,'bold'),
            text="S", bg="lavender",command=lambda:btnClick("S")).grid(row=4,column=6)

btnT=Button(root,padx=10,pady=10,bd=5, fg="black",font=('arial',20,'bold'),
            text="T", bg="lavender",command=lambda:btnClick("T")).grid(row=4,column=7)

btnU=Button(root,padx=10,pady=10,bd=5, fg="black",font=('arial',20,'bold'),
            text="U", bg="lavender",command=lambda:btnClick("U")).grid(row=4,column=8)

btnV=Button(root,padx=10,pady=10,bd=5, fg="black",font=('arial',20,'bold'),
            text="V", bg="lavender",command=lambda:btnClick("V")).grid(row=4,column=9)

btnW=Button(root,padx=10,pady=10,bd=5, fg="black",font=('arial',20,'bold'),
            text="W", bg="lavender",command=lambda:btnClick("W")).grid(row=4,column=10)

btnX=Button(root,padx=10,pady=10,bd=5, fg="black",font=('arial',20,'bold'),
            text="X", bg="lavender",command=lambda:btnClick("X")).grid(row=4,column=11)
#------------------------------------------------------------------------------------------------------------
btny=Button(root,padx=10,pady=10,bd=5, fg="black",font=('arial',20,'bold'),
            text="y", bg="lavender",command=lambda:btnClick("y")).grid(row=5,column=0)

btnz=Button(root,padx=10,pady=10,bd=5, fg="black",font=('arial',20,'bold'),
            text="z", bg="lavender",command=lambda:btnClick("z")).grid(row=5,column=1)
#--------------------------------------------------------------------------------------------------------------------------------------
btnY=Button(root,padx=10,pady=10,bd=5, fg="black",font=('arial',20,'bold'),
            text="Y", bg="lavender",command=lambda:btnClick("Y")).grid(row=5,column=10)

btnZ=Button(root,padx=10,pady=10,bd=5, fg="black",font=('arial',20,'bold'),
            text="Z", bg="lavender",command=lambda:btnClick("Z")).grid(row=5,column=11)
#----------------------------------------------------------------------------------------------------------------------------------------------
btnClear=Button(root,padx=10,pady=10,bd=5, fg="black",font=('arial',20,'bold'),
            text="-", bg="lavender",command=btnClearDisplay).grid(row=5,column=2)
#---------------------------------------------------------------------------------------------------------------------------------------------------
btn_dot=Button(root,padx=10,pady=10,bd=5, fg="black",font=('arial',20,'bold'),
            text=".", bg="lavender",command=lambda:btnClick(".")).grid(row=5,column=3)

btn_question=Button(root,padx=10,pady=10,bd=5, fg="black",font=('arial',20,'bold'),
            text="?", bg="lavender",command=lambda:btnClick("?")).grid(row=5,column=4)

btnspace=Button(root,padx=10,pady=10,bd=5, fg="black",font=('arial',20,'bold'),
            text=" ", bg="lavender",command=lambda:btnClick(" ")).grid(row=5,column=5)
btnColon=Button(root,padx=10,pady=10,bd=5, fg="black",font=('arial',20,'bold'),
            text=":", bg="lavender",command=lambda:btnClick(":")).grid(row=5,column=6)

btn_at=Button(root,padx=10,pady=10,bd=5, fg="black",font=('arial',20,'bold'),
            text="@", bg="lavender",command=lambda:btnClick(" ")).grid(row=5,column=7)

btne_mark=Button(root,padx=10,pady=10,bd=5, fg="black",font=('arial',20,'bold'),
            text=" !", bg="lavender",command=lambda:btnClick("!")).grid(row=5,column=8)

btn_comma=Button(root,padx=10,pady=10,bd=5, fg="black",font=('arial',20,'bold'),
            text=",", bg="lavender",command=lambda:btnClick(",")).grid(row=5,column=9)
























