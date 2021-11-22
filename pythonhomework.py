# 1. HW:
# - Write a program that uses everything you have learned in this notebook at least once.
# - Write comments that label each section of your program.
# - For each thing your program does, write at least one line of output that explains what your program did."

#Bu program kişiden input komudu ile girdiler alıp kişinin isteğine göre ondalık veya normal sayılar ile 4 işlem yapmaktadır.

print("Hello, Welcome my little mat program")
name = input("Lets start. What's your name")
print("Hello again " + name.title())
işlem = int(input("You want to deal with decimal numbers?\n1.Yes\n2.No"))
if işlem == 1:
    ondaliksayi1 = float(input("give me the first decimal number you want"))
    ondaliksayi2 = float(input("give me the second decimal number you want"))
    ondalikcalcnumber = int(input("what do you want to do with these numbers " + name + "\nToplama için 1\nÇıkartma için 2\nBölme için 3\nÇarpma için 4 write"))
    if ondalikcalcnumber == 1:
        print(ondaliksayi1 + ondaliksayi2)
        print("Thanks for the using my code")
        exit()

    if ondalikcalcnumber == 2:
        print(ondaliksayi1 - ondaliksayi2)
        print("Thanks for the using my code")
        exit()

    if ondalikcalcnumber == 3:
        print(ondaliksayi1 / ondaliksayi2)
        print("Thanks for the using my code")
        exit()
    
    if ondalikcalcnumber == 4:
        print(ondaliksayi1 * ondaliksayi2)
        print("Thanks for the using my code")
        exit()
        

    else:
        print("Fazla sayı girdiniz")
        exit()
else:
    breakpoint





sayi1 = int(input("give me the first number you want"))
sayi2 = int(input("give me the second number you want"))
calculatenumber = int(input("what do you want to do with these numbers " + name + "\nToplama için 1\nÇıkartma için 2\nBölme için 3\nÇarpma için 4 write"))

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
    print("Fazla sayı girdiniz")
    exit()
