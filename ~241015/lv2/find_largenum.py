#내가 푼 방법(시간초과)
def solution(numbers):
    answer = []
    for i in range(len(numbers)):
        found=False
        for j in range(i,len(numbers)):
            if numbers[j]>numbers[i]:
                found=True
                answer.append(numbers[j])
                break
        if not found:
            answer.append(-1)
    return answer

#다른사람의 풀이 
def solution(numbers):
    answer = [-1] * len(numbers)  # 미리 답안을 -1로 초기화
    stack = []  # 인덱스를 저장할 스택

    for i, num in enumerate(numbers):
        # 스택이 비어있지 않고, 현재 숫자가 스택의 top에 있는 숫자보다 클 때
        while stack and numbers[stack[-1]] < num:
            index = stack.pop()  # 스택에서 인덱스를 꺼냄
            answer[index] = num  # 꺼낸 인덱스에 해당하는 답을 현재 숫자로 업데이트
        stack.append(i)  # 현재 인덱스를 스택에 추가

    return answer
