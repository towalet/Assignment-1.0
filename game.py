'''
Anthony Vydysh
PROG10004 Programming Principles
Due Date: 10/10/2023

This module Implements the game data and logic.'''

import role1,role2
import random

# START OF QUESTs
# quest 1 role1 
def game1role1():
    tries=3 # assigned variable for the number of tries
    # print statement tells the rules of the 1st challenge for role 1
    print(role1.name,"has spawned in a field full of apple trees, you have to eat 3 apples,\n each apple can randomly take or give you HP the player that has the most HP will win.")
    while tries>0: # A while loop that lets the challenge play 3 times, till the the tries are less than 0
        print()
        input("Press [ENTER] to eat an apple: ") # gets input from user to continue
        apple=random.randint(-2,2) # Generates a random integer for the picked role
        apple2=random.randint(-2,2) # Generates a random integer for the enemy
        print("Before eating the apple your health is",role1.health,"HP") # statement that presents your health before the operation
        role1.health=role1.health-apple # operation with health and random int
        print("After you ate an apple your health has became", role1.health,"HP") # statement that presents your health after the operation
        role2.health=role2.health-apple2 # The results for the enemy role is calculated
        print("And",role2.name,"has",role2.health,"HP") # prints the results of the enemy
        tries=tries-1
    print()
    # The results are compared to establish what role has won
    if role1.health>role2.health: # If role 1 has a higher health result than role 2
        print(role1.name,"has won the first challenge! Congratulations !!!") # Prints statement for the chosen role's win
        role1.wins=role1.wins+1
    elif role1.health<role2.health: # If role 2 has a higher health result than role 1
        print(role2.name,"has won! You have lost the first challenge! ") # Prints statement for the enemies win, and tells you that you lost
    else: print("It is a tie") # Else prints that it is a tie (If their health is equal)

# The first game for the first role 
# The player gets a short description and rules of the game and is now able to press ENTER for each try

# quest 1 role2

def game1role2():
    tries=3 # assigned variable for the number of tries
    # print statement tells the rules of the 1st challenge for role 2
    print(role2.name,"has spawned in a field full of apple trees, you have to eat 3 apples,\n each apple can randomly take or give you HP. The player that has the most HP will win.")
    while tries>0: # A while loop that lets the challenge play 3 times, till the the tries are less than 0
        print()
        input("Press [ENTER] to eat an apple: ") # gets input from user to continue
        apple=random.randint(-2,2) # Generates a random integer for the picked role
        apple2=random.randint(-2,2) # Generates a random integer for the enemy
        print("Before eating the apple your health is",role2.health,"HP") # statement that presents your health before the operation
        role2.health=role2.health-apple # operation with health and random int
        print("After you ate an apple your health has became", role2.health,"HP") # statement that presents your health after the operation
        role1.health=role2.health-apple2 # The results for the enemy role is calculated
        print("And",role1.name,"has",role1.health,"HP")
        tries=tries-1
    print()
    if role1.health>role2.health:
        print(role1.name,"has won! You have lost the first challenge !")
    elif role1.health<role2.health:
        print(role2.name,"has won the challenge! Congratulations !!!") 
        role2.wins=role2.wins+1
    else: print("It is a tie") # Else prints that it is a tie (If their health is equal)
    
# Mission 2
# quest 2 for role 1
def game2role1():
    tries=3 # Variable assigned to the number of tries
    input("Press [ENTER] to continue with your 2nd game !") # User gets the option to click ENTER to start challenge 2
    print()
    # Welcomes the user to the second stage of the game where they are able to compete with the second role 
    # Atributes strength will affect the number of dice for each role
    print("Welcome, you have been moved to the next destination- the bar. Here you will play a game of dice where your and your enemies attributes will affect the outcome of the game ")
    print("You will have 3 tries to throw a pair of dice and your stenghth will increase the number of points with every try. Your strength is", role1.strength,"ST.")
    print("Each dice goes from 1 to 6 and you have two of them, so your minimum each try is 2 points and maximum is 12 points!")
    print("Good Luck,",role1.name)

    dicetotal=0 # initial number of total dice points assigned for each role
    dicetotal2=0
    while tries>0:
        print()
        input("Press [ENTER] to through the dice !")
        # dice 1 and dice 2 is the random dice points that are given to role 1
        dice1=random.randint(1,6)
        dice2=random.randint(1,6)
        # dice 3 and dice 4 is the random dice points that are given to role 2
        dice3=random.randint(1,6)
        dice4=random.randint(1,6)
        dicetotal=dice1+dice2+dicetotal+role1.strength # Calculation for the total points for role 1 
        dicetotal2=dice3+dice4+dicetotal2+role2.strength # Calculation for the total points for role 2
        print()
        # Prints the outcome for the chosen role by the user
        print("You have thrown your dice and your fist dice and it landed on",dice1,", your second dice landed on",dice2,".\nYour strength attribute has added an additional",role1.strength,"points, therefore your total is", dicetotal,"points")
        print()
        # Prints the outcome for the enemies role
        print("While your enemies",role2.name," fist dice has landed on",dice3,", and their second dice landed on",dice4,".\nTheir strength attribute has added an additional",role2.strength,"points, therefore your total is", dicetotal2,"points")
        tries=tries-1 # subtracts the number of tries for each loop cycle
    print()
    # Compares the total dice points for each role to find winner
    if dicetotal<dicetotal2:
        print(role2.name,"has lost! You have lost the first challenge !")
    elif dicetotal>dicetotal2:
        print(role1.name,"has won the challenge! Congratulations !!!") 
        role1.wins=role1.wins+1
    else: print("It is a tie") # Else prints that it is a tie (If their health is equal)

    print()
    # This part of the code decides what kind of loss or win it is in this challenge
    if 6<=dicetotal<16: # range of points that decide if it is a critical loss
        print("Critical Loss! ")
        role1.health=role1.health-5 # subtracts  5 health points if it is a critical loss
        print("Due to the critical loss, you lost 5 HP. \nYour current health is:",role1.health,"HP") # Prints the health changes of the role 
    elif 16<=dicetotal<26: # range of points that decide if it is a loss
        print("Loss! ")
        role1.health=role1.health-3 # subtracts 3 health points if it is a loss
        print("Due to the loss, you lost 3 HP. \nYour current health is: ",role1.health,"HP") # Prints the health changes of the role 
    elif 24<=dicetotal<33: # range of points that decide if it is a win
        print("Win !")
        print("Congratulations ! You won the second challenge!")
    elif 33<=dicetotal: # range of points that decide if it is a critical win
        print("Critical Win !!!")
        print("Congratulations ! You won the second challenge!")
    elif dicetotal2==dicetotal: # If both total points are equal
        print("You have tied with your enemy in challenge 2") # Lets the user know that the points are tied

# quest 2 for role 2
def game2role2():
    tries=3
    input("Press [ENTER] to continue with your 2nd game !")
    print()
    # Welcomes the user to the second stage of the game where they are able to compete with the second role 
    # Atributes strength will affect the number of dice for each role
    print("Welcome you have been moved to the next destination- the bar. Here you will play a game of dice where your and your enemies attributes will effect the outcome of the game ")
    print("You will have 3 tries to throw a pair of dice and your stenghth will increase the number of points with every try. Your strength is", role2.strength,"ST.")
    print("Each dice goes from 1 to 6 and you have two of them, so your minimum each try is 2 points and maximum is 12 points!")
    print("Good Luck,",role2.name)  

    dicetotal=0 # initial number of total dice points assigned for each role
    dicetotal2=0
    while tries>0:
        print()
        input("Press [ENTER] to through the dice !")
        # dice 1 and dice 2 is the random dice points that are given to role 2
        dice1=random.randint(1,6)
        dice2=random.randint(1,6)
        # dice 1 and dice 2 is the random dice points that are given to role 1
        dice3=random.randint(1,6)
        dice4=random.randint(1,6)
        dicetotal=dice1+dice2+dicetotal+role2.strength # Calculation for the total points for role 2
        dicetotal2=dice3+dice4+dicetotal2+role1.strength # Calculation for the total points for role 1
        print()
        # Prints the outcome for the chosen role by the user
        print("You have thrown your dice and your fist dice and it landed on",dice1,", your second dice landed on",dice2,".\nYour strength attribute has added an additional",role2.strength,"points, therefore your total is", dicetotal,"points")
        print()
        # Prints the outcome for the enemies role
        print("While your enemie's",role1.name," fist dice has landed on",dice3,", and their second dice landed on",dice4,".\nTheir strength attribute has added an additional",role1.strength,"points, therefore your total is", dicetotal2,"points")
        tries=tries-1
    print()
    # Compares the total dice points for each role to find winne
    if dicetotal>dicetotal2:
        print(role1.name,"has won! You have lost the first challenge !")
    elif dicetotal<dicetotal2:
        print(role2.name,"has won the challenge! Congratulations !!!") 
        role2.wins=role2.wins+1
    else: print("It is a tie") # Else prints that it is a tie (If their health is equal)

    print() 
    # This part of the code decides what kind of loss or win it is in this challenge 
    if 6<=dicetotal<16: # range of points that decide if it is a critical loss
        print("Critical Loss! ")
        role2.health=role2.health-5 # subtracts  5 health points if it is a critical loss
        print("Due to the critical loss, you lost 5 HP. \nYour current health is:",role2.health,"HP") # Prints the health changes of the role 
    elif 16<=dicetotal<26: # range of points that decide if it is a loss
        print("Loss! ")
        role2.health=role2.health-3 # subtracts 3 health points if it is a loss
        print("Due to the loss, you lost 3 HP. \nYour current health is: ",role2.health,"HP") # Prints the health changes of the role 
    elif 24<=dicetotal<33: # range of points that decide if it is a win
        print("Win !")
        print("Congratulations ! You won the second challenge!")
    elif 33<=dicetotal: # range of points that decide if it is a critical win
        print("Critical Win !!!")
        print("Congratulations ! You won the second challenge!")
    elif dicetotal2==dicetotal: # If both total points are equal
        print("You have tied with your enemy in challenge 2") # Lets the user know that the points are tied

# quest 3 for role1
def quest3role1():
    input("Press [ENTER] to play the last challenge! ")
    print()
    # Welcomes to quest 3
    print("Welcome to the last challenge, this challenge will decide who wins! Either you, the",role1.name,", or your enemy, the",role2.name,", will win the game!")
    # The quest is presented, rules of the game are told
    print("In this challenge you will be shooting a bow, your goal is to hit the middle of the target.\nYou will have 3 tries to shoot the bow. The minimum points that could be achieved is 0 and the maximum is 10.")
    print("The attributes that will affect the score are the players intelligence and dexterity! \nFor this challenge you have only one attribute, which is dexterity. Your current dexterity is",role1.dexterity,"DT")
    print()
    # Input to press ENTER is asked to continue game
    input("Are you ready to start the challenge? Press [ENTER] if yes: ")
    # Gives an overview of the situation
    print("You and the",role2.name,"have spawned in a field with a target, pick up the bow and arrows and shoot your first shot!")

    tries=3 # Assigns the number of tries
    totalpointsrole1=0 # Assigns the total of points
    totalpointsrole2=0
    # The quest is looped for 3 times 
    while tries>0:
        print()
        input("Press [ENTER] to shoot an arrow: ")
        print()
        # Randomizes a number of points for role1
        shotrole1=random.randint(0,10)
        # Randomizes a number of points for role2
        shotrole2=random.randint(0,10)
        # Adds the random number for each role to the attributes to create the total
        totalpointsrole1=shotrole1+totalpointsrole1+role1.dexterity
        totalpointsrole2=shotrole2+totalpointsrole2+role2.iq
        # Presents the results for the chosen role by the user
        print("You shot an arrow at the target, and it landed on",shotrole1,"points. Your dexterity has given 1 point to your total. \nYour total is",totalpointsrole1,"points." )
        print()
        # Presents the results for the enemy
        print(role2.name,"has shot the target and the arrow landed on",shotrole2,"points. \nTheir intelligence attribute has given them an extra 2 points.\nTheir total is",totalpointsrole2,"points.")
        tries-=1 # Decreses the number of tries each loop

    # Compares the total points for each role to find winner
    if totalpointsrole1>totalpointsrole2:
            print(role1.name,"has won! You have won the last challenge !") 
            role1.wins=role1.wins+1 # adds a win to the role
    elif totalpointsrole1<totalpointsrole2:
            print(role2.name,"has won the challenge! You have lost the last challenge !!!") 
    else: print("It is a tie") 

    print()
    # This part of the code decides what kind of loss or win it is in this challenge
    if 0<=totalpointsrole1<7 and totalpointsrole1<totalpointsrole2: # Range of points for critical loss
        print("Critical Loss! ")
        role1.health=role1.health-5 # Subtracts 5 from the total health if critical loss
        print("Due to the critical loss, you lost 5 HP. \nYour current health is:",role1.health,"HP")
    elif 7<=totalpointsrole1<24 and totalpointsrole1<totalpointsrole2: # Range of points for loss
        print("Loss! ")
        role1.health=role1.health-3 # Subtracts 3 from the total health if loss
        print("Due to the loss, you lost 3 HP. \nYour current health is: ",role1.health)
    elif 24<=totalpointsrole1<31 and totalpointsrole1>totalpointsrole2: # Range of points for win
        print("Win !")
        print("Congratulations! You won in the third challenge! ") # Congratulates the user
    elif 31<=totalpointsrole1 and totalpointsrole1>totalpointsrole2: # Range of points for Critical Win
        print("Critical Win !!!")
        print("Congratulations! You won in the third challenge! ") # Congratulates the user
    elif totalpointsrole1==totalpointsrole2: # If both total points = to each other it is a tie
        print("You have tied with your enemy in challenge 3")

# quest 3 for role2
def quest3role2():
    input("Press [ENTER] to play the last challenge! ")
    print()
    # Welcomes to quest 3
    print("Welcome to the last challenge, this challenge will decide who wins! Either you, the",role2.name,", or your enemy, the",role1.name,", will win the game!")
    # The quest is presented, rules of the game are told
    print("In this challenge you will be shooting a bow, your goal is to hit the middle of the target.\nYou will have 3 tries to shoot the bow. The minimum points that could be achieved is 0 and the maximum is 10.")
    print("The attributes that will affect the score are the players intelligence and dexterity! \nFor this challenge you have only one attribute, which is intellegence. Your current intellegence is",role2.iq,"IQ")
    print()
    # Input to press ENTER is asked to continue game
    input("Are you ready to start the challenge? Press [ENTER] if yes: ")
    # Gives an overview of the situation
    print("You and the",role1.name,"have spawned in a field with a target, pick up the bow and arrows and shoot your first shot!")

    tries=3 # Assigns the number of tries
    totalpointsrole1=0 # Assigns the total of points
    totalpointsrole2=0
    # The quest is looped for 3 times 
    while tries>0:
        print()
        input("Press [ENTER] to shoot an arrow: ")
        print()
        # Randomizes a number of points for role2
        shotrole1=random.randint(0,10)
        # Randomizes a number of points for role1
        shotrole2=random.randint(0,10)
        # Adds the random number for each role to the attributes to create the total
        totalpointsrole1=shotrole1+totalpointsrole1+role2.iq
        totalpointsrole2=shotrole2+totalpointsrole2+role1.dexterity
        # Presents the results for the chosen role by the user
        print("You shot an arrow at the target, and it landed on",shotrole1,"points. Your intellegence has given 2 point to your total. \nYour total is",totalpointsrole1,"points." )
        print()
        # Presents the results for the enemy
        print(role1.name,"has shot the target and the arrow landed on",shotrole2,"points. \nTheir dexterity attribute has given them an extra 1 points.\nTheir total is",totalpointsrole2,"points.")
        tries-=1 # Decreses the number of tries each loop

    # Compares the total points for each role to find winner
    if totalpointsrole1>totalpointsrole2:
            print(role2.name,"has won! You have won the last challenge !")
            role2.wins=role2.wins+1 # adds a win to the role
    elif totalpointsrole1<totalpointsrole2:
            print(role1.name,"has won the challenge! You have lost the last challenge !!!") 
    else: print("It is a tie") 

    print()
    # This part of the code decides what kind of loss or win it is in this challenge
    if 0<=totalpointsrole1<7 and totalpointsrole1<totalpointsrole2: # Range of points for critical loss
        print("Critical Loss! ")
        role2.health=role2.health-5 # Subtracts 5 from the total health if critical loss
        print("Due to the critical loss, you lost 5 HP. \nYour current health is:",role2.health,"HP")
    elif 7<=totalpointsrole1<24 and totalpointsrole1<totalpointsrole2: # Range of points for loss
        print("Loss! ")
        role2.health=role2.health-3 # Subtracts 3 from the total health if loss
        print("Due to the loss, you lost 3 HP. \nYour current health is: ",role2.health)
    elif 24<=totalpointsrole1<31 and totalpointsrole1>totalpointsrole2: # Range of points for win
        print("Win !")
        print("Congratulations! You won in the third challenge! ") # Congratulates the user
    elif 31<=totalpointsrole1 and totalpointsrole1>totalpointsrole2: # Range of points for Critical Win
        print("Critical Win !!!")
        print("Congratulations! You won in the third challenge! ") # Congratulates the user
    elif totalpointsrole1==totalpointsrole2: # If both total points = to each other it is a tie
        print("You have tied with your enemy in challenge 3")
# Decides if role 1 will win or lose  the overall game

def role1win():
    # Decides if role 1 will win or lose  the overall game
    if role1.wins>1:
        print("You have won the game!!! Congratulations")
        print()
        print("GAME OVER")
    else:
        print("You have lost !!! Try Again")
        print()
        print("GAME OVER")

def role2win():
    # Decides if role 1 will win or lose  the overall game
    if role2.wins>1:
        print("You have won the game!!! Congratulations")
        print()
        print("GAME OVER")
    else:
        print("You have lost !!! Try Again")
        print()
        print("GAME OVER")
