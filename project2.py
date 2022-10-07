print("Hello Play Rock Paper Scissors")
print("These are the Rules:\nrock vs paper paper wins\nrock vs scissor rock wins\npaper vs scissor scissor win.")
p1=int(input("Choose(You are Player1)\n1 for Rock\n2 for Paper\n3 for Scissors"))
p2=int(input("Choose(You are Player2)\n1 for Rock\n2 for Paper\n3 for Scissors"))
if (p1==1) and (p2==3):
    print("Player1 Wins Rock smashes Scissors")
elif (p1==3) and (p2==1):
    print("Player2 Wins Rock smashes Scissors")   
elif (p1== 2) and (p2==3) :
    print("Player2 Wins Scissors cuts Paper")
elif (p1==3) and (p1==2):
    print("Player1 Wins Scissors cuts Paper")
elif (p1==2) and (p2==1):
    print("Player1 Wins Paper covers Rock")
elif (p1==1) and (p2==2):
    print("Player2 Wins Paper covers Rock")              
else:
    print("Error")
