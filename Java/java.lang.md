## Java의 Lang 패키지

> 👀 이 글에서는 자바의 java.lang 패키지에 대해 알아봅니다.

Java 를 사용할때 우리는 정의한 클래스를 사용하기위해 별도로 import 를 통해서 사용하게됩니다. 그렇지만 String, Integer 등 우리가 정의하지않았지만 자바에서 `기본` 적으로 제공되는 이 클래스는 어디서 왔을까요 ?

## Java 의 lang 패키지

우리가 따로 import 하지 않고 사용하는 기본 자료형 이라고 불리는 이는 java 의 lang 패키지에 정의 되어 있습니다. Java 공식 자료에는 다음과 같이 작성되어 있습니다.

> java doucment 의 lang
> java.lang :
> Provides classes that are fundamental to the design of the Java programming language.

요약된 설명은 다음 과 같다. 🤔

> java.lang : 자바 프로그래밍 언어 설계의 기본이되는 클래스를 제공합니다.

물론 공식 문서의 java.lang 패키지 공식문서를 들어가서 요약본이아닌 설명을 해석 하면 다음과 같이 써져 있다.

### java.lang

> Java 프로그래밍 언어 설계의 기본이 되는 수업을 제공합니다. 가장 중요한 클래스는 클래스 계층 구조의 루트인 Object와 런타임에 클래스를 나타내는 인스턴스인 Class입니다.
> 원시 타입의 값을 마치 객체처럼 표현해야 하는 경우가 종종 있습니다. 래퍼 클래스인 Bool, Character, Integer, Long, Float, Double은 이러한 용도로 사용됩니다. 예를 들어 Double 타입의 객체에는 참조 타입의 변수에 해당 값에 대한 참조를 저장할 수 있는 방식으로 해당 값을 표현하는 타입이 Double인 필드가 포함됩니다. 이러한 클래스는 또한 원시 값 간의 변환을 위한 여러 메서드를 제공하며, 같음 및 해시코드와 같은 표준 메서드를 지원합니다. Void 클래스는 무효 유형을 나타내는 Class 객체에 대한 참조를 보유하는 비 불변성 클래스입니다.

> Math 클래스는 사인, 코사인, 제곱근과 같이 일반적으로 사용되는 수학 함수를 제공합니다. String, StringBuffer, StringBuilder 클래스도 마찬가지로 문자열에 대해 일반적으로 사용되는 연산을 제공합니다.

> ClassLoader, Process, ProcessBuilder, Runtime, SecurityManager, System 클래스는 클래스의 동적 로드, 외부 프로세스 생성, 시간 등의 호스트 환경 조회, 보안 정책 적용을 관리하는 '시스템 작업'을 제공합니다.

> Throwable 클래스는 throw 문으로 던질 수 있는 객체를 포함합니다. Throwable의 서브클래스는 에러와 예외를 나타냅니다.

간단하게 요약하면 Java 를 사용하면서 사용하는 String, Integer,Object등 Wrapper 클래스 뿐만아니라 수학계산에 사용하는 Math, 예외를 표시하는 Throwable 도 lang 패키지에 있다. ✔

> 🤔 java.lang 이 있다는건 알겠는데 임포트없이 쓸수있다! 라는 것은 보이지 않는다.

이 궁금증은 oracle 자바 스펙에서 확인할 수 있는데 공식문서에는 해당 내용이 다음과 같이 작성되어 있다.

> Code in a compilation unit automatically has access to all types declared in its package and also automatically imports all of the public types declared in the predefined package java.lang.

> 컴파일 유닛코드는 해당 패키지에 선언된 모든 유형에 자동으로 액새스 하고 미리 정의된 패키지 java.lang에 선언된 모든 공용 유형을 자동으로 포함 시킵니다.

즉 java는 컴파일에서 java.lang 패키지를 포함 하므로 컴파일러에게 java.lang 에 선언된 클래스들이 사용 되는데 문제가 없도록 만든것 같다.

## 참고자료

- [오라클 자바8 문서](https://docs.oracle.com/javase/8/docs)
- [자바 스팩](https://docs.oracle.com/javase/specs/jls/se10/html/jls-7.html)
