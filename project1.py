print("This is Yusra's travel agency")
i=int(input("Select your mode of transport\n1 to go by air\n2 to go by bus\n3 for ferry"))
if i ==1:
    print("You have chosen to go by aeroplane")
    print("The cost 1$ per mile flown")
    
    inp=int(input("Choose where you would like to go?\n 1 for Redding\n2 for Cork\n3 for Rome"))
    inpu=int(input("Choose your set location\n3 for Redding\n4 for Cork\n5 for Rome"))
    print("Buisness and Economy")
    c=int(input("1 for Buisness\n2 for Economy"))
    if c==1:
        b=100
        print(500+5,"and additional costs for buisness which are",b)
    elif c==2:
        e=50
        print(500+5,"and additional costs for economy which are",e)
    if (inp==3 and inpu==4) or (inp==5) and (inpu==2):
        print("The distance between Cork and Rome is 500 miles")
    elif (inp==1 and inpu==4):
        print("The distance between Cork and Redding is 150 miles")
    if c==1:
        print(150+0.15,"and additionall costs for buisness which are",b)
        print("So the total cost is",150+b+0.15)
    elif c==2:
        print(150+0.15,"and additionall costs for economy which are",e)
        print("So the total cost is",150+e+0.15)
    elif (inp==2) and (inpu==3):
        print("The distance between Cork and Redding is 150 miles")
    if c==1:
        print(150+0.15,"and additionall costs for buisness which are",b)
        print("So the total cost is",150+b+0.15)
    elif c==2:
        print(150+0.15,"and additionall costs for economy which are",e)
        print("So the total cost is",150+e+0.15)
    elif (inp==2) and (inpu==3):
            print("The distance between Cork and Redding is 150 miles")
    if c==1:
        print(150+0.15,"and additionall costs for buisness which are",b)
        print("So the total cost is",150+b+0.15)
    elif c==2:
        print(150+0.15,"and additionall costs for economy which are",e)
        print("So the total cost is",150+e+0.15)
           
        
elif i==2:
    print("You have chosen to go by bus")
    print("The fare is 10 cents per mile")

    T=int(input("Choose where you would like to go?\n 1 for Redding\n2 for Cork\n3 for Rome"))
    y=int(input("Choose your set location\n3 for Redding\n4 for Cork\n5 for Rome"))
    
elif i==3:
    print("You have chosen to go by ferry")
    print("The price is 50 cents per mile")
else:
    print("Error")
    
    
    
