#Dominick Daito Jr
#Ex-1

#defines a function that prints out a string and calls it
def hello_string():
    print("Hello from my function")

hello_string()

print("------")

#defines a function that prints out the numbers from range 1 to 20
def range_one_to_twenty():
    #assigns the variable count to 1. While count is less than or equal to 20, print out count. Iterates one to count
    count = 1
    while count <= 20:
        print(count, end=" ")
        count+=1

range_one_to_twenty()

print("------")

#defines a function that asks the user for an integer and multiplies it by 7 and prints it
def number_times_seven():
    userinteger = int(input("Choose a number"))
    userinteger = userinteger * 7
    print(userinteger)

number_times_seven()

print("------")

#defines a function where the user is asked to store three strings into three variables. Creates a list from those strings, sorts it, and prints it.
def list_function(listitem1, listitem2, listitem3):
    my_list = [listitem1, listitem2, listitem3]
    my_list.sort()
    print(my_list)

#Asks the user to store three strings into three variables
listitem1 = input("choose a string")
listitem2 = input("choose another string")
listitem3 = input("choose the last string")
list_function(listitem1, listitem2, listitem3)
    