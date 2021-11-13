def solution(L, x):
    res = [i for i,j in enumerate(L) if j == x]
    if x not in L:
        return [-1]
    else:
        return res

# 계속 인덱스 하나만 반환되는 문제가 있었는데, 이는 index() 메서드의 특징임. 
# 탐색 대상이 되는 원소의 인덱스를 딱 한번만 찾아주고 끝냄


# 참고 : https://pydole.tistory.com/entry/Python-Find-all-index-values-of-a-specific-element-using-enumerate-enumerate%EB%A5%BC-%ED%99%9C%EC%9A%A9%ED%95%9C-%ED%8A%B9%EC%A0%95%EC%9A%94%EC%86%8C%EC%9D%98-%EB%A6%AC%EC%8A%A4%ED%8A%B8-index-%EA%B0%92-%EB%AA%A8%EB%91%90-%EC%B0%BE%EA%B8%B0
