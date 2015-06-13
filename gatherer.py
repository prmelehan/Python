#!/usr/bin/python

#----------------------------------------------------------#
# A script where you must gather as many items as possible.#
#----------------------------------------------------------#

#Version for Apple Computers
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
    print("inven: shows all items that have been purchased")
    print("bank: shows item count")
    print("survive: uses resources to grow stronger")
    print("store: a store to buy items")
    console()
#Search Function
userItems = 0
userDays = 0
things = {"sword" : 0, "armor" : 0, "wand" : 0, "ruby" : 0, "platinum" : 0, "gold" : 0, "cape" : 0, "puppy" : 0, "pillow" : 0}
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
def inven():
    global things
    print("Inventory: ")
    print("")
    for key, value in things.items():
        print(key + " : " + str(value))
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
    elif(command == "store"):
        store()
    elif(command == "inven"):
        inven()
    elif(command == "quit"):
        exit()
    else:
        print("Command not found. Type -help for a list of commands")
        console()
def searchDict(values, searchFor):
        for v in values:
                if searchFor in v:
                    return True

#Checking if string 'Mary' exists in dictionary value
def store():
    itemsPrices = {"sword" : 30, "armor" : 45, "wand" : 50, "ruby" : 200, "platinum" : 175, "gold" : 180, "cape" : 75, "puppy" : 90, "pillow" : 5}
    itemsArray = ["sword", "armor", "wand", "ruby", "platinum", "gold", "cape", "puppy", "pillow"]
    itemPrompt = input("Store-$: ")
    splicedItems = itemPrompt.split()
    global things
    global userItems
    if(splicedItems[0] == "purchase"):
        item = searchDict(itemsArray, splicedItems[1])
        itemName = splicedItems[1]
        if(item):
            itemCost = itemsPrices[itemName]
            if(userItems >= itemCost):
                things[itemName] += 1
                userItems -= itemCost
                print("Item purchased")
                store()
            else:
                print("You do not have enough items to buy " + itemName +". Cost is " + str(itemCost) + " items")
                store()
        else:
            print ("Item not found. Type ls -a for a list of items")
            store()
    elif(itemPrompt == "ls -a"):
        print("")
        print("List of items that can be bought:")
        print("")
        print("Item  |  Cost")
        print("sword: 30 items")
        print("armor: 45 items")
        print("wand: 50 items")
        print("ruby: 200 items")
        print("platinum: 175 items")
        print("gold: 180 items")
        print("cape: 75 items")
        print("puppy: 90 items")
        print("pillow: 15 items")
        store()
    elif(itemPrompt == "exit"):
        os.system('cls' if os.name == 'nt' else 'clear')
        console()
    else:
        print ("Command not found. Type 'purchase |item to purchase|' ")
        store()
def start():
    os.system('cls' if os.name == 'nt' else 'clear')
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