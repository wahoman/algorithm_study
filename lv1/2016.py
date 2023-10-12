def solution(a, b):
    answer = ''
    s=0
    lst1=['FRI','SAT','SUN','MON','TUE','WED','THU']
    lst2=[0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    for i in range(a):
        s+=lst2[i]
    return lst1[(s+b-1)%7]
