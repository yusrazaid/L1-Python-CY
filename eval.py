x=1
print(eval('x+1'))
import math

num="st"
su=eval()
print(su)
#--------------------------------------
#Lambda
x=lambda j:j/8
print(x(16))

x = lambda a, b, c : a + b + c
print(x(5, 6, 2))

def myfunc(n):
  return lambda a : a * n
mydoubler = myfunc(2)
print(mydoubler(11))

def myfunc(n):
    return lambda a : a * n
mytripler = myfunc(3)
print(mytripler(11))


    
