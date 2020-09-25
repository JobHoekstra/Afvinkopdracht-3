print("If your answer to a question is yes, type \"yes\"." "\n" "And if your answer is no, type \"no\".")

vegetarian = input("Is anyone in your party a vegetarian? ")
vegan = input("Is anyone in your party a vegan? ")
gluten_free = input("Is anyone in your party gluten-free? ")

res1 = "Joe's Gourmet Burgers"
res2 = "Main Street Pizza Company"
res3 = "Corner Café"
res4 = "Mama's Fine Italian"
res5 = "The Chef's Kitchen"


print("Here are your restaurant choices:")
if vegetarian == "yes":
    if vegan == "yes":
        if gluten_free == "yes":
            print(res3)
            print(res5)
        else:
            print(res3)
            print(res5)
    else:
        if gluten_free == "yes":
            print(res2)
            print(res3)
            print(res5)
        else:
            print(res2)
            print(res3)
            print(res4)
            print(res5)
else:
    if vegan == "yes":
        if gluten_free == "yes":
            print(res3)
            print(res5)
        else:
            print(res3)
            print(res5)
    else:
        if gluten_free == "yes":
            print(res2)
            print(res3)
            print(res5)
        else:
            print(res1)
            print(res2)
            print(res3)
            print(res4)
            print(res5)
