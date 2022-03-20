n=int(input())
s,X=1,1
while(1):
    X+=(s-1)*6
    if X>=n:
        break
    s+=1
print(s)
# 1 , 6, 12 , 18, 24 , 30 

print(int(-(-(3+(12*int(input())-3)**.5)//6)))