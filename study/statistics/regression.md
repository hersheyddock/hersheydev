### ML 문제의 2가지 큰 유형

1. 회귀 문제(Regression) 
2. 분류 문제(Classification)

The main difference between Regression and Classification algorithms is that Regression algorithms are used to predict the continuous values such as price, salary, age, etc. While, Classification algorithms are used to predict/classify the discrete values such as Male or Female, True or False, Spam or Not Spam, etc.

![](https://images.velog.io/images/hersheythings/post/1a3422a9-82e4-4a92-b398-064cf3c5ab7b/image.png)

그리고 대표적으로 회귀 문제에는 선형회귀분석(Linear Regression), 분류 문제에는 로지스틱 회귀(Logistics Regression) 방법론이 사용된다. 이때, 로지스틱 회귀의 경우 이름만 회귀이고 실질적으로는 분류 문제에 사용되는 방법이라는 것을 숙지하자! (교수님 말씀을 빌리자면 붕어빵 안에 붕어가 안들어가있듯이 ㅋㅋ)

----
### Linear Regression vs Logistic Regression
![](https://images.velog.io/images/hersheythings/post/831e9573-0e98-4e01-b58b-67d1eab9cdd6/image.png)

우선 본 문서의 결론은 위 그림으로 귀결될 수 있는데, 차근차근 그 과정에 대해서 알아보고 다시 한 번 그림을 살펴보도록 하자.

### 1. Linear Regression
#### Linear Statiscal Model이란?
Linear Statiscal Model이란 독립 변수 $x$($x_{1}, x_{2},..., x_{k}$)와 종속 변수 $y$ 간의 관계를 선형의 모델로 정의하는 모델이다. 

> $Y = \beta_{0} + \beta_{1} x_{1} + \beta_{2}x_{2}+... +\beta_{k}x_{k} + \epsilon$

* $Y$ : 우리가 독립변수 $X$를 통해서 추정하려고 하는 종속변수
* $X$ : 우리에게 주어진 데이터들로, Y를 추정하기 위한 재료이다.
* 회귀계수 $\beta$ : 독립변수 $X$에 곱해져있는 $\beta_{0}, \beta_{1}, ..., \beta_{k}$는 회귀계수라고 불리며 우리가 선형회귀 모델을 통해서 추정하려고 하는 핵심적인 값, 즉 모수(parameter)이다. 
* $\epsilon$ : 회귀식의 오차항으로, 기댓값이 0인 확률 변수 $s.t.\,\,\hat y = \hat\beta_{0} + \hat\beta_{1} x_{1} + \hat\beta_{2}x_{2}+... +\hat\beta_{k}x_{k}$) ($x$는 이미 알고있는 값이기 때문에 추정치를 의미하는 $\hat x$을 사용하지 않음에 주의!)

이 때, 독립변수 $x$가 1개면 단순선형회귀분석(simple linear regression), 여러개면 다중선형회귀분석(multiple linear regression)이라고 한다.

#### SSE (단순선형회귀분석 가정)
$E(Y) = \hat\beta_{0} + \hat\beta_{1}x_{1}$
* $Y=\beta_{0}+\beta_{1}x_{1}+\epsilon\,\,\,where \,\,E(\epsilon) = 0$
* 우리는 모수의 추정량인 $\hat\beta_{0}, \hat\beta_{1}$을 찾는게 목적 !

#### LSE(Least-Square Method)
- n개의 데이터 포인트에 대해서 회귀식(Fitted Line)을 학습시키는 방법
- Fitted Line과 실제값 간의 차이(vertical deviation = error)의 제곱합(SSE)을 최소화시키는 것이 목적. 즉, Minimize SSE가 목표.
- Fitted Line $: \hat y= \hat\beta_{0}+\hat\beta_{1}x_{1}$
- Sum of Squares of the vertical deviation(Sum of Squares of Error) = $\sum_{i=1}^{n}(y_{i}-\hat y)^2 = \sum_{i=1}^{n}(y-(\hat\beta_{0}+\hat\beta_{1}x_{1}))$

> SSE를 최소로 만들기 위해서는 $\hat\beta_{0}, \hat\beta_{1}$에 의해 영향을 받을 것이므로 두 변수에 대해 SSE를 미분하고, 이 때 0이 되는 $\hat\beta_{0},\,\hat\beta_{1}$ 값을 찾아내야 한다. 
> 
> $s.t.\,\, \frac {\partial SSE}{\partial \hat\beta_{0}}=0,\,\, \frac{\partial SSE}{\partial \hat\beta_{1}}=0$

![](https://images.velog.io/images/hersheythings/post/ab3cf53a-a9e6-4abb-a21a-e2d02ea4e9be/image.png)

### 2. Logistic Regression
일단, 로지스틱 회귀 모형에서는 선형 회귀 모델과는 다르게 독립변수 $Y$의 값이 0 또는 1 Binary하게 도출되는 것이 가장 큰 특징이다. 

그리고 이러한 특징은 자연스럽게 True/False 여부를 판별하는 분류 문제로 이어질 수 있게 된다. (ex. 이 사람이 이 상품을 좋아할 것인가(True), 안 좋아할 것인가(False) 등)

#### Logistic Function
* $f(x) = \frac {L}{1+e^{-k(x-x_{0})}}$

위 함수를 쉽게 표현하면, input으로는 $-\infin$부터 $\infin$ 까지 전부 받고, output으로는 0과 $L$ 사이의 값을 뱉는 함수이다. 

* $x_{0}$ : 함수의 중간 지점 (midpoint)
* $L$ : 함수의 최댓값 (curve's maximum value)
* $k$ : 함수의 기울기(steepness of the curve)

모델을 좀 더 단순화하면 아래와 같을 수 있다.

#### Standard Logistic Function
* $f(x) = \frac {1}{1+e^{-x}} = \frac{e^{x}}{1+e^{x}}$

* 위 함수는 $x_{0}$가 0이고, $L$이 1인 경우에 해당. 즉, 중간 지점이 0이고 최대치는 1인 경우.

![](https://images.velog.io/images/hersheythings/post/4804a4dc-2f97-44e8-9241-9e21177d834c/image.png)

#### Logistic Regression의 목적식

* 선형회귀분석과 마찬가지로, 학습을 위해서는 목적식이라는게 필요함. SSE를 최소로 만들었던 것처럼, 로지스틱 회귀에서는 손실값을 최소로 만드는 방법을 사용.
* 주로 Cross-Entropy Loss(CE)를 사용하여 모델을 학습시킨다.

먼저, 목적식을 사용하기 전에 $\hat y = P(y=1|\vec x)$을 구해야 함. 즉, 특정 데이터가 주어졌을 때 해당 데이터가 참일 확률을 구하여 손실함수에 반영해야 함.

* $\hat y = P(y=1|\vec x) = \frac {exp(\vec x\hat \beta)}{1+exp(\vec x\hat \beta)}$
* 손실 함수 : $L_{CE} = -(y\,log\,\hat y+(1-y)\,log(1-\hat y))$

위 수식으로 정의되는 손실 함수의 값을 낮게 만드는 것이 목적 ! 수식의 구조에 의하면...

* $y$가 1일때 $L_{CE}$가 낮아지려면, $\hat y$도 높은 값을 가져야 함
* $y$가 0일때 $L_{CE}$가 낮아지려면, $\hat y$도 낮은 값을 가져야 함

우리가 학습해야할 값은 로지스틱 회귀 함수의 정의역에 곱해지는 $\hat \beta$의 값으로, $\hat \beta$는 $L_{CE}$를 최소화하도록 최적화되어야 한다. (Gradient Descent 방식을 사용; $\frac{\partial L_{SE}} {\partial \hat \beta}$)
