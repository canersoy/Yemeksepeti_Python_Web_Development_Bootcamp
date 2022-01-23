"""liste = [1,2,3,4,5,6,7,1,3,3,3,2,2,1,23]
yukarıdaki listeden ilk 3 sayısını silip ekrana yazdırınız. 
"""
liste = [1,2,3,4,5,6,7,1,3,3,3,2,2,1,23]
print(liste)
for i in range(3):
    liste.pop(0)
print(liste)