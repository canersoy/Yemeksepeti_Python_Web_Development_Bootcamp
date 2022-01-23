"""
Bir listeyi bir sözlükte sıralamak için bir Python programı yazın <br>
Örnek Veri: num = {'n1': [2, 3, 1], 'n2': [5, 1, 2], 'n3': [3, 2, 4]}
"""
num = {'n1': [2, 3, 1], 'n2': [5, 1, 2], 'n3': [3, 2, 4]}
for key, value in num.items():
    value.sort()
print(num)
