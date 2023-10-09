'''
Anthony Vydysh
PROG10004 Programming Principles
Due Date: 10/10/2023

This module implements the interactivity with the user'''

import role1,role2,game
import random
print()

# Introduces and welcomes the user to the game
print("Welcome to the \"Fairy Land\", here you will go through 3 fun and interesting quests."
      "\nAfter you pick your character you will start your fun and interesting journey! ")
print("To win the game you will have to win at least 2 quests out of the 3.")
print()
input("Press ENTER if you are ready to see the given characters: ")

print()
# The first roles name, age and atributes are presented to the user 
print("The first character that is presented is",role1.name,", he is",role1.age,"years old, and his starting health is",role1.health,"HP.\nHis main atributes are his dexterity",role1.dexterity,"DT","and his strength is",role1.strength,"ST.")
print()
# The second roles name, age and atributes are presented to the user 
print("The second character that is presented is",role2.name,", he is",role2.age,"years old, and his starting healthh is",role2.health,"HP.\nHis main atribtes are his intelligents",role2.iq,"IQ","and his strength is",role2.strength,"ST.")
print()
input("Are you ready to continue, if yes press ENTER:" )
print("To pick character",role1.name,"Press \"1\" \nTo pick character",role2.name,"press \"2\"")
print()
status=True
# Lets the user to pick a role they liked they can press 1 for role 1 and 2 for role 2
pickrole=eval(input("After reviewing the charactersistics, what charater would you like to pick? Press 1 or 2: " ))
print()
while status==True:
    # if user picked role 1, then the role is presented
    if pickrole==1:
        print("You have succesfully picked",role1.name,". You will be able to use his strength and dexterity to succeed throughout your journey!")
        status=False 
        break # Breaks the loop
    # if user picked role 2, then the role is presented
    elif pickrole==2:
        print("You have succesfully picked",role2.name,". You will be able to use his strength and intelligence to succeed throughout your journey!")
        status=False
        break # Breaks the loop 
    # If the user didnt pick either get the opportunity to try again
    else:
        print("You have to enter either 1 or 2, try again !")
        pickrole=eval(input("Enter 1 or 2 to pick character: "))
print()

# Quest 1
gamestat1=True
while gamestat1==True:
    # If role 1 was picked plays game for role1
    if pickrole==1:
        game.game1role1()
        gamestat1==False
        break
    # If role 2 was picked plays game for role2
    elif pickrole==2:
        game.game1role2()
        gamestat1==False
        break
    else: print("Pick 1 or 2 to continue! ")
print()
# Quest 2
gamestat1=True
while gamestat1==True:
    # If role 1 was picked plays game 2 for role1
    if pickrole==1:
        game.game2role1()
        gamestat1=False
        break
    # If role 2 was picked plays game 2 for role2
    elif pickrole==2:
        game.game2role2()
        gamestat1=False
        break

# Quest 3 
gamestat1=True
while gamestat1==True:
    # If role 1 was picked plays game 3 for role1
    if pickrole==1:
        game.quest3role1()
        gamestat1=False
        break
    # If role 2 was picked plays game 3 for role2
    elif pickrole==2:
        game.quest3role2()
        gamestat1=False
        break
print()
# Presentation of the winner
# If role 1 had the most wins the imported code will play
if pickrole==1:
    game.role1win()
# If role 2 had the most wins the imported code will play
elif pickrole==2:
    game.role2win()