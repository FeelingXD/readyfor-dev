# Python의 magic-method 🤔

## Magic-method

> 파이썬에서 사용되는 특별한 메소드를 '매직 메소드' ,'스페셜 메소드', '던더 메서드(Double UNDERscore method)라고 부르기도 합니다.

매직 메소드는 이미 파이썬 내에 정의되어있고, 클래스 내부에서 매직 메소드를 오버라이딩하여 사용한다. 또한 직접 호출하지않고, 정해직 규칙에 따라 호출되는 특징이 있다.

- 던더 메서드라고 불리는 이유는 메소드가 '\_\_main\_\_' 처럼 언더바 두개가 앞뒤로 오기때문이다.

## 어떻게 사용될까?

파이썬의 클래스간 연산 혹은 미리정의된동작등을 실행하는데 이용된다.

### 몇가지 종류

#### \_\_init\_\_ : 생성자

파이썬의 생성자 메소드 \_\_new\_\_ 실행이후 호출되며 데이터를 초기화 하는데 사용한다.

#### \_\_add\_\_ :

흔히 클래스간의 + 메소드 호출시 사용된다. python 에서 1+1 실행시
int(1)+int(1) int의 add 메소드가 실행되는것과 같다.

#### \_\_len\_\_ :

객체의 길이를 반환할때 사용 len() 함수가 사용될때 내부적으로 이 메세드가 실행됨

...

### 예제

```python
class Person(object):
    def __init__(self,name, salary):
        self._name = name
        self._salary = salary
    def __add__(self,target):
        return self._salary+target._salary
영수 = Person("영수",200)
철수 = Person("철수",300)
print(영수+철수)# 500
```
