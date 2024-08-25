# 코틀린 

>코틀린은 젯브레인즈사에서 개발하는 크로스 플랫폼 범용 프로그래밍 언어로, 자바와 완벽하게 호환되게 설계되었으며 일반적으로 JVM에서 사용되나 자바스크립트, LLVM 그리고 데이터 사이언스 영역에서도 사용 가능하다.
파일 확장자는 일반적으로 .kt를 사용하며 코틀린 스크립트는 .kts를 사용한다.
코틀린은 2019년 5월 7일 이후로 구글의 안드로이드 앱 개발에서 선호하는 언어가 되었다.

![](https://velog.velcdn.com/images/youngerjesus/post/ba30d109-ffe7-4f3f-ac49-1878a88b2a47/kotlin.jpeg)

## 코틀린 과 자바

코틀린은 기존의 자바와 100% 호환성을 유지하면서 어떻게 하면 더 간결하고 생산성이 좋은 언어를 만들수 있을까 ? 라는 철학으로 부터 출발했다.  

코틀린을 만든 젯브레인(jetbrain)은 기존의 프로젝트 들이 Java,C# 으로 이루어져 있어 유지 보수 하기에 많은 시간적인 비용이 발생했다. 이를 해결하고자 Java에 100% 호환되면서 조금더 간결하고 유지보수가 용이한 언어인 `kotlin` 이 나오게된다.

> kotlin 이 java 와 100% 호환하는법 😸

- kotlin 은 컴파일시 javabytecode(.class) 파일로 변환되어 JVM 에 실행되게된다. 이러한 방법은 Java -> class <- kotlin 이므로 java -> kotlin , 혹은 kotlin -> java 도 호환 할수 있게된다.

- kotlin 은 컴파일시 javabytecode 로 변환되므로 기존의 java 의 생태계를 그대로 사용할 수 있다.


## 코틀린 특징

- 간결함 : 코틀린은 자바 코드에 비해 간결하고 직관적이며, 많은 보일러플레이트 코드 (getter,setter 등) 코드를 줄여줍니다. 

- 정적 타입 : 코틀린은 `var` , `val` 등의 키워드로 정적타입이 아닌것처럼 보일 수 도 있지만 컴파일시 타입체크가 이르어져 런타임 에러를 방지 할 수 있습니다.

- 널 안전성 : 기존의 java에서는 null 관리는 매우 귀찮은 일이였습니다. kotlin 에서는 null 안정성을 제공하며 개발자는 값이 null 일경우 명시적으로 다뤄야합니다.

- 함수형 프로그래밍 지원 : 코틀린은 함수형 프로그래밍 패러다임을 지원하며, 고차 함수, 람다 표현등 자유롭게 혼하합할 수 있습니다.

- 확장 함수 : 코틀린은 클래스에 댛나 확장 기능을 제공하여, 기존 클래스의 메서드를 새로 정의 할 수 있습니다.

- 데이터 클래스 : 코틀린은 데이터 전송 객체(DTO)를 쉽게 만들 수 있는 데이터 클래스를 제공합니다.

- 코루틴: 코틀린의 꽃으로도 불리는 코루틴은 자바에는 없는 코틀린만의 독특한 동시성 프로그래밍 기능입니다. 

## 참고한 글
- [코틀린 나무위키](https://namu.wiki/w/Kotlin)