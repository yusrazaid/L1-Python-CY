import math
test_num=float(input("Enter a decimal"))
print("The value of your number rounded up is",math.ceil(test_num))
print("The value of your number rounded down is",math.floor(test_num))
print(math.sqrt(625))
print(math.pow(3,3))
print(math.radians(90))           
print(math.remainder(25,4))

n=int(input("Hello and we are US Bank and we use simple interest Enter the number of dollars/pounds you would like to save in the bank our rate is 10% interest annually"))
t=int(input("Enter the number of years you would like to keep it in the bank"))
A= n*(1+t*1/10)
print(A)

num=int(input("Enter how much you want to save in US Bank our rate is 10% annually"))
time=int(input("Enter how many years would you like to keep your money here"))
r=0.1
a=num*(1+r/100)*time
print(a)
