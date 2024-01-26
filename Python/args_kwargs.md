# [Python] \*args 와 \*\*kwargs 란?

![이게뭐노..](https://i.namu.wiki/i/0f8QIHX185ZnBJ4yXJf_00Ds5QG1BM2_3xtouAfSto7AsNNl7yvCmLXUa6hTbSLlqy4mSoA5TKFTXhFb3qm1kALBYHE8PMbi90DgYEStO65jjFSnY9eh23XhpB5b9-t5c9CXNI59Vyk8ZvGw9Q-cvQ.webp)

> 데커레이터를 사용할때 혹은 다른 오픈된 깃허브 소스를 보다보면 다음과 같은 코드들이 있다.

```python

def some_cool_func(*args,**kwargs):
    # arg~~
    # ..
    pass
```

여기서 매개변수를 \*args, \*\*kwargs 를 사용하는데 이것은 무었을 의미할까 ? 궁금했다. 🤔

## args와 kwargs 📝

args 는 흔히 사용하는 매개변수의 약어이다. (argument) 그리고  
kwargs는 Keyword Argument 의 약어이다.

\*args 와 \*\*kwargs 를 이해하기 전에 Python 의 postion argument와 keyward argument 를 잠깐 설명해보자면 다음과 같다.

```python
# Position argument & Keyword argument

def func(sender,receiver):
    print(f'보낸사람 :{sender} 받는사람 :{receiver}')

# 흔하게 사용하는 postion argument
func("지민","광수")
# >>> 보낸사람 :지민 받는사람 :광수

#keyword argument 로 매개변수 전달하기
func(receiver="광수", sender="지민") #순서를 변경하되 keyword로 값을 넘김

# >>> 보낸사람 :지민 받는사람 :광수
```

1. 일반적으로 사용하는 position argument 는 함수(메서드) 사용시 매개변수 넣는 위치에 따라 전달인자의 값이 들어가게된다 이를 psition argument라 한다 (순서 중요)
2. keyword argument 는 함수에서 사용하는 매개변수를 알고있다면 직접 지정해서 위치에 관계없이 사용할 수있다. 대표적인 예로 print() 의 end ,seq 키워드 가 있다.

다시 돌아와서 \*args 와 \*\*kwargs 는 파이썬에서 가변인자(전달 받는 갯수가 정해지지않음)를 받는 매개변수이다.

\*args 는 postion argument 의 가변인자를 \*\*kwargs 는 keyword argument 를 받는다.

### 사용해보기 ✨

```python
def args_test(*args,**kwargs):
    print(f'{args}' , f'{kwargs}' )
args_test('hello',hello='world')
args_test('hello','world','position',hello='world')
args_test(key='value',value='this value')
# >>> ('hello',) {'hello': 'world'}
# >>> ('hello', 'world', 'position') {'hello': 'world'}
# >>> () {'key': 'value', 'value': 'this value'}
```

> [!NOTE]  
> 위의 예제 처럼 key 를 지정한 값들은 모두 kwargs 에 딕셔너리형태로 저장되며 그전의 매개변수는 args에 일괄 tuple 형태로 보관된다. 만약 로직에서 매개변수를 사용하려면 tuple , dictionary 처럼 사용 할 수 있다.

### 주의점 ⚠️

> [!WARNING]
> 가변인자의 매개변수의 순서는 중요하다 postion argument 가변인자가 keyword argument 보다 먼저 사용되어야 한다. 이는 파이썬 규칙이다.

```python
# 가변인자 순서가 바뀐경우 kwargs 와 args
def test_reverse_arguments(**kwargs,*args):
# >>> SyntaxError: arguments cannot follow var-keyword argument 선언하기 이전 파이썬 인터프리터가 오류를 출력한다.
```

이는 함수를 사용 할때도 마찬가지이다.

```python
def test(*args,**kwargs):
    print(args,kwargs)

test(key='hello','error')
# >>> SyntaxError: positional argument follows keyword argument # 위치 변수는 키워드 변수이전에 나와야한다.!
```

```python
# 가변인자 키워드를 변경해서 사용 할 수 있다.
def animals(*unnamed_animal,**animal_dict):
    '''
        위와같이 *args. **kwargs 를 변경해서 사용할 수 있다.
    '''

```

> [!TIP]
> Python 매개변수 순서는 다음을 지켜야한다.
>
> 1. 가변인자 변수는 항상 일반 매개변수의 뒤에 위치해야한다.
> 2. 매개변수에서 위치 매개변수가 키워드 매개변수 앞에 위치해야한다.

## 정리

- args,kwargs는 python 에서 사용하는 가변인자 변수이다.
- args 는 tuple 형태로 kwargs 는 dictionary 형태로 값을 받는다.
- 가변인자 매개변수 순서는 중요하다. (선언, 사용시 모두)

---
