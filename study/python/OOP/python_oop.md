예전에 py-evm의 TX Execution 모델 코드를 뜯어보면서 추상화시켜서 재작성했던 적이 있다.

근데, 저 self가 대체 뭔지 모르겠어서 이번 기회에 다시 찾아보았다. 

#### Python과 객체 지향

* [참고 : 파이썬 문법 - 클래스 만들기](https://offbyone.tistory.com/126)
![](https://images.velog.io/images/hersheythings/post/4969ff9e-6283-45f6-bf78-f701926ef683/image.png)

java에서 열심히 학습한 바와 같이, 객체 지향 프로그래밍에서는 객체를 기준으로 프로그램을 컨트롤할 수 있다. 우선, 객체를 먼저 정의한다. 

객체는 멤버 변수(데이터)와 멤버 메소드(객체의 데이터, 즉 상태를 변경하는 함수)로 구성된다. 이 요소들끼리 서로 상호작용하면서 객체의 상태가 바뀌어 원하는 결과를 얻는 프로그램 방식이 객체지향 프로그래밍이다. 
 
 #### 간단한 객체지향 프로그래밍 개념
```
data = [4,1,5,3,2] // 멤버 변수를 통해 데이터 할당
data.sort() // .sort 메소드로 데이터를 정렬하는 기능 사용
data
[1, 2, 3, 4, 5]
// 클래스는 별도로 작성해놓지 않았음
```

지금까지 클래스(class)와 객체(object)라는 단어를 사용했는데, 객체 지향 프로그램이에서 한가지만 더 추가하면 인스턴스(instance)라는 단어가 있다. 클래스(class)는 프로그램이 실행되었을 때 생성되는 객체가 어떤 멤버변수와 메소드를 가지는지 정의해둔 것을 말합니다. 즉, 사전에 특정 이름으로 정의되어 객체를 감싸고 있는 상위의 집합을 클래스라고 부른다. 

클래스를 생성할 때, 파이썬 프로그램이 실행되면 클래스 정의는 메모리로 로드되어 그 정의에 기반한 객체를 생성할 수 있도록 준비가 됩니다. 그럼 인스턴스(instance)는 뭘까. 별거 없다 그냥 클래스 정의로부터 실제 객체를 생성한 것을 인스턴스라고 한다. 

객체는 개념적인 말로 실제 만질 수 있는 사물, 어떤 추상적인 개념, 클래스의 인스턴스 등 인식할 수 있는 모든 것을 통칭하는 말이라고 할 수 있다. 그래서 객체지향 프로그래밍에서 인스턴스와 객체라는 단어는 일반적으로 혼용해서 쓴다. 귀에 걸면 귀걸이, 코에 걸면 코걸이니까 맥락에 따라 잘 이해하고 사용하길. 

### Python에서 클래스 정의하기

```
class MyClass: 
	name = "MyName" 
	def print(self, str): 
    		print(self.name + " " + str) 

x = MyClass() 
x.print("Hello, Python") 

>>> MyNameHello, Python 

x.name 
>>> 'MyName' 
```
클래스의 선언은 class 로 시작해서 뒤에 클래스 이름을 적고 콜론(:)으로 행을 마치면 된다. 그 뒤부터 클래스의 멤버(필드)와 메소드들은 들여쓰기로 적어준다. 클래스의 끝은 들여쓰기가 class와 같은 레벨이 나오는 곳에서 끝난다.

메소드는 일반적인 함수와 같은 형식으로 작성을 할 수 있는데, 한가지 차이점은 함수의 인자중에 **첫번째는 반드시 self이어야 한다**. self의 의미는 클래스 자신을 가리키는 것인데, 메소드 호출시 파이썬이 내부적으로 클래스 자체의 참조를 넘기게 된다. 이 인자는 메서드를 호출할 때는 없는것처럼 사용된다.

클래스의 사용은 x = MyClass() 처럼 객체를 인스턴스화 하고(객체를 생성하고) 사용하면 된다. 멤버 변수의 사용은 x.print("Hello, Python") 에서 처럼 객체 변수에 마침표(.)를 사용한다. 


MyClass의 두가지 멤버인 name 멤버 변수와 print 메소드는 기본적으로 public이다. 이 의미는 외부에서 바로 접근하여 사용할 수 있다는 뜻이다. (default가 public)


클래스를 생성할 때 필요한 값을 줄 수 있는 생성자로는 __init__() 메소드가 제공된다. 

```
>>> class MyClass: 
		name = "MyName" 
        
        def __init__(self, name): 
        	self.name = name 
        
        def print(self, str): 
            print(self.name + " " + str) 

>>> x = MyClass("Hong Gil Dong") 

>>> x.print("Hello, Python") 
Hong Gil Dong Hello, Python 

```

__init__(self, name): 에서처럼 생성자에도 항상 첫번째 인자로 self를 지정해야 한다. 두번째 인자로 주어진 name은 멤버 변수 name과 이름이 같지만, 해당 멤버는 self.name으로 구분할 수 있다.

----
#### EVM Gas Consumption 관련 코드 (partial)
```
// py-evm which is a python Ethereum client written in Python lang.
// The code below is partially pasted from the total computation process. 

    #
    # Gas Consumption
    #
    def get_gas_meter(self) -> GasMeter:
        return GasMeter(self.msg.gas)

    def consume_gas(self, amount: int, reason: str) -> None:
        """
        Consume ``amount`` of gas from the remaining gas.
        Raise `eth.exceptions.OutOfGas` if there is not enough gas remaining.
        """
        return self._gas_meter.consume_gas(amount, reason)
```
