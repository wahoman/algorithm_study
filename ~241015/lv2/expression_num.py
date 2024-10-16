def solution(n):
    answer = 0
    start=1
    while start<=n:
        total=0
        for i in range(start,n+1):
            total+=i
            if total ==n:
                answer+=1
                break
            elif total>n:
                break

        start+=1
    return answer