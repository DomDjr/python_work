#Dominick Daito Jr
#Ex-2
import random

#defines a function that prints a random number from 1 to 6.
def dice_1():
    rndm_num = random.randint(1,6)
    print(rndm_num)

#defines a function that prints a random number from 1 to 6 that is converted into an integer. 
def dice_2():
    rndm_num = int(random.randint(1,6))
    print(rndm_num)
#defines a variable called count to call out the function 

#defines a function that stores a random number and random dice side.
def dice_3(sides):
    rndm_num = int(random.randint(1, sides))
    print(rndm_num)
#accepts an integer from the user to be stored in a variable that is then used for a range from 1 to sides.
sides = int(input("Choose how many sides the dice has"))

#defines a function that is similar to the function dice_3.
def dice_4(sides):
#if the user stores zero into the variable sides, an if-statement will occur that will change the value to 6.
    if sides == 0 :
        sides = 6
#stores a random integer from the range 1 to the variable sides and prints it out.
    rndm_num = int(random.randint(1, sides))
    print(rndm_num)
#asks the user to input how many sides the dice has
sides = int(input("Choose how many sides the dice has"))

#defines a function that is similar to the function dice_4
def dice_5(sides):
#if the user stores 0 in sides then that value will change to 6 and store 6 in the variable sides.
    if sides == 0 :
        sides = 6
#if the user doesnt store these specified integers, a string will be printed out.
    if sides != 4 or 6 or 8 or 10 or 12 or 20:
        print("The sides must be one of these 6 values [4,6,8,10,12,20]")
    rndm_num = int(random.randint(1, sides))
    print(rndm_num)
sides = int(input("Choose how many sides the dice has"))

#defines a function called dice_6 that is similar to dice_5. Creates another parameter called rolls.
def dice_6(sides,rolls):
#if the user stores 0 in sides then that value will change to 6 and store 6 in the variable sides.
    if sides == 0 :
        sides = 6
#if the user doesnt store these specified integers, a string will be printed out.
    if sides != 4 or 6 or 8 or 10 or 12 or 20:
        print("The sides must be one of these 6 values [4,6,8,10,12,20]")
    rndm_num = int(random.randint(1, sides))
#stores a random integer form 1, to rolls. Reassigns the variable rolls with the random integer.
    rolls = int(random.randint(1, rolls))
#prints out the random number and random number of rolls on the same line.
    print(rndm_num, end=" ")
    print(rolls)
sides = int(input("Choose how many sides the dice has"))
#asks the user to print out how many rolls the dice will have
rolls = int(input("Choose how many rolls"))

#defines a function that is similar to dice_6.
def dice_7(sides, rolls):
#if the variable sides equals zero, it will be reassigned with the value of 6.
    if sides == 0:
        sides = 6
#if the variable sides doesnt equal these specified integers, a string will be printed out notifying the user.
    if sides != 4 or 6 or 8 or 10 or 12 or 20:
        print("The sides must be one of these 6 values [4,6,8,10,12,20]")
#stores a random integer from 1 to sides to rndm_num and an integer from 1 to rolls to rolls
    rndm_num = int(random.randint(1, sides))
    rolls = int(random.randint(1, rolls))
#creates a list from the values and prints it out.
    my_list = [rndm_num, rolls]
    return my_list
#asks the user to input an integer for the number of sides and rolls.
sides = int(input("Choose how many sides the dice has"))
rolls = int(input("Choose how many rolls"))

#calls out the function dice_1
dice_1()

#while the value of count is less than the value of rndm_num, it will add one to count.
count = 1
rndm_num = int(random.randint(1,6))
while count < rndm_num:
        if count < rndm_num:
            count+=1
#if count equals rndm_num it will call out dice_2
        if count == rndm_num:
            dice_2()

#calls out the defined functions.
dice_3(sides)
dice_4(sides)
dice_5(sides)
dice_6(sides, rolls)
dice_7(sides, rolls)


    


    