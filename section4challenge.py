choice = "-"

while choice != "0":

    if choice in "12345":
        print("You chose {}".format(choice))
    else:
        print("Please choose a language from the list below:")
        print("1:\t C#")
        print("2:\t C++")
        print("3:\t C")
        print("4:\t Java")
        print("5:\t Python")
        print("0:\t Extension")
    choice = input()
