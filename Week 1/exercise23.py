"""
Bir metin içerisindeki büyük ve küçük harflerin listesini
yazdıran python programını yazınız.
"""
metin = input("Bir metin giriniz: ")
liste1 = [i for i in metin if i.islower()]
liste1 = list(dict.fromkeys(liste1)) #duplicate'leri silmek için
liste2 = [i for i in metin if i.isupper()]
liste2 = list(dict.fromkeys(liste2)) #duplicate'leri silmek için
print("Kucuk harfler: " + str(liste1))
print("Buyuk harfler: " + str(liste2))