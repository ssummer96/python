m,n = map(int, input().split())

def check(x):
    if x==1:
        return False
    for i in range(2,int(x**0.5)+1):
        if x%i==0:
            return False
    return True

for i in range(m,n+1):
    if check(i):
        print(i)




