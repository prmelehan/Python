#!/usr/bin/python

#----------------------------------------------------------#
# A script where you must gather as many items as possible.#
#----------------------------------------------------------#
import sys
import math
import os
from random import randint
from time import sleep
# help list
def helpList():
    print("-help: get commands")
    print("search: searches a random biome for materials")
    print("-version: gets game version")
    print("-pversion: gets python version")
    print("survive: uses resources to grow stronger")
    console()
#Search Function
userItems = 0
userDays = 0
def survive():
    global userDays
    global userItems
    if(userItems >= 25):
        userItems -= 25
        userDays += 1
        print("You added a day to your survival time")
        console()
    else:
        print("You do not have enough items to add a day to your survival. 25 minimum")
        console()
def search():
    biomeNames = ["Forrest", "Mountains", "Rainforrest", "Plains", "Arctic"]
    biome_assoc = {"Forrest" : 3, "Mountains" : 4, "Rainforrest" : 7, "Plains" : 6, "Arctic" : 2}
    randINT = randint(0, 4)
    biome_num = biomeNames[randINT]
    biome_result = biome_assoc[biome_num]
    waitTime = randint(1, 100)
    maxAmountNum = math.pow(biome_result, 2)
    itemAmount = randint(1, maxAmountNum)
    print("Searching the " + biome_num + "...")
    sleep(waitTime)
    print("You found " + str(itemAmount) + " items!")
    global userItems
    userItems += itemAmount
    console()
#Console prompt function
def bank():
    global userItems
    print("You have "+ str(userItems) + " items!" )
    console()
def console():
    version = "1.0"
    command = input("Gatherer-$: ")
    
    if(command == "-pversion"):
        print (sys.version)
        console()
    elif(command == "-version"):
        print (version)
        console()
    elif(command == "search"):
        search()
    elif(command == "-help"):
        helpList()
    elif(command == "bank"):
        bank()
    elif(command == "survive"):
        survive()
    elif(command == "quit"):
        exit()
    else:
        print("Command not found. Type -help for a list of commands")
        console()

def start():
    os.system('clear')
    print("Welcome to gatherer...")
    prompt = input("Press enter to play: ")
    if(prompt == ""):
        print("  ")
        print("To play gatherer, you collect items you find in the world to kill animals and survive.")
        print("  ")
        print("To start searching, type in the console 'search'.")
        print("Searching will search a random biome and grab items it finds")
        print("Collect enough items before you die by the animals of the Night.")
        print("  ")
        print("If at anytime you need help, type '-help' for a list of commands. ")
        startBool = input("Press Enter to start: ")
        if(startBool == ""):
            console()
        else:
            exit()
    else:
        exit()
        
start()