def solution(s):
    list=[]
    for char in s :
        if char=='(':
            list.append(char)
        elif char ==')':
            if len(list)==0:
                return False
            list.pop()
    if len(list)==0:
        return True
    else:
        return False