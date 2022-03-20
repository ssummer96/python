n=int(input())

x=n%5

if n==4 or n==7:
    print(-1)
else:
    if x==0:
        print(n//5)
    elif x==1:
        print(n//5+1) # 5묶음 -1 3묶음 +2
    elif x==2:
        print(n//5+2)
    elif x==3:
        print(n//5+1)
    elif x==4:
        print(n//5+2)
