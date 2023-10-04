import role1,role2
import random

# START OF QUEST

# Mission 1

# Statement shows the characters HP and a quick description of the fist mission
def game1role1():
    tries=3
    print(role1.name,"has spawned in a field full of apple trees, you have to eat 3 apples,\n each apple can randomly take or give you HP the player that has the most HP will win.")
    while tries>0:
        print()
        input("Press [ENTER] to eat an apple: ")
        apple=random.randint(-2,2)
        apple2=random.randint(-2,2)
        print("Before eating the apple your health is",role1.health,"HP")
        role1.health=role1.health-apple
        print("After you ate an apple your health has became", role1.health,"HP")
        role2.health=role2.health-apple2
        print("And",role2.name,"has",role2.health,"HP")
        tries=tries-1
    print()
    if role1.health>role2.health:
        print(role1.name,"has won! Congratulations !!!")
    elif role1.health<role2.health:
        print(role2.name,"has won! You have lost! ")
    else: print("It is a tie")

def game1role2():
    tries=3
    print(role2.name,"has spawned in a field full of apple trees, you have to eat 3 apples,\n each apple can randomly take or give you HP. The player that has the most HP will win.")
    while tries>0:
        print()
        input("Press [ENTER] to eat an apple: ")
        apple=random.randint(-2,2)
        apple2=random.randint(-2,2)
        print("Before eating the apple your health is",role2.health,"HP")
        role2.health=role2.health-apple
        print("After you ate an apple your health has became", role2.health,"HP")
        role1.health=role2.health-apple2
        print("And",role1.name,"has",role1.health,"HP")
        tries=tries-1
    print()
    if role1.health>role2.health:
        print(role1.name,"has won! You have lost !")
    elif role1.health<role2.health:
        print(role2.name,"has won! Congratulations !!!")
    else: print("It is a tie")
    




