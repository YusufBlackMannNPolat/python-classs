# Variables
message = "hello world, people!"
print (message)


message = "Well, new one!"
print (message)

# Naming Rules
# Can: Letters, Numbers, Underscores
message_25 = "25 is here"

# Can't: Start w numbers or underscore
# 2message = "Can't do"
# - No spaces
# message 1
# - No keywords
# int, if, for, etc.

# Best Practices:
# - Short but descriptive
h_message = "Hello World"

# NameError
# print(h_messageee)

# Exercises

# 1- Print a description of yourself, stored in a variable with description name.
desmyself = "hello my name is yusuf, Im 18, i love software works"
print (desmyself)
# 2- Change the value of the variable to something else and print it.
desmyself = "Changed"
print (desmyself)

#String
ch = 'a'
ch = "a"
print(type(desmyself))

#Functions
name = "yusuf polat"
print(name.title())
print(name.upper())
print(name.lower())

# String concatenation
name = "Yusuf"
last_name = "Polat"
print(name + " " + last_name)

full_name = name + " " + last_name
print(full_name)

# Whitespace
print("Hello World!")
print("Hello")

# Stripping Whitespaces
name = "        Yusuf "
print(name.lstrip() + "Polat")
# Left strip
print(name.rstrip() + "Polat")
print(name.strip() + "Polat")
print(name.strip().lstrip() + "Polat")


# Exercises:
# -1
name = "Yusuf".lower()
print (name)
print (name.lower())
print (name.title())
print (name.upper())

# -2
firstname = "Yusuf"
lastname = "Polat"

fullname = firstname + lastname
print(fullname)

# -3
firstname = "Yusuf"
lastname = ""



# -4





# Numbers
# Integer
print(3 + 2)
print(3 - 2)
print(3 * 2)
print(3 / 2)

# power
print(5 ** 2)

calc = 5 + 2 * 2
print(calc)

calc = (5 + 2) * 2
print(calc)

# Floating-Point numbers
print(0.1 + 0.1)

print(0.1 + 0.2)

# Exercises:
# -1
print(5 + 5)
print(4 - 4)
print(7 * 2)
print(6 / 2)


# -2


# -3
print(0.1 * 0.2)

# -Write a pr