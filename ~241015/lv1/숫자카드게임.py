N,M=map(int,input().split())
lst=[]
for i in range(N):
    lst.append(list(map(int,input().split())))
lst2=[]
for j in range(N):
    lst2.append(max(lst[j]))

print(min(lst2))