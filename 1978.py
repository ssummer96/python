n=int(input())

li=map(int, input().split())

for x in li:

    for i in range(1,x):
        if i!=1 and i!=x and x%i==0:
            n-=1
            break
    if x==1:
        n-=1
print(n)