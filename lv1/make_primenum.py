def is_prime(n):
    if n<=1:
        return False
    for a in range(2,int(n**0.5)+1):
        if n%a==0:
            return False
    return True
        

def solution(nums):
    count=0
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            for z in range(j+1,len(nums)):
                d=nums[i]+nums[j]+nums[z]
                if is_prime(d):
                    count += 1
    return count