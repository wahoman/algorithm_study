def solution(a, b, n):
    answer = 0
    while n>=a:
        receive=(n//a)*b
        n=n%a+receive
        answer+=receive
    return answer