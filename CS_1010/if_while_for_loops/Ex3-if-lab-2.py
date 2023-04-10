#Dominick Daito Jr
print("A set of four animals will be states, choose one and the computer will guess which one you chose.")

#Asks the user to choose between four animals.
userAnimalChoice = input("Choose between a tarantula, snake, fish, octopus. Type [Y/N] when you have it")

#uses if statements to utilize process of elimination. If the animal has legs, it will ask what environment it lives. 
if userAnimalChoice == "Y":
    userAnimalQuestion = input("Does your animal have legs[Y/N]")
    if userAnimalQuestion == "Y":
        userAnimalQuestion2 = input("Does your animal live in the water[Y/N]?")
#If the user types in 'Y' then the program will guess octopus, "N", the program will guess turantula.
        if userAnimalQuestion2 == "Y":
            print("your animal is an octopus")
        if userAnimalQuestion2 == "N":
            print("your animal a turantula")
#if the user types in "N" it will ask the user if it lives on land.
    if userAnimalQuestion == "N": 
        userAnimalQuestion3 = input("Does your animal live on land?[Y/N]")
#If the user types in "Y", the program will guess snake. "N", the program will guess fish.
        if userAnimalQuestion3 == "Y":
            print("your animal ia a snake")
        if userAnimalQuestion3 == "N":
            print("Its a fish then")
                
        
            
    
   

        
   
    


     
