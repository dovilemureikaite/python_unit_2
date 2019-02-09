# Mod3_2-3.1_intro_Python.ipynb
# __________________________________________________________
#
# TASK 1
#
# [ ] create a list of 4 to 6 strings: birds
# print each bird in the list

birds = ["parrot", "robin", "pigeon", "crow", "duck"]

for bird in birds:
    print(bird)
# _____________________
# [ ]  create a list of 7 integers: player_points
# [ ] print double the points for each point value

player_points = [10,4,2,6,24,3,5]
for point_value in player_points:
    print(2*point_value)
# _____________________
#
# [ ] create long_string by concatenating the items in the "birds" list previously created
# print long_string - make sure to put a space betweeen the bird names

long_string = ""

for bird_item in birds:
    long_string += bird_item + " "
    
print("result:", long_string)
# ______________________
#
# TASK 2
#
# [ ] Using cities from the example above iterate throught the list using "for"/"in"
# [ ] Print only cities starting with "m"

only_m = ""
print("cities:",cities)

for city in cities:
    if city.lower().startswith("m"):
        only_m += city + " "

print("only m:",only_m)
#
# _______________________
# [ ] Using cities from the example above iterate throught the list using "for"/"in"
# cities = ["New York", "Shanghai", "Munich", "Tokyo", "Dubai", "Mexico City", "São Paulo", "Hyderabad"]
# [ ] sort into lists with "A" in the city name and without "A" in the name: a_city & no_a_city

a_city = []
no_a_city = []

for city in cities:
    if "a" in city.lower():
        a_city.append(city)
    else:
        no_a_city.append(city)

print("with    'a':",a_city)
print("without 'a':",no_a_city)
# ___________________________
#
# TASK 3
#
# Program: Paint Stock
# check a list for a paint color request and print status of color "found"/"not found"
#
# create list, paint_colors, with 5+ colors
# get user input of string:color_request
# iterate through each color in paint_colors to check for a match with color_request
#
# [ ] complete paint stock

paint_colors = ["red", "green", "blue", "orange", "white", "pink"]
color_request = input("enter a color: ")

for color in paint_colors:
    if color.lower() == color_request.lower():
        print("found",color,"color")
    else:
        print("not found")
#
# ___________________________
#
# TASK 4
#
# Program: Foot Bones Quiz
# Create a function that will iterate through foot_bones looking for a match of a string argument
#
# Call the function 2 times with the name of a footbone
# print immediate feedback for each answer (correct - incorrect)
# print the total # of foot_bones identified
# The program will use the foot_bones list:
# Bonus: remove correct response item from list if correct so user cannot answer same item twice
#
# [ ] Complete Foot Bones Quiz
# foot_bones = ["calcaneus", "talus", "cuboid", "navicular", "lateral cuneiform",
#             "intermediate cuneiform", "medial cuneiform"]

# function
def foot_bones_quiz(search_bone, bones):
    for bone_item in bones:
        if bone_item.lower() == search_bone.lower():
            return "correct"
        else:
            pass
    return "incorrect"
#     

# bones list
foot_bones = ["calcaneus", "talus", "cuboid", "navicular", "lateral cuneiform","intermediate cuneiform", "medial cuneiform"]

# program (with bonus version)
i = 0
total = 0
while i < 2: 
    bone = input("Enter a bone: ")
    print(foot_bones_quiz(bone, foot_bones))
    if foot_bones_quiz(bone, foot_bones) == "correct":
        total += 1
        foot_bones.remove(bone)
    else:
        pass
    i += 1
# end while cycle

# print total
print ("Total:",total)
# ______________________
#
# Mod3_2-3.2_intro_Python.ipynb
# _________________________________________________________
#
# TASK 1
#
# [ ] for x = 6, use range(x) to print the numbers 1 through 6
x = 6
for count in range(1,x+1):
    print(count)
# _________________
#
# [ ] using range(x) multiply the numbers 1 through 7
# 1x2x3x4x5x6x7 = 5040

total = 1
for number in range(1,8):
    total = total * number
    print(total)
print("result:",total)
#
# __________________
# [ ] print the second half of a spelling list using a range(stop) loop to iterate the list
spell_list = ["Wednesday", "Tuesday", "February", "November", "Annual", "Calendar", "Solstice"]

# length of 2nd half of list
half_2 = int(len(spell_list)/2)

for word in range(half_2,len(spell_list)):
    print(spell_list[word])
# ___________________
#
# TASK 2
#
# # [ ] using range(start,stop), .append() the numbers 5 to 15 to the list: five_fifteen
# [ ] print list five_fifteen

five_fifteen = []

print("before append:",five_fifteen)

for num in range(5,16):
    five_fifteen.append(num)
#
print ("after  append:",five_fifteen)
# ____________________
# [ ] using range(start,stop) - print the 3rd, 4th and 5th words in spell_list
# output should include "February", "November", "Annual"
spell_list = ["Tuesday", "Wednesday", "February", "November", "Annual", "Calendar", "Solstice"]

for word in range(2,5):
    print(spell_list[word])
#
# _____________________
# [ ] using code find the index of "Annual" in spell_list
# [ ] using range, print the spell_list including "Annual" to end of list
spell_list = ["Tuesday", "Wednesday", "February", "November", "Annual", "Calendar", "Solstice"]

ind = spell_list.index("Annual")

for word in range(ind,len(spell_list)):
    print(spell_list[word])
#
# ______________________
#
# TASK 3
#
# [ ] print numbers 10 to 20 by 2's using range

for num in range(10,21,2):
    print(num)
# ________________________
# [ ] print numbers 20 to 10 using range (need to countdown)
# Hint: start at 20

for num in range(20,9,-1):
    print(num)
# _________________________
# [ ] print first and every third word in spell_list
spell_list = ["Tuesday", "Wednesday", "February", "November", "Annual", "Calendar", "Solstice"]

for word in range(0,len(spell_list),3):
    print(spell_list[word])
#
# __________________________
#
# TASK 4
#
# Program: List of letters
# Input a word string (word)
# find the string length of word
# use range() to iterate through each letter in word (can use to range loops)
# Save odd and even letters from the word as lists
# odd_letters: starting at index 0,2,...
# even_letters: starting at index 1,3,...
# print odd and even lists
#
# [ ] complete List of letters program- test with the word "complexity"

word = input("Enter a word: ")
word_length = len(word)

odd_letters = []
even_letters = []

# odd letters
for odd_ltr in range(0,word_length,2):
    odd_letters.append(word[odd_ltr])
#

# even letters
for even_ltr in range(1,word_length,2):
    even_letters.append(word[even_ltr])
#

print("odd  letters:",odd_letters)
print("even letters:",even_letters)
# ___________________
#
# TASK 5
#
# [ ] fix the error printing odd numbers 1 - 9
for num in range(1,10,2):
    print(num)
# ____________________
#
# Mod3_2-3.3_intro_Python.ipynb
# ________________________________________________________________
#
# TASK 1
#
# [ ] extend the list common_birds with list birds_seen which you must create
common_birds = ["chicken", "blue jay", "crow", "pigeon"]
birds_seen = ["parrot","robin","magpie"]

common_birds.extend(birds_seen)

print(common_birds)
# ________________
#
# [ ] Create 2 lists zero_nine and ten_onehundred that contain 1-9, and 10 - 100 by 10's.
# [ ] use list addition to concatenate the lists into all_num and print

zero_nine = list(range(1,10))
ten_onehundred = list(range(10,101,10))
all_num = zero_nine + ten_onehundred

print(zero_nine)
print(ten_onehundred)
print(all_num)
# ___________________
#
# TASK 2
#
# [ ] create and  print a list of multiples of 5 from 5 to 100
# { ] reverse the list and print

multi_five = list(range(5,101))
multi_five_new = []

for num in multi_five:
    if num/5 == int(num/5):
        multi_five_new.append(num)
    else:
        pass

print("Before reverse:",multi_five_new)

multi_five_new.reverse()


print("After  reverse:",multi_five_new)    
# ________________
#
# [ ] Create two lists: fours & more_fours containing multiples of four from 4 to 44
# [ ] combine and print so that the output is mirrored [44, 40,...8, 4, 4, 8, ...40, 44]

generated_list = list(range(4,45))
fours = []
more_fours = []

for num in generated_list:
    if num/4 == int(num/4):
        fours.append(num)
        more_fours.append(num)
    else:
        pass

print("     fours:",fours)
print("more_fours:",more_fours)

fours.reverse()

combined = fours + more_fours

print("  mirrored:",combined)
# ________________
#
# TASK 3
#
# [ ] print cites from visited_cities list in alphbetical order using .sort()
# [ ] only print cities that names start "Q" or earlier
visited_cities = ["New York", "Shanghai", "Munich", "Tokyo", "Dubai", "Mexico City", "São Paulo", "Hyderabad"]

visited_cities.sort()

for city in visited_cities:
    if city[0]<="Q":
        print(city)
    else:
        pass
#
# _________________
#
# [ ] make a sorted copy (sorted_cities) of visited_cities list
# [ ] remove city names 5 characters or less from sorted_cities 
# [ ] print visitied cites and sorted cities
visited_cities = ["New York", "Shanghai", "Munich", "Tokyo", "Dubai", "Mexico City", "São Paulo", "Hyderabad"]

sorted_cities = sorted(visited_cities)

print("visited cities:",visited_cities)
print(" sorted cities:",sorted_cities)

for city in sorted_cities:
    if len(city) <= 5:
        sorted_cities.remove(city)
    else:
        pass

print("  after remove:", sorted_cities)
# __________________
#
# TASK 4
#
# Program: Merge & Sort Animals
# Create a program that
# takes user to build a list: add_animals
# merges add_anmials with exisiting list: anmimals
# provides a sorted list to view in alpa or reverse alpha order
#
# step 1 get user input to build add_animals list
#
# [ ] build a list (add_animals) using a while loop, stop adding when an empty string is entered
add_animals = []

while True:
    anim = input("Enter animal:").title()
    if anim != "":
        add_animals.append(anim)
    else:
        break
#
print(add_animals)
#
# step 2 Merge the lists: add_animals into animals
#
# [ ] extend the lists into animals, then sort 
animals = ["Chimpanzee", "Panther", "Wolf", "Armadillo"]

animals.extend(add_animals)

print(animals)
# sort is used in the step no.3 (Dovile)
#
# step 3 Allow animals list to be viewed alpha or reverse alpha order
#
# [ ] get input if list should be viewed alpha or reverse alpha and display list

order = input("How to sort? (A - for alpha, R - for reverse): ")

if order.upper() == "A":
    animals.sort()
    print(animals)
elif order.upper() == "R":
    animals.sort()
    animals.reverse()
    print(animals)
else:
    print("! Wrong entered value")
# ___________________
#
# Mod3_2-3.4_intro_Python.ipynb
# ____________________________________________________________________
#
# TASK 1
#
# [ ] split the string(rhyme) into a list of words (rhyme_words)
# [ ] print each word on it's own line
rhyme = 'Jack and Jill went up the hill To fetch a pail of water' 

rhyme_words = rhyme.split()

for word in rhyme_words:
    print(word)
# ________________
#
# [ ] split code_tip into a list and print the first and every other word
code_tip = "Python uses spaces for indentation"

code_words = code_tip.split()

for word in range(0,len(code_words),2):
    print(code_words[word])
# _________________
#
# TASK 2
#
# [ ] split poem into a list of phrases by splitting on "*" a
# [ ] print each phrase on a new line in title case
poem = "Write code frequently*Save code frequently*Comment code frequently*Study code frequently*"

poem_words = poem.split("*")

for word in poem_words:
    print(word.title())
# __________________
#
# TASK 3
#
# [ ] .join() letters list objects with an Asterisk: "*"
letters = ["A", "s", "t", "e", "r", "i", "s", "k"]

print("*".join(letters))
# ___________________
#
# TASK 4
#
# Program: Choose the separator
# get user input on what to use to join words (" ", *, -, etc...) - store in variable: separator
# join pharse_words with the separator and print
# [ ] complete Choose the separator
phrase_words = ['Jack', 'and', 'Jill', 'went', 'up', 'the', 'hill', 'To', 'fetch', 'a', 'pail', 'of', 'water']

separator = input("Enter 'separator': ")

print(separator.join(phrase_words))
# ____________________
#
# TASK 5
#
# [ ] use 3 print() statements to output text to one line 
# [ ] separate the lines by using "- " (dash space)

print("Monday", end="- ")
print("Tuesday", end="- ")
print("Wednesday")
# _____________________
#
# TASK 6
#
# [ ] create a string (fact) of 20 or more characters and cast to a list (fact_letters)
# [ ] iterate fact, printing each char on one line, except for spaces print a new line

fact = "always save your work"
fact_letters = list(fact)

print("List: ",fact_letters)

for ltr in fact:
    if ltr == " ":
        print(ltr, end="\n")
    else:
        print(ltr, end="")
# _____________________
#
# TASK 7
#
# Program: add the digits
# create a 20 digit string, and cast to a list
# then add all the digits as integers
# print the equation and answer
# Hint: use cast to sum the digits, and .join() to create the equation (1+2+3+...)
# [ ] create add the digits

# [ ] create add the digits
digit_str = "1 2 3 4"
digit_list = digit_str.split(" ")

sum = 0
for digit in digit_list:
    sum = sum + int(digit)

print("+".join(digit_list) + "=",sum)
# _____________________
#
# Mod3_2-3_IntroPy_Practice.ipynb
# _______________________________________________________________________
#
# TASK 1
#
# [ ] print out the "physical states of matter" (matter_states) in 4 sentences using list iteration
# each sentence should be of the format: "Solid - is state of matter #1" 
matter_states = ['solid', 'liquid', 'gas', 'plasma']

for state in matter_states:
    print(state.title() + " - state of matter #" + str(matter_states.index(state)+1))
# __________________
#
# [ ] iterate the list (birds) to see any bird names start with "c" and remove that item from the list
# print the birds list before and after removals
birds = ["turkey", "hawk", "chicken", "dove", "crow"]

print("Before removal:",birds)

for bird in birds:
    if bird.lower().startswith("c"):
        birds.remove(bird)
    else:
        pass

print(" After removal:",birds)
# __________________
#
# the team makes 1pt, 2pt or 3pt baskets
# [ ] print the occurace of each type of basket(1pt, 2pt, 3pt) & total points using the list baskets
baskets = [2,2,2,1,2,1,3,3,1,2,2,2,2,1,3]

pt1 = 0
pt2 = 0
pt3 = 0
total = 0

for bsk in baskets:
    if bsk == 1:
        pt1 = baskets.count(bsk)
    elif bsk == 2:
        pt2 = baskets.count(bsk)
    elif bsk == 3:
        pt3 = baskets.count(bsk)
    else:
        pass

print("basket 1pt:",pt1)
print("basket 2pt:",pt2)
print("basket 3pt:",pt3)
print("     total:",pt1+pt2+pt3)
# ___________________
#
# TASK 2
#
# [ ] using range() print "hello" 4 times

for x in range(4):
    print("hello")
# ___________________
#
# [ ] find spell_list length
# [ ] use range() to iterate each half of spell_list  
# [ ] label & print the first and second halves
spell_list = ["Tuesday", "Wednesday", "February", "November", "Annual", "Calendar", "Solstice"]

spl_length= len(spell_list)

print ("First half:")
for word in range(0,int(spl_length/2)):
    print(spell_list[word], end=" ")

print ("\nSecond half:")
for word in range(int(spl_length/2),spl_length):
    print(spell_list[word],end=" ")
# _____________________
# [ ] build a list of numbers from 20 to 29: twenties 
# append each number to twenties list using range(start,stop) iteration
# [ ] print twenties
twenties = []

for num in range(20,30):
    twenties.append(num)

print(twenties)
# _____________________
# [ ] iterate through the numbers populated in the list twenties and add each number to a variable: total
# [ ] print total
total = 0

for num in twenties:
    total = total + num

print("Total:",total)
# ______________________
# check your answer above using range(start,stop)
# [ ] iterate each number from 20 to 29 using range()
# [ ] add each number to a variable (total) to calculate the sum
# should match earlier task 
total = 0

for num in range(0,len(twenties)):
    total = total + twenties[num]

print("Total:",total)
# ______________________
#
# TASK 3
#
# [ ] create a list of odd numbers (odd_nums) from 1 to 25 using range(start,stop,skip)
# [ ] print odd_nums
# hint: odd numbers are 2 digits apart

odd_nums = list(range(1,26,2))

print(odd_nums)
# _______________________
#
# [ ] create a Decending list of odd numbers (odd_nums) from 25 to 1 using range(start,stop,skip)
# [ ] print odd_nums,  output should resemble [25, 23, ...]

# way no.1
odd_nums = list(range(25,0,-2))
print("no.1:",odd_nums)

#way no.2
odd_nums_b = list(range(1,26,2))
odd_nums_b.reverse()
print("no.2:",odd_nums_b)
# ________________________
#
# the list, elements, contains the names of the first 20 elements in atomic number order
# [ ] print the even number elements "2 - Helium, 4 - Beryllium,.." in the list with the atomic number
elements = ['Hydrogen', 'Helium', 'Lithium', 'Beryllium', 'Boron', 'Carbon', 'Nitrogen', 'Oxygen', 'Fluorine', \
 'Neon', 'Sodium', 'Magnesium', 'Aluminum', 'Silicon', 'Phosphorus', 'Sulfur', 'Chlorine', 'Argon', \
 'Potassium', 'Calcium']

for el in range(1,len(elements),2):
    print(el+1,"-",elements[el], end=" ")
# _______________________
# [ ] # the list, elements_60, contains the names of the first 60 elements in atomic number order
# [ ] print the odd number elements "1 - Hydrogen, 3 - Lithium,.." in the list with the atomic number elements_60
elements_60 = ['Hydrogen', 'Helium', 'Lithium', 'Beryllium', 'Boron', 'Carbon', 'Nitrogen', \
 'Oxygen', 'Fluorine', 'Neon', 'Sodium', 'Magnesium', 'Aluminum', 'Silicon', \
 'Phosphorus', 'Sulfur', 'Chlorine', 'Argon', 'Potassium', 'Calcium', 'Hydrogen', \
 'Helium', 'Lithium', 'Beryllium', 'Boron', 'Carbon', 'Nitrogen', 'Oxygen', 'Fluorine', \
 'Neon', 'Sodium', 'Magnesium', 'Aluminum', 'Silicon', 'Phosphorus', 'Sulfur', 'Chlorine', \
 'Argon', 'Potassium', 'Calcium', 'Scandium', 'Titanium', 'Vanadium', 'Chromium', 'Manganese', \
 'Iron', 'Cobalt', 'Nickel', 'Copper', 'Zinc', 'Gallium', 'Germanium', 'Arsenic', 'Selenium', \
 'Bromine', 'Krypton', 'Rubidium', 'Strontium', 'Yttrium', 'Zirconium']

for el in range(0,len(elements_60),2):
    print(el+1,"-",elements_60[el], end=" ")
# ________________________
#
# TASK 4
#
# [ ] print the combined lists (numbers_1 & numbers_2) using "+" operator
numbers_1 = [20, 21, 22, 23, 24, 25, 26, 27, 28, 29]

# pythonic casting of a range into a list
numbers_2 = list(range(30,50,2))

print("numbers_1:",numbers_1)
print("numbers_2:",numbers_2)

print(" combined:",numbers_1 + numbers_2)
# ________________________
# [ ] print the combined element lists (first_row & second_row) using ".extend()" method
first_row = ['Hydrogen', 'Helium']
second_row = ['Lithium', 'Beryllium', 'Boron', 'Carbon', 'Nitrogen', 'Oxygen', 'Fluorine', 'Neon']

first_row.extend(second_row)

print("1st Row:", first_row)
print("2nd Row:", second_row)
# _________________________
#
# Project: Combine 3 element rows
# Choose to use *"+" or ".extend()" *to build output similar to
#
# The 1st three rows of the Period Table of Elements contain:
# ['Hydrogen', 'Helium', 'Lithium', 'Beryllium', 'Boron', 'Carbon', 'Nitrogen', 'Oxygen', 'Fluorine', 'Neon', 'Sodium', 'Magnesium', 'Aluminum', 'Silicon', 'Phosphorus', 'Sulfur', 'Chlorine', 'Argon']
#
# The row breakdown is
# Row 1: Hydrogen, Helium
# Row 2: Lithium, Beryllium, Boron, Carbon, Nitrogen, Oxygen, Fluorine, Neon
# Row 3: Sodium, Magnesium, Aluminum, Silicon, Phosphorus, Sulfur, Chlorine, Argon
#
# [ ] create the program: combined 3 element rows 

elem_1 = ['Hydrogen', 'Helium'] 
elem_2 = ['Lithium', 'Beryllium', 'Boron', 'Carbon', 'Nitrogen', 'Oxygen', 'Fluorine', 'Neon']
elem_3 = ['Sodium', 'Magnesium', 'Aluminum', 'Silicon', 'Phosphorus', 'Sulfur', 'Chlorine', 'Argon']

print("The 1st three rows of the Period Table of Elements contain:")
print(elem_1 + elem_2 + elem_3)
# __________________
#
# [ ] .extend() jack_jill with "next_line" string - print the result
jack_jill = ['Jack', 'and', 'Jill', 'went', 'up', 'the', 'hill']
next_line = ['To', 'fetch', 'a', 'pail', 'of', 'water']

jack_jill.extend(next_line)
print(jack_jill)
# ___________________
#
# TASK 5
#
# [ ] use .reverse() to print elements starting with "Calcium", "Chlorine",... in reverse order
elements = ['Hydrogen', 'Helium', 'Lithium', 'Beryllium', 'Boron', 'Carbon', 'Nitrogen', 'Oxygen', 'Fluorine', \
 'Neon', 'Sodium', 'Magnesium', 'Aluminum', 'Silicon', 'Phosphorus', 'Sulfur', 'Chlorine', 'Argon', \
 'Potassium', 'Calcium']

elements.reverse()
print(elements)
# ______________________
#
# [ ] reverse order of the list... Then print only words that are 8 characters or longer from the now reversed order
spell_list = ["Tuesday", "Wednesday", "February", "November", "Annual", "Calendar", "Solstice"]

spell_list.reverse()

for word in spell_list:
    if len(word) >= 8:
        print(word)
    else:
        pass
# _____________________
#
# TASK 6
#
# [ ] sort the list element, so names are in alphabetical order and print elements
elements = ['Hydrogen', 'Helium', 'Lithium', 'Beryllium', 'Boron', 'Carbon', 'Nitrogen', 'Oxygen', 'Fluorine', \
 'Neon', 'Sodium', 'Magnesium', 'Aluminum', 'Silicon', 'Phosphorus', 'Sulfur', 'Chlorine', 'Argon', \
 'Potassium', 'Calcium']

elements.sort()

print(elements)
# _____________________
#
# [ ] print the list, numbers, sorted and then below print the original numbers list 
numbers = [2,2,2,1,2,1,3,3,1,2,2,2,2,1,3]

print("  sorted:",sorted(numbers))
print("original:",numbers)
# ______________________
#
# TASK 7
#
# [ ] split the string, daily_fact, into a list of word strings: fact_words
# [ ] print each string in fact_words in upper case on it's own line
daily_fact = "Did you know that there are 1.4 billion students in the world?"

fact_words = daily_fact.split()

for word in fact_words:
    print(word.upper())
# ________________________
#
# [ ] convert the string, code_tip, into a list made from splitting on the letter "o"

code_tip = "Did you know that there are 1.4 billion students in the world?"
code_after = code_tip.split("o")
print(code_after)
# _________________________
# [ ] split poem on "b" to create a list: poem_words
# [ ] print poem_words by iterating the list
poem = "The bright brain, has bran!"

poem_words = poem.split("b")

for word in poem_words:
    print(word)
# _________________________
#
# TASK 8
#
# [ ] print a comma separated string output from the list of Halogen elements using ".join()"
halogens = ['Chlorine', 'Florine', 'Bromine', 'Iodine']

print(",".join(halogens))
# __________________________
#
# [ ] split the sentence, code_tip, into a words list
# [ ] print the joined words in the list with no spaces in-between
# [ ] Bonus: capitalize each word in the list before .join()
code_tip ="Read code aloud or explain the code step by step to a peer"

code_list = code_tip.split()
print("splitted:",code_list)

#Bonus
for word in range(0,len(code_list)):
    code_list[word] = code_list[word].title()

print("   upper:",code_list)
print("  joined:","".join(code_list))
# _____________________________
#
# TASK 8 (second part)
#
# [ ] cast the long_word into individual letters list 
# [ ] print each letter on a line
long_word = 'decelerating'

letters = list(long_word)

for ltr in letters:
    print(ltr, end="")
# __________________
# [ ] use use end= in print to output each string in questions with a "?" and on new lines
questions = ["What's the closest planet to the Sun", "How deep do Dolphins swim", "What time is it"]

for word in questions:
    print(word, end="?\n")
# ____________________
# [ ] print each item in foot bones 
#    - capitalized, both words if two word name
#    - separated by a comma and space
#    - and keeping on a single print line
foot_bones = ["calcaneus", "talus", "cuboid", "navicular", "lateral cuneiform", 
            "intermediate cuneiform", "medial cuneiform"]

for i in range(0,len(foot_bones)):
    foot_bones[i] = foot_bones[i].title()
    if i == len(foot_bones)-1:
        print(foot_bones[i])
    else:
        print(foot_bones[i], end=", ")
        pass
# _____________________
#
# Required_Code_MOD3_IntroPy.ipynb
# _____________________________________________________________________
#
# Program: poem mixer
# This program takes string input and then prints out a mixed order version of the string
# Program Parts
# program flow gathers the word list, modifies the case and order, and prints
# get string input, input like a poem, verse or saying
# split the string into a list of individual words
# determine the length of the list
# Loop the length of the list by index number and for each list index:
# if a word is short (3 letters or less) make the word in the list lowercase
# if a word is long (7 letters or more) make the word in the list uppercase
# call the word_mixer function with the modified list
# print the return value from the word_mixer function
# word_mixer Function has 1 argument: an original list of string words, containing greater than 5 words and the function returns a new list.
# sort the original list
# create a new list
# Loop while the list is longer than 5 words:
# in each loop pop a word from the sorted original list and append to the new list
# pop the word 5th from the end of the list and append to the new list
# pop the first word in the list and append to the new list
# pop the last word in the list and append to the new list
# return the new list on exiting the loop
#
# [] create poem mixer
# [] copy and paste in edX assignment page

#function
def word_mixer(words_list):
    words_list.sort()
    new_words = []
    while len(words_list) > 5:
        new_words.append(words_list.pop(-5))
        new_words.append(words_list.pop(0))
        new_words.append(words_list.pop(len(words_list)-1))
    return new_words
#        

#main program
user_input = input("Enter a saying or poem: \n")
words_list = user_input.split()
len_list = len(words_list)

for i in range(0,len_list):
    if len(words_list[i]) <= 3:
        words_list[i] = words_list[i].lower()
    elif len(words_list[i]) >=7:
        words_list[i] = words_list[i].upper()
    else:
        pass

print()
#result = word_mixer(words_list)
print("RESULT:"," ".join(word_mixer(words_list)))
#
#
