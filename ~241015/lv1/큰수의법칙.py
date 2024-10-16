N,M,K=map(int,input().split())
lst=list(map(int,input().split()))
sum=0
lst.sort(reverse=True)
for i in range(1,M+1):
    if i%K==0:
        sum+=lst[1]
    else:
        sum+=lst[0]
print(sum)
