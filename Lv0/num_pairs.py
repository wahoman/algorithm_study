def solution(n):
    answer = 0
    lst=[]
    for i in range(1,n+1):
        if n%i==0:
            lst.append(i)
    for j in range(len(lst)):
        for z in range(len(lst)):
            if lst[j]*lst[z]==n:
                answer+=1
    return answer