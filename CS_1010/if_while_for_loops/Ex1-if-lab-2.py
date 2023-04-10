#Dominick Daito Jr
# put your name as a comment at the top of your program

# this statement lets you use the random number generator
import random

# this statement generates an integer from 0 to 20 inclusive
# and stores it in the variable secretNum
secretNum = random.randint(1,20)

print()
print("The computer has selected a secret number from 0 to 20 inclusive\n")
print("You have to guess it in as few tries as possible.\n")
print("To do this enter a number between 0 and 20 and the computer will")
print("tell you if your guess is lower or higher than the secret number.")
print("When you guess the correct number the computer will tell you")
print("you how many guesses it took.")

# your code goes here
print("--------------------------------------------")
print("You have seven attempts to guess the secret number")
userInput = int(input("choose a number"))

# sets the guesscounter to 7 
guessCount = 7

#while userInput doesnt equal secretNum and guessCount is less than or equal to 7 then if statements will occur
while userInput != secretNum and guessCount <= 7:
#if userinput is greater than secretNum then it will print that secretNum is less and subract one from guessCount
    if userInput > secretNum:
        print("Secret number is less than your number")
        guessCount -= 1
        print("You have",guessCount, "attempts")
        userInput = int(input("choose a number"))
#if userinput is less than secretNum then it will print that secretNum is greater and subract one from guessCount
    elif userInput < secretNum:
        print("Secret number is greater than your number")
        guessCount -= 1
        print("You have",guessCount, "attempts")
        userInput = int(input("choose a number"))
#if guessCount equals 0 then print statements will occur to let the user know they ran out of attempts. secretNum will be displayed
    if guessCount == 0:
        print("Sorry you have reached max attempts. Try again")
        print("The secret number was", secretNum)
        break

#if the user guesses the secretNum then print statements will occur to let them know as well as the number of attempts used.
if userInput == secretNum:
    guessCount = 7 - guessCount
    print("Right on")
    print("You guessed the number in", guessCount, "attempts")
