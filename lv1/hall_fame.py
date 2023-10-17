def solution(k, score):
    result=[]
    lst=[]
    for i in range(len(score)):
        lst.append(score[i])
        lst.sort(reverse=True)
        if i<k:
            result.append(lst[-1])
        else:
            result.append(lst[k-1])
    return result