def solution(s):
    answer = []
    last_seen={}
    for i,ch in enumerate(s):
        if ch in last_seen:
            answer.append(i-last_seen[ch])
        else:
            answer.append(-1)
        
        last_seen[ch]=i
    return answer
