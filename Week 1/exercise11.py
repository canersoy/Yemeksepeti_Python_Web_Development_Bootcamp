"""
Aşağıdaki üç farklı sözlüğü tek sözlükte birleştiren python kodunu yazınız.
dict1={1:10, 2:20}
dict2={3:30, 4:40}
dict3={5:50,6:60}
Beklenen Çıktı : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
"""
dict1={1:10, 2:20}
dict2={3:30, 4:40}
dict3={5:50,6:60}
dict4 = dict(dict1)
dict4.update(dict2)
dict4.update(dict3)
print(dict4)