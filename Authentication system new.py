password=["yusramaira"]
username=["Yusra"]

while True:  
    print("Hi my name is Yusra and this is my authentication system")
    wusername=input("What is your username?: ").strip().capitalize()
    npassword=input("What is your password?: ")
    if((wusername in username) and (npassword in password)):
        print("Hello {}".format(username))
        change=input("Would you like to change your password  ? (y/n)").strip().lower()
        if change=="y":
                np= input("Enter your new password: ")
                password[0]=np
                print("Your password has successfully changed")
        elif(change=="n"):
                print("No problem there will be no further changes to your pre existing account")
        elif np>=8:
                print("You are all good to go your password has been re set")
        else:
                print("Error")
    else:
        print("Error")
    
