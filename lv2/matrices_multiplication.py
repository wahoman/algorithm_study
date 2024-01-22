def solution(arr1, arr2):
    answer = []
    for i in range(len(arr1)):
        row=[]
        for x in range(len(arr2[0])):
            sum=0
            for j in range(len(arr1[0])):
                sum += arr1[i][j]*arr2[j][x]
            row.append(sum)
        answer.append(row)
    return answer
    