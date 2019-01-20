# Mod2_2-2.1_Intro_Python.ipynb
# _____________________________________________________
#
# TASK 1
#
# [ ] create team_names list and populate with 3-5 team name strings
team_names = ["John", "Steve", "Paul", "Roger"]

# [ ] print the list
print(team_names)
# _________________

# [ ] Create a list mix_list with numbers and strings with 4-6 items
mix_list = [1, 5, "Something", "Good", "today"]

# [ ] print the list
print(mix_list)
# ________________
#
# TASK 2
#
# [ ] Create a list, streets, that lists the name of 5 street name strings
streets = ["Oak", "Oxford", "Park Wood", "Harrods Avenue", "Wood Lane"]

# [ ] print a message that there is "No Parking" on index 0 or index 4 streets
print("No parking on",streets[0],"and",streets[4],"streets")
# ________________
#
# [ ] Create a list, num_2_add, made of 5 different numbers between 0 - 25
num_2_add = [0, 5, 7, 10, 20]

# [ ] print the sum of the numbers
sum = 0
for i in num_2_add:
    sum += i
#
print("Sum:",sum)
# _________________
#
# TASK 3
#
# [ ] Review & Run, but ***Do Not Edit*** this code cell
# [ ] Fix the error by only editing and running the block below

print(" Total of checks 3 & 4 = $", pay_checks[2] + pay_checks[3])
#
# [ ] Fix the error above by creating and running code in this cell
pay_checks = [1, 2, 3, 4]
# __________________
#
# Mod2_2-2.2_Intro_Python.ipynb
# ________________________________________________________
#
# TASK 1
#
# Currency Values
# [ ] create a list of 3 or more currency denomination values, cur_values
# cur_values, contains values of coins and paper bills (.01, .05, etc.)

cur_values = [0.01, 0.05, 1.00, 5.00, 10.00]

# [ ] print the list

print(cur_values)

# [ ] append an item to the list and print the list

cur_values.append(20.00)
print(cur_values)
# ____________________
#
# Currency Names
# [ ] create a list of 3 or more currency denomination NAMES, cur_names
# cur_names contains the NAMES of coins and paper bills (penny, etc.)

cur_names = ["Nickel", "Quarter", "Dime", "Dollar"]

# [ ] print the list

print(cur_names)

# [ ] append an item to the list and print the list

cur_names.append("Hal-Dollar")
print(cur_names)
# _____________________
#
# TASK 2
#
# [ ] append additional values to the Currency Names list using input()

i = 0
while i < 4:
    cur_names.append(input("Enter value: "))
    print(cur_names)
    i += 1
#

# [ ] print the appended list
print("----")
print(cur_names)
# ______________________
#
# TASK 3
#
# while loop .append()
# define an empty list: bday_survey
# get user input, bday, asking for the day of the month they were born (1-31) or "q" to finish
# using a while loop (while user not entering "quit")
# append the bday input to the bday_survey list
# get user input, bday, asking for the day of the month they were born (1-31) or "q" to finish
# print bday_survey list

# [ ] complete the Birthday Survey task above
bday_survey = []
bday = input("Day you were born (1 to 31) (q - to finish): ")

while bday.lower().startswith("q") == False:
        bday_survey.append(bday)
        bday = input("Day you were born (1 to 31) (q - to finish): ")
#
print()
print (bday_survey)
# ______________________
#
# TASK 4
#
# [ ] Fix the Error
three_numbers = [1, 1, 2]
print("an item in the list is: ", three_numbers[2])
# ________________________
#
# Mod2_2-2.3_Intro_Python.ipynb
# _________________________________________________________________
#
# TASK 1
#
# replace items in a list
# create a list, three_num, containing 3 single digit integers
# print three_num
# check if index 0 value is < 5
# if < 5 , replace index 0 with a string: "small"
# else, replace index 0 with a string: "large"
# print three_num
#
# [ ] complete "replace items in a list" task
three_num = [3, 20, 30]
print(three_num)

if three_num[0] < 5:
    three_num[0] = "small"
else:
    three_num[0] = "large"

print(three_num) 
# _____________________
#
# Function Challenge: create replacement function
# Create a function, str_replace, that takes 2 arguments: int_list and index
# int_list is a list of single digit integers
# index is the index that will be checked - such as with int_list[index]
# Function replicates purpose of task "replace items in a list" above and replaces an integer with a string "small" or "large"
# return int_list
# Test the function!
# 
# [ ]  create challenge function
def str_replace(int_list,index):
    if int_list[index] < 5:
        int_list[index] = "small"
    else:
        int_list[index] = "large"
    return int_list
#

print(str_replace([2, 3, 4],0))
print(str_replace([6, 7, 8],1))
# ______________________
#
# TASK 2
#
# modify items in a list
# create a list, three_words, containing 3 different capitalized word stings
# print three_words
# modify the first item in three_words to uppercase
# modify the third item to swapcase
# print three_words
#
# [ ] complete coding task described above
three_words = ["Good","Happy","Day"]
print(three_words)
three_words[0] = three_words[0].upper()
three_words[2] = three_words[2].swapcase()
print(three_words)
# _______________________
#
# TASK 3
#
# [ ] insert a name from user input into the party_list in the second position (index 1)
party_list = ["Joana", "Alton", "Tobias"]
party_list.insert(1,input("Enter name: "))

# [ ] print the updated list
print(party_list)
# _________________________
#
# TASK 4
#
# [ ] Fix the Error
tree_list = ["oak"]
print("tree_list before =", tree_list)
tree_list.insert(1,"pine")
print("tree_list after  =", tree_list)
# ________________________
# 
# Mod2_2-2.4_Intro_Python.ipynb
# __________________________________________________________________
#
# TASK 1
#
# [ ] print ft_bones list
# [ ] delete "cuboid" from ft_bones
# [ ] reprint list
ft_bones = ["calcaneus", "talus", "cuboid", "navicular", "lateral cuneiform", 
            "intermediate cuneiform", "medial cuneiform"]

print(ft_bones)
del ft_bones[2]
print(ft_bones)
# ____________________
#
# TASK 2
#
# [ ] print ft_bones list
# [ ] delete "cuboid" from ft_bones
# [ ] delete "navicular" from list
# [ ] reprint list
# [ ] check for deletion of "cuboid" and "navicular"
ft_bones = ["calcaneus", "talus", "cuboid", "navicular", "lateral cuneiform", 
            "intermediate cuneiform", "medial cuneiform"]
print(ft_bones)
del ft_bones[2]
del ft_bones[2]
print(ft_bones)
# ___________________
#
# TASK 3
#
# [ ] pop() and print the first and last items from the ft_bones list
ft_bones = ["calcaneus", "talus", "cuboid", "navicular", "lateral cuneiform", 
            "intermediate cuneiform", "medial cuneiform"]

print("Last poped:",ft_bones.pop())
print("First poped:",ft_bones.pop(0))

# [ ] print the remaining list
print(ft_bones)
# ___________________
#
# TASK 4 pt 1
#
# Cash Register Input
# create a empty list purchase_amounts
# populate the list with user input for the price of items
# continue adding to list with while until "done" is entered
# can use while True: with break
# print purchase_amounts
# continue to pt 2
#
#[ ] complete the Register Input task above
purchase_amounts = []

while True:
    price = input("Enter price: ")
    if price == "done":
        break
    else:
        purchase_amounts.append(price)
#

print(purchase_amounts)    
# ___________________
#
# TASK 4 pt 2
#
# Cash Register Total
# create a subtotal variable = 0 create a while loop that runs while purchase_amount (is not empty)
# inside the loop
# pop() the last list value cast as a float type
# add the float value to a subtotal variable
# after exiting the loop print subtotal
# be sure to populate purchase_amounts by running pt 1 above
#
# [ ] complete the Register Total task above
subtotal = 0

while purchase_amounts:
    pop_num = float(purchase_amounts.pop())
    subtotal += pop_num
#
print("Subtotal:",subtotal)
# ___________________
#
# TASK 5
#
# [ ] remove one "Poodle" from the list: dogs , or print "no Poodle found"
# [ ] print list before and after
dogs = ["Lab", "Pug", "Poodle", "Poodle", "Pug", "Poodle"]

print("Before:", dogs)

if "Poodle" in dogs:
    dogs.remove("Poodle")
else:
    print("no Poodle found")

print("After:",dogs)
# _____________________
#
# Mod2_2-2_introPy_Practice.ipynb
# ________________________________________________________________
#
# [ ] create and populate list called days_of_week then print it
days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
print(days_of_week)
# _____________________
#
# [ ] after days_of_week is run above, print the days in the list at odd indexes 1,3,5

print (days_of_week[1::2])
# _____________________
#
# Phone letters
# Create a list, phone_letters, where the index 0 - 9 contains the letters for keys 0 - 9.
# 0 = ' ' (a space)
# 1 = '' (empty)
# 2 = 'ABC'
# 3 = 'DEF'
# etc...

# [ ] create and populate list called phone_letters then print it
phone_letters = [" ", "", "ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ" ]

print(phone_letters)
# ______________________
#
# for the 2 cells below
# Use days_of_week list created above
# Run the cell above to make the list available
#
# [ ] create a variable: day, assign day to "Tuesday" using days_of_week[]
# [ ] print day variable

day = days_of_week[1]
print(day)
# ______________________
# PART 2
# [ ] assign day to days_of_week index = 5
# [ ] print day

day = days_of_week[5]
print(day)
# ______________________
#
# for the exercises below
# Use days_of_week list created above
#
# Run the cell defining days_of_week above to make the list available
# [ ] Make up a new day! - append an 8th day of the week to days_of_week 
# [ ] print days_of_week
days_of_week.append("Endsday")
print(days_of_week)
# _____________________
# [ ] Make up another new day - insert a new day into the middle of days_of_week between Wed - Thurs
# [ ] print days_of_week
days_of_week.insert(3,"Midsday")
print(days_of_week)
# _____________________
# [ ]  Extend the weekend - insert a day between Fri & Sat in the days_of_week list
# [ ] print days_of_week
days_of_week.insert(6,"Resterday")
print(days_of_week)
# ______________________
# exercises below assume days_of_week appended/inserted 3 extra days in previous exercises
#
# [ ] print days_of_week 
# [ ] modified week is too long - pop() the last index of days_of_week & print .pop() value
# [ ] print days_of_week

print(days_of_week)
print(days_of_week.pop())
print(days_of_week)
# _______________________
# [ ] print days_of_week 
# [ ] delete (del) the new day added to the middle of the week 
# [ ] print days_of_week

print(days_of_week)
del days_of_week[3]
print(days_of_week)
# _______________________
# [ ] print days_of_week 
# [ ] programmers choice - pop() any day in days_of week & print .pop() value
# [ ] print days_of_week

print(days_of_week)
print(days_of_week.pop(5))
print(days_of_week)
# _______________________
#
# Program: Letter to Number Function
#
# for the exercise below
# Use phone_letters list created above
# Run the cell above to make the list available
# create funtion let_to_num()
# let_to_num() takes input of a single letter, space or empty string stored in an argument variable: letter
# use while key < 10: to try numbers 0 - 9 as index for phone_letters ("key" = phone dial pad key)
# check if letter variable is in the index of phone_letters[key]
# key = 0
# while key < 10:
# if # Create Code: determine if letter is **`in`** any of the phone_letters[key] where key is the index 0 -9:
#    return key
# else:
#    key = key + 1
# return "Not Found"
# return the number or "Not Found"
# call let_to_num() to test the function so it prints the argument and return value with:
# space
# lowercase letter
# different letter, uppercase
# a number
# Bonus: create a special case to check if empty string ("") was submitted
# the problem is that an empty string will be found in all strings as
#
# if "" in "ABC": 
# is True, and is true for any phone_letters, but should return 1
# [ ] create let_to_num()
# 
def let_to_num(letter):
    letter = letter.upper()
    key = 0
    while key < 10:
        if letter in phone_letters[key] and len(letter) > 0:
            return key
            break
        elif len(letter) == 0:
            return 1
            break
        else:
            if key < 9:
                key += 1
            else:
                return "Not found"
                break
#end function

#Testing function
print("Argument: ' ' \tReturn:",let_to_num(" "))
print("Argument: '' \tReturn:",let_to_num(""))
print("Argument: 'A' \tReturn:",let_to_num("A"))
print("Argument: 'a' \tReturn:",let_to_num("a"))
print("Argument: 'qq' \tReturn:",let_to_num("qq"))
print("Argument: 'EE' \tReturn:",let_to_num("EE"))
print("Argument: '1' \tReturn:",let_to_num("1"))
# ______________________________
#
# Challenge: reverse a string
# using
# while
# .pop()
# insert()
# pop() the first item in the list and
#
# [ ] Challenge: write the code for "reverse a string"
my_list = ["A", "B", "C", "D", "E", "F", "G", "H"]
print("Original:",my_list)
i = 1
while i <= len(my_list) :
    my_list.insert(len(my_list)-i,my_list.pop(0))
    i += 1
#
print(" Reverse:",my_list)
# ______________________________
#
# Required_Code_MOD2_IntroPy.ipynb
# ___________________________________________________________________
#
# Program: list-o-matic
# This program takes string input and checks if that string is in a list of strings
#
# if string is in the list it removes the first instance from list
# if string is not in the list the input gets appended to the list
# if the string is empty then the last item is popped from the list
# if the list becomes empty the program ends
# if the user enters "quit" then the program ends
# program has 2 parts
#
# program flow which can be modified to ask for a specific type of item. This is the programmers choice. Add a list of fish, trees, books, movies, songs.... your choice.
# list-o-matic Function which takes arguments of a string and a list. The function modifies the list and returns a message as seen below.

# [] create list-o-matic

# Function list_o_matic

def list_o_matic(str_my,list_my):
    if len(str_my) == 0:
        return list_my.pop() + " popped from list"
    else:
        if str_my in list_my:
            list_my.remove(str_my)
            return "1 instance of " + str_my + " removed from list"
        else:
            list_my.append(str_my)
            return "1 instance of " + str_my + " appended to list"
#end function

# Main program
animals = ["dog", "cat", "fish", "bird", "snake"]

while animals:
    print()
    print("Look at all the animals: ", animals)
    name = input("Enter the name of an animal: ")
    if name.lower() == "quit":
        print("Goodbye!")
        break
    else:
        print(list_o_matic(name,animals))
#end loop
#
