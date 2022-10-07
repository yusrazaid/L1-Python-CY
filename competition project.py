print("GET READY FOR EASTER")
print("In this project you will go shopping in the nearest stores for easter")
ui=int(input("Which of these stores would you like to go to\n1 for Michaels\n2 for Morrison\n3 for Asda"))
print("Great choice time for the next step\nSHOPPING!!!!!")
s=int(input("Grab your shopping cart\n1 for big\n2 for small"))
if ui==1:
    if s==1:
        print("With a big trolley you can buy more")
        input1=input("What would you like to buy?\nWould you like a bunny costume $20 y/n")
    elif s=="2":
        print("With a small trolley you cannot buy as much")
    else:
        print("Error")
elif ui==2:
    if s==1:
        print("With a big trolley you can buy more")
    elif s==2:
        print("With a small trolley you cannot buy as much")
    else:
        print("Error")
elif  ui==3:
    if s==1:
        print("With a big trolley you can buy more")
    elif s==2:
        print("With a small trolley you cannot buy as much")
    else:
        print("Error")
else:
    print("Error")
    

    

