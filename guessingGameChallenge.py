import random

highest =1000
answer = random.randint(1, highest)
print(answer)   #TODO: remove after testing
guess = 0   # initialise to any number that is not equal to answer
print("Please guess number between 1 and {}: ".format(highest))

while guess != answer:
    guess =int(input())
    if guess == 0:
        print("Game over!")
        break
    if guess == answer:
        print("Well done, you guessed it")
        break
    else:
        if guess > answer:
            print("Please guess lower")
        elif guess < answer:
            print("Please guess higher")
        guess =int(input())
        # if guess == answer:
        #     print("Well done, you guessed it")
        # else:
        #     print("Sorry you have not guessed correctly")