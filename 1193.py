X=int(input())
count = 0
num = 1
while num<=X: 
    num+=count 
    count+=1
if count%2==1:
    result1=count-num+X
    result2=num-X
else:
    result1=num-X
    result2=count-num+X
print(f"{result1}/{result2}")
