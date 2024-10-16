a,b=map(int,input().split())			
lst=[]
for i in range(a):
	l=list(map(int,input().split()))
	lst.append(min(l))

print(max(lst))