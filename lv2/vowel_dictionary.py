def solution(word):
    answer=0
    letters={'A':0,'E':1,'I':2,'O':3,'U':4}
    weights=[781,156,31,6,1]
    for i,char in enumerate(word):
        answer+=letters[char]*weights[i]+1
    
    
    return answer