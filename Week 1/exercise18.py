"""sozluk = {'S  001': ['Math', 'Science'], 'S    002': ['Math', 'English']} 

ilgili sözlükten anahtar kısımlarında bulunan boşlukları temizleyen
python kodu yazınız. 
"""
sozluk = {'S  001': ['Math', 'Science'], 'S    002': ['Math', 'English']} 
sozluk2 = {i.replace(" ",""):j for i,j in sozluk.items()}
print(sozluk2)
