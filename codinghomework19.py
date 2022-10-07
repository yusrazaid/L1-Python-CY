num=int(input("Enter a number: "))
numm=int(input("Enter a number: "))
def subtraction(num,numm):
    minus=num-numm
    return minus
def addition(num,numm):
    add=num+numm
    return add
def multiplication(num,numm):
    product=num*numm
    return product
def division(num,numm):
    quotient=num/numm
    return quotient
o=input("Enter your operation: ")
print(o)
if(o=="addition"):
    print("Your sum is",addition(num,numm))
elif(o=="subtraction"):
    print("Your difference is",subtraction(num,numm))
elif(o=="multiplication"):
    print("Your product is",multiplication(num,numm))
elif(o=="division"):
    print("Your quotient is",division(num,numm))
else:
    print("Error")

num1=int(input("Enter a number: "))
num2=int(input("Enter a number to subtract by the first: "))
def subtraction(num1,num2):
    minus=num1-num2
    return minus
print("The subtraction of 2 numbers",subtraction(num1,num2))

        
    





