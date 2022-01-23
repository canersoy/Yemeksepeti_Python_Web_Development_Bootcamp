"""
Girilen on sayı içerisinden en büyük üç sayıyı bulmak
için bir Python fonksiyonu yazınız
"""
liste = []
i = 0
for i in range(10):
    liste.append(input(str(i+1) + ". sayiyi giriniz: "))
liste.sort(reverse=True)
print("Girilen 10 sayi arasindan en büyük 3 tanesi sirasiyla: " + liste[0] + " " 
+ liste[1] + " " + liste[2])
