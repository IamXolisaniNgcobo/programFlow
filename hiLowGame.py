low = 1
high = 1000

print("Please think of a number between {} and {}".format(low, high))
input("Press enter to start")

guesses = 1
while low != high:
    # print("\tGuessing in the range of {} to {}".format(low, high))
    guess = low + (high - low) // 2
    high_low = input("My guess is {}. Should I guess higher or lower? "
                     "Enter h or l, or c is my guess was correct "
                     .format(guess).casefold())

    if high_low == "h":
        # guess higher. The low end of the range becomes 1 greater than the guess.
        low = guess + 1
    elif high_low == "l":
        high = guess - 1
        # guess lower. The low end of the range becomes one less than the guess
    elif high_low == "c":
        print("I got it in {} guesses!".format(guesses))
        break
    else:
        print("please enter h or l, or c ")

    # guesses = guesses + 1
    guesses += 1
else:
    print("You thought of the number {}".format(low))
    print("i got it in {} guesses".format(guesses))