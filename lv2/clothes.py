def solution(clothes):
    clothes_type={}
    for item in clothes:
        if item[1] in clothes_type:
            clothes_type[item[1]]+=1
        else:
            clothes_type[item[1]]=1
    
    combinations=1
    for num in clothes_type.values():
        combinations*=(num+1)
    return combinations-1