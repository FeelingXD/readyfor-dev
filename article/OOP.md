# OOP (Object-Orient-Programming)

> 이 글에서는 프로그래밍 패러다임 중 하나인 OOP(객체지향개발)에 대해 서술한 글 입니다.

## 1. OOP 이전에는 .. 👀

초기의 컴퓨터 프로그래밍은 단순 명령어 집합 혹은 일렬을 과정에따른 순서대로 처리하는 **절차 지향 프로그래밍** 방식 이였다. 과거에는 컴퓨터 성능이 크게 좋지않고 그에따라 구동가능한 프로그램의 크기 또한 제한적이기에 절차 지향 프로그래밍 으로 충분히 문제를 해결 할 수 있었다.

## 2. 절차지향의 문제와 새로운 패러다임 OOP

인류의 발전으로 컴퓨터 성능의 발전과 그에따른 프로그램의 요구사항이 많아짐에 따라 기존의 **절차 지향 프로그래밍** 의 문제점들이 드러나기 시작했다.

### 2-1. 절차지향의 문제점들

- 유지보수 , 디버깅의 어려움 : 절차지향 프로그래밍의 코드 재사용을위해 GO TO 문법등으로 코드를 재사용 하려 했으나 오히려 유지보수와 디버깅이 더욱어려워졌다.
- 구조적 개선의 어려움 : 실행순서에따라 결과가 달라질수 있어 프로그래밍을 설계하는것도 유지보수하는것도 매우 어려움

### 2-2. OOP 의 등장

절차지향의 문제들에 따라 OOP(객체 지향 프로그래밍)이 떠오르게 되었다.
기존의 절차 지향 프로그래밍이 단순 명령의 집합과 순서에 집중했다면 OOP는 프로그램의 동작을 현실의 물건들 즉 객체와 비교하여 추상화 하고 프로그래밍을 이 객체들의 상호 작용하는 방법으로 해결하고자 하였다.

## 3. OOP 의 4가지 특징들

> 👀 객체 지향 프로그래밍은 다음과 같은 특징을 갖는다.
> 이글에서는 OOP에 대해 간단하게 서술하므로 다른글을 통해 자세히 다룰 예정이다.

### 추상화(Abstraction)

객체를 자세하게 표현하는것이아닌 객체의 공통되는 속성이나 기능을 묶어 불필요한 기능을 생략하고 객체의 중요한 부분만 개략화 하는것이다.

> [!NOTE]
> 철수 와 영희는 사람이며 성별만 다르다. 이럴때 사람으로 추상화 하고 하위객체에서 성별을 추가할 수 있다.

### 캡슐화(Encapsulation)

캡슐화(encapsulation)란 객체 지향 프로그래밍(OOP)에서 객체의 데이터와 기능을 하나로 묶고 외부에 노출되지 않도록 숨김 처리하는 것을 말한다. 변수, 메소드, 클래스에 대해 접근 제어자를 사용함으로써 캡슐화를 할 수 있다.

> [!WARNING]
> 캡슐화 와 정보은닉 이 같은 의미처럼 혼용 되곤하는데 정보은닉은 캡슐화의 특징 중 하나일뿐 캡슐화 자체는 아니다. 캡슐화 != 정보은닉

> [!NOTE]  
> 자판기 와 사용자의 관점에서 사용자는 현금을 넣고 원하는 물건을 고른다.
> 사용자는 자판기에 어떤 물건이 있고 물건가격이 어떠한지 알 수 있지만 자판기가 어떤방법으로 해당 음료수를 고르고 사용자에게 주기위해 움직이는지 알수 없다.

### 다형성(Polymorphism)

다형성(polymorphism)은 여러 가지 형태를 갖는 성질 말한다.

### 상속(Inheritance)

객체 지향 프로그래밍에서 자손 클래스가 조상 클래스의 기능을 그대로 재사용 하는 것을 말한다.

> [!NOTE]
> 사람의 아이는 사람의 형태를 동물의 아이는 동물을 형태를 띈다
> 자손이 그조상과 완전히 같지 않지만 대부분의 특징을 물려 받는다.

## 참고한글

- [위키](http://wiki.hash.kr/)