"""Girilen bir metnin son 2 karakterini 4 defa çoğaltarak ekrana yazan
Python programını yazınız. `*` aritmetik operatöründen faydalanabilirsiniz.
"""
metin = input("Bir metin giriniz: ")
print(metin[len(metin)-2:]*4)