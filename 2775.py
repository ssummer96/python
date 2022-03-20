T=int(input())
while T:
    T-=1
    floor=[]
    k=int(input())
    n=int(input())
    
    floor.append([x for x in range(1,n+1)])
    #[[1,2,3,4,5]]

    # 층수만큼 반복함
    for i in range(k):
        li=[]

        # 호수만큼 반복함
        for j in range(n):
            num=0

            # 전 층의 인덱스까지의 합을 li에 추가
            for m in range(j+1):
                num+=floor[i][m]
            li.append(num)

        # li를 floor에 추가(새로운층 생성)
        floor.append(li)    

    #print(floor)
    print(floor[k][n-1])


