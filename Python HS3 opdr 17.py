print("In case of a bad Wi-Fi connection, follow the upcoming steps:")
print("Reboot the computer and try to connect.")
answer = input("Did that fix the problem? yes/no ")
if answer == "yes":
    print("You're all set.")
if answer == "no":
    print("Reboot the router and try to connect.")
if answer == "no":
    answer = input("Did that fix the problem? yes/no ")
    if answer == "yes":
        print("You're all set.")
if answer == "no":
    print("Make sure the cables between the router & modem are plugged in firmly.")
if answer == "no":
    answer = input("Did that fix the problem? yes/no ")
    if answer == "yes":
        print("You're all set.")
if answer == "no":
    print ("Move the router to a new location and try to connect.")
if answer == "no":
    answer = input("Did that fix the problem? yes/no ")
    if answer == "yes":
        print("You're all set.")
if answer == "no":
    print("Get a new router.")
