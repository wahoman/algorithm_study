def solution(array, commands):
    answer = []
    for command in commands:
        start, end, target= command
        selected=sorted(array[start-1:end])
        answer.append(selected[target-1])
    return answer