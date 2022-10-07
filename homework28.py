from time import sleep
for i in range(11): 
    print(i) 
    sleep(1)
ui=int(input("Enter a year and this program will tell if it is a leap year"))
if ui%400==0:
    print("It is a leap year")
elif ui%100==0:
    print("It is a leap year")
elif ui%4==0:
    print("It is a leap year")
else:
    print("It is not  leap year")
import math
print(math.sqrt(81))
print(math.pow(2,3))
print(math.ceil(2.3))
print(math.floor(6.8))
import random
print(random.randint(1,6))
choice=["a","b","c"]
print(random.choice(choice))
