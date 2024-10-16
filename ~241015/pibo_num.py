def solution(n):
    s=[0,1]
    for i in range(2,n+1):
        fibo=s[i-2]+s[i-1]
        s.append(fibo)
    answer=s[n]%1234567    
    return answer