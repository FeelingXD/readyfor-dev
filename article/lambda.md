## 람다 함수 알아보기 👀

> 이 글에서는 람다식, 또는 람다 함수라고 불리는 lambda Λ 에 대해 알아봅니다.✨

## 람다(Λ)

람다 함수는 프로그래밍 언어에서 사용되는 개념으로 익명함수(Annonymous functions)을 지칭하는 용어입니다. 프로그래밍 언어에 따라서 화살표함수(Javascript), 익명함수, 람다 등 다양한 용어로 사용됩니다. 람다식은 컴퓨터 과학분야에서 의 람다 대수 입니다.  
`람다` 라는 표현은 막상 어렵게 다가오지만 함수를 단순하게 표현하는 방법이라고 생각하시면 됩니다.

```python
#python
def func(): # 함수의 기본형태
    print("hello world!")

(lambda: print("Hello, world!"))# 위의 함수와 동일합니다.
```

```java
//java
public class lambda(x){

    public void helloWorld(){
        System.out.println("hello world!");
    }

    () -> System.out.println("hello world!");
}
```

```javascript
// javascript

function func() {
  console.log("hello world!");
}

() => console.log("hello world!"); // 위의함수와 동일합니다.
// 이러한 형태로 화살표 함수라고도 불린다.
```

## 람다 구조 엿보기 🤔

> 이 글에서는 파이썬을 기준으로 내용을 작성합니다. 다른 언어에서는 사용법이 다를수 있습니다.

람다 문법을 처음 접하면 람다의 짧은 문법에 어렵게 다가온다. 간단한 예제와 함께 알아보자

```python
def double(x:int)->int:# 입력수의 두배를 반환하는 함수 dobule
    return x*2
```

위의 `double` 함수는 int 값을 전달받아 두배를 반환한다. 이를 lambda 로 표현하면 다음과 같다.

```python
lambda x: x*2 # 위와 동일한 역할은 한다.
```

훨씬 간결해 졌지만 처음 보는 사람들은 오히려 짧아져서 이해하기 어렵게 다가올 수 있다.
위의 람다구문에 해석을 달자면 `lambda x(사용할 매개변수): (반환값)` 라고 표현 할 수 있겠다. 람다 또한 일반 함수처럼 매개변수가 없을수도 반환이 없을수 도 반환값이 필요하지 않을수도 있다. 🤔 몇가지 추가적인 예시와 함께 감을 잡아보자.

```python
# 매개변수가 없는경우
def no_argument_func(): # 다음과 같은 매개변수가 없는 함수 선언
    return "no_argument"

# 람다로 변형시
lambda : "no_argument" # lambda로 람다문법 선언후 매개변수에 아무것도 없으며 no_argument 문자열만 존제

# 람다에서 기본적으로 return은 식자체를 반환하는것으로 이해 할 수 있다.
# 이전 식에서는 실제로 lambda : (return)"no_argument" 와 같다.

# 매개변수가 두개인 경우

def add(a,b):
    return a+b

# 람다로 변형시
lambda a,b: a+b  # lambda (사용할매개변수) : (식) -> lambda a,b:(return) a+b
# 매개변수가 더 추가할수있음 lambda a,b,c: .. 등

# 반환값없이 콜백함수 이용하기
def print_hello()->None:
    print("hello") # 사용시 "hello" 를 출력하고 이외의 반환값 없음

lambda : print("hello")
```

## 어디에 쓸수 있을까 ?

우선 함수로 사용될 수 있는곳은 람다도 사용가능 하다.

람다가 사용되는곳은 대표적으로 `콜백함수` 사용되는 경우가 있다.

> [!NOTE]
> 콜백함수 ❓  
> 콜백 함수는 전달인자로 다른 함수에 전달되는 함수입니다. 이는 일종의 루틴이나 동작을 완료하기 위해 외부 함수 내부에서 호출됩니다.

```python
# 파이썬의 sort의 key 값으로 주는 경우 이경우도 콜백함수로 볼수 있다.
arr= [1,3,2,4]
arr.sort()
# arr = [1,2,3,4]
arr.sort(key=lambda x:-x)
# arr = [4,3,2,1] 내림차순으로 정렬됨

```

## 참고한글

- [람다대수\_위키피디아](https://ko.wikipedia.org/wiki/%EB%9E%8C%EB%8B%A4_%EB%8C%80%EC%88%98)
