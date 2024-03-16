## STACK 대신 DEQUE를 사용하자

> 학부생 시절 Java 에서 Stack자료형 대신 Deque 를 사용해야 한다는 말을 듣고 사용해 왔는데 이글을 통해서 왜 Stack 자료형 대신 Deque를 사용해야하는지 작성합니다.

## Stack 과 Deque

### 일반적인 자료구조에서..

> 일반적인 자료구조의 관점에서 Deque 와 Stack 은 다음과 같다.
#### Stack 📚
![](https://media.geeksforgeeks.org/wp-content/cdn-uploads/20230726165552/Stack-Data-Structure.png)

> [!NOTE]
대표적인 LIFO(Last in First Out) 자료구조로 늦게 입력된 자료가 먼저 나가는 자료구조이다.

#### Deque 📚
![](https://miro.medium.com/v2/resize:fit:925/1*FUh1NionDrsK1vflgfBYPg.png)
>[!NOTE]
Queue 와 Stack 의 특징을 동시에 가지고 있는 Deque은 먼저 입력된 자료, 가장 늦은 자료 두가지 모두에 대해 접근할 수 있다.

## 왜 JAVA 에서는 Stack대신 Deque 를 사용 하라는 걸까? 🤔
### 공식 문서(javadoc)에서 LIFO 관련은 스택 사용하길 권장함
자바 공식 문서 Stack 항목에 다음과 같이 작성되어 있다.

>A more complete and consistent set of LIFO stack operations is provided by the Deque interface and its implementations, which should be used in preference to this class. For example:

> [!NOTE]
>번역   
Deque 인터페이스와 그 구현체는 더 완전하고 일관된 LIFO 스택 연산을 제공합니다. 예를들어 다음과 같이 사용할 수 있습니다.

```java
Deque<Integer> stack = new ArrayDeque<Integer>();
stack.push(1);
```


추가적으로 javadoc deque 문서에는 다음과 같이 작성되어 있다.

> Deques can also be used as LIFO (Last-In-First-Out) stacks. This interface should be used in preference to the legacy Stack class.

> [!NOTE]
> 번역   
> Deques 자료형은 LIFO stack 으로도 사용할 수 있습니다. Deque 인터페이스는 기존의 Stack class 를 대신해서 사용 할 수 있습니다.

###  여러 관점에서 Stack 대신 Deque를 사용하는 이유

- 객체지향 관점: java.util 의 Stack 은 클래스이고 Deque는 인터페이스 자료형입니다. 클래스는 하나만 확장할 수있으며(단일 상속) 인터페이스는 단일 클래스로 얼마든 확장할 수 있습니다.(유형 다중 상속 interface), Deque를 사용하면 Stack의 구체적인 클래스의 종속성이 제거되며 다른 Deque 구현 체(LinkedList,ArrayDeque)를 사용 할 수 있습니다.

- 불일치 : 사실 기존의 java.util 의 stack은 자료구조의 stack과 조금 일치하지 않습니다. Stack 은 내부적으로 Vector를 상속받아서 구현하는데 Vector는 인덱스 접근을 허용하기에 Stack의 최근 데이터의 접근보다 많은것을 허용하고 있습니다. 

- 성능 관점 : java.util의 Stack은 내부적으로 자바의 Vector 클래스를 사용합니다. 기본적으로 vector 클래스는 ArrayList의 스레드 안전 버전입니다. 다만 자바에서 스레드 안전을 보장하기위해 `syncronized` 키워드를 사용하며 이는 내부적으로 lock 을 구현해서 사용합니다. 다중 스레드 환경에서는 의미 있을 수 있으나 단일 스레드환경에서 내부적으로 lock을 사용하는데 오버헤드가 발생합니다. 

## 정리

- java.util 의 Stack 대신 Deque를 사용하도록 하자.
- Stack 은 내부적으로 Vector를 상속하여 사용하므로 성능 문제가있다.


## 참조
- [[Java] 왜 Stack 대신 Deque를 사용하는가?](https://vanslog.io/posts/language/java/why-use-deque-instead-of-stack/)
- [Why should I use Deque over Stack?](https://stackoverflow.com/questions/12524826/why-should-i-use-deque-over-stack)