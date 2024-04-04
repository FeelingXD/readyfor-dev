## Java package-private

> 문득 Junit으로 테스트를 작성할때 다른 클래스를 작성할때처럼 메소드에 지정자 없이 테스트를 작성하고 있었는데 접근제어자를 지정하지 않았을때 어떤 접근제어자가 설정 될지 궁금해졌다.
```java
@Test
    void test(){ // 접근제어자가 없는 메서드나 클래스는 어떤 접근제어를 할까 🤔
        //given

        //when

        //then
    }
```

## Java의 접근제어자

접근제어자는 객체 지향적 설계에서 클래스의 노출을 최소화 하는데 도움을 준다.

자바에서는 이러한 정보 은닉을 위해 접근 제어자를 사용한다.

클래스나 메서드 앞에 작성하여 접근제어자를 명시한다.

```java
class Main{ 
   
    private void privateMethod(){ // private 접근

    }
    public void publicMethod(){ // public 접근

    }
    protected void protectedMethod(){ // protect 접근

    }
    void defaultMethod(){// package-private , default 접근

    }
    
}
```

접근제어자의 종류는 다음과 같다.

- public (어디서든 접근가능)
- private(선언한 클래스 에서만 접근가능)
- protected(선언한 클래스, 같은 패키지, 상속받은 자식 클래스, 에서접근가능)
- default(package-private, 선언한 클래스, 같은 패키지 에서만 접근가능)

## package-private (default)

![](https://www.tcpschool.com/lectures/img_java_access_default.png)

명시적으로 package-private 를 접근제어자로 표시하려면 `default` 키워드를 사용하면된다.
default 는 접근제어자중 상당히 마이너하고 사용하면안된다 vs 사용하기어렵다. 등 대립이나 논란도 어느정도 있는 편이다.


## 결론

- 기본적으로 접근제어자 없이 작성되는 메소드나 클래스, 변수등은 모두 default(package-private) 접근제어자가 설정된다.

## 참조 및 더 읽어볼글
- [TCP_SCHOOL_접근제어자](https://www.tcpschool.com/java/java_modifier_accessModifier)
- [package-private는 안쓰나요?](https://hyeon9mak.github.io/Java-dont-use-package-private/)
- [package-private를 쓰지말아야하는이유](https://dev.to/cauchypeano/why-you-should-avoid-package-private-scope-in-java-anl)