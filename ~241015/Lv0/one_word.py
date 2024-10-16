def solution(s):
    answer = ''
    s = sorted(s)
    count = 0
    for i in range(len(s)):
        if i == len(s) - 1 or s[i] != s[i + 1]:
            if count == 0:
                answer += s[i]
            count = 0
        else:
            count += 1
    return answer
