def solution(n):
    if n<=1:
        return 1
    return n+solution(n//2)

print(solution(10))