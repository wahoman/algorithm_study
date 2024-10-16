def solution(dots):
    a=[]
    b=[]
    for i in range(4):
        a.append(dots[i][0])
        b.append(dots[i][1])
    
    return (max(a)-min(a))*(max(b)-min(b))