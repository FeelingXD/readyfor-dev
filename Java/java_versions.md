## 자바 버전들( Java versions )

> 이 글에서는 자바 특정 자바 버전 몇가지에 대해 다룹니다.(8,11,17)

## 왜 특정 버전에 대해서만 다루나요 ?

JAVA 는 옛날언어 라는 프레임이 있지만 Java도 매년 여러가지 업데이트를 통해 JAVA 사용자들에게 더 좋은 서비스를 제공하고자 하고있습니다. 그중 몇가지 버전(8,11,17)은 
LTS(LONG TERM SUPPORT)로 장기 지원 버전이기에 장기적으로 변화가 적고 지원기능에대해 장기적으로 업데이트, 개선 을 지원하기에 결정 하였습니다.


## JAVA 8
>[!NOTE] 
> JAVA 8 버전부터 기존의 딱딱하고 JAVA는 옛날 언어다 라는 프레임을 많이 개선한 버전이라고 생각됩니다. 😉   

### JAVA 8 의 대표적 특징들 ✨
1. 람다 표현식(Lambda Expression): 람다 표현식은 함수형 프로그래밍의 개념을 JAVA에도 도입한 것입니다. 이를 통해 간결하고 유연한 코드 작성이 가능해졌습니다. 대표적으로 익명클래스로 한번만 사용되는것들을 람다로 대체할 수 있게되었으며 아래 서술 할 Stream api 등에 다양하게 사용되고 있습니다.

2. 함수형 인터페이스 (Functional Interfaces): 함수형 인터페이스는 람다 표현식과 함께 사용되는 인터페이스입니다. 이를 통해 람다 표현식을 쉽게 정의하고 사용할 수 있습니다.

3. 스트림 API(Stream API): 스트림 API는 컬렉션 데이터를 처리하기 위한 새로운 방법을 제공합니다. 이를 통해 데이터를 효율적으로 처리하고 병렬 처리하기 위한 기능을 제공합니다.(병렬 스트림 등)

4. 디폴트 메서드(Default Methods): 디폴트 메서드는 인터페이스에 기본적인 구현을 제공하는 기능입니다. 이를 통해 인터페이스를 수정하지 않고도 새로운 기능을 추가할 수 있습니다. (기존의 인터페이스 메서드는 클래스에서 사용하려면 구현을 강제했지만 default method가 있으면 구현하지않더라도 기존 인터페이스으 default method 를 사용하게합니다.)

5. Optional 클래스(Optional Class): Optional 클래스는 null을 처리하는 새로운 방법을 제공합니다. 이를 통해 NullPointerException 오류를 방지하고 코드의 안정성을 높일 수 있습니다.


- 디폴트메서드 가 생기면서 더 interface와 abstract class 의 경계가 모호해지고있다는 생각이든다.
- Optional 클래스 자바의 고질적인 뜬금없이 튀어나오는 NPE를 효과적으로 줄이게 해주는 마법같은 존재다.

## JAVA 11

1. 동적 타입지원 var : 키워드 var을 통해 동적으로 타입 지정이 가능해졋다. (Java 10 이후)
```java
HashMap<String, List<Employee>> employeeMap = new HashMap<String, List<Employee>>();
// var 키워드로 간결하게 복합객체도 표현 할수 있다.
var employeeMap = new HashMap<String, List<Employee>>();

```
2. 문자열 처리 API 추가 : isBlank() , strip() ,lines() 등 다른 언어에서 지원하는 문자열 메서드도 JAVA에서 지원하게되었다.

3. GC 알고리즘 개선 (JAVA 9 이후) G1GC 알고리즘이 기본으로 설정되었다.

## JAVA 17

> SpringBoot3 부터 JAVA 17을 반드시사용해야한다. 

1. Sealed 상속제한 :  sealed 를통해 특정 클래스만 상속 가능하도록 제한 할수 있게되었다.
```JAVA
public static sealed abstract class Bird permits Sparrow, Penguin {
    public abstract void fly();
}

public static final class Sparrow extends Bird {
    @Override
    public void fly() {
        System.out.println("Sparrow fly");
    }
}

public static final class Penguin extends Bird {
    @Override
    public void fly() {
        System.out.println("Penguin can't fly");
    }
}
public static final class Tiger extends Bird { //compile error: 'Tiger' is not allowed in the sealed hierarchy
    @Override
    public void fly() {
        
    }
}
```
2. 텍스트 블록 : 여러줄에걸친 문자열 작성시 텍스트 블록을 통해 사용할수있다. 
```JAVA
String text_JAVA = 
                    "{\n" +
                  "  \"name\": \"John Doe\",\n" +
                  "  \"age\": 45,\n" +
                  "  \"address\": \"Doe Street, 23, Java Town\"\n" +
                  "}";

String text_JAVA17 ="""
  { 
    "name": "John Doe",
    "age": 45,
    "address": "Doe Street, 23, Java Town"
  }

"""

```
3. Switch 표현식 (Switch expression) :  기존 스위치문은 case 마다 break 를 걸어주고 코드중복이 생기는 이슈가 있었다. 17에서는 표현식을 도입하여 개선했다.

```java
// 기존의 java switch
private static void test(int n) {
	switch (n) {
    	case 1: 
        case 2:
        case 3: {
        	System.out.println("1-3");
    		break;
    	}
        case 4 : {
        	System.out.println("4");
    		break;
        }
    }
}

// switch expression
private static void test(int n) {
	switch (n) {
    	case 1, 2, 3 -> System.out.println("1-3");
        case 4 -> System.out.println("4");
    }
}
```

4. Record 클래스 : Kotlin의 Data클래스와 매우 유사하다 기존 POJO에서 Getter Setter등의 중복되는 메서드 생성을 줄이기위해 Lombok을 사용하곤 했는데 JAVA에서 자체 지원을 통해 개선된거같다. (JAVA 16 이후)
5. 컴팩트한 숫자 포맷 지원 : NumberFormat 클래스를 통해 숫자 포맷을 지원하게 되었다.

```Java
NumberFormat fmt = NumberFormat.getCompactNumberInstance(Locale.ENGLISH, NumberFormat.Style.SHORT);
System.out.println(fmt.format(1000));
System.out.println(fmt.format(100000));
System.out.println(fmt.format(1000000));

[Output]
1K
100K
1M
```


## 참조

- [자바17에는 뭐가 달라졌을까](https://e-una.tistory.com/46)
- [Java 8  에서 17 로 갈 때 코드 작성시 도움 되는 new features](https://warpgate3.tistory.com/entry/Java-8-to-17)
- [whats-new-between-java-11-and-java-17](https://dzone.com/articles/whats-new-between-java-11-and-java-17)