def check(x):
    if x==1:
        return False
    for i in range(2,int(x**0.5)+1):
        if x%i==0:
            return False
    return True

li=[]
all=list(range(2,246912))
for i in all:
    if check(i): li.append(i)


while True:
    s=0
    n=int(input())
    if n==0: break

    for i in li:
        if n<i<=2*n:
            s+=1
    print(s)
