def solution(picture, k):
    answer = []
    for i in range(len(picture)):
        for z in range(k):
            row = ''
            for j in range(len(picture[i])):
                row += picture[i][j] * k
            answer.append(row)
    return answer
