
choice=input( "To use us please tell us where you live out of these choice \n1for Wokingham,\n2for Redding,\n3 for London" )
if choice=="1":
    sech=input("Here are some resteraunts available\n1 forPizza hut\n2 for Papa Johns\n3  for Zizzi Pizza\n which one would you like?")
    if sech=="1":
        input("Pizza hut Wokingham has 4 star rating and can be contacted at pizzahut@gmail.com\nhere are some of the popular choices choose 1!\n 1 for Cheese Pizza\n2 for Veggie Pizza\n3 for Pepperoni Pizza")
        print("Your bill is $15")
        print("Excellent Choice Thanks for ordering with us enjoy your meal!")
    elif sech=="2":
        input("Papa Johns Wokingham has a 3.5 star rating and can be contacted at papajohnspizza@gmail.com\nhere are some of the popular choices choose1d!\n1 for Chicken Shawarma Pizza\n2 for cheese pizza\n3 for Cheese Mushroom and Pineapple pizza")
        print("Your bill is $12")
        print("Excellent Choice\n  Thanks for ordering with us enjoy your meal!")
    elif sech=="3":
        input("Zizzi pizza Wokingham has a 3 start rating and can be contacted at Zizzi.Pizza@yahoo.com\nhere are some of the options\n1Thin Cheese pizza\n2 for Sun dried tomato pizza\n3 for Pepperoni pizza")
        print("Your bill is $9")
        print("Excellent Choice\n  Thanks for ordering with us enjoy your meal!")
    else:
        print("Error")
elif choice=="2":
    thech=input("Here are some resteraunts available\n1for KFC\n2 for Mc Donalds\n3  for Subway\n which one would you like?")
    if thech=="1":
        input("KFC Redding has a 4.5 star rating and can be contacted at KFC@hotmail.com\nhere are some of the popular choices choose 1!\n3 for Hot wings\n2 for Party Bucket\n3 for Mighty Bucket for one")
        print("Your bill is $10")
        print("Excellent Choice\n  Thanks for ordering with us enjoy your meal!")
    elif thech=="2":
        input("Mc Donalds Redding has a 4.4 star rating and can be contacted at macdonalds@gmail.com\nhere are some of the popular choices\n1 for Big Mac\nVegan Burger\nFilet o Fish burger")
        print("Your bill is $2")
        print("Excellent Choice\n  Thanks for ordering with us enjoy your meal!")
    elif thech=="3":
        input("Subway Redding has a 4 star rating and can be contacted at subwayredding@hotmail.com\nhere are some of the popular choices choose 1!\n1 for a Meaty Cheesy footlong\n2 for Veggie footlong\n3 for Tuna Footlong")
        print("Your bill is $5")
        print("Excellent Choice\n  Thanks for ordering with us enjoy your meal!")
    else:
        print("Error")
elif choice=="3":
    fouech=input("Here are some resteraunts available\n1for Mc Donalds\n2 for Nandos\n3 for Nawabs which one would you like?")
    if fouech=="1":
        input("Mc Donalds London has a 4.5 star rating and can be contacted at macdonalds@gmail.com\nhere are some of the popular choices choose 1!\nDouble beef burger\n Filet o fish burger\nBig Mac")
        print("Your bill is $5")
        print("Excellent Choice\n  Thanks for ordering with us enjoy your meal!")
    elif fouech=="1":
        input("Nandos London has a 4.8 star rating and can be contacted at nandosLondon@gmail.com\nhere are some of the popular choices\n1 for Hot chicken wings\n2 for Grilled chicken leg\n3 for Chicken pita wrap")
        print("Your bill is $11")
        print("Excellent Choice\n  Thanks for ordering with us enjoy your meal!")
    elif fouech=="1":
        input("Nawabs  London has a 4.9 star raating and can be contacted at nawabsbuffet@gmail.com\nhere are some of the popular options\n1 for 1hour stay\n2 for 1 hour 30 mins stay\n3 for 2 hour stay")
        print("Your bill is $50")
        print("Excellent Choice\n  Thanks for ordering with us enjoy your meal!")
    else:
        print("Error")
else:
    print("Error")
    
    
