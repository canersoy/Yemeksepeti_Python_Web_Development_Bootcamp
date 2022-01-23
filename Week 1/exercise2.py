"""
Kullanıcı tarafından girilen bir metnin ilk iki ve son iki karakterini
ekrana yazdıran Python programını yazınız.
"""
metin = input("Bir metin giriniz: ")
print("İlk iki karakter: " + metin[0] + " ve " + metin[1])
print("Son iki karakter: " + metin[len(metin)-2] + " ve " + metin[len(metin)-1])
