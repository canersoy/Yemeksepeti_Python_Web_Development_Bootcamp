"""
Seven Segment Display 
https://en.wikipedia.org/wiki/Seven-segment_display

* * * * *
*       *
*       *
* * * * *
*       *
*       *
* * * * *

8 sayısı girildiğinde yukarıdaki çıktıyı veren python programını 0 dan 9 a 
kadar olan sayılar için yazalım
## hex,bin,zfill, tek satırda if
"""
a,b,c,d,e,f,g = map(int,list(str(bin(0x6D))[2:].zfill(7)))
print(("*" if a else " ")*8)
print("*" if f else " "," "*4,"*" if b else " ")
print("*" if f else " "," "*4,"*" if b else " ")
print(("*" if g else " ")*8)
print("*" if e else " "," "*4,"*" if c else " ")
print("*" if e else " "," "*4,"*" if c else " ")
print(("*" if d else " ")*8)