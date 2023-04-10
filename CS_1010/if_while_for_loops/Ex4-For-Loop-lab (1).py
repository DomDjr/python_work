#Dominick Daito Jr
#Ex-4

#creates a right triangle with 5 rows
for i in range (0,6):
    print("o"*i)

print("-------")

#creates a triangle with 7 rows
for i in range (0,7):
    print("o"*i)
    
print("-------")

#asks the user the amount of rows for a triangle
userinput = int(input("choose the amount of rows for the triangle"))
count = 0

#prints out a triangle that produces a type of output where the longest row of o's is equal to the input number
for i in range (0, userinput):
    while count <= userinput:
        print("o"*count)
        count+=1
#reverses the output of rows to print out from the start of the userinput to 0
count = userinput
while count >= 0:
    count-=1
    print('o'*count)

print("-------")

#asks the user for the amount of rows the triangle should have
pyramidinput = int(input("choose the amount of rows for your integer"))
#assigns variables to help create a pyramid
count = 0
numberofO = 1
numberofspaces = userinput * 2
#creates a pyramid by subtracting the amount of spaces based on the user input and creates a pyramid abiding by the user input of rows.
for i in range (0, userinput):
     while count <= userinput:
        print(" "*numberofspaces, 'o'* numberofO)
        numberofO = numberofO + 2
        count += 1
        numberofspaces -=1
        




        
       
        