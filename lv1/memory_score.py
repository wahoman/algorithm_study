def solution(name, yearning, photo):
    answer = []
    
    for a in range(len(photo)):
        answer.append(0)
        for b in range(len(photo[a])):
            if photo[a][b] in name:
                answer[a]+=yearning[name.index(photo[a][b])]
            
                
    return answer