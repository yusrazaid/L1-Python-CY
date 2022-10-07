choice = 0
while(choice != "end"):
    choice=input("Enter 1 for area of triangle \nEnter 2 for area of square \nEnter 3 for area of rectangle \nEnter 4 for area of circle \nEnter 5 for area of parralellogram \nEnter 6 for area of a rhombus \nEnter 7 for volume of cylinder \nEnter 8 for volume of cube\nEnter 9 for volume of cuboid \nEnter 10 for volume of right prism \nEnter 11 for volume right pyramid \nEnter 12 for volume of right circular cone \nEnter 13 for volume of sphere \nEnter 14 for volume of a hemi-sphere \nEnter end to stop the program: ")
    if(choice=="1"):
        b=int(input("Enter the base"))
        h=int(input("Enter the height"))
        area=0.5*b*h
        print("Your answer is",area)
    elif(choice=="2"):
        l=int(input("Enter the length"))
        a=l*l
        print("Your answer is",a)
    elif(choice=="3"):
        base=int(input("Enter the base"))
        height=int(input("Enter the height"))
        arearec=base*height
        print("Your answer is",arearec)
    elif( choice=="4"):
        radius=int(input("Enter the radius"))
        areacirc=3.14*radius**2
        print("Your answer is",areacirc)
    elif(choice=="5"):
        ht=int(input("Enter the height"))
        bs=int(input("Enter the base"))
        areaparr=ht*bs
        print("Your answer is",areaparr)
    elif(choice=="6"):
        length=int(input("Enter the length"))
        arearhom=length**2
        print("Your answer is",arearhom)
    elif(choice=="7"):
        ra=int(input("Enter the radius"))
        hi=int(input("Enter the height"))
        ans=3.14*ra**2*hi
        print("Your answer is",ans)
    elif(choice=="8"):
        ba=int(input("Enter the base"))
        out=ba**3
        print("Your answer is",out)
    elif(choice=="9"):
        hg=int(input("Enter the height"))
        be=int(input("Enter the base"))
        dep=int(input("Ente the depth"))
        output=hg*be*dep
        print("Your answer is",output)
    elif(choice=="10"):
       le=int(input("Enter the length"))
       base1=int(input("Enter the base"))
       d=int(input("Enter the depth"))
       vol=0.5*base1*le*d
       print("Your answer is",vol)
    elif(choice=="11"):
        he=int(input("Enter the height"))
        bse=int(input("Enter the base"))
        depth=int(input("Enter the depth"))
        volume=(1/3)*he*bse*depth
        print("Your answer is",volume)
    elif(choice=="12"):
        bas=int(input("Enter the base"))
        hei=int(input("Enter the height"))
        pyrvol=bas**2*hei*(1/3)
        print("Your answer is",pyrvol)
    elif(choice=="13"):    
        radis=int(input("Enter the radius"))
        sphvol=(4/3)*3.14*radis**3
        print("Your answer is",sphvol)
    elif(choice==14):
        radi=int(input("Enter the radius"))
        hemsphvol=0.5*(4/3)*3.14*radi**3
        print("Your answer is",hemsphvol)
    elif(choice!="end"):
        print("Please enter a valid number")

#This was the first and second question
        


    choicep=input("Enter square for perimeter of a square \nEnter rectangle for perimeter of a rectanle")
if(choicep=="square"):
    side=input("Enter the side length")
    squarep=side*4
    print(squarep)
    print("This was here")
elif(choicep=="rectangle"):
    s1=input("Enter the side1 length")
    s2=input("Enter the side2 length")
    ou=s1+s1+s2+s2



    

    

    
    
    


             

    
 

