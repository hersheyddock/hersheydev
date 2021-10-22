### numpy.random 모듈
> * np.random.randint() : 균일 분포의 정수 난수 생성
* np.random.rand() : 0부터 1사이의 균일 분포의 난수 matrix array 생성
* np.random.randn() : 표준 정규 분포에서의 난수 생성 (평균 0, 표준편차=1)

### numpy.random.normal()에 대해
![](https://images.velog.io/images/hersheythings/post/bdca7b26-b0b9-4a4f-8fe7-3b6550eb3f02/image.png)

위 numpy.random 모듈에서의 np.random.randn()와 numpy.random.normal()이 다른 점은 표준정규분포인지 아닌지의 여부이다. 즉, 후자의 경우 내가 모수를 선택할 수 있다. 

numpy.random.nomral()의 경우에는 ``` loc(평균), scale(표준편차), size(행렬의 크기)```를 인자로 받는다.

#### 예시
```
#표준정규분포에서 n개의 난수 생성과 cdf
x1 = np.random.randn(1) #np.random.randn(n) 
norm_cdf1 = stats.norm.cdf(x1)

#정규분포에서 평균이 3, 표준편차가 2인 값 1개를 랜덤하게 샘플링
x2 = np.random.normal(loc=3, scale=2, size=1) 
norm_cdf2 = stats.norm.cdf(x2, loc=3, scale=2)
```

#### Reference
* https://www.sharpsightlabs.com/blog/numpy-random-normal/
* https://nittaku.tistory.com/443
