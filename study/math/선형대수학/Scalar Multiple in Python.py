# 리스트의 각 원소를 상수배(scalar multiple)하는 연산을 만들어보자 
def scalar_multiple(x, y):
    assert type(x) == list
    assert type(y) == int
    for i in range(0, len(x)):
        x[i] = x[i]*y
        if x[i] == x[i]*y: 
            break # 스칼라배하는 연산이 i번만큼 실행되어서 1번만 실행 및 출력하려고 반복문 깬 것.
        print(x)
    
e1 = [1,0,0] # 표준단위벡터 e1
k = 2 # scalar in R^1

scalar_multiple(e1, k)

--------------------------------------------------

# numpy를 활용해서 매우 쉽게 특정 벡터에 스칼라배 연산하는 방법
import numpy as np
vec = np.array([1,0,0])
k_0 = 2 
np.multiply(vec,k_0)
