name = input("Please enter your name: ")
age = int(input("How old are you? {} ".format(name)))

if 18 <= age <= 30:
    print("Welcome to holiday")
else:
    print("you must be older than 18 but not older than 30")