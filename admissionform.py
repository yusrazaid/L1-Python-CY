start=input("This is the year 11 admission form you can choose\n1for art\n2 for commerce\n3 for science")
if start=="1":
    input("You have chose Art!\nEnter your name: ")
    int(input("Enter your contact"))
    score=int(input("Enter your year 10 percentage: "))
    if score>=90 and score <=100:
        print("You are Eligible to take art your score is very high\n:D")
        print("Your scholarship fees are about $1000")
    elif score>=80 and score<=90:
        print("You are Eligible to take arts your score is good\n:)")
        print("Your scholarship fees are about $1200")
    elif score>=70 and score<=80:
        print("You are Eligible to take art your score is pretty good\n:} ")
        print("Your scholarship fees are about $1500")
    elif score>=60 and score<=70:
        print("You are Eligible to take art your score is ok\n:I")
        print("Your scholarship fees are about $800")
    elif score>=50 and score<=60:
        print("You are Eligible to take art your score is just enough\n:(")
        print("Your scholarship fees are about $1100")
    else:
        print("You are not Eligible to take arts your score is lower than the accepted percentage")
elif start=="2":
    input("You have chose Commerce!\nEnter your name: ")
    int(input("Enter your contact"))
    score=int(input("Enter your year 10 percentage: "))
    if score>=90 and score <=100:
        print("You are Eligible to take commerce your score is very high\n:D")
        print("Your scholarship fees are about $999")
    elif score>=80 and score<=90:
        print("You are Eligible to take commerce your score is good\n:)")
        print("Your scholarship fees are about $1900")
    elif score>=70 and score<=80:
        print("You are Eligible to take commerce your score is pretty good\n:} ")
        print("Your scholarship fees are about $1600")
    elif score>=60 and score<=70:
        print("You are Eligible to take commerce your score is ok\n:I")
        print("Your scholarship fees are about $1000")
    elif score>=50 and score<=60:
        print("You are Eligible to take commerce your score is just enough\n:(")
        print("Your scholarship fees are about $1850")
        
    else:
        print("You are not Eligible to take commerce your score is lower than the accepted percentage")
elif start=="3":
    input("You have chose Science!\nEnter your name: ")
    int(input("Enter your contact"))
    score=int(input("Enter your year 10 percentage: "))
    if score>=90 and score <=100:
        print("You are Eligible to take science your score is very high\n:D")
        print("Your scholarship fees are about $1000")

    elif score>=80 and score<=90:
        print("You are Eligible to take science your score is good\n:)")
        print("Your scholarship fees are about $1500")
    elif score>=70 and score<=80:
        print("You are Eligible to take science your score is pretty good\n:} ")
        print("Your scholarship fees are about $1050")
    elif score>=60 and score<=70:
        print("You are Eligible to take science your score is ok\n:I")
        print("Your scholarship fees are about $2000")
    elif score>=50 and score<=60:
        print("You are Eligible to take science your score is just enough\n:(")
        print("Your scholarship fees are about $600")
        
    else:
        print("You are not Eligible to take science your score is lower than the accepted percentage")
     
else:
    print("Error")
