number = int(input("Enter an integer: "))

if number > 0:
    print("Positive")
elif number < 0:
    print("Negative")
elif number == 0:
    print("Zero")

if (number % 2) == 0:
    print(str(number) + " is an even number.")
else:
    print(str(number) + " is an odd number.")
