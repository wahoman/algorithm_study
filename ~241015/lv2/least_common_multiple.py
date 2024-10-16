import math

def solution(arr):
    lcm=arr[0]
    for i in range(1,len(arr)):
        lcm = lcm * arr[i] // math.gcd(lcm, arr[i])
    return lcm