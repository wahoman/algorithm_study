import math
def solution(n, m):
    gcd=math.gcd(n,m)
    lcd=n*m//gcd
    
    return [gcd,lcd]