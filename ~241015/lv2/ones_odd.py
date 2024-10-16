def is_odd_ones(n):
    count = 0
    while n:
        count += n & 1
        n >>= 1
    return count % 2

def generate_nth_tue_morse_efficient(n, x, y):
    result = ''
    for i in range(x, y + 1):
        # 각 위치의 값이 1의 개수가 홀수면 '1', 짝수면 '0'
        result += '1' if is_odd_ones(i) else '0'
    return result
