def solution(sides):
    answer = []
    a=max(sides)
    b=min(sides)
    for i in range(a-b+1,a+b):
        answer.append(i)

    return len(answer)