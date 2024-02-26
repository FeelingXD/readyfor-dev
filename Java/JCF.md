## Java의 Collections Framwork

> 🗒️ -이 글에서는 JCF(Java Colleciton Framework)에 대해 작성 합니다.

## JCF( Java Collections Framework)

Java Collections Framework(JCF)는 다수의 데이터를 처리할수있는 Java의 프레임워크입니다. Collections는 배열처럼 다수의 데이터를 묶는 그룹이나 집합으로 이해하시면 좋습니다.

JCF는 흔하게 사용되는 집합(Set) 해쉬(Hash) ,리스트(List) 과같은 집합 자료형을 제공합니다.

## 컬렉션 프레임워크의 장점

1. 데이터 구조와 알고리즘을 제공하므로 직접 작성할 필요가 없어 일이 줄어듭니다.
    - 미리정의된 JCF 의 클래스를 사용함으로써 재사용성 높은 코드를 작성할 수 있다.
2. 데이터 구조와 알고리즘의 고성능 구현을 제공함으로써 성능을 향상시킵니다. 각 인터페이스의 다양한 구현을 상호 교환할 수 있으므로 구현을 전환하여 프로그램을 조정할 수 있습니다. 
    - 공통되는 부분은 자바의 interface로 사용하고 실제 생성자는 사용하고자 하는 목적에  맞게 casting 해서 사용한다. 

3. 컬렉션을 주고받을 수 있는 공통 언어를 설정하여 서로 관련이 없는 API 간의 상호 운용성을 제공합니다.
    - 각 관련없는 컬렉션 객체에 대해 상호작용의 예를 들어주는것같다.
### 예시
1. 과거 JCF 이전의 자바에서는 HashTable, MAP,LIST 가 따로 존재하여 해쉬맵 트리맵등 사용에따라 사용자가 추가적인 클래스로 구현해야했다. JAVA 가 발전하면서 JCF 에서 미리정의된 여러 컬렉션 객체를 제공함으로써 작성해야할 코드가 줄었다.
2. JAVA 에서는 Stack 이나 Queue를 구현할때 JCF를 통해 다음과 같이 작성한다.
```java 
import java.util.*;

public void static main(){
    Queue<Integer> q = new LinkedList<>();
    // Queue 인터페이스에는 poll 을 사용하여 원소를 가져옴
    Stack<Integer> s = new LinkedList<>();
    // Stack 인터페이스에서는 top, pop 을 사용하여 원소를 가져옴

    // 하지만 Queue <- >Stack은 다른 인터페이스 기에 stack 에서는 queue 메서드를 queue 에서는 stack 메서드를 사용 할 수 없음 
}
```
3. 관련없는 api간의 상호 운용성을 제공하기 위해 컬렉션 MAP <-> Tree(예시) 데이터를 옮길때 알려진 공통api(JFC)를 이용하여 데이터 손실이나 오류를 줄일 수 있다.

## 컬렉션 프레임워크 살펴보기 ✨

JCF에서 자바에서 사용되는 다양한 자료구조의 구현과 인터페이스를 제공한다.

![](https://velog.velcdn.com/images/eenaa/post/a0242d27-e534-432a-ac06-a0112f693d02/image.png)


### Collections vs Map 🤔

>[!NOTE]
> Collections 
순서, 집합관게를 표현하는 자료형 배열, 리스트, 집합

>[!NOTE]
> Map
키와 값으로 데이터를 핸들링 하는자료형 내부적으로는 Hashfunction이 동작한다.

## 동기화 보장 ?

같은 자료구조를 사용한다해도 실제 컴퓨터에서 사용할때는 `동기화` 의관점도 생각해야한다.
해당 자료를 멀티 스레드 구조에서 스레드세이프를 생각하지 않을 수 가없다. 
하지만 Java에서 스레드를 보장하기위한 키워드인 `syncronized` 는 락이 걸리기에 동기화를 보장하지않는 다른 자료형과 비교했을때 성능이 떨어질 수 있다. 내가 어떤 자료형이 필요하고 이객체가 다른 스레드에서도 사용할 수 있는지에 대한 고려가 필요하다.

## Collection, Collections

자바에는 추가적으로 Colelctions 라는 클래스도 있는데 이는 Collection 에 대한 정렬, 자료검색등 기능적인 부분을 제공한다. Collections 는 정적인 클래스형태를 띈다. 

## 생각
개인적으로 JCF는 라이브러리라고 생각할만큼 목적이 명확하고 그에 따라 프레임워크 보다는 하나의 라이브러리로 보여지기도 한다. 

하지만 JCF 가 표준화된 인터페이스를제공하는점, 해당 클래스를 상속받아 사용자가 추가적으로 구현을 하지않는점 과 이미 구현된 클래스를 제공하는점 ,효율적이고 일관된 방식으로 컬렉션을 다루게 하는점들이 프레임워크로 분류되는 이유 이다.

## 참조
- [오라클 자바 문서](https://docs.oracle.com/javase/8/docs/technotes/guides/collections/overview.html)



