def inner_product(a, b):
    assert len(a) == len(b) #a,b 2개 벡터의 길이 동일해야 내적 가능
    
    inner_product = []
    
    for i in range(len(a)):
        inner_product.append(a[i] * b[i])
    
    result = sum(inner_product)
    
    return result
  
  
# 출력
a = [1,1,1]
b = [2,4,6]

c = inner_product(a,b)
c
