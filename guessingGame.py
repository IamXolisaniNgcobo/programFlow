answer = 5

print("Please guess number between 1 and 10: ")
guess =int(input())

# if guess != answer:
#     if guess < answer:
#         print("Please guess higher")
#     else: # it must be greater than answer
#         print("Please guess lower")
#     guess = int(input())
#     if guess ==answer:
#         print("Well done, you guessed it.")
#     else:
#         print("Sorry, you have not guessed correctly.")
# else:
#     print("You got it first time.")


# if guess < answer:
#     print("Please guess higher")
#     guess = int(input())
#     if guess == answer:
#         print("Well done, you guessed it")
#     else:
#         print("Sorry, you have not guessed correctly")
# elif guess > answer:
#     print("Please guess lower")
#     guess = int(input())
#     if guess == answer:
#         print("Well done, you guessed it")
#     else:
#         print("Sorry, you have not guessed correctly")
# else:
#     print("You got it first time")

# exercise 1 If statement
# tree1 = "pine"
# tree2 = "gum"
# if tree1 ==tree2:
#     print("The trees are the same")
# else:
#     print("The trees are different      n  ")

# exercise 2
# x = 5
# y = 7
#
# if x > y:
#     print("x is greater than y")
# elif x < y:
#     print("x is smaller than y")
# elif x == y:
#     print("x equals y")

#Exercise 3, start with if guess == answer:

if guess == answer:
    print("You got it first time")
else:
    if guess > answer:
        print("Please guess lower")
    elif guess < answer:
        print("Please guess higher")
    guess =int(input())
    if guess == answer:
        print("Well done, you guessed it")
    else:
        print("Sorry you have not guessed correctly")
