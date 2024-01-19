# Python GC는 어떻게 동작하는가

> 파이썬 GC 에대한 글입니다. 파이썬 GC는 어떻게 동작 하는지에 대해 서술합니다.

## Python 의 GC

파이썬에서는 기본적으로 garbage_collection 이외에도 reference counting을 통해 할당된 메모리를 관리한다.

기본적으로 refernce counting은 각객체의 참조 횟수가 0이면 도달할수 없는객체로 판단하여 collecting을 한다. 하지만 [참조횟수가 0은 아니지만 도달할수없는 경우](#cycleproblem)의 문제도 있다. 이를 해결하기위해 Python 에서는 추가적으로 cyclic garbage collection 을 통한 가비지 컬렉션을 추가적으로 사용한다.

## 레퍼런스 카운팅

파이썬에서 다른객체가 객체를 참조할때 참조하는 객체의 레퍼런스 카운트를 증가시킵니다. 또 참조가 없어질때 해당 레퍼런스 카운트를 다시 감소시킵니다. 이 카운터가 0이되면 해당 객체는 참조하는경우가 없으므로 메모리에서 해제시킵니다.

## [순환 참조](#순환-참조cycleproblem)

GC설명에서 살짝 언급한 참조횟수가 0이 아니지만 도달할수없는 경우의 예시이다.

```python
#ex1 자기 자신을 참조
cycle =[]
cycle.append(cycle) # 이경우 cycle은 ref-count가 1이지만 더이상참조할수없다.
# END
```

위의경우 자기자신을 참조한경우고 저이후 프로그램이 종료되는경우 메모리를 레퍼런스 카운팅 방법으로는 해제할 수 없다.

```python
# ex2 서로를 순환참조 A->B B->A
>>> a = Foo()  # 0x60
>>> b = Foo()  # 0xa8
>>> a.x = b  # 0x60의 x는 0xa8를 가리킨다.
>>> b.x = a  # 0xa8의 x는 0x60를 가리킨다.
# 이 시점에서 0x60의 레퍼런스 카운터는 a와 b.x로 2
# 0xa8의 레퍼런스 카운터는 b와 a.x로 2다.
>>> del a  # 0x60은 1로 감소한다. 0xa8은 b와 0x60.x로 2다.
>>> del b  # 0xa8도 1로 감소한다.
```

위의 경우에서도 서로를 참조하기때문에 레퍼런스 카운트는 0이아니지만 도달할수없는 메모리로 가비지(쓰레기)가 된다.

## python garbage collector

### 가비지 컬렉션의 작동방식

[순환참조 문제](#순환-참조) 를 해결하는 cyclic garbage collection 이 어떤 방식으로 동작하는지 알아보자.

#### 가비지 컬렉션의 기준

가비지 컬렉터는 내부적으로 generation(세대), 와 threshold(임계값)으로 가비지 컬렉션 주기와 객체를 관리한다. 객체들은 최근 생성된 객체의 generation(0) 부터 old(2) 까지 세대로 구분한다. 비교적 젊은세대(0) 에 가까울수록 더 자주 collection 하도록 설계되어있다.

#### 순환 참조의 감지

순환참조문제는 컨테이너 클래스(객체) 에 의에서만 발생할 수 있음을 먼저 알아야한다. 다른 객체를 참조할수있는 컨테이너형 객체만 순환참조 문제를 일으킬수 있다. GC는 순환 참조를 해결하기 위해 아이디어로 모든 컨테이너 객체를 추적한다.

![GC ROOT](https://i.postimg.cc/g0YWdCJj/image.png)

1. GC 시작시 ->GC ROOT로 모든 컨테이너 객체를 추적하고
2. GC_REF 는 모든 컨테이너 객체가가지는 REF_COUNT를 복사한 값으로 추가필드로 컨테이너 객체에 남게된다.
3. 레퍼런스 카운트를 증감 시키지않고 GC_REF를 통해 참조에 CONTAINER 객체가 있을경우 감소시킨다.
4. 이를통해 GC_REF 가 0이된 객체가 있다면 해당 객체가 UNREACHABLE?(도달 불가능 할수 있는값) 임을 인지한다. GC_REF==0 이라고 모든객체가 닿을수 없는객체는 아니다.
5. GC 가 UNREACHABLE? 에있는 컨테이너를 순회하면서 REACHABLE 이있을경우 해당 객체는 REACHABLE로 옮기고 GC_REF를 1로 설정한다.
6. 그럼에도 미접근객체가 있을경우 메모리를 해제하게된다.

## 참고자료, 읽어볼글

- [PYTHON GC](https://velog.io/@jshong0907/Python-GC-2)
- [Python GC가 작동하는원리](https://blog.winterjung.dev/2018/02/18/python-gc)
- [Instagram이 gc를 없엔이유](https://luavis.me/python/dismissing-python-garbage-collection-at-instagram) 인스타그램이 GC를 사용하지않는 재밋는이유 🤔
- [GC없는 PYTHON을 추구하면 안되는걸까?](https://www.youtube.com/watch?v=e2hT7dYzURo)
