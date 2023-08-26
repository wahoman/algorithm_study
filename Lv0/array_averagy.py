def solution(numbers):
    answer = 0
    for char in numbers:
        answer+=char
    return answer/len(numbers)