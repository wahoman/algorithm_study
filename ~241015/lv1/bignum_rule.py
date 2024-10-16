N,M,K=map(int,input().split())
a=list(map(int,input().split())
a.sort()
b=a[-1]
c=a[-2]
d=M/(k+1)*(k*b+c)
e=M%(k+1)*b
print(d+e)
