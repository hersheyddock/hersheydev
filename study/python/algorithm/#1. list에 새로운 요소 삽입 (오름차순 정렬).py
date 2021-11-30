# 리스트 L 과 정수 x 가 인자로 주어질 때, 리스트 내의 올바른 위치에 x 를 삽입하여 그 결과 리스트를 반환하는 함수 solution 을 완성하세요.
# 인자로 주어지는 리스트 L 은 정수 원소들로 이루어져 있으며 크기에 따라 (오름차순으로) 정렬되어 있다고 가정합니다.
# 예를 들어, L = [20, 37, 58, 72, 91] 이고 x = 65 인 경우, 올바른 리턴 값은 [20, 37, 58, 65, 72, 91] 입니다.
# 주의 : x가 리스트 내의 모든 원소보다 작거나, 큰 경우에도 오름차순 정렬이 그대로 성립해야 함!!!!

def solution(L, x):
    answer = L    
    for i in range(0, len(L)):
        if x < L[i]:
            L.insert(i, x) #만약 모든 원소보다 작은 값이라면?
            break
        elif x > max(L):
            L.insert(len(L), x)
        elif x < min(L):
            L.insert(0, x)
    return answer
