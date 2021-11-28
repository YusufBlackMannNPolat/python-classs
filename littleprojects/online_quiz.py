print("Merhaba, Online quiz programına hoşgeldiniz")

playing = input("Oyunu oynamak istiyormusunuz ?")

if playing.lower() != "evet":
    exit()
    
print("Tekrar hoşgeldiniz o zaman başlayalım")

Score = 0

cevap1 = input("Aşağıdakilerden hangisi tortul kayaçların özelliklerinden biri değildir?\nA- İçlerinde fosil bulunur\nB- Tabakalı bir yapı gösterir\nC- Göl yada deniz tabanlarında birikerek oluşurlar\nD- Volkanik sahalarda yaygındır")
if cevap1.upper() == "D":
    print("Doğru cevap.")
    Score += 1

else:
    print("Yanlış cevap")
    
cevap2 = input("Aşağıda verilen kayaçlardan hangisi değişime uğrayan kayaçlar arasında yer almaz?\nA- Gnays\nB- Antrasit\nC- Mermer\nD- Elmas")
if cevap2.upper() == "B":
    print("Doğru cevap.")
    Score += 1

else:
    print("Yanlış cevap")

cevap3 = input("Aşağıdaki ülkelerden hangisi levha sınırında yer almaktadır?\nA- Libya\nB- İngiltere\nC- Nijerya\nD- Filipinler")
if cevap3.upper() == "D":
    print("Doğru cevap.")
    Score += 1

else:
    print("Yanlış cevap")
    
cevap4 = input("Aşağıda verilen göllerden hangisi oluşumu bakımından diğer üçünden farkldır?\nA- Terkos\nB- Nazik\nC- Erçek\nD- Çıldır")
if cevap4.upper() == "A":
    Score += 1
    print("Doğru cevap.\nBu soru ile tüm sorularımız bitmiştir.")

else:
    print("Yanlış cevap")
    
print("Doğru bildiğiniz cevap sayısı " + str(Score))
print("Aldığınız puan " + str((Score / 4) * 100) + "%.")
