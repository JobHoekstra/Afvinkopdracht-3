pocketnumber = int(input("Enter a pocket number: "))

if pocketnumber < 0 or pocketnumber > 36:
    print("Error: This is not a valid pocket number.")
elif pocketnumber == 0:
    print("The color of the pocket is green.")
elif pocketnumber <= 10:
    if (pocketnumber % 2) == 0:
        print("The color of the pocket is black.")
    else:
        print("The color of the pocket is red.")
elif pocketnumber >= 11 and pocketnumber <= 18:
    if (pocketnumber % 2) == 0:
        print("The color of the pocket is red.")
    else:
        print("The color of the pocket is black.")
elif pocketnumber >= 19 and pocketnumber <= 28:
    if (pocketnumber % 2) == 0:
        print("The color of the pocket is black.")
    else:
        print("The color of the pocket is red.")
elif pocketnumber >= 29 and pocketnumber <= 36:
    if (pocketnumber % 2) == 0:
        print("The color of the pocket is red.")
    else:
        print("The color of the pocket is black.")
