"""
Kullanıcı tarafından girilen bir kelimenin palindrom olup olmadığını
karşılaştırma operatöründen faydalanarak print() fonksiyonu ile ekrana yazdırınız.
"""
metin = input("Bir metin giriniz: ")
if metin == metin[::-1]:
    print(metin + " kelimesi tersten " + metin[::-1] + ". Yani palindrom.")
else:
    print(metin + " kelimesi tersten " + metin[::-1] + ". Yani palindrom DEGİL.")