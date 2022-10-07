import random
num = random. randint(1, 20)
turns=10
guess=None
failed=0
while turns<10:
    failed=0
    guess=int(input("guess a number between 1 and 20: "))
    guess = int(guess)
if guess == num:
    print("congratulations!")
elif num!=guess:
    failed+=1
elif failed==turns:
    print("You lost")
else:
    print("Error")
        
        
    
        
