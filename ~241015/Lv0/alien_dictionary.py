def solution(spell, dic):
    for word in dic:
        count=0
        for char in spell:            
            if char not in word:
                count+=1
        if count==0 :
            return 1

    return 2