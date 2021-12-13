# 1. HW:
# - Write a program that uses everything you have learned in this notebook at least once.
# - Write comments that label each section of your program.
# - For each thing your program does, write at least one line of output that explains what your program did."

#This program takes inputs from the person with the input command and performs 4 operations with decimal or normal numbers according to the person's request.

print("Hello, Welcome my little mat program")   #We use the print code to communicate with the person using the program (print code is required to write something we want to the console)
name = input("Lets start. What's your name")   #We create a variable (name variable name) and with the input command we get the data to be entered into the variable from the user
print("Hello again " + name.title())   #While we continue to communicate with the user with the print command, we call our variable with the (+) operator and add the text inside the variable next to our sentence.
#The title command, on the other hand, helps us capitalize the first letter of the word or sentence in the variable.

işlem = int(input("You want to deal with decimal numbers?\n1.Yes\n2.No")) #We create a variable (name of our variable is işlem) and specify that this variable is of an int data type.
#With the input command, we get the answer to the question we asked again and continue.
if işlem == 1: #With the if command, if the condition we want is met, that is, if the işlem variable is equal to the number 1, the commands under the if command start to run.
    ondaliksayi1 = float(input("give me the first decimal number you want")) #We open a variable (variable name is ondaliksayi1) and we say that this variable will contain data of type float. We get the first data with input
    ondaliksayi2 = float(input("give me the second decimal number you want")) #we do the same things in this variable (our variable name this time is ondaliksayi2)
    ondalikcalcnumber = int(input("what do you want to do with these numbers " + name.title() + "\nToplama için 1\nÇıkartma için 2\nBölme için 3\nÇarpma için 4 write")) #we open a variable, we say that it will store data of type int (variable name ondalikcalcnumber) we ask the person with the input command, we transfer the answer we receive into the variable
    if ondalikcalcnumber == 1: #if the data of decimalcalcnumber variable is 1 it means run this
        print(ondaliksayi1 + ondaliksayi2) #Sum and print variable ondaliksayi1 and ondaliksayi2
        print("Thanks for the using my code") #we print a thank you note after the transaction
        exit() #and we end the program

    if ondalikcalcnumber == 2:
        print(ondaliksayi1 - ondaliksayi2) #Extract and print variable ondaliksayi1 and ondaliksayi2
        print("Thanks for the using my code") #we print a thank you note after the transaction
        exit() #and we end the program

    if ondalikcalcnumber == 3:
        print(ondaliksayi1 / ondaliksayi2) #Split and print variable ondaliksayi1 and ondaliksayi2
        print("Thanks for the using my code") #we print a thank you note after the transaction
        exit() #and we end the program
    
    if ondalikcalcnumber == 4:
        print(ondaliksayi1 * ondaliksayi2) #Multiply and print variable ondaliksayi1 and ondaliksayi2
        print("Thanks for the using my code") #we print a thank you note after the transaction
        exit() #and we end the program
        

    else:
        print("Yanlış bir komut girdiniz") #if we enter an answer other than the one we want in the ondalikcalcnumber variable, this command works and prints a warning
        exit() #and we end the program
elif işlem < 2: #this command works together with the first if command we used, if the number in the işlem variable is greater than 2, it goes inside itself
    print("Yanlış bir komut girdiniz") #This error text is printed when entered inside the elif command
    exit() #and we end the program



print("we are dealing with normal numbers") 
sayi1 = int(input("give me the first number you want"))
sayi2 = int(input("give me the second number you want"))
calculatenumber = int(input("what do you want to do with these numbers " + name.title() + "\nToplama için 1\nÇıkartma için 2\nBölme için 3\nÇarpma için 4 write"))

if calculatenumber == 1:
    print(sayi1 + sayi2)
    print("Thanks for the using my code")
    exit()

if calculatenumber == 2:
    print(sayi1 - sayi2)
    print("Thanks for the using my code")
    exit()

if calculatenumber == 3:
    print(sayi1 / sayi2)
    print("Thanks for the using my code")
    exit()
    
if calculatenumber == 4:
    print(sayi1 * sayi2)
    print("Thanks for the using my code")
    exit()

else:
    print("Yanlış bir komut girdiniz")
    exit()