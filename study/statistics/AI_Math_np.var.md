## Numpy로 분산(Variance) 계산하기
우선, 분산이라는 것은 특정 데이터(확률 변수)가 평균으로부터 얼마나 흩어져있는지를 강조하여 나타내는 지표이다. 분산의 수학적 정의는 다음과 같다.

* $Var(X)\,=\,E[(X-\mu)^2]\,=\,E(X^2)-[E(X)]^2$

앞서 말한 것처럼, 확률 변수 $X$가 모평균 $\mu$와 얼마나 차이가 큰지를 강조해서 보여주는 것이기 때문에 단순히 편차의 기댓값이 아니라 편차 제곱의 기댓값으로 계산이 된다. 

이를 좀 더 표준화 내지 보정하기 위해서 분산에 루트를 취하면 표준편차(Standard Deviation; $\sigma$)로 정의할 수 있다. 

* $Var(X)\,=\,E[(X-\mu)^2]$
* $\sqrt{Var(X)}\,=\,\sqrt{E[(X-\mu)^2]}=\,\sigma_{x}$

### Numpy로 분산 계산해보기
![](https://images.velog.io/images/hersheythings/post/aab27bc6-8e94-492d-9c1b-fc9f2f9f63cf/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA%202021-10-22%20%E1%84%8B%E1%85%A9%E1%84%8C%E1%85%A5%E1%86%AB%2011.27.03.png)

Numpy로 분산을 계산하는 방법은 간단하다. 우리가 다루려는 행렬이 n*n 사이즈라고 가정하고, numpy에서 행렬의 분산을 계산하는 케이스를 크게 3가지로 나누어서 살펴보자.

#### 1) 행,열을 나누지 않고 모든 성분의 분산 계산
```
a = np.array([[1, 2], [3, 4]])
np.var(a)
```

#### 2) 1~n행, k번째 열에 위치한 원소들의 분산 계산
```
np.var(a, axis=0)
>> array([1.,  1.])
```

#### 3) k번째 행, 1~n행에 위치한 원소들의 분산 계산
```
np.var(a, axis=1)
>> array([0.25,  0.25])
```

### ddof는 뭘까?
사실 이 개념때문에 글을 쓰려고 했던 것인데, ddof란게 뭔가 딱 봐도 degree of freedom을 뜻해보이긴 했다. 그런데 자세히 구현을 하려면 뭔 의미인지는 알아야 하기 때문에 numpy 문서를 살펴보았고 아래와 같이 적혀있었다.

> “Delta Degrees of Freedom”: the divisor used in the calculation is N - ddof, where N represents the number of elements. By default ddof is zero.

우리가 모분산($\sigma^2$)을 계산할 때와 표본분산($s^2$)을 계산할 때 모두, 편차제곱의 평균로 정의하는데, 이 때 표본분산의 경우에는 평균을 구할 때 원소 갯수 n에서 -1을 한 값으로 나누게 된다. **이렇게 계산해야 더 비편향적인 값이 되기 때문이다.** (자세한 내용은 수리통계학에서)

따라서, 예시를 보면 아래와 같이 편향적 분산, 비편향적 분산의 계산을 numpy에서 다르게 할 수 있다.

```
biased_var = np.var(x)
unbaised_var = np.var(x,ddof=1)
```

오늘의 계산 연습은 일단 끝! 후 그나저나 반복문 계산이 왜 아직도 와닿질 않는지 모르겠다... 누구한테 코딩 사고력을 좀 많이 배워야할 것 같다.

----
* Source : https://numpy.org/doc/stable/reference/generated/numpy.var.html
