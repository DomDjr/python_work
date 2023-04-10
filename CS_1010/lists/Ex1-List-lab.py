#Dominick Daito Jr
#Ex-1

#Creates three variables with strings and prints them out
RedFoxVariable = "A Red Fox"
BlueMouseVariable = " chased a Blue mouse"
GreenMeadowVariable = " across a Green meadow"
print(RedFoxVariable)
print(BlueMouseVariable)
print(GreenMeadowVariable)
print("--------------------------")

#concatenates the three variables into one and prints it
RedBlueGreen = RedFoxVariable + BlueMouseVariable + GreenMeadowVariable
print(RedBlueGreen)

print("--------------------------")

#Turns the string into all lowercase, prints it out, and prints out the original
LowerCase = RedBlueGreen.lower()
print(LowerCase)
print(RedBlueGreen)

print("--------------------------")

#sets the string to all uppercase and prints it out as well as the original
UpperCase = RedBlueGreen.upper()
print(UpperCase)
print(RedBlueGreen)

print("--------------------------")

#prints out the character at index 19
print(RedBlueGreen[19])

print("--------------------------")

#prints out the characters from index 19 to 23
print(RedBlueGreen[19:23])

print("--------------------------")

#prints out the length of the concatenated string
RedBlueGreenLength = len(RedBlueGreen)
print(RedBlueGreenLength)

print("--------------------------")

#tests whether the string is an integer
IntegerTest = RedBlueGreen.isdigit()
print(IntegerTest)

print("--------------------------")

#tests whether the string can be converted into an integer
StringToInteger = "100"
IntegerTest2 = StringToInteger.isdigit()
print(IntegerTest2)














