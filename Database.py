
students={
         "Alice":{"id":"ID001","age":26,"grade":"A"},
         "Bob":{"id":"ID002","age":27,"grade":"B"},
         "Claire":{"id":"ID003","age":17,"grade":"C"},
         "Dan":{"id":"ID004","age":21,"grade":"D"},
         "Emma":{"id":"ID005","age":22,"grade":"E"}
         }

print(students)
i=(input("Enter the student you would like the name of"))
if(i=="Alice"or i=="alice"):
    print(students["Alice"])
elif(i=="Bob" or i=="bob"):
    print(students["Bob"])
elif(i=="Claire"or i=="claire"):
    print(students["Claire"])
elif(i=="Dan" or i=="dan"):
    print(students["Dan"])
else:
    print(students["Emma"])

    

              
         
