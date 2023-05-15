weight = float(input("Enter your wight: "))
choice = str.lower(input("(K)g or (L)ib? "))
if choice == "k":
    weight = weight * 2.204623
    print("Your weight in lbs: " + str(int(weight)))
elif choice == "l":
    weight = weight * 0.4535924
    print("Your weight in Kgs: " + str(int(weight)))
else:
    print("Wrong input")
    return