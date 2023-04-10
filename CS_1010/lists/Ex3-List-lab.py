#Dominick Daito Jr
#Ex-3

#creates a list with characters
my_char_list = ['a', 'b', 'a', 'c', 'd', 'a', 'd', 'z', 'r', 'a']

print("--------------")

#print the length of the list
my_char_listLength = len(my_char_list)
print(my_char_listLength)

print("--------------")

#prints out the index of the first "d" in the list
indexOfD = my_char_list.index('d')
print(indexOfD)

print("--------------")

#inserts the character "a" in index four
my_char_list.insert(4, 'a')
print(my_char_list)

print("--------------")

#prints the length of the list again
print(len(my_char_list))

print("--------------")

#counts and prints the amount of "a" in the list
countinga = my_char_list.count('a')
print(countinga)

print("--------------")

#prints each character in the list from the index range 0-11
count = 0
while count < 11:
    print(my_char_list[count], end=" ")
    count += 1