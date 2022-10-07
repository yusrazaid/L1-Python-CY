l=["cat"," mat","sat"]
import random
o=random.choice(l)
print(o)

while True:

    
    if o=="cat":
        word=["_","_","_"]
        u=word[0]="c"
        q=word[1]="a"
        s=word[2]="t"
        i=input("Choose a letter")
        print(i)
        if i=="c":
            print(u,"__")
        elif i=="a":
            print("_",q,"_")
        elif i=="t":
            print("__",s)
        else:
            print("try again")
    elif o=="mat":
        word=["_","_","_"]
        t=word[0]="m"
        a=word[1]="a"
        b=word[2]="t"
        r=input("Choose a letter")
        print(r)
        if r=="c":
            print(t,"__")
        elif r=="a":
            print("_",a,"_")
        elif r=="t":
            print("__",b)
        else:
            print("try again")
  
        
        
        
