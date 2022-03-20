import math 
A,B,V=map(int, input().split())
# 반올림메소드 ceil
print(math.ceil((V-B)/(A-B)))
