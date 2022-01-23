"""İki farklı listede tutulan verileri tek bir listede sırasıyla append,
extend metodlarıyla ve "+" operatörü ile birleştiren python kodunu yazınız. 
liste1 = [1,2,3]
liste2 = [4,5,6]
liste3 = ?????
"""
liste1 = [1,2,3]
liste2 = [4,5,6]
liste1.append(liste2)
print(liste1)

liste1 = [1,2,3]
liste2 = [4,5,6]
liste1.extend(liste2)
print(liste1)

liste1 = [1,2,3]
liste2 = [4,5,6]
print(liste1+liste2)
