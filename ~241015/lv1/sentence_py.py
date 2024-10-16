def solution(s):
    a=0
    b=0
    s=s.upper()
    for i in range(len(s)):
        if s[i]=='P':
            a+=1
        if s[i]=='Y':
            b+=1
    if a==b:
        return True
    else:
        return False