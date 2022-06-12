import random
from math import trunc
from random import randint
import time
import keyboard

letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]


def titleScreen():
    choice = input("How fast can you press a letter on your keyboard?   1) Go")
    if choice == "1":
        press()


def press():
    global letters
    print("-------------------------------------------------------------------")
    letter = random.choice(letters)
    print("Quick press the " + letter + " key!!!")
    playerCount = 0
    timeStart = time.time()
    ispress = False
    while not ispress:
        if keyboard.is_pressed(letter):
            ispress = True

    timeEnd = time.time()

    timeSpent = timeEnd - timeStart
    timeConvertToMakePretty(timeSpent)


def timeConvertToMakePretty(time):

    print("-------------------------------------------------------------------")
    print("Time Lasped: "  + str(round(time, 2)) + " seconds")
    titleScreen()


titleScreen()
