def solution(want, number, discount):
    answer = 0
    want_list = []
    for i in range(len(want)):
        want_list.extend([want[i]] * number[i])
    
    for start in range(len(discount) - 9):
        discount_slice = discount[start:start+10]
        temp_want_list = want_list[:]
        for item in discount_slice:
            if item in temp_want_list:
                temp_want_list.remove(item)
        
        if not temp_want_list:
            answer += 1

    return answer
