#imports
import random
import math
from random import seed
from random import randint

def game():
    print("Welcome to the random number game!\nThe point of the game is to guess a random number that has been selected previously.")
    num = randint(0, 10)
    print("A random integer from 1 to 10 has been selected.")
    answer = input("What number do you think it is? ")
    if num == answer:
        print("Correct!")
    else:
        print("Incorrect. The answer was " + str(num))

game()