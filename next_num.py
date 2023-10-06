def solution(n):
    a=bin(n)[2:]
    b=str(a).count('1')
    c=n+1
    while str(bin(c)[2:]).count('1')!=b  :
        c+=1
    return c