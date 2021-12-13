# Q-1

number1 = int(input("Pls enter a number"))
if number1 > 10:
    print("The number is greater than 10")
elif number1 <= 10:
    print("The number is less than or equal to 10")
else:
    print("Pls enter natural number")
    

# Q-3

derece = int(input("Hava kaç derece"))
if derece >= 18 and derece <= 24:
    print("Hava güzel")
elif derece >= 25:
    print("yanarsın")
elif derece <= 10 or derece < 18:
    print("donarsın")
    
    
# Q-4

liste = []
for i in range(10):
    liste.append(int(input("Bir sayı veriniz")))
    
if liste == None:
    print("Liste boştur")
    
yükseknumara = max(liste)
print(yükseknumara)





def floatsaathesap():
    floattürüsaat = float(input("Float değerindeki saati veriniz"))
    floattürüsaat2 = floattürüsaat[2:] * 60
    print(str(floattürüsaat[1]) + "." +str(floattürüsaat2) )
    
print(floatsaathesap)

floattürüsaat = float(input("Float değerindeki saati veriniz"))
floattürüsaat
print(floattürüsaat  * 60)


    

