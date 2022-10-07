print("This is Yusra's travel agency\n")
ui=int(input("Select your mode of transport\n\n1 to go by air\n\n2 to go by bus\n\n3 for ferry"))
if ui==1:
    print("You have chosen to go via air")
    print("The cost is 1$ per mile flown")
    travel=int(input("Choose where you would like to go\n\n1 for Redding\n\n2 for Cork\n\n3 for Rome: \n"))
    start=int(input("Choose your set location\n\n1 for Paris\n\n2 for Zurich\n\n3 for Madrid"))
    bne=int(input("Buisness and Economy\n\n1 for Buisness\n2 for Economy"))
    if travel==1 and start==2:
        if bne==1:
            print("The distance between Redding and Zurich is 700 miles")
            print("The total cost is 700 with additional costs for buisness which are 100 so\n800$\n\nEnjoy Your Flight :D")
        elif bne==2:
            print("The distance between Redding and Zurich is 700 miles")
            print("The total cost is 700 with additional costs for economy which are 50 so\n750$\n\nEnjoy Your Flight :D")
        else:
            print("Error")
    elif travel==1 and start==3:
        if  bne==1:
            print("The distance between Redding and Madrid is 1000 miles")
            print("The total cost is 1000 with additional costs for economy which are 100 so\n1100$\n\nEnjoy Your Flight :D")
        elif bne==2:
            print("The distance between Redding and Madrid is 1000 miles")
            print("The total cost is 1000 with additional costs for economy which are 50 so\n1050$\n\nEnjoy Your Flight :D")
        else:
            print("Error")
    elif travel==1 and start==1:
        if bne==1:
            print("The distance between Redding and Paris is 521 miles")
            print("The total cost is 521 with additional costs for buisness which are 100 so\n671$\n\nEnjoy Your Flight :D")
        elif bne==2:
            print("The distance between Redding and Paris is 521 miles")
            print("The total cost is 521 with additional costs for economy which are 50 so\n571$\n\nEnjoy Your Flight :D")
        else:
            print("Error")
    elif travel==2 and start==1:
        if bne==2:
            print("The distance between Cork and Paris is 1171 miles")
            print("The total cost is 1171 with additional costs for economy which are 50 so\n1221$\n\nEnjoy Your Flight :D")
        elif bne==1:
            print("The distance between Cork and Paris is 1171 miles")
            print("The total cost is 1171 with additional costs for buisness which are 100 so\n1271$\n\nEnjoy Your Flight :D")
        else:
            print("Error")
    elif travel==2 and start==2:
        if bne==1:
            print("The distance between Cork and Zurich 1700 miles")
            print("The total cost is  with additional costs for buisness which are 100 so\n1800\n\nEnjoy Your Flight :D")
        elif bne==2:
            print("The distance between Cork and Zurich is 1700 miles")
            print("The total cost is 1700 with additional costs for economy which are 50 so\n1750$\n\nEnjoy Your Flight :D")
        else:
             print("Error")
    elif travel==2 and start==3:
        if  bne==2:
            print("The distance between Cork and Madrid is 1200 miles")
            print("The total cost is 1200 with additional costs for economy which are 50 so\n1250$\n\nEnjoy Your Flight :D")
        elif bne==1:
            print("The distance between Cork and Madrid is 1200 miles")
            print("The total cost is 1200 with additional costs for economy which are 100 so\n1300$\n\nEnjoy Your Flight :D")
        else:
           print("Error")
    elif travel==3 and start==1:
        if  bne==2:
            print("The distance between Rome and Paris is 883 miles")
            print("The total cost is 883 with additional costs for economy which are 50 so\n933$\n\nEnjoy Your Flight :D")
        elif bne==1:
            print("The distance between Rome and Madrid is 883 miles")
            print("The total cost is 883 with additional costs for economy which are 100 so\n983$\n\nEnjoy Your Flight :D")
        else:
            print("Error")
    elif travel==3 and start==2:
        if  bne==1:
            print("The distance between Rome and Zurich is 422 miles")
            print("The total cost is 422 with additional costs for economy which are 100 so\n522$\n\nEnjoy Your Flight :D")
        elif bne==2:
            print("The distance between Rome and Madrid is 600 miles")
            print("The total cost is 422 with additional costs for economy which are 50 so\n472$\n\nEnjoy Your Flight :D")
        else:
            print("Error")
    elif travel==3 and start==3:
        if bne==1:
            print("The distance between Rome and Madrid is 600 miles")
            print("The total cost is 883 with additional costs for buisness which are 100 so\n700$\n\nEnjoy Your Flight :D")
        elif bne==2:
            print("The distance between Rome and Madrid is 600 miles")
            print("The total cost is 600 with additional costs for economy which are 50 so\n650$\n\nEnjoy Your Flight :D")
        else:
            print("Error")

elif ui==2:
    print("You have chosen to go by bus")
    print("The cost is 0.50$ per mile driven")
    travel=int(input("Choose where you would like to go\n\n1 for Redding\n\n2 for Cork\n\n3 for Rome: \n"))
    start=int(input("Choose your set location\n\n1 for Paris\n\n2 for Zurich\n\n3 for Madrid"))
    bne=int(input("Buisness and Economy\n\n1 for Buisness\n2 for Economy"))
    if travel==1 and start==2:
        if  bne==1:
            print("The distance between Redding and Zurich is 700 miles")
            print("The total cost is 350 with additional costs for buisness which are 20 so\n$370\n\nEnjoy Your Ride :D")
        elif bne==2:
            print("The distance between Redding and Zurich is 700 miles")
            print("The total cost is 350 with additional costs for economy which are 10 so\n360$\n\nEnjoy Your Ride :D")
        else:
             print("Error")
    elif travel==1 and start==3:
        if  bne==1:
            print("The distance between Redding and Madrid is 1000 miles")
            print("The total cost is 500 with additional costs for economy which are 20 so\n1020$\n\nEnjoy Your Ride :D")
        elif bne==2:
            print("The distance between Redding and Madrid is 1000 miles")
            print("The total cost is 500 with additional costs for economy which are 10 so\n510$\n\nEnjoy Your Ride :D")
        else:
            print("Error")
    elif travel==1 and start==1:
        if   bne==1:
            print("The distance between Redding and Paris is 521 miles")
            print("The total cost is 260.10 with additional costs for buisness which are 20 so\n280.10$\n\nEnjoy Your Ride :D")
        elif bne==2:
            print("The distance between Redding and Paris is 521 miles")
            print("The total cost is 260.10 with additional costs for economy which are 10 so\n270.10$\n\nEnjoy Your Ride :D")
        else:
            print("Error")
    elif travel==2 and start==1:
        if bne==2:
            print("The distance between Cork and Paris is 1171 miles")
            print("The total cost is 1171 with additional costs for economy which are 50 so\n1221$\n\nEnjoy Your Ride :D")
        elif bne==1:
            print("The distance between Cork and Paris is 1171 miles")
            print("The total cost is 585.50 with additional costs for buisness which are 20 so\n$605.50\n\nEnjoy Your Ride :D")
        else:
            print("Error")
    elif travel==2 and start==2:
        if bne==1:
            print("The distance between Cork and Zurich 1700 miles")
            print("The total cost is 850 with additional costs for buisness which are 20 so\n$870\n\nEnjoy Your Ride:D")
        elif bne==2:
            print("The distance between Cork and Zurich is 1700 miles")
            print("The total cost is 850 with additional costs for economy which are 10 so\860$\n\nEnjoy Your Ride :D")
        else:
            print("Error")
    elif travel==2 and start==3:
        if bne==2:
            print("The distance between Cork and Madrid is 1200 miles")
            print("The total cost is 600 with additional costs for economy which are 10 so\n610$\n\nEnjoy Your Ride:D")
        elif bne==1:
            print("The distance between Cork and Madrid is 1200 miles")
            print("The total cost is 600 with additional costs for economy which are 20 so\n620$\n\nEnjoy Your Ride :D")
        else:
            print("Error")
    elif travel==3 and start==1:
        if bne==2:
            print("The distance between Rome and Paris is 883 miles")
            print("The total cost is 441.50 with additional costs for economy which are 10 so\n451.50$\n\nEnjoy Your Ride :D")
        elif bne==1:
            print("The distance between Rome and Madrid is 883 miles")
            print("The total cost is 441.50 with additional costs for buisness which are 20 so\n461.50$\n\nEnjoy Your Ride :D")
        else:
            print("Error")
    elif travel==3 and start==2:
        if bne==1:
            print("The distance between Rome and Zurich is 422 miles")
            print("The total cost is 422 with additional costs for buisness which are 100 so\n522$\n\nEnjoy Your Ride :D")
        elif bne==2:
            print("The distance between Rome and Madrid is 600 miles")
            print("The total cost is 422 with additional costs for economy which are 50 so\n472$\n\nEnjoy Your Ride :D")
        else:
            print("Error")
    elif travel==3 and start==3:
        if bne==2:
            print("The distance between Rome and Madrid is 600 miles")
            print("The total cost is 300 with additional costs for economy which are 10 so\n310$\n\nEnjoy Your Ride :D")
        elif bne==1:
            print("The distance between Rome and Madrid is 600 miles")
            print("The total cost is 300 with additional costs for buisness which are 100 so\n320$\n\nEnjoy Your Ride :D")
        else:
            print("Error")


elif ui==3:
    print("You have chosen to go by Ferry")
    print("The cost is 0.50$ per mile traveled")
    travel=int(input("Choose where you would like to go\n\n1 for Redding\n\n2 for Cork\n\n3 for Rome: \n"))
    start=int(input("Choose your set location\n\n1 for Paris\n\n2 for Zurich\n\n3 for Madrid"))
    bne=int(input("Buisness and Economy\n\n1 for Buisness\n2 for Economy"))
    if travel==1 and start==2:
        if bne==1:
            print("The distance between Redding and Zurich is 700 miles")
            print("The total cost is 350 with additional costs for buisness which are 120 so\n$470\n\nEnjoy Your Ride :D")
        elif bne==2:
            print("The distance between Redding and Zurich is 700 miles")
            print("The total cost is 350 with additional costs for economy which are 70 so\n420$\n\nEnjoy Your Ride :D")
    elif travel==1 and start==3:
        if bne==1:
            print("The distance between Redding and Madrid is 1000 miles")
            print("The total cost is 500 with additional costs for economy which are 120 so\n620$\n\nEnjoy Your Ride :D")
        elif bne==2:
            print("The distance between Redding and Madrid is 1000 miles")
            print("The total cost is 500 with additional costs for economy which are 70 so\n570$\n\nEnjoy Your Ride :D")
        else:
           print("Error")
    elif travel==1 and start==1:
        if bne==1:
            print("The distance between Redding and Paris is 521 miles")
            print("The total cost is 260.10 with additional costs for buisness which are 20 so\n280.10$\n\nEnjoy Your Ride :D")
        elif bne==2:
            print("The distance between Redding and Paris is 521 miles")
            print("The total cost is 260.10 with additional costs for economy which are 10 so\n270.10$\n\nEnjoy Your Ride :D")
        else:
           print("Error")
    elif travel==2 and start==1:
        if bne==2:
            print("The distance between Cork and Paris is 1171 miles")
            print("The total cost is 1171 with additional costs for economy which are 70 so\n1221$\n\nEnjoy Your Ride :D")
        elif bne==1:
            print("The distance between Cork and Paris is 1171 miles")
            print("The total cost is 585.50 with additional costs for buisness which are 120 so\n$705.50\n\nEnjoy Your Ride :D")
        else:
            print("Error")
    elif travel==2 and start==2:
        if bne==1:
            print("The distance between Cork and Zurich 1700 miles")
            print("The total cost is 850 with additional costs for buisness which are 120 so\n970$\n\nEnjoy Your Ride:D")
        elif bne==2:
            print("The distance between Cork and Zurich is 1700 miles")
            print("The total cost is 850 with additional costs for economy which are 70 so\920$\n\nEnjoy Your Ride :D")
        else:
            print("Error")
    elif travel==2 and start==3:
        if bne==2:
            print("The distance between Cork and Madrid is 1200 miles")
            print("The total cost is 600 with additional costs for economy which are 70 so\n670$\n\nEnjoy Your Ride:D")
        elif bne==1:
            print("The distance between Cork and Madrid is 1200 miles")
            print("The total cost is 600 with additional costs for buisness which are 120 so\n720$\n\nEnjoy Your Ride :D")
        else:
            print("Error")
    elif travel==3 and start==1:
        if bne==2:
            print("The distance between Rome and Paris is 883 miles")
            print("The total cost is 441.50 with additional costs for economy which are 70 so\n511.50$\n\nEnjoy Your Ride :D")
        elif bne==1:
            print("The distance between Rome and Madrid is 883 miles")
            print("The total cost is 441.50 with additional costs for buisness which are 70 so\n561.50$\n\nEnjoy Your Ride :D")
        else:
            print("Error")
    elif travel==3 and start==2:
        if bne==1:
            print("The distance between Rome and Zurich is 422 miles")
            print("The total cost is 422 with additional costs for buisness which are 120 so\n442$\n\nEnjoy Your Ride :D")
        elif bne==2:
            print("The distance between Rome and Madrid is 600 miles")
            print("The total cost is 422 with additional costs for economy which are 70 so\n492$\n\nEnjoy Your Ride :D")
        else:
           print("Error")
    elif travel==3 and start==3:
        if bne==2:
            print("The distance between Rome and Madrid is 600 miles")
            print("The total cost is 300 with additional costs for economy which are 70 so\n370$\n\nEnjoy Your Ride :D")
        elif bne==1:
            print("The distance between Rome and Madrid is 600 miles")
            print("The total cost is 300 with additional costs for buisness which are 120 so\n420$\n\nEnjoy Your Ride")
        else :
            print("Error")
    else:
        print("Error")

else:
    print("Error")
    


   
           


        
           
