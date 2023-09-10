def solution(my_string, queries):
    for i in range(len(queries)):
        start,end=queries[i][0],queries[i][1]
        substring=my_string[start:end+1]
        reverse=substring[::-1]
        my_string=my_string[:start]+reverse+my_string[end+1:]
    return my_string