#리스트 L 과, 그 안에서 찾으려 하는 원소 x 가 인자로 주어질 때, x 와 같은 값을 가지는 원소의 인덱스를 리턴하는 함수 solution() 을 완성하세요. 
#만약 리스트 L 안에 x 와 같은 값을 가지는 원소가 존재하지 않는 경우에는 -1 을 리턴합니다

def solution(L, x):
    answer = 0
    for i in range(len(L)):
        if x == L[i]:
            answer = i
            return answer
        
    if x not in L:
        answer = -1
        return answer

      
# 위 코드는 알고리즘 효율성을 전혀 고려하지 않고 로직의 정확도만 생각한 코드이기 때문에 정확도는 100%가 나오지만 효율성 테스트는 전부 통과하지 못함.
# 따라서 다른 파이썬 문서를 통해 이진 탐색(Binary Search)을 구현해보기로 하자.
