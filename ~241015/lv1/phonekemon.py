def solution(nums):
    nums1=list(set(nums))
    a=len(nums)//2
    b=len(nums1)
    
    if a>b:
        return b
    else:
        return a