import role1,role2
import random
print()
# Introduces and welcomes the user to the game
print("Welcome to the Fairy Land, here you will go through lots of quests and missions."
      "After you pick your character you will start your fun and interesting journey! ")
input("Press ENTER if you are ready to see the given characters: ")

print()
print("The first character that is presented is",role1.name,",he is",role1.age,"years old, and his starting health is",role1.health,"HP.\nHis main atributes are his dexterity",role1.dexterity,"DT","and his strength is",role1.strength,"ST.")
print()
print("The second character that is presented is",role2.name,",he is",role2.age,"years old, and his starting healthh is",role2.health,"HP.\nHis main atribtes are his intelligents",role2.iq,"IQ","and his strength is",role2.strength,"ST.")
print()
continue1=input("Are you ready to continue, if yes press ENTER:" )
print("To pick character",role1.name,"Press \"1\" \nTo pick character",role2.name,"press \"2\"")
print()
status=True
while status==True:
    pickrole=eval(input("After reviewing the charactersistics, what charater would you like to pick? Press 1 or 2: " ))
    if pickrole==1:
        print("You have succesfully picked",role1.name,". If you are lucky, you will be able to increase his strength and dexterity throughout your journey!")
        status=False
        role=role1.name
    elif pickrole==2:
        print("You have succesfully picked",role2.name,". If you are lucky, you will be able to increase his strength and intelligence throughout your journey!")
        status=False
        role=role2.name
    else:
        print("You have to enter either 1 or 2, try again !")
print()