#Dominick Daito Jr
print("This program will guess what shape you choose")
StartScreen = input("Are you ready to start? [Y/N]")

while StartScreen != "Y":
    StartScreen = input("Are you ready start?[Y/N]")

if StartScreen == "Y":
    redCondition = input("Is your shape red[Y/N]?")
    if redCondition == "Y":
        evenOrOddRed = input("Does your shape have an even number on it?[Y/N]")
        if evenOrOddRed == "Y":
            twoOrFour = input("Is your even number 2?[Y/N]")
            if twoOrFour == "Y":
                print("i guess red sqaure")
            if twoOrFour == "N":
                print('then i guess red quadrilateral')
        if evenOrOddRed == "N":
            fiveOrsSeven = input("Is your odd number 5?[Y/N]")
            if fiveOrsSeven == "Y":
                print("I guess red triangle")
            if fiveOrsSeven == "N":
                print("I guess red pentagon")
                    
                    
    if redCondition == "N":
        evenOrOddBlue = input("Does your shape have an even number on it?[Y/N]")
        if evenOrOddBlue == "Y":
            sixOrEight = input("Is your number 6[Y/N]?")
            if sixOrEight == "Y":
                print("I guess blue square")
            if sixOrEight == "N":
                print("I guess blue octagon")
        if evenOrOddBlue == "N":
            oneOrThree = input("is your number 1?[Y/N]")
            if oneOrThree == "Y":
                print("I guess blue triangle")
            if oneOrThree == "N":
                print("I guess blue pentagon")

                
        
            