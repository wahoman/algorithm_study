def solution(s, skip, index):
    
    alphabets=[chr(i) for i in range(97,123)]
    
    for sk in skip:
        alphabets.remove(sk)
        
    result=''
    
    for char in s:
        cur_idx=alphabets.index(char)
        
        for _ in range(index):
            cur_idx+=1
            if cur_idx==len(alphabets):
                cur_idx=0
                
        result+=alphabets[cur_idx]
    return result