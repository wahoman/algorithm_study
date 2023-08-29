def solution(numbers, num1, num2):
    answer = []
    
    if len(numbers)==num2:
        for i in range(num1,num2+1):
            answer.append(numbers[i])
    else:
        for j in range(num1,num2+1):
            answer.append(numbers[j])
    return answer