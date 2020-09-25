length1 = float(input("What length does rectangle 1 have? "))
width1 = float(input("What width does rectangle 1 have? "))
length2 = float(input("What length does rectangle 2 have? "))
width2 = float(input("What width does rectangle 2 have? "))

area_rectangle1 = length1 * width1
area_rectangle2 = length2 * width2

if area_rectangle1 > area_rectangle2:
    print("The area of rectangle 1 is larger than the area of rectangle 2.")
elif area_rectangle1 < area_rectangle2:
    print("The area of rectangle 2 is larger than the area of rectangle 1.")
else:
    print("The areas of both rectangles are equal.")
