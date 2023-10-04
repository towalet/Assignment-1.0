import role1,role2
import random

# START OF QUEST

# Mission 1
# The first game for the first role 
# The player gets a short description and rules of the game and is now able to press ENTER for each try
# def game1role1():
#     tries=3
#     print(role1.name,"has spawned in a field full of apple trees, you have to eat 3 apples,\n each apple can randomly take or give you HP the player that has the most HP will win.")
#     while tries>0:
#         print()
#         input("Press [ENTER] to eat an apple: ")
#         apple=random.randint(-2,2)
#         apple2=random.randint(-2,2)
#         print("Before eating the apple your health is",role1.health,"HP")
#         role1.health=role1.health-apple
#         print("After you ate an apple your health has became", role1.health,"HP")
#         role2.health=role2.health-apple2
#         print("And",role2.name,"has",role2.health,"HP")
#         tries=tries-1
#     print()
#     if role1.health>role2.health:
#         print(role1.name,"has won! Congratulations !!!")
#     elif role1.health<role2.health:
#         print(role2.name,"has won! You have lost! ")
#     else: print("It is a tie")

# # The first game for the first role 
# # The player gets a short description and rules of the game and is now able to press ENTER for each try
# def game1role2():
#     tries=3
#     print(role2.name,"has spawned in a field full of apple trees, you have to eat 3 apples,\n each apple can randomly take or give you HP. The player that has the most HP will win.")
#     while tries>0:
#         print()
#         input("Press [ENTER] to eat an apple: ")
#         apple=random.randint(-2,2)
#         apple2=random.randint(-2,2)
#         print("Before eating the apple your health is",role2.health,"HP")
#         role2.health=role2.health-apple
#         print("After you ate an apple your health has became", role2.health,"HP")
#         role1.health=role2.health-apple2
#         print("And",role1.name,"has",role1.health,"HP")
#         tries=tries-1
#     print()
#     if role1.health>role2.health:
#         print(role1.name,"has won! You have lost !")
#     elif role1.health<role2.health:
#         print(role2.name,"has won! Congratulations !!!")
#     else: print("It is a tie")
    
# Mission 2

tries=3
input("Press [ENTER] to continue with your 2nd game !")
print()
print("Welcome you have been moved to the next destination, the bar, here you will play a game of dice where your and your enemies attributes will effect the outcome of the game ")
print("You will have 3 tries to throw a pair of dice and your stenghth will increase the number with every try. Your strength is", role1.strength,"ST.")
print("Each dice goes from 1 to 6 and you have two of them, so your minimum each try is 2 and maximum is 12!")

dicetotal=0
dicetotal2=0
while tries>0:
    print()
    input("Press [ENTER] to through the dice !")
    dice1=random.randint(1,6)
    dice2=random.randint(1,6)
    dice3=random.randint(1,6)
    dice4=random.randint(1,6)
    dicetotal=dice1+dice2+dicetotal+role1.strength
    dicetotal2=dice3+dice4+dicetotal2+role2.strength
    print()
    print("You have thrown your dice and your fist dice and it landed on",dice1,", your second dice landed on",dice2,".\nYour strength attribute has added an additional",role1.strength,"points, therefore your total is", dicetotal,"points")
    print()
    print("While your enemies",role2.name," fist dice has landed on",dice3,", and their second dice landed on",dice4,".\nTheir strength attribute has added an additional",role2.strength,"points, therefore your total is", dicetotal2,"points")
    tries=tries-1

print()  
if 6<=dicetotal<16:
    print("Critical Loss! ")
    role1.health=role1.health-5
    print("Due to the critical loss, you lost 5 HP. \nYour current health is:",role1.health,"HP")
elif 16<=dicetotal<26:
    print("Loss! ")
    role1.health=role1.health-3
    print("Due to the loss, you lost 3 HP. \nYour current health is: ",role1.health)
elif 24<=dicetotal<33:
    print("Win !")
    print("Congratulations !")
elif 33<=dicetotal:
    print("Critical Win !!!")
    print("Congratulations !")





