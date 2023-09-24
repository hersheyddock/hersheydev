# 인자로 0 또는 양의 정수인 x 가 주어질 때, Fibonacci 순열의 해당 값을 구하여 반환하는 함수 solution() 을 완성하세요.
# Fibonacci 순열은 아래와 같이 정의됩니다.
# F0 = 0
# F1 = 1
# Fn = Fn - 1 + Fn - 2, n >= 2

def solution(x):

    if x == 0:
        fn = 0

    elif x == 1:
        fn = 1
    
    elif x >= 2:
        fn = solution(x-1) + solution(x-2)
    
    return fn
