def solution(L, x):
    # index 정의
    start, end = 0, len(L)-1
    
    # binary search 구조 정의   
    while start <= end:
        mid = (start+end)//2
        if L[mid] == x:
            return mid
        elif L[mid] > x:
            end = mid-1
        elif L[mid] < x: 
            start = mid+1
    
    # 위 while loop를 만족하지 않을 경우
    return -1 
