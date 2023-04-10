#Dominick Daito Jr
#Ex-2

#creates a list with integers
my_num_list = [3, 6, 4, 83, 2, 7, 2, 17, 4, 9, 0, 44, 2]

print('--------------------')

#prints the integer on index 3
print(my_num_list[3])

print('--------------------')

#removes the integer on index 8 and prints the list
my_num_list.append(8)
print(my_num_list)

print('--------------------')

#inserts the integer 33 on index 4
my_num_list.insert(4,33)
print(my_num_list)

print('--------------------')

#creates a variable to print the amount of 2's in the list
TwosCount = my_num_list.count(2)
print(TwosCount)

print('--------------------')

#sorts the list from least to greates and prints it
my_num_list.sort()
print(my_num_list)

print('--------------------')

#prints the length of the list, or the amount of integers
LengthOfList = len(my_num_list)
print(LengthOfList)

print('--------------------')

#removes four integers and prints them as well as the original list
poplist = my_num_list.pop()
poplist2 = my_num_list.pop()
poplist3 = my_num_list.pop()
poplist4 = my_num_list.pop()
print(poplist, poplist2, poplist3, poplist4)
print(my_num_list)

print('--------------------')

#prints the length of the list again
LengthOfList2 = len(my_num_list)
print(LengthOfList2)

print('--------------------')

#creates a loop to print out each integer in the list while the variable count is less than 11
count = 0
while count < 11:
    print(my_num_list[count], end=' ')
    count += 1
print(' ')

print('--------------------')







