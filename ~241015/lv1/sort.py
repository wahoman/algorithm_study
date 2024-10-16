n=int(input())
lst=[]
for i in range(n):
    lst.append(int(input()))
    
lst=list(set(lst))
lst.sort()
for j in range(len(lst)):
    print(lst[j])