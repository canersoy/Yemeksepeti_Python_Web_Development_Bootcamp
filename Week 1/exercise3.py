"""
Kullanıcıdan değişecek metin ve eski harf ve yeni harf bilgisini alarak girilen
metin üzerinden değişikliği yapıp sonucu ekrana yazdıran Python programını yazınız.
"""
metin = input("Bir metin giriniz: ")
eskiHarf = input("Degisecek harfi giriniz: ")
yeniHarf = input("Yeni harfi giriniz: ")
print("Yeni metin: " + metin.replace(eskiHarf,yeniHarf))