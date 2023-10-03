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