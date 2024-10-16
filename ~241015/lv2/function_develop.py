import math

def solution(progresses, speeds):
    days_required=[]
    for i in range(len(progresses)):
        remaining_progress=100-progresses[i]
        days=math.ceil(remaining_progress/speeds[i])
        days_required.append(days)
        
    answer=[]
    max_day=days_required[0]
    count=1
    
    for day in days_required[1:]:
        if day<=max_day:
            count+=1
        else:
            answer.append(count)
            count=1
            max_day=day
    
    answer.append(count)
    return answer