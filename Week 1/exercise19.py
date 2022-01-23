"""
liste1=[1,2,3]
liste2=[4,5,6,7,8]
iki listeyi liste3 ile birleştiriniz?
"""
liste1=[1,2,3]
liste2=[4,5,6,7,8]
liste1.extend(liste2)
liste3 = liste1.copy()
print(liste3)