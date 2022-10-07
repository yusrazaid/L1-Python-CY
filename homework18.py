input1=int(input("Enter the temprature in faraneight for the conversion to celsius"))
c=(5*(input1-32))/9
print(c)
colors={
    "sunset":
    {
        1:"red",
        2:"orange",
        3:"yellow",
     },
    "ocean":
    {
        4:"green",
        5:"blue",
        6:"purple",
}   
}       
print(colors)

l=[1,2,3,4,5,6,7,8]
it=iter(l)
d=dict(zip(it,it))
print(d)

a=6
b=8
t=a
a=b
b=t
print(a,b)


