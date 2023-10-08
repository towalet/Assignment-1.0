import role1,role2,game
import random
print()

# Introduces and welcomes the user to the game
print("Welcome to the Fairy Land, here you will go through 3 fun and interesting quests."
      " After you pick your character you will start your fun and interesting journey! ")
print("To win the game you will have to win at least 2 quests out of the 3.")
print()
input("Press ENTER if you are ready to see the given characters: ")

print()
print("The first character that is presented is",role1.name,", he is",role1.age,"years old, and his starting health is",role1.health,"HP.\nHis main atributes are his dexterity",role1.dexterity,"DT","and his strength is",role1.strength,"ST.")
print()
print("The second character that is presented is",role2.name,", he is",role2.age,"years old, and his starting healthh is",role2.health,"HP.\nHis main atribtes are his intelligents",role2.iq,"IQ","and his strength is",role2.strength,"ST.")
print()
continue1=input("Are you ready to continue, if yes press ENTER:" )
print("To pick character",role1.name,"Press \"1\" \nTo pick character",role2.name,"press \"2\"")
print()
status=True
pickrole=eval(input("After reviewing the charactersistics, what charater would you like to pick? Press 1 or 2: " ))
print()
while status==True:
    if pickrole==1:
        print("You have succesfully picked",role1.name,". You will be able to use his strength and dexterity to succeed throughout your journey!")
        status=False
        break
    elif pickrole==2:
        print("You have succesfully picked",role2.name,". You will be able to use his strength and intelligence to succeed throughout your journey!")
        status=False
        break
    else:
        print("You have to enter either 1 or 2, try again !")
        pickrole=eval(input("Enter 1 or 2 to pick character: "))
print()

# Quest 1
gamestat1=True
while gamestat1==True:
    if pickrole==1:
        game.game1role1()
        gamestat1==False
        break
    elif pickrole==2:
        game.game1role2()
        gamestat1==False
        break
    else: print("Pick 1 or 2 to continue! ")
print()
# Quest 2
gamestat1=True
while gamestat1==True:
    if pickrole==1:
        game.game2role1()
        gamestat1=False
        break
    elif pickrole==2:
        game.game2role2()
        gamestat1=False
        break

# Quest 3 
gamestat1=True
while gamestat1==True:
    if pickrole==1:
        game.quest3role1()
        gamestat1=False
        break
    elif pickrole==2:
        game.quest3role2()
        gamestat1=False
        break
print()

if pickrole==1:
    game.role1win()
elif pickrole==2:
    game.role2win()