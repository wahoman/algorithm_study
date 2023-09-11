def solution(arr, queries):
    answer=[]
    for query in queries:
        a,b,c=query
        sub=arr[a:b+1]
        values=[x for x in sub if x>c]
        if values:
            answer.append(min(values))
        else:
            answer.append(-1)
        
    return answer