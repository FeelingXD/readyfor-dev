# 파이썬의 Decorator ✨

> 이 글은 @staticmethod, @classmethod, @property 등  
> 다양하게 사용되는 Python의 데코레이터에 대해서 다룹니다

## 데코레이터란 ? 👀

파이썬의 데코레이터는 함수나 메서드 에 적용되어, 사용하려는 함수, 메서드의 기능을 확장하거나 변경하는 역할을합니다. 데코레이터(Decorator) 말 그대로 꾸며주는 기능을 합니다. 기본적으로 데코레이터는 함수를 인자로 받고 추가기능(데코레이터) 를 추가한 고차함수를 반환 합니다.

## 데코레이터 맛보기 👅 - 예시

> 데코레이터는 언제 사용해야할까 ?
>
> 함수, 혹은 메서드를 사용 하는데 공통적으로 사용되는 다른 기능(함수)이 있을때 사용하는게 좋다.  
> 설명이 모호한 관계로 예시와 함께 알아보자! 🤔

다음 함수를 살펴보자

```python
def hello():
    print("hello") # 인사를 하는 함수
def greet():
    print("greeting") # 반갑다고 하는 함수
# >>> hello
# >>> greeting
```

우선 간단한 인사를 하는 두 함수가 있다. greet , hello 가 있지만  
인사 이전에 내 이름을 소개하고 싶어졌다.  
우선 가장 간단한 방법으로는 다음과 같이 이름을 말하는 기능을 추가 해주면된다.

```python
def hello():
    print("my name is ..")
    print("hello")

def greet()
    print("my name is ..")
    print("greeting")
```

하지만 이렇게 함수를 수정하는경우 함수가 너무많은 기능을 하며 , greet 과 hello에 불필요한 코드중복이 발생하게 된다.
이럴 경우 파이썬 데커레이터 를 사용할수있다.

```python
# 데커레이터 정의
def introduce_myself(func):
    def wrapper():
        print("my name is ..")
        func()
    return wrapper

@introduce_myself
def hello():
    print("hello")

@introduce_myself
def greet()
    print("greeting")
```

### 데커레이터 만들어보기 🐬

데커레이터 의 문법은 함수처럼 작성하되 다음과 같은 특징이있다.

- 함수를 반환하는 고차함수 형태이다.
- 데커레이터 사용시 @(데코레이터함수이름) 으로 사용하는 데커레이터를 명시해준다.

데커레이터 의 기본형은 다음과 같다.

```python
# 데커레이터 기본형태
def deco(func): # 임의의 데코레이터 생성 인자는 데코레이터가 사용하는 함수를 가져옴
    def wrapper(*args,**kwargs): # args, kwargs는 매개함수에서 사용할 매개변수
        #추가 로직작성
        func(*args,**kwargs)
        #추가 로직 작성
    return wrapper # 추가로직을 감싼 고차함수 반환
```

### 어떻게 실행되는거지 ? 👀

```python
def deco(f):
    print("just defined!")
    return f
@deco
def greet(name):
    print(f"greeting {name}")
```

위의코드는 wrapper형태로 감싸지 않은 데코레이터이다 이를 그대로 실행하면 다음과 같이나온다.

```
>>> just defined!
```

어디서도 greet 함수를 호출하거나 deco를 호출하지않았는데 deco의 내부로직이 실행 되었다.  
왜 이렇게 된것일까 ? 🤔

파이썬에서 데커레이터는 다음과 같이 실행된다.

```python
def deco(f):
    print("just defined!")
    return f
@deco # 데커레이터 로 함수가 호출되면 호출한 함수를 재정의
def greet(name):
    print(f"greeting {name}")

# greet=deco(greet(name)) << 다음과 같이 동작하기에
# wrapper로 감싸지 않는다면 정의 하면서 deco wrapper 되지 않은 로직이 실행된다.
```

즉 greet(혹은 다른 함수 라도)가 정의될때 `@func` 형태의 데커레이터를 만난다면 함수를 감싸 함수를 재정의하게 된다.

## 어디에 사용할수 있을까?

[맛보기 목차](#데코레이터-맛보기-👅---예시)에서도 언급했지만 함수, 혹은 메서드를 사용 하는데 `공통적으로 사용되는 다른 기능`이 있을때 사용 할 수 있다.

몇가지 예시들

- 웹사이트에 페이지를 접근하는데 권한이 확인이 필요한 페이지와 그렇지 않은 페이지를 구분해야하는 경우 (로그인 회원만 확인가능한 페이지 등)
- 특정 함수나 메서드의 호출 로그를 남겨야하는경우 (데커레이터를 이용해 전후 함수호출을 남겨둘 수 있음)

## 마치며

파이썬의 데커레이터에대해 간단하게 작성하였습니다. 데커레이터에 대해 딮하게 또 데커레이터를 잘 표현햇다고 생각하는 @staticmethod , @property 등을 내용으로 작성하지 않았지만(다른 글을 통해 다루어보겠습니다. 😅) 이글을 읽는 분들에게 도움이 되면 좋겠습니다.

## 참고자료

- [임커밋'데커레이터](https://www.youtube.com/watch?v=3t26Z4vk7XE)
