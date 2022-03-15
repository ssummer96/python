# 반복횟수
T=int(input())
while T:
    T-=1
    H,W,N=map(int, input().split())
    # N이 H의 배수일때
    if N%H==0:
        print((H*100)+N//H)
    else:
        print(N%H*100+N//H+1)