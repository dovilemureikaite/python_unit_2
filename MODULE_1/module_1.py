# Mod1_2-1.1_Intro_Python.ipynb
# _______________________________________________________
# 
## TASK 1
#
# [ ] assign a string 5 or more letters long to the variable: street_name
# [ ] print the 1st, 3rd and 5th characters
street_name = "Gedimino"
print("1st:",street_name[0])
print("3rd:",street_name[2])
print("5th:",street_name[4])
# ___________________________
#
# [ ] Create an input variable: team_name - ask that second letter = "i", "o", or "u"
# [ ] Test if team_name 2nd character = "i", "o", or "u" and print a message
# note: use if, elif and else
team_name = input("Enter team name: ")
if team_name[1].lower() == "i":
    print("2nd character is i")
elif team_name[1].lower() == "o":
    print("2nd character is o")
elif team_name[1].lower() == "u":
    print("2nd character is u")
else:
    print("2nd character is not i, o or u")
# ____________________________
#
## TASK 2
#
# [ ] assign a string 5 or more letters long to the variable: street_name
# [ ] print the last 3 characters of street_name
street_name = "Goldenroad"
print("1st from the end:",street_name[-1])
print("2nd from the end:",street_name[-2])
print("3rd from the end:",street_name[-3])
# ____________________________
#
# [ ] create and assign string variable: first_name
first_name = "Dovile"
# [ ] print the first and last letters of name
print("First letter:",first_name[0])
print("Last letter:",first_name[-1])
# ____________________________
#
## TASK 3
#
# [ ] Review, Run, Fix the error using string index
shoe = "tennis"
# print the last letter
print(shoe[-1])
# ____________________________
#
# Mod1_2-1.2_Intro_Python.ipynb
# __________________________________________________________
#
## TASK 1
#
# [ ] slice long_word to print "act" and to print "tic"
long_word = "characteristics"

print(long_word[4:7])
print(long_word[11:14])
# _____________________________
#
# [ ] slice long_word to print "sequence"
long_word = "Consequences"
print(long_word[3:11])
# _____________________________
#
## TASK 2
#
# [ ] print the first half of the long_word
long_word = "Consequences"
print(long_word[:6])
# _____________________________
#
## TASK 3
#
# [ ] print the second half of the long_word
long_word = "Consequences"
print(long_word[6:])
# _____________________________
#
## TASK 4
#
# [ ] print the 1st and every 3rd letter of long_word
long_word = "Acknowledgement"
print(long_word[::3])
# _____________________________
#
# [ ] print every other character of long_word starting at the 3rd character
long_word = "Acknowledgement"
print(long_word[2::2])
# _____________________________
#
## TASK 5
#
# [ ] reverse long_word
long_word = "stressed"
print(long_word[::-1])
# _____________________________
#
# [ ] print the first 5 letters of long_word in reverse
long_word = "characteristics"
print(long_word[4::-1])
# _____________________________
#
## TASK 6
#
# [ ] print the first 4 letters of long_word
# [ ] print the first 4 letters of long_word in reverse
# [ ] print the last 4 letters of long_word in reverse
# [ ] print the letters spanning indexes 3 to 6 of long_word in Reverse
long_word = "timeline"
print(long_word[:4])
print(long_word[3::-1])
print(long_word[:3:-1])
print(long_word[6:2:-1])
# _____________________________
#
# Mod1_2-1.3_Intro_Python.ipynb
# __________________________________________________________
#
## TASK 1
#
# [ ] Get user input for first_name
# [ ] iterate through letters in first_name 
#    - print each letter on a new line
first_name = input("Enter first name: ")
for ltr in first_name:
    print(ltr)
# end
# ____________________________
#
## TASK 2
#
# Program: capitalize-io
# get user input for first_name
# create an empty string variable: new_name
# iterate through letters in first_name
# add each letter in new_name
# capitalize if letter is an "i" or "o" *(hint: if, elif, else)
# print new_name
#
# [ ] Create capitalize-io
first_name = input("Enter first name: ")
new_name = ""
for ltr in first_name:
    if ltr == "i":
        new_name += ltr.upper()
    elif ltr == "o":
        new_name += ltr.upper()
    else:
        new_name += ltr
# end
print (new_name)
# _____________________________
#
## TASK 3
#
# [ ] create & print a variable, other_word, made of every other letter in long_word
long_word = "juxtaposition"
other_word = ""

for ltr in long_word[::2]:
    other_word += ltr
# end
print(other_word)
# _____________________________
#
# Mirror Color
# [ ] get user input, fav_color
# [ ] print fav_color backwards + fav_color
# example: "Red" prints "deRRed"

fav_color = input("Enter favourite color: ")
new_color = ""

for ltr in fav_color[::-1]:
    new_color += ltr
# end
print(new_color + fav_color)
# ______________________________
#
# Mod1_2-1.4_Intro_Python.ipynb
# ______________________________________________________
#
## TASK 1
#
# [ ] use len() to find the midpoint of the string 
# [ ] print the halves on separate lines
random_tip = "wear a hat when it rains"
point = int(len(random_tip)/2)

print("First half:",random_tip[:point])
print("Second half:",random_tip[point:])
# ______________________________
#
## TASK 2
#
## for letters: "e" and "a" in random_tip
# [ ] print letter counts 
# [ ] BONUS: print which letter is most frequent
random_tip = "wear a hat when it rains"

print("e:",random_tip.count("e"))
print("a:",random_tip.count("a"))

if random_tip.count("e") > random_tip.count("a"):
    print("\"e\" is most frequent")
elif random_tip.count("a") > random_tip.count("e"):
    print("\"a\" is most frequent")
else:
    print("Equal")
# ______________________________
#
## TASK 3
#
# [ ] print long_word from the location of the first and second "t"
long_word = "juxtaposition"
print("First \"t\":",long_word.find("t"))
print("Second \"t\":",long_word.find("t",long_word.find("t")+1))
print(long_word[long_word.find("t"):long_word.find("t",long_word.find("t")+1)+1])
# _______________________________
#
## TASK 4
#
# Program: print each word in a quote
# start = 0
# space_index = quote.find(" ")
# while space_index != -1:
# code to print word (index slice start:space_index)
#Output should look like below:
# they
# stumble
# who
# run
# fast
#
# [ ] Print each word in the quote on a new line  
quote = "they stumble who run fast"

start = 0
space_index = quote.find(" ")

while space_index != -1:
    print(quote[start:space_index])
    start = space_index+1
    space_index = quote.find(" ",space_index+1)
    
    if space_index == -1:
        print(quote[start:])
#
#
# Mod1_2-1_IntroPy_Practice.ipynb
# __________________________________________________________
#
## TASK 1
#
# [ ] access and print the second character from planet_name: "u"
planet_name = "Jupiter"

print(planet_name[1])
# ____________________________
#
# [ ] access and print the first character from planet_name: "J"
planet_name = "Jupiter"

print(planet_name[0])
# _____________________________
#
# [ ] access and print the first and last characters from planet_name
planet_name = "Jupiter"

print("First character:",planet_name[0])
print("Last character:",planet_name[-1])
# _____________________________
#
# [ ] using a negative index access and print the first character from planet_name: "J"
planet_name = "Jupiter"

print(planet_name[-7])
# _____________________________
#
## TASK 2
#
# [ ] print planet_name sliced into the first 3 characters and remaining characters
planet_name = "Neptune"

print(planet_name[:3])
print(planet_name[3:])
# _____________________________
#
# [ ] print 1st char and then every 3rd char of wise_words
# use string slice with a step
wise_words = 'Play it who opens'

print(wise_words[::3])
# ______________________________
#
# [ ] print planet_name in reverse

print(planet_name[::-1])
# _______________________________
#
## TASK 3
#
# [ ] Get user input for 1 fav_food
# [ ] iterate through letters in fav_food 
#    - print each letter on a new line

fav_food = input("Enter favourite food: ")
for ltr in fav_food:
    print(ltr)
# end
# _______________________________
#
# [ ] iterate work_tip string concatenate each letter to variable: new_string 
# [ ] concatenate the letter or a "-" instead of a space " "
# tip: concatenate string example: word = word + "a"
work_tip = "Good code is commented code"
new_string = ""
for ltr in work_tip:
    if ltr == " ":
        new_string += "-"
    else:
        new_string += ltr
# end
print (new_string)
# _______________________________
#
# [ ] Print the first 4 letters of name on new line
name = "Hiroto"
for ltr in name[:4]:
    print(ltr)
# ________________________________
#
# [ ] Print every other letter from 2nd to last letter of name 
name = "Hiroto"
print(name[1::2])
# ________________________________
#
## TASK 4 (first)
#
# Program: Mystery Name
# get user input for first_name
# create an empty string variable: new_name
# iterate through letters in first_name Backwards
# add each letter to new_name as you iterate
# Replace the letter if "e", "t" or "a" with "?" (hint: if, elif, elif, else)
# print new_name
# example: "Alton" = "no?l?"
#
# [ ] Create Mystery Name

first_name = input("Enter first name: ")
new_name = ""
for ltr in first_name[::-1]:
    if ltr.lower() == "e":
        new_name += "?"
    elif ltr.lower() == "t":
        new_name += "?"
    elif ltr.lower() == "a":
        new_name += "?"
    else:
        new_name += ltr
# end
print (new_name)
# __________________________________
#
## TASK 4 (second)
#
# [ ] find and display the length of the string: topic
topic = "len() returns the length of a string"
print(len(topic))
# __________________________________
#
# [ ] use len() to find and display the mid_pt (middle) index (+/- 1) of the string: topic
# note: index values are whole numbers
topic = "len() can take a sequence, like a string, as an argument"
mid_pt = int(len(topic)/2)
print(mid_pt)
# ___________________________________
#
# [ ] print index where first instance of the word  "code" starts using .find()
work_tip = "Good code is commented code"
print(work_tip.find("code"))
# ____________________________________
# [ ] search for "code" in code_tip using .find() 
# [ ] search substring with substring index start= 13,end = last char 
# [ ] save result in variable: code_index
# [ ] display index of where "code" is found, or print "not found" if code_index == -1
work_tip = "Good code is commented code"
code_index = work_tip.find("code",13)
if code_index == -1:
    print("Not found")
else:
    print("Code index =",code_index)
#end
# _____________________________________
#
## TASK 5
#
# [ ] find and report (print) number of w's, o's + use of word "code"
work_tip = "Good code is commented code"
print("count 'w' =",work_tip.count("w"))
print("count 'o' =",work_tip.count("o"))
print("count 'code' =",work_tip.count("code"))
# _____________________________________
#
# [ ]  count times letter "i" appears in code_tip string
# [ ] find and display the index of all the letter i's in code_tip
# Remember: if .find("i") has No Match, -1 is returned
code_tip = "code a conditional decision like you would say it"
print ("count 'i':" ,code_tip.count("i"))
indx = code_tip.find("i")

while indx >= 0:
    print("'i' at index =", indx)
    indx = code_tip.find("i", indx + 1)
#end
# _____________________________________
#
## TASK 6
#
# Program: Words after "G"/"g"
# Create a program inputs a phrase (like a famous quotation) and prints all of the words that start with h-z
# 
# loop each character in the input string
# check if character is a letter
# add a letter to word each loop until a non-alpha char is encountered
# if character is alpha
# 
# add character to word
# non-alpha detected (space, punctuation, digit,...) defines the end of a word and goes to else
# else
# check if word is greater than "g" alphabetically
# print word
# set word = empty string
# or else
# set word = empty string and build the next word
# Hint: use .lower()
# ---
# [] create words after "G"
# sample quote "Wheresoever you go, go with all your heart" ~ Confucius (551 BC - 479 BC)
# 
# Dovile's comment: space (" ") added to input string so that loop could encounter end of the string
word = ""
phrase = input("Enter a 1 sentence quote, non-alpha separate words: ") + " "

for ltr in phrase:
    if ltr.lower().isalpha():
        word += ltr
    else:
        if (word[0:1].lower() > "g"):
            print(word)
            word = ""
        else:
            word = ""
#
# ________________________
#
# Required_Code_MOD1_IntroPy.ipynb
# ____________________________________________________________
#
# Program: Words after "G"/"g"
# Create a program inputs a phrase (like a famous quotation) and prints all of the words that start with h-z
# split the words by building a placeholder variable: word
#
# loop each character in the input string
# check if character is a letter
# add a letter to word each loop until a non-alpha char is encountered
# if character is alpha
#
# add character to word
# non-alpha detected (space, punctuation, digit,...) defines the end of a word and goes to else
# else
# check if word is greater than "g" alphabetically
# print word
# set word = empty string
# or else
# set word = empty string and build the next word
# Hint: use .lower()
# Consider how you will print the last word if it doesn't end with a non-alpha character like a space or punctuation?
# ---
# [] create words after "G" following the Assignment requirements use of functions, menhods and kwyowrds
# sample quote "Wheresoever you go, go with all your heart" ~ Confucius (551 BC - 479 BC)
# [] copy and paste in edX assignment page
# ---
# Dovile's comment: space (" ") added to input string so that loop could encounter end of the string
word = ""
phrase = input("Enter a 1 sentence quote, non-alpha separate words: ") + " "

for ltr in phrase:
    if ltr.lower().isalpha():
        word += ltr
    else:
        if (word[0:1].lower() > "g"):
            print(word.upper())
            word = ""
        else:
            word = ""
#
# ________________________________
