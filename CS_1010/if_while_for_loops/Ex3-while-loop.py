#Dominick Daito Jr
#Ex-3

#asks the user to choose an integer or type "q" to end the input. The input is then stored into the variable userInteger. if the user inputs "q", then it will print "ending", if an integer is inputted, it will print the users subtotal. 
userInteger = input("choose an integer to add or type [q] to quit")
if userInteger == "q":
    print("Ending")
if userInteger != "q":
    subtotal = userInteger
    print("Your subtotal is", userInteger)
#a while loop is used to add the users INTEGER input as a subtotal. The users input will continously be added until the user inputs "q", in which the users grand total will be printed. This will end the loop.
while userInteger != "q":
    if userInteger != "q":
        userInteger = int(userInteger)
        userIntegerLoop = input("choose an integer to add or type [q] to quit!")
        #if userIntegerLoop doesnt equal "q" the variable will be converted into an integer and added into the subtotal which will then be printed after each loop.
        if userIntegerLoop != "q":
            userIntegerLoop = int(userIntegerLoop)
            userInteger = userInteger + userIntegerLoop
            subtotal = userInteger 
            print("Your subtotal is", subtotal)
        #if the user does input "q", the program will print the grandTotal, meaning the final calculations of the subtotal will be stored into the variable grandTotal and will ultimately end the loop.
        if userIntegerLoop == "q":
            grandTotal = subtotal
            print("Your grand total is", grandTotal)
            print("Thank you")
            break
    

