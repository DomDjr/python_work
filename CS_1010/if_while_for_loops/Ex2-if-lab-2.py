#Dominick Daito Jr
print()
print("Think of a number between 0 and 20 inclusive\n")
print("The program will print out a number and wait for your input\n")
print("If the number is lower than your secret number enter the character L")
print("If the number is higher than your secret number enter the character H")
print("If the number is equal to your secret number enter the character E")
print("The program gets 7 chances to guess your number")
print("If it guesses your number it will print out the number of guesses it took")
print()

# your code goes here
print("------------------------------------------")

#imports a random number from the range 1-20 and prints it onto the console.
import random
computerNum = random.randint(1,20)
print(computerNum)

#Asks the user if the computers number is less than, greater than, or equal theirs. 
userNum = input("Is the computer number less than, greater than, or equal to yours? [L,G,E]")

#stores the number of guesses the computer has in ComputerGuesses. Starts with 7
ComputerGuesses = 7

#as long as the computers guesses is less than or equal to 7 and the user doesnt input "E" then the loop will continue.
while ComputerGuesses <= 7 and userNum != "E":
    if userNum == "L":
        #each time the user inputs "L" the computers guesses decreases by one and a new random number is printed followed with the same input statement.
        ComputerGuesses -= 1
        print("The program has", ComputerGuesses, "attempts left")
        import random
        computerNum = random.randint(1,20)
        print(computerNum)
        userNum = input("Is the computer number less than, greater than, or equal to yours? [L,G,E]")
    if userNum == "G":
        #each time the user inputs"G"the computers guesses decreases by one and a new random number is printed followed with the same input statement.
        ComputerGuesses -= 1
        print("The program has", ComputerGuesses, "attempts left")
        import random
        computerNum = random.randint(1,20)
        print(computerNum)
        userNum = input("Is the computer number less than, greater than, or equal to yours? [L,G,E]")
    if ComputerGuesses == 0:
        #once the computers guesses reaches 0, print statements will occur to let the user know the computer ran out of attempts and the loop ends.
        print("The program has", ComputerGuesses, "attempts left")
        print("You are out of attempts. Try again.")
        break
    
if userNum == "E":
    #if the computer picked the users number, then print statements will let them know how many attempts it took the computer to guess.
    print("Nice!")
    print("The program guessed your number with", ComputerGuesses, "attempts remaining")
        
