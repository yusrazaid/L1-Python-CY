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
o=input("Enter your operation\n1 for addition\n2 for subtraction\n3 for multiplication\n4 for division ")
print(o)
if(o=="1"):
    print("Your sum is",addition(num,numm))
elif(o=="2"):
    print("Your difference is",subtraction(num,numm))
elif(o=="3"):
    print("Your product is",multiplication(num,numm))
elif(o=="4"):
    print("Your quotient is",division(num,numm))
else:
    print("Error run again")

def mt(num):
    for i in range(1,11):
        print(num,"X",i,"=",(num*i))
n=int(input("Enter a number you would like to find the multiplication of"))
mt(n)

def evenORodd(nu):
    if nu%2==0:
        print("even")
    else:
        print("odd")
input1=int(input("Enter a number to determine if it is even or odd"))
evenORodd(input1)
s=input("Enter a text")
out=s[::-1]
if out==s:
    print("Your text is palindromic")
else:
    print("Your text is not")
l=[1,3,594,8692,1,9,7]
"""def countFactors(i):
    factor=1
    count=0
    for i in l:
        while factor<=i:
            if i%factor==0:
                count+=1
            factor+=1
    return count
print(countFactors(l))

inputfirst=int(input("Enter a number and see if it is prime!"))
while factor<=i:
            if i%factor==0:
                count+=1
            factor+=1
            return count
if count==2:
    print("Your number is prime!")
else:
    print("Your number is not prime")"""



