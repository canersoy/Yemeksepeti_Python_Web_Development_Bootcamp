"""
liste1 = ["1",1,2,"3"]
Yukarıdaki listenin bir kopyasını alarak 250 sayısını listenin sonuna ekleyiniz,
her iki listeyi ekrana yazdırınız.
Beklenen Çıktı:
["1",1,2,"3"] => Liste1 Çıktısı
["1",1,2,"3",250] => Liste2 Çıktısı
"""
liste1 = ["1",1,2,"3"]
liste2 = liste1.copy()
liste2.append("250")
print(liste1)
print(liste2)