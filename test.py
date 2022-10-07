l=[-1,56,9,-2,8,7]
for i in l:
    if i>0:
        print(i)
    else:
       continue
############
t=(1,4,"hi",8.9,5,True)
l=list(t)
l.append(11)
o=tuple(l)
print(o)
print(type(o))
###########
p=[1,8,9,33,57,6,84,9]
for j in p:
    if j%2==0:
        print(j+1)
    else:
        print(j+1)
###############
A={19,34,56,7}
B={1,2,5,19,34,7}
print(A.union(B))
print(A.intersection(B))




       

        
        
