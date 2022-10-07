tupl=(5,True,"hi")#packing tuple
(green,red,yellow)=tupl#unpacking tuple
print(red)
print(green)
print(yellow)
tup=(5,True,"hi",4.2)#packing tuple
(pink,purple,*blue)=tup#unpacking tuple but using * to get  the non coresponding values
print(purple)
print(blue)
print(pink)#unpacking tuple
b=(tupl,3)
c=(b,6,"Qwerty")
print(c)#printing a tuple inside of a tuple inside of a tuple
t=("Coding",)#Having only one element in a tuple but for it to work add a comma
l=list(t)
l.append("Is fun")
tu=tuple(l)
print(tu)#Adding something to a tuple by turning it in to a list then back into a tuple
g=(5,6,7,False,"Yusra")
print(g.index(False))#finding the index of something in a tuple
if "Yusra" in g:
    print("YAY!")
else:
    print("Nooooo")#Using conditions to find if something is in a tuple
h=("supercalifragilistic","expialadocious", 1,False,3.3)    
for i in h:
    print(i)#separating tuple with for loop
print(h[2::])

    
   



