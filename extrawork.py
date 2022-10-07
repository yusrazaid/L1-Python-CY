num = int(input("Enter a number: "))  
  
if num < 0:  
   print("Enter a positive number")  
else:  
   sum = 0   
   while(num > 0):  
       sum += num
       num -= 1  
   print("The sum is",sum)
######################################
n=int(input("Enter a number"))
ans=bin(n)
print(ans)
##############################################this is the binary conversion
nu=int(input("enter a number"))
anser=oct(nu)
print(anser)
########################################this is the octal conversion
number=int(input("Enter a number"))
answer=hex(number)
print(answer)
####################################################
l=list(input("Enter a list"))
if len(l)==0:
    print("Your list is empty")
else:
    print("Your list has something in it")############checking if a list has something in it
for i in range(1,8):
   for j in range(1,9):
      print("*",end="")
   print()   
    
           

  



    

    
