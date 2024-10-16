def solution(n):
    n=list(str(n))
    n.sort(reverse=True)
    s=''.join(n)
    return int(s)