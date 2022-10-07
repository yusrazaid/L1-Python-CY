#Ask user for name

name=input("What is your name?: ")

#Ask user for age

age=input("How old are you?: ")

#Ask user for city
city=input("What city do you live in?: ")

#Ask user what they enjoy
hobby=input("What is your hobby?: ")

#Create output text

string=('Your name is {} and you are {} years old.You live in {} and your hobby is {}')
output=string.format(name,age,city,hobby)

#Print output to screen
print(output)
