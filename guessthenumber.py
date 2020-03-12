#imports
import random
import math
from random import seed
from random import randint

def changelog():
    print("Version 1.2:")
    print(" - Added ability to choose upper and lower bounds (integers only).")

def game():
    num1 = input("What is the lower bound integer to be used? ")
    num2 = input("What is the upper bound integer to be used? ")
    num = randint(int(num1), int(num2))
    print("A random integer from " + num1 + " to " + num2 + " has been selected.")
    answer = int(input("What number do you think it is? "))
    if num == answer:
        print("Correct! The answer was " + str(num))
    else:
        print("Incorrect. The answer was " + str(num))
    again = input("Do you want to play again? Y or N ").lower()
    if again == "y":
        game()
    else:
        print("OK, Goodbye!")
        quit()

def isready():
    ready = input("Are you ready? Y or N ").lower()
    if ready == "y":
        game()
    elif ready == "n":
        print("OK, Goodbye!")
        quit()
    else:
        print("I'm not sure I understand...")
        isready()

print("Welcome to the random number game! v1.1\nThe point of the game is to guess a random number that has been selected previously.")
changes = input("Do you want to see the changelog? Y or N: ").lower()
if changes == "y":
    changelog()
isready()
print("OK, Goodbye!")
quit()
