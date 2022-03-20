m=int(input())
n=int(input())
li=[]

def check(x):
    if x==1:
        return False
    for i in range(1,x):
        if i!=1 and x%i==0:
            return False
    return True

for i in range(m,n+1):

    if check(i):
        li.append(i)
    
if li==[]:
    print(-1)
else:
    print(sum(li))
    print(min(li))

