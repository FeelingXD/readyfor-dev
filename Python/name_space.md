# Python 의 네임스페이스(namespace)

> 이 글에서는 파이썬의 `namespace` 에 대해서 알아봅니다. 🥕

## 파이썬의 네임스페이스

### 정의 🤔

파이썬 공식문서에서는 namespace를 다음과 같의 정의되어 있습니다.

> [!NOTE]
> namespace  
> The place where a variable is stored. Namespaces are implemented as dictionaries. There are the local, global and built-in namespaces as well as nested namespaces in objects (in methods). Namespaces support modularity by preventing naming conflicts. For instance, the functions builtins.open and os.open() are distinguished by their namespaces. Namespaces also aid readability and maintainability by making it clear which module implements a function. For instance, writing random.seed() or itertools.islice() makes it clear that those functions are implemented by the random and itertools modules, respectively.

번역하면 다음과 같이 설명하고있다. 👀

> [!NOTE]
> 네임스페이스  
> 변수가 저장되는 장소입니다. 네임스페이스는 파이썬의 dictionary 형태로 구현되어있습니다.
> 로컬,전역 및 내장 네임스페이스 와 객체(메서드 내)의 중첩 네임스페이스 가 있습니다.
> 네임스페이스는 이름 충돌을 방지하여 모듈성을 지원합니다. 예를 들어 builtins.open 과 os.open() 함수는 네임스페이스로 구분됩니다. 네임스페이스는 또한 어떤 모듈이 함수를 구현하는지 명확하게 함으로써 가독성과 유지보수성을 돕습니다. 예를 들어 random.seed() 혹은 itertools.islice()를 작성하면 해당 함수가 각각 random 및 itertools 모듈에서 구현되었음을 명확히 알 수 있습니다.

### 파이썬의 스코프

> 네임스페이스를 자세하게 알아보기전 간단하게 파이썬의 스코프를 정리하고자 한다.
>
> 파이썬은 대부분의 다른언어와 다르게 중괄호(brace, `{}`) 를 사용하지 않고 들여쓰기(indent) 를 사용하여서 스코프를 구분한다.

```python
# 파이썬의 스코프1

a = "global" # 전역
def cool_func():
    a = "local" # 지역
    print(a) # >>> local
print(a) # >>> global
```

위의 예제에서는 같은 변수명을가진 `a` 라도 스코프에 따라 출력하는 결과물이 달라진다.
즉 가장 인접한 스코프를 검사하여 해당 변수의 값을 참조한다. 그럼 바로 인접한 스코프에 찾으려는 변수 가 없으면 어떻게 될까 ?

```python
# 파이썬의 스코프2
a ="global"
def cool_fun():
    print(a)
# >>> global
```

가장 인접한 스코프에서 찾을수없으면 스코프는 상위 스코프에서 값을 찾으려고한다. 그럼에도 없다면 오류를 반환한다.

### 스코프와 네임스페이스

> 파이썬의 네임스페이스는 위에서 설명한 스코프와 밀접하게 관련이 있는데 특정 스코프에 살아있는 변수들이 저장되는 곳이 `네임 스페이스` 라고 이해할 수 있다.

파이썬에서는 다음 함수들을 통해 네임스코프를 확인할 수 있다.

- locals() : 로컬 네임스페이스 정보를 출력
- globals() : 글로벌 네임스페이스 정보를 출력

```python
# 스코프와 네임스페이스

a = "global" # 전역
def cool_func():
    a = "local" # 지역
    print(locals()) # {'a': 'local'}
print(locals())  # {'__name__': '__main__', '__doc__': None, '__package__': '' ...
print(globals()) # {'__name__': '__main__', '__doc__': None, '__package__': '', ...
```

> [!TIP]
> cool_fun 내부의 locals와 다르게 함수 밖의 `print(locals())` ,`print(globals())` 의 결과가 같은 걸 확인 할 수 있는데 이는 밖의 locals 가 globals 와 같기 때문이다. 즉 전역스코프에서 locals를 사용하면 globals와 같다.

## 참고

[파이썬\_공식문서\_namespace]()
