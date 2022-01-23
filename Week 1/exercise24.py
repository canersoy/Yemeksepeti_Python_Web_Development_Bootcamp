"""
kullanıcıdan alınan 10 sayının çift ve tek sayıların
sayısını ekrana yazdıran programı yazınız. 
"""
liste = []
i = 0
for i in range(10):
    liste.append(int(input(str(i+1) + ". sayiyi giriniz: ")))
cift = [i for i in liste if i % 2 == 0]
cift = list(dict.fromkeys(cift)) #duplicate'leri silmek için
tek = [i for i in liste if i % 2 != 0]
tek = list(dict.fromkeys(tek)) #duplicate'leri silmek için
print("Cift sayilar: " + str(cift))
print("Tek sayilar: " + str(tek))
