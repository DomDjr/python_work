#Dominick Daito Jr
#Ex-1

#imports the time and random functions to help with the progarm
import time
import random

#prints "What are you doing today?" with pauses that increase as each word is printed
print("What")
time.sleep(0.25)
print("are")
time.sleep(0.30)
print("you")
time.sleep(0.40)
print("doing")
time.sleep(0.55)
print("today?")
time.sleep(1.00)
print(time.time())
time.sleep(0.50)
print(time.time())
time.sleep(1.00)
print(time.time())

#sets count to 0 then proceeds to add one to the variable as long as count isnt greater than or equal to 10
count = 0
while (count <= 10):
    print(count)
    count += 1

#sets countHorizontal to 0, adds one to the variable as long as it isnt greater than or equal to 10. Prints the variable in a horizontal line.
countHorizontal = 0
while countHorizontal <= 10:
    print(countHorizontal, end="-")
    countHorizontal += 1

#sets countPause to 0, adds one as long countPause isnt greater than or equal to 5. Prints the variable with a 0.50 pause
countPause = 0
while countPause <= 5:
    time.sleep(0.50)
    print(countPause)
    countPause += 1

#sets countByTwo to 10. As long as countByTwo is greater than 20, it will add two to the variable and print it out.
countByTwo = 10
while countByTwo <= 20:
    print(countByTwo)
    countByTwo += 2

#sets the variable countDownByThree to 20 and as long as countDownByThree is greater than or equal to 0, it will subtract three and print it out
countDownByThree = 20
while countDownByThree >= 0:
    print(countDownByThree)
    countDownByThree -= 3

#uses the random number function to set the variable randomInteger to a random number. Sets countRandomInt to 0 and uses a while loop to print a random integer ten times horizontally as long as count is less then or equal to 10
randomInteger = random.randint(0,100)
countRandomInt = 0
while countRandomInt <= 10:
    print(randomInteger, end=" ")
    randomInteger = random.randint(0,100)
    print(countRandomInt, end=" ")
    countRandomInt += 1
print(" ")

#sets the variable oneHundredInput to an input that is converted to an integer. A while loop is used to continously ask the user until a number greater than 100 is inputted by the user. 
oneHundredInput = int(input("enter an integer greater than one hundred."))
while oneHundredInput <= 100:
    oneHundredInput = int(input("enter an integer greater than one hundred!"))
if oneHundredInput > 100:
    print("Thank you")
    