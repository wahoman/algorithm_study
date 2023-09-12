def solution(arr):
    if len(arr) > len(arr[0]):
        gap=len(arr)-len(arr[0])
        for i in range(len(arr)):
            for _ in range(gap):
                arr[i].append(0)
            
    lst=[]            
    if len(arr)<len(arr[0]):
        for j in range(len(arr[0])):
            lst.append(0)
        for z in range(len(arr[0])-len(arr)):    
            arr.append(lst)
      
    return arr