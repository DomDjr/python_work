#Dominick Daito Jr
#Ex-2

#assigns the variable oneToOneHundred to equal one, and the variable count to 0. Uses a while loop to add the variables count and oneToOneHundred only if oneToOneHundred is less than or equal to 100. Adds 1 each to count each time the loop is executed.
oneToOneHundred = 1
count = 0 
while oneToOneHundred <= 100:
    oneToOneHundred = count + oneToOneHundred
    print(count,"+", end= " ")
    print(oneToOneHundred, "=", end=" ")
    print (oneToOneHundred + count)
    count += 1

print("Finished")