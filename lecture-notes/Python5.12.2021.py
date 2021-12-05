# List Comprehensions
squares = []


for number in range(1, 11):
    new_squares = number ** 2
    squares.append(new_squares)
    
for square in squares:
    print(square)
    
squares = [number ** 2 for number in range(1, 11)]

print(squares)


# Non-numerical versions
students = ["Jonas", "Yusuf", "diana"]


great_students = []
for student in students:
    great_students.append(student.title() + " the great...")
    
for great_student in great_students:
    print("Hello " + great_student)
    
# great_students = [add " the great" to each student, for each student in the list of students]
great_students = [student.title()  + " The Great!" for student in students]

for great_student in great_students:
    print("Hello " + great_student)
    
    
# Exercises
# 1:
numbs = []

for numb in range(10, 100):
    new_numbs = numb + 10
    numbs.append(new_numbs)
    
for nnum in numbs:
    print(numbs)

#new_numbs = [numbs + 10 for numbs in range(10, 100)]
#print(new_numbs)


# Strings as Lists
s = "Bedir"
for letter in s:
    print(letter)
    
    
ls = list(s)
print(ls)


# Slicing strings
name = "Braddock"
first_ch = name[0]
last_ch = name[-1]

first_4_letters = name[:4]
last_4_letters = name[4:]

print(first_4_letters)
print(last_4_letters)


sentence = "He was the champ!"
print(sentence[3:6])

# Finding substrings
message = "He fought for all!"
all_present = "all" in message
print(all_present)


all_index = message.find("all")
print(all_index)
print(message[all_index:all_index+len("all")])


msg = "Cats and dogs... Cats and dogs..."
print(msg.find("Cats"))

print(msg.rfind("Cats"))

# Replace
print(msg.replace("dogs", "turtels"))




# count
print(msg.count("dogs"))

# Splits
sentence = "The hockey team lost"
ls = sentence.split(" ")
print(ls)


weird_sent = "Here-we-are-why-here"
ls = weird_sent.split("-")
print(ls)
ls = weird_sent.split("w")
print(ls)

# Tuples
# İmmutable - never can change
colors = ("red", "green", "blue")
print(colors[0])

for color in colors:
    print(color)
    
    
# colors.pop()
# colors.append("purple")
# colors[0] = "Red"

# String formatting with numbers
# print("Hi " +  23)
num = 23
print("Hi " + str(num))

print("Hi there beatiful number %d." % num)

ls = [7, 13, 19]
print("Some of the amazing prime numbers are %d, %d, and %d." % (ls[0],ls[1],ls[2]))

print("some tries: %s %d %f" % ("hey there", 3, 3.0))

# %s - string
# %d - int
# %f - floats

print("A float: %.2f" % 3.0)
float_number = 3.0
print(f"A float: {float_number}, {num}")

print("Some of the amazing prime numbers are {}, {}, and {}.".format(ls[0], ls[2], ls[1]))

# Variable types
# String


# Int
a = 2

# Float
b = 3.0

# Bool
# True and False
val = True
val = False

# Basic math operators
a = 3 + 2 # sum
a = 3 - 2 # sub
a = 4 * 2 # mult
a = 5 / 2 # div
a = 5 // 2 # div - wo remainder
a = 5 % 2 # remainder
a = 5 ** 2 # power

# FUNCTIONS
#def function_name(arguments):
    #whatever the action we need
    
# function_name(arguments)

print("You are an amazing person Allie")
print("We are appriciating your existence...")
print("Please spend more time with us.")
print("To enroll, click the button below")

print("You are an amazing person Tarık")
print("We are appriciating your existence...")
print("Please spend more time with us.")
print("To enroll, click the button below")

print("You are an amazing person Bedir")
print("We are appriciating your existence...")
print("Please spend more time with us.")
print("To enroll, click the button below")


def ad_run(name):
    print(f"You are an amazing person {name}!")
    print("We are appriciating your existence...")
    print("Please spend more time with us.")
    print("To enroll, click the button below")
    
    
ad_run("Allie")
ad_run("Tarık")
ad_run("Bedir")
ad_run("Nilgün")

emails = ["em1@gmail.com", "em2@gmail.com", "em3@gmail.com", "em4@gmail.com", ]
message = "No pen, meant pencil"
for email in emails:
    print(f"Sent to: {email}")
    print(f"Message: {message}")
    
new_emails = emails[:2]
def email_students():
    message = "No pen, meant pencil"
for email in new_emails:
    print(f"Sent to: {email}")
    print(f"Message: {message}")

def get_number_of_words(sentence):
    ls = sentence.split(" ")
    return len(ls)

message = "The world is an amazing place!"
lenght = get_number_of_words(message)
print(lenght)

isimler = "bedir", "yusuf", "jonas"

def ad_ad(isimler):
    for i in isimler:
        print(f"You are an amazing person {isimler}!")
        print(f"We are appriciating your existence {isimler}")
        print(f"Please spend more time with us {isimler}")
    
ad_ad(isimler[2])